#!/usr/bin/env python3
"""Small Pandoc wrapper for Markdown to docx/pdf rendering."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def build_command(args: argparse.Namespace, pandoc: str) -> list[str]:
    cmd = [pandoc, str(args.input), "-o", str(args.output)]

    if args.to == "docx":
        cmd.extend(["--to", "docx"])
        if args.reference_doc:
            cmd.extend(["--reference-doc", str(args.reference_doc)])

    if args.to == "pdf":
        if args.pdf_engine:
            cmd.extend(["--pdf-engine", args.pdf_engine])
        if args.template:
            cmd.extend(["--template", str(args.template)])

    for extra in args.extra_arg or []:
        cmd.append(extra)

    return cmd


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Markdown to docx or pdf through Pandoc.")
    parser.add_argument("input", type=Path, help="Input Markdown file.")
    parser.add_argument("--to", choices=["docx", "pdf"], required=True, help="Target output format.")
    parser.add_argument("--output", "-o", type=Path, required=True, help="Output file path.")
    parser.add_argument("--reference-doc", type=Path, help="Word reference.docx template.")
    parser.add_argument("--template", type=Path, help="PDF template path, reserved for Pandoc-compatible templates.")
    parser.add_argument("--pdf-engine", help="Pandoc PDF engine, for example xelatex or lualatex.")
    parser.add_argument("--extra-arg", action="append", help="Extra argument passed through to Pandoc.")
    parser.add_argument("--dry-run", action="store_true", help="Print the command without running it.")
    args = parser.parse_args()

    if not args.input.exists():
        print(json.dumps({"ok": False, "error": f"Input not found: {args.input}"}, ensure_ascii=False))
        return 2

    pandoc = shutil.which("pandoc")
    cmd = build_command(args, pandoc or "pandoc")
    if args.dry_run:
        print(
            json.dumps(
                {"ok": True, "pandoc_found": bool(pandoc), "command": cmd},
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    if not pandoc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": "Pandoc was not found on PATH. Install Pandoc or provide clean Markdown as the fallback artifact.",
                },
                ensure_ascii=False,
            )
        )
        return 127

    args.output.parent.mkdir(parents=True, exist_ok=True)
    completed = subprocess.run(cmd, text=True, capture_output=True, check=False)
    result = {
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "command": cmd,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "output": str(args.output),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
