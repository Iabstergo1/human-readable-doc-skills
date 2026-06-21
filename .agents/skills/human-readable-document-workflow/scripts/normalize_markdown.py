#!/usr/bin/env python3
"""Normalize Markdown spacing and report simple renderability issues."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def is_table_line(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2


def normalize_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    out: list[str] = []
    previous_was_table = False

    for line in lines:
        is_heading = bool(re.match(r"#{1,6}\s+\S", line))
        is_fence = line.startswith("```")
        is_table = is_table_line(line)

        if (is_heading or is_fence or (is_table and not previous_was_table)) and out and out[-1] != "":
            out.append("")

        out.append(line)

        if is_heading or is_fence:
            out.append("")
        previous_was_table = is_table

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

    normalized = "\n".join(collapsed).strip() + "\n"
    return normalized


def analyze_markdown(text: str) -> list[dict[str, object]]:
    warnings: list[dict[str, object]] = []
    previous_heading = 0
    nonblank = 0
    list_lines = 0

    for line_no, line in enumerate(text.splitlines(), start=1):
        if line.strip():
            nonblank += 1
        if re.match(r"\s*([-*+]|\d+\.)\s+", line):
            list_lines += 1

        heading = re.match(r"^(#{1,6})\s+\S", line)
        if heading:
            level = len(heading.group(1))
            if previous_heading and level > previous_heading + 1:
                warnings.append(
                    {
                        "line": line_no,
                        "type": "heading-level-jump",
                        "message": f"Heading jumps from H{previous_heading} to H{level}.",
                    }
                )
            previous_heading = level

        if line.strip() == "```":
            warnings.append(
                {
                    "line": line_no,
                    "type": "missing-code-language",
                    "message": "Code fence has no language label.",
                }
            )

    if nonblank and list_lines / nonblank > 0.6:
        warnings.append(
            {
                "line": None,
                "type": "list-density",
                "message": "More than 60% of nonblank lines are list items; consider paragraphs where appropriate.",
            }
        )

    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize Markdown spacing and report basic issues.")
    parser.add_argument("input", help="Markdown file to normalize.")
    parser.add_argument("--output", "-o", help="Write normalized Markdown to this file. Defaults to stdout.")
    parser.add_argument("--check", action="store_true", help="Only check whether normalization would change the file.")
    parser.add_argument("--report", help="Write JSON warning report to this file.")
    args = parser.parse_args()

    input_path = Path(args.input)
    original = input_path.read_text(encoding="utf-8")
    normalized = normalize_markdown(original)
    warnings = analyze_markdown(normalized)

    report = {"changed": normalized != original, "warnings": warnings}
    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    if args.check:
        print(json.dumps(report, ensure_ascii=False))
        return 1 if report["changed"] or warnings else 0

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(normalized, encoding="utf-8", newline="\n")
    else:
        sys.stdout.write(normalized)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
