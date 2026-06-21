#!/usr/bin/env python3
"""Detect common Chinese and English AI-style filler in Markdown or plain text."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SEVERITY_ORDER = {"info": 0, "warning": 1, "error": 2}


@dataclass(frozen=True)
class Rule:
    id: str
    language: str
    category: str
    severity: str
    pattern: str
    message: str
    suggestion: str
    replacement: str | None = None


RULES = [
    Rule(
        "zh-grand-opening",
        "zh-CN",
        "generic-opening",
        "warning",
        r"在当今|随着.{0,12}(不断|深入|发展)|数字化转型.{0,8}深入",
        "中文宏大开头容易用时代背景替代具体问题。",
        "直接交代对象、场景、痛点和约束。",
        "",
    ),
    Rule(
        "zh-empty-significance",
        "zh-CN",
        "empty-significance",
        "warning",
        r"具有重要意义|意义重大|深远意义|奠定.{0,8}基础",
        "意义句缺少对象、条件和可观察影响。",
        "改成具体收益、适用边界或待验证假设。",
        "",
    ),
    Rule(
        "zh-mechanical-transition",
        "zh-CN",
        "mechanical-structure",
        "info",
        r"首先|其次|最后|总而言之|综上所述",
        "机械转折可能制造模板感。",
        "用因果、对比、依赖或限制关系连接段落。",
        "",
    ),
    Rule(
        "zh-false-depth",
        "zh-CN",
        "false-depth",
        "warning",
        r"不仅.{0,12}更是|不是.{0,12}而是|不只是.{0,12}也是",
        "伪深刻二分法可能没有解释真实差异。",
        "说明两个对象的机制差异、证据或后果。",
        None,
    ),
    Rule(
        "zh-marketing-tone",
        "zh-CN",
        "marketing-tone",
        "warning",
        r"全方位|革命性|极致|赋能|打造.{0,12}闭环|领先",
        "营销腔会削弱技术或报告可信度。",
        "替换为机制、指标、功能边界或用户动作。",
        "",
    ),
    Rule(
        "zh-flattery-service",
        "zh-CN",
        "service-tone",
        "info",
        r"您提出的.{0,12}非常重要|非常荣幸|希望.{0,8}帮助到您|感谢您的信任",
        "客服式客套可能不适合专业文档。",
        "删除多余客套，直接交代处理结果或建议。",
        "",
    ),
    Rule(
        "zh-bureaucratic",
        "zh-CN",
        "bureaucratic-misuse",
        "info",
        r"高度重视|扎实推进|统筹协调|落实落细|形成合力",
        "公文套话可能替代具体责任和动作。",
        "写清执行者、动作、时间和交付物。",
        None,
    ),
    Rule(
        "zh-unsourced-claim",
        "zh-CN",
        "unsupported-claim",
        "warning",
        r"显然|众所周知|业界普遍认为|大量实践表明",
        "无来源判断会把假设包装成事实。",
        "补来源；没有来源时改成假设或待验证项。",
        None,
    ),
    Rule(
        "en-generic-opening",
        "en",
        "generic-opening",
        "warning",
        r"in today's fast-paced|ever-evolving landscape|in the modern era",
        "Generic opening delays the actual problem.",
        "Start with the concrete object, constraint, or reader problem.",
        "",
    ),
    Rule(
        "en-corporate-filler",
        "en",
        "corporate-filler",
        "warning",
        r"\b(seamless|robust|leverage|streamline|best-in-class)\b",
        "Corporate filler can sound polished without adding information.",
        "Replace with mechanism, measurable effect, or boundary.",
        None,
    ),
    Rule(
        "en-empty-enthusiasm",
        "en",
        "empty-enthusiasm",
        "warning",
        r"game-changer|unlock the full potential|revolutionary",
        "Empty enthusiasm overpromises without evidence.",
        "State the observable improvement and condition.",
        "",
    ),
    Rule(
        "en-overhedging",
        "en",
        "over-hedging",
        "info",
        r"it is important to note that|may potentially|could possibly",
        "Over-hedging weakens clear claims.",
        "Name the condition directly.",
        "",
    ),
    Rule(
        "en-template-conclusion",
        "en",
        "template-conclusion",
        "info",
        r"\bin conclusion\b|ultimately,? this highlights|the future is bright",
        "Template conclusions often repeat the introduction generically.",
        "End with a decision, risk, limitation, or next step.",
        "",
    ),
]


def is_table_line(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2


def protected_lines(text: str) -> set[int]:
    protected: set[int] = set()
    lines = text.splitlines()
    in_frontmatter = False
    in_code = False

    for index, line in enumerate(lines, start=1):
        stripped = line.strip()
        if index == 1 and stripped == "---":
            in_frontmatter = True
            protected.add(index)
            continue
        if in_frontmatter:
            protected.add(index)
            if stripped == "---":
                in_frontmatter = False
            continue
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code = not in_code
            protected.add(index)
            continue
        if in_code:
            protected.add(index)
            continue
        if is_table_line(line):
            protected.add(index)
            continue
        if re.search(r"https?://|www\.", line):
            protected.add(index)
            continue
        if re.match(r"\s*>", line):
            protected.add(index)
            continue
        if re.search(r"\[[^\]]+\]\([^)]+\)|\[[A-Za-z][^\]]{0,80}\]", line):
            protected.add(index)
            continue
    return protected


def should_skip_rule(rule: Rule, line: str) -> bool:
    if rule.id == "zh-mechanical-transition":
        has_order_marker = re.search(r"首先|其次|最后", line)
        has_ordered_context = re.search(
            r"令|表示|定义|变量|假设|模型|命题|证明|步骤|阶段|流程|procedure|step",
            line,
            flags=re.IGNORECASE,
        )
        if has_order_marker and has_ordered_context:
            return True

    if rule.id == "zh-false-depth":
        is_boundary_contrast = re.search(r"不是.{0,24}而是", line)
        has_boundary_context = re.search(
            r"目标|非目标|定义|边界|输入|输出|数据|记录|变量|模型|状态|schema|任务|职责",
            line,
            flags=re.IGNORECASE,
        )
        if is_boundary_contrast and has_boundary_context:
            return True

    return False


def lint_text(text: str, min_severity: str = "info") -> list[dict[str, object]]:
    issues: list[dict[str, object]] = []
    protected = protected_lines(text)
    threshold = SEVERITY_ORDER[min_severity]
    for line_no, line in enumerate(text.splitlines(), start=1):
        if line_no in protected:
            continue
        for rule in RULES:
            if SEVERITY_ORDER[rule.severity] < threshold:
                continue
            if should_skip_rule(rule, line):
                continue
            if re.search(rule.pattern, line, flags=re.IGNORECASE):
                issues.append(
                    {
                        "line": line_no,
                        "rule": rule.id,
                        "severity": rule.severity,
                        "language": rule.language,
                        "category": rule.category,
                        "message": rule.message,
                        "suggestion": rule.suggestion,
                        "text": line.strip(),
                    }
                )
    return issues


def apply_fixes(text: str) -> str:
    lines = text.splitlines()
    protected = protected_lines(text)
    fixed_lines: list[str] = []
    for line_no, line in enumerate(lines, start=1):
        fixed = line
        if line_no not in protected:
            for rule in RULES:
                if rule.replacement is not None:
                    fixed = re.sub(rule.pattern, rule.replacement, fixed, flags=re.IGNORECASE)
            fixed = re.sub(r"[ \t]+$", "", fixed)
        fixed_lines.append(fixed)
    return "\n".join(fixed_lines).strip() + "\n"


def format_text(result: dict[str, object]) -> str:
    if result["ok"]:
        return "ok: no issues found"
    lines = [f"issues: {result['issue_count']}"]
    for issue in result["issues"]:
        lines.append(
            f"{issue['line']}: {issue['severity']} {issue['rule']} "
            f"({issue['category']}) - {issue['message']}"
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint common AI-style phrases in text.")
    parser.add_argument("input", help="Markdown or text file to inspect.")
    parser.add_argument("--fix", action="store_true", help="Apply conservative removals/replacements.")
    parser.add_argument("--no-fix", action="store_true", help="Explicitly disable fixes. This is the default.")
    parser.add_argument("--output", "-o", help="Write fixed text to this file. Defaults to stdout with --fix.")
    parser.add_argument("--format", choices=["json", "text"], default="json", help="Output format.")
    parser.add_argument(
        "--min-severity",
        choices=["info", "warning", "error"],
        default="info",
        help="Minimum severity to report.",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON lint output.")
    args = parser.parse_args()

    input_path = Path(args.input)
    text = input_path.read_text(encoding="utf-8")
    issues = lint_text(text, min_severity=args.min_severity)

    if args.fix and not args.no_fix:
        fixed = apply_fixes(text)
        if args.output:
            Path(args.output).write_text(fixed, encoding="utf-8", newline="\n")
        else:
            sys.stdout.write(fixed)
        return 1 if issues else 0

    result = {"ok": not issues, "issue_count": len(issues), "issues": issues}
    if args.format == "text":
        print(format_text(result))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
