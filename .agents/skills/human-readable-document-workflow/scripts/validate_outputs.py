#!/usr/bin/env python3
"""Validate generated document artifacts."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PLACEHOLDER_PATTERN = re.compile(
    r"TODO|TBD|FIXME|\[待补充\]|\[citation needed\]|<[^>\n]{1,80}>",
    flags=re.IGNORECASE,
)


def inspect_file(path: Path) -> dict[str, object]:
    exists = path.exists()
    size = path.stat().st_size if exists else 0
    return {"path": str(path), "exists": exists, "size": size, "ok": exists and size > 0}


def inspect_markdown(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return [{"path": str(path), "line": None, "issue": "markdown-file-not-found"}]

    issues: list[dict[str, object]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if PLACEHOLDER_PATTERN.search(line):
            issues.append({"path": str(path), "line": line_no, "issue": "placeholder", "text": line.strip()})
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generated files and Markdown placeholders.")
    parser.add_argument("paths", nargs="*", type=Path, help="Files that should exist and be non-empty.")
    parser.add_argument("--markdown", action="append", type=Path, default=[], help="Markdown file to scan for placeholders.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    args = parser.parse_args()

    files = [inspect_file(path) for path in args.paths]
    markdown_issues: list[dict[str, object]] = []
    for path in args.markdown:
        markdown_issues.extend(inspect_markdown(path))

    ok = all(item["ok"] for item in files) and not markdown_issues
    result = {"ok": ok, "files": files, "markdown_issues": markdown_issues}
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
