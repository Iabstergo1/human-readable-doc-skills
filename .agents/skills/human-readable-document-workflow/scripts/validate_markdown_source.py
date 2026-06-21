#!/usr/bin/env python3
"""Validate clean Markdown source documents for handoff."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PLACEHOLDER_PATTERN = re.compile(
    r"TODO|FIXME|TKTK|\[待补充\]|\[citation needed\]",
    flags=re.IGNORECASE,
)


def is_table_line(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2


def frontmatter_bounds(lines: list[str]) -> tuple[int | None, int | None]:
    if not lines or lines[0].strip() != "---":
        return None, None
    for index, line in enumerate(lines[1:], start=2):
        if line.strip() == "---":
            return 1, index
    return 1, None


def inspect_markdown(path: Path, max_line_length: int = 180) -> list[dict[str, object]]:
    if not path.exists():
        return [{"path": str(path), "line": None, "issue": "markdown-file-not-found"}]

    issues: list[dict[str, object]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        return [{"path": str(path), "line": None, "issue": "markdown-empty"}]

    frontmatter_start, frontmatter_end = frontmatter_bounds(lines)
    if frontmatter_start is not None and frontmatter_end is None:
        issues.append({"path": str(path), "line": 1, "issue": "frontmatter-unclosed"})

    heading_seen = False
    in_code = False
    fence_start: int | None = None
    previous_heading_level = 0

    for line_no, line in enumerate(lines, start=1):
        stripped = line.strip()
        if PLACEHOLDER_PATTERN.search(line):
            issues.append(
                {
                    "path": str(path),
                    "line": line_no,
                    "issue": "placeholder",
                    "text": stripped,
                }
            )
        if re.match(r"^#\s+\S", line):
            heading_seen = True
        heading = re.match(r"^(#{1,6})\s+\S", line)
        if heading:
            level = len(heading.group(1))
            if previous_heading_level and level > previous_heading_level + 1:
                issues.append(
                    {
                        "path": str(path),
                        "line": line_no,
                        "issue": "skipped-heading-level",
                    }
                )
            previous_heading_level = level
        if stripped.startswith("```") or stripped.startswith("~~~"):
            if not in_code:
                in_code = True
                fence_start = line_no
            else:
                in_code = False
                fence_start = None
        if len(line) > max_line_length and not re.search(r"https?://", line):
            issues.append(
                {
                    "path": str(path),
                    "line": line_no,
                    "issue": "long-line",
                    "length": len(line),
                }
            )
        if is_table_line(line):
            previous_line = lines[line_no - 2] if line_no > 1 else ""
            next_line = lines[line_no] if line_no < len(lines) else ""
            if previous_line.strip() and not is_table_line(previous_line):
                issues.append(
                    {
                        "path": str(path),
                        "line": line_no,
                        "issue": "table-missing-leading-blank",
                    }
                )
            if next_line.strip() and not is_table_line(next_line):
                issues.append(
                    {
                        "path": str(path),
                        "line": line_no,
                        "issue": "table-missing-trailing-blank",
                    }
                )

    if in_code:
        issues.append(
            {
                "path": str(path),
                "line": fence_start,
                "issue": "unclosed-code-fence",
            }
        )
    if not heading_seen:
        issues.append({"path": str(path), "line": None, "issue": "missing-h1"})
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Markdown source before document handoff.")
    parser.add_argument("paths", nargs="+", type=Path, help="Markdown source files to scan.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    parser.add_argument("--max-line-length", type=int, default=180, help="Maximum non-URL Markdown line length.")
    args = parser.parse_args()

    markdown_issues: list[dict[str, object]] = []
    for path in args.paths:
        markdown_issues.extend(inspect_markdown(path, max_line_length=args.max_line_length))

    ok = not markdown_issues
    result = {
        "ok": ok,
        "markdown_issues": markdown_issues,
        "markdown_issue_count": len(markdown_issues),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
