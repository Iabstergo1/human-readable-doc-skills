#!/usr/bin/env python3
"""Detect common Chinese and English AI-style filler in Markdown or plain text."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


RULES = [
    {
        "id": "zh-grand-opening",
        "pattern": r"在当今|随着.*不断|数字化转型.*深入",
        "message": "中文宏大开头容易显得空泛。",
        "suggestion": "直接交代具体背景、对象和问题。",
        "replacement": "",
    },
    {
        "id": "zh-importance",
        "pattern": r"具有重要意义|深远意义|奠定坚实基础",
        "message": "意义句缺少具体对象和条件。",
        "suggestion": "改成对谁、在什么场景下、产生什么可观察影响。",
        "replacement": "有助于",
    },
    {
        "id": "zh-summary-cliche",
        "pattern": r"总而言之|综上所述",
        "message": "套话总结容易制造模板感。",
        "suggestion": "用具体限制、结论或下一步收束。",
        "replacement": "",
    },
    {
        "id": "zh-marketing",
        "pattern": r"全方位|革命性|极致|赋能|打造.*闭环",
        "message": "营销腔会削弱可信度。",
        "suggestion": "替换为机制、指标或可验证结果。",
        "replacement": "",
    },
    {
        "id": "en-generic-opening",
        "pattern": r"in today's fast-paced|ever-evolving landscape",
        "message": "Generic opening phrase.",
        "suggestion": "Start with the concrete problem or context.",
        "replacement": "",
    },
    {
        "id": "en-empty-enthusiasm",
        "pattern": r"game-changer|unlock the full potential|seamless experience",
        "message": "Empty enthusiasm or corporate filler.",
        "suggestion": "Describe the mechanism or observable outcome.",
        "replacement": "",
    },
    {
        "id": "en-overhedging",
        "pattern": r"it is important to note that|may potentially",
        "message": "Over-hedging weakens the sentence.",
        "suggestion": "State the condition or claim directly.",
        "replacement": "",
    },
]


def lint_text(text: str) -> list[dict[str, object]]:
    issues: list[dict[str, object]] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        for rule in RULES:
            if re.search(rule["pattern"], line, flags=re.IGNORECASE):
                issues.append(
                    {
                        "line": line_no,
                        "rule": rule["id"],
                        "message": rule["message"],
                        "suggestion": rule["suggestion"],
                        "text": line.strip(),
                    }
                )
    return issues


def apply_fixes(text: str) -> str:
    fixed = text
    for rule in RULES:
        replacement = rule.get("replacement")
        if replacement is not None:
            fixed = re.sub(rule["pattern"], str(replacement), fixed, flags=re.IGNORECASE)
    fixed = re.sub(r"[ \t]+\n", "\n", fixed)
    return fixed


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint common AI-style phrases in text.")
    parser.add_argument("input", help="Markdown or text file to inspect.")
    parser.add_argument("--fix", action="store_true", help="Apply conservative phrase removal/replacement.")
    parser.add_argument("--output", "-o", help="Write fixed text to this file. Defaults to stdout when --fix is used.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON lint output.")
    args = parser.parse_args()

    input_path = Path(args.input)
    text = input_path.read_text(encoding="utf-8")
    issues = lint_text(text)

    if args.fix:
        fixed = apply_fixes(text)
        if args.output:
            Path(args.output).write_text(fixed, encoding="utf-8", newline="\n")
        else:
            sys.stdout.write(fixed)
        return 1 if issues else 0

    result = {"ok": not issues, "issue_count": len(issues), "issues": issues}
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
