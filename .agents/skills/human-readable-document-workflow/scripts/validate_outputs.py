#!/usr/bin/env python3
"""Validate generated document artifacts."""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path


PLACEHOLDER_PATTERN = re.compile(
    r"TODO|FIXME|TKTK|\[待补充\]|\[citation needed\]",
    flags=re.IGNORECASE,
)


def is_table_line(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2


def inspect_file(path: Path) -> dict[str, object]:
    exists = path.exists()
    size = path.stat().st_size if exists else 0
    issues: list[str] = []
    if not exists:
        issues.append("file-not-found")
    elif size == 0:
        issues.append("file-empty")
    elif path.suffix.lower() == ".docx":
        if not zipfile.is_zipfile(path):
            issues.append("docx-not-zip")
        else:
            with zipfile.ZipFile(path) as archive:
                names = set(archive.namelist())
            if "word/document.xml" not in names:
                issues.append("docx-missing-word-document")
    elif path.suffix.lower() == ".pdf":
        with path.open("rb") as handle:
            header = handle.read(4)
        if header != b"%PDF":
            issues.append("pdf-header-invalid")
    return {
        "path": str(path),
        "exists": exists,
        "size": size,
        "issues": issues,
        "ok": not issues,
    }


def inspect_markdown(path: Path, max_line_length: int = 180) -> list[dict[str, object]]:
    if not path.exists():
        return [{"path": str(path), "line": None, "issue": "markdown-file-not-found"}]

    issues: list[dict[str, object]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    heading_seen = False
    in_code = False
    fence_start: int | None = None

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
    parser = argparse.ArgumentParser(description="Validate generated files and Markdown placeholders.")
    parser.add_argument("paths", nargs="*", type=Path, help="Files that should exist and be non-empty.")
    parser.add_argument("--markdown", action="append", type=Path, default=[], help="Markdown file to scan.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    parser.add_argument("--max-line-length", type=int, default=180, help="Maximum non-URL Markdown line length.")
    args = parser.parse_args()

    files = [inspect_file(path) for path in args.paths]
    markdown_issues: list[dict[str, object]] = []
    for path in args.markdown:
        markdown_issues.extend(inspect_markdown(path, max_line_length=args.max_line_length))

    ok = all(item["ok"] for item in files) and not markdown_issues
    result = {
        "ok": ok,
        "files": files,
        "markdown_issues": markdown_issues,
        "markdown_issue_count": len(markdown_issues),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
