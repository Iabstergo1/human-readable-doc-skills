#!/usr/bin/env python3
"""Normalize Markdown spacing and report renderability issues."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


DEFAULT_MAX_LINE_LENGTH = 180


def is_table_line(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2


def fence_info(line: str) -> tuple[str, int, str] | None:
    match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
    if not match:
        return None
    marker = match.group(1)
    return marker[0], len(marker), match.group(2).strip()


def is_fence(line: str) -> bool:
    return fence_info(line) is not None


def is_heading(line: str) -> bool:
    return bool(re.match(r"^#{1,6}\s+\S", line))


def normalize_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    raw_lines = [line.rstrip() for line in text.split("\n")]
    lines = raw_lines[:-1] if raw_lines and raw_lines[-1] == "" else raw_lines
    out: list[str] = []
    previous_was_table = False
    active_fence_char: str | None = None
    active_fence_len = 0

    for index, line in enumerate(lines):
        table = is_table_line(line)
        fence = fence_info(line)
        fence_is_opening = fence is not None and active_fence_char is None
        fence_is_closing = (
            fence is not None
            and active_fence_char == fence[0]
            and fence[1] >= active_fence_len
        )
        starts_block = is_heading(line) or fence_is_opening or (table and not previous_was_table)
        if starts_block and out and out[-1] != "":
            out.append("")

        if line == "":
            if out and out[-1] != "":
                out.append("")
            previous_was_table = False
            continue

        out.append(line)

        next_line = lines[index + 1] if index + 1 < len(lines) else None
        table_ends = table and (next_line is None or not is_table_line(next_line))
        if fence_is_opening and fence is not None:
            active_fence_char = fence[0]
            active_fence_len = fence[1]
        elif fence_is_closing:
            active_fence_char = None
            active_fence_len = 0
        should_have_blank_after = is_heading(line) or fence_is_closing or table_ends
        if should_have_blank_after and next_line is not None and next_line.strip():
            out.append("")
        previous_was_table = table

    collapsed: list[str] = []
    blank_count = 0
    for line in out:
        if line == "":
            blank_count += 1
            if blank_count <= 2:
                collapsed.append(line)
        else:
            blank_count = 0
            collapsed.append(line)

    return "\n".join(collapsed).strip() + "\n"


def analyze_frontmatter(lines: list[str]) -> list[dict[str, object]]:
    warnings: list[dict[str, object]] = []
    if not lines:
        return warnings
    if lines[0].startswith("--- ") and lines[0].strip() != "---":
        warnings.append(
            {
                "line": 1,
                "type": "single-line-frontmatter",
                "message": "YAML frontmatter must open with a line containing only '---'.",
            }
        )
    if lines[0].strip() == "---":
        closing = None
        for index, line in enumerate(lines[1:], start=2):
            if line.strip() == "---":
                closing = index
                break
        if closing is None:
            warnings.append(
                {
                    "line": 1,
                    "type": "unclosed-frontmatter",
                    "message": "YAML frontmatter is not closed.",
                }
            )
    return warnings


def analyze_markdown(text: str, max_line_length: int = DEFAULT_MAX_LINE_LENGTH) -> list[dict[str, object]]:
    warnings: list[dict[str, object]] = []
    lines = text.splitlines()
    warnings.extend(analyze_frontmatter(lines))

    previous_heading = 0
    first_heading_seen = False
    nonblank = 0
    list_lines = 0
    active_fence_char: str | None = None
    active_fence_len = 0
    fence_start: int | None = None

    for line_no, line in enumerate(lines, start=1):
        stripped = line.strip()
        fence = fence_info(line)
        if fence is not None:
            is_opening = active_fence_char is None
            is_closing = active_fence_char == fence[0] and fence[1] >= active_fence_len
            if is_opening:
                active_fence_char = fence[0]
                active_fence_len = fence[1]
                fence_start = line_no
                if not fence[2]:
                    warnings.append(
                        {
                            "line": line_no,
                            "type": "missing-code-language",
                            "message": "Code fence has no language label.",
                        }
                    )
            elif is_closing:
                active_fence_char = None
                active_fence_len = 0
                fence_start = None
            continue

        if active_fence_char is not None:
            continue

        if stripped:
            nonblank += 1
        if re.match(r"\s*([-*+]|\d+\.)\s+", line):
            list_lines += 1

        heading = re.match(r"^(#{1,6})\s+\S", line)
        if heading:
            level = len(heading.group(1))
            if not first_heading_seen:
                first_heading_seen = True
                if level != 1:
                    warnings.append(
                        {
                            "line": line_no,
                            "type": "first-heading-not-h1",
                            "message": "The first heading should be H1.",
                        }
                    )
            if previous_heading and level > previous_heading + 1:
                warnings.append(
                    {
                        "line": line_no,
                        "type": "heading-level-jump",
                        "message": f"Heading jumps from H{previous_heading} to H{level}.",
                    }
                )
            previous_heading = level

        if is_table_line(line):
            previous_line = lines[line_no - 2] if line_no > 1 else ""
            next_line = lines[line_no] if line_no < len(lines) else ""
            previous_is_table = line_no > 1 and is_table_line(previous_line)
            next_is_table = line_no < len(lines) and is_table_line(next_line)
            if not previous_is_table and previous_line.strip():
                warnings.append(
                    {
                        "line": line_no,
                        "type": "table-missing-leading-blank",
                        "message": "Table should have a blank line before it.",
                    }
                )
            if not next_is_table and next_line.strip():
                warnings.append(
                    {
                        "line": line_no,
                        "type": "table-missing-trailing-blank",
                        "message": "Table should have a blank line after it.",
                    }
                )

        if len(line) > max_line_length and not re.search(r"https?://", line):
            warnings.append(
                {
                    "line": line_no,
                    "type": "long-line",
                    "message": f"Line exceeds {max_line_length} characters.",
                    "length": len(line),
                }
            )

    if active_fence_char is not None:
        warnings.append(
            {
                "line": fence_start,
                "type": "unclosed-code-fence",
                "message": "Code fence is not closed.",
            }
        )

    if not first_heading_seen:
        warnings.append(
            {
                "line": None,
                "type": "missing-h1",
                "message": "Markdown file has no heading.",
            }
        )

    if nonblank and list_lines / nonblank > 0.85:
        warnings.append(
            {
                "line": None,
                "type": "list-density",
                "message": "More than 85% of nonblank lines are list items.",
            }
        )

    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize Markdown spacing and report issues.")
    parser.add_argument("input", help="Markdown file to normalize.")
    parser.add_argument("--output", "-o", help="Write normalized Markdown to this file.")
    parser.add_argument("--check", action="store_true", help="Only check whether normalization would change the file.")
    parser.add_argument("--report", help="Write JSON warning report to this file.")
    parser.add_argument("--fix", action="store_true", help="Write normalized Markdown. Uses --output or updates input.")
    parser.add_argument(
        "--max-line-length",
        type=int,
        default=DEFAULT_MAX_LINE_LENGTH,
        help="Maximum non-URL line length before warning.",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    original = input_path.read_text(encoding="utf-8")
    normalized = normalize_markdown(original)
    warnings = analyze_markdown(normalized, max_line_length=args.max_line_length)
    changed = normalized != original
    report = {"ok": not changed and not warnings, "changed": changed, "warnings": warnings}

    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    if args.check:
        print(json.dumps(report, ensure_ascii=False))
        return 1 if changed or warnings else 0

    if args.fix:
        output_path = Path(args.output) if args.output else input_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(normalized, encoding="utf-8", newline="\n")
        print(json.dumps(report, ensure_ascii=False))
        return 0 if not warnings else 1

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(normalized, encoding="utf-8", newline="\n")
    else:
        sys.stdout.write(normalized)
    return 0 if not warnings else 1


if __name__ == "__main__":
    raise SystemExit(main())
