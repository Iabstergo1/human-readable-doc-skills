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
MODE_CHOICES = ("document-safe", "creative-blog", "serious-review", "zh-source-safe")


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
    modes: tuple[str, ...] = ()


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
        r"game-changer|unlock the full potential|revolutionary|awesome|magical|magic\b",
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
    Rule(
        "zh-real-human-risk",
        "zh-CN",
        "zh-real-human-risk",
        "warning",
        r"嗯|呃|怎么说|说实话|我当时|其实有点|可能吧|就是.{0,8}吧|你要是问我",
        "文本可能是真人声口，直接去 AI 腔可能会损伤原意和语气。",
        "先停手或只做格式清理；如需改写，确认是改语体、简化、翻译还是摘要。",
        None,
        ("zh-source-safe",),
    ),
    Rule(
        "zh-register-downgrade",
        "zh-CN",
        "zh-register-downgrade",
        "warning",
        r"改得.{0,8}口语|别.{0,4}正式|像朋友聊天|去掉.{0,8}术语|小学生也能懂",
        "语体降级要求可能破坏正式文档的精确性。",
        "先确认目标语体；技术、学术、SOP 和公文类文本应保留必要正式性。",
        None,
        ("zh-source-safe", "serious-review"),
    ),
    Rule(
        "zh-over-sanitized",
        "zh-CN",
        "zh-over-sanitized",
        "info",
        r"完全中性|去掉.{0,8}个人|删掉.{0,8}口头|统一成客观|不要任何情绪",
        "过度消毒可能把真人文本改成无菌中性文。",
        "保留有信息量的个人判断、犹疑和真实语气，只删除模板化噪音。",
        None,
        ("zh-source-safe",),
    ),
    Rule(
        "en-detectorish-overcorrection",
        "en",
        "en-detectorish-overcorrection",
        "warning",
        r"AI detector|perplexity|burstiness|stylometry|make it less detectable|sentence fragments",
        "Detector-oriented rewriting can damage formal documents.",
        "Use document-safe cleanup unless the user explicitly requested creative or blog style.",
        None,
        ("document-safe", "creative-blog"),
    ),
    Rule(
        "en-tricolon-padding",
        "en",
        "tricolon-padding",
        "info",
        r"\b[A-Za-z][A-Za-z-]+,\s+[A-Za-z][A-Za-z-]+,\s+and\s+[A-Za-z][A-Za-z-]+\b",
        "Rule-of-three phrasing can become padded and automatic.",
        "Keep the list only when all three items are distinct and useful.",
        None,
        ("creative-blog", "document-safe"),
    ),
    Rule(
        "en-em-dash-overuse",
        "en",
        "em-dash-overuse",
        "info",
        r"—.{0,80}—|--.{0,80}--",
        "Repeated dash framing can make sentences sound machine-patterned.",
        "Keep a dash only when it clarifies interruption or apposition.",
        None,
        ("document-safe", "creative-blog"),
    ),
    Rule(
        "en-negative-parallelism",
        "en",
        "negative-parallelism",
        "info",
        r"not (just|merely|only).{0,50}but (also )?",
        "Negative parallelism can create contrast without a real distinction.",
        "Keep it only when the contrast defines a boundary, tradeoff, or mechanism.",
        None,
        ("creative-blog", "document-safe"),
    ),
    Rule(
        "en-false-range",
        "en",
        "false-range",
        "warning",
        r"everything in between|across every dimension|at every level|from .{1,30} to .{1,30} and beyond",
        "False ranges imply broad coverage without stating the real scope.",
        "List the actual scope or state the boundary.",
        None,
        ("creative-blog", "document-safe"),
    ),
    Rule(
        "en-bold-list-overuse",
        "en",
        "bold-list-overuse",
        "info",
        r"^\s*[-*]\s+\*\*(Key|Important|Note|Tip|Remember|First|Second|Third)[^*]{0,40}\*\*",
        "Repeated bold-header bullets can turn prose into a generic outline.",
        "Use bold labels only when they add real scanning structure.",
        None,
        ("creative-blog", "document-safe"),
    ),
    Rule(
        "serious-register-violation",
        "mixed",
        "serious-register-violation",
        "warning",
        r"awesome|super\b|magic|magically|crush it|no-brainer|🚀|✨|😊|牛逼|绝绝子|YYDS|拿捏|打工人",
        "Formal documents should avoid slang, emoji, hype, and forced friendliness.",
        "Use sober professional wording tied to observable behavior.",
        None,
        ("serious-review",),
    ),
    Rule(
        "software-anthropomorphism",
        "mixed",
        "serious-register-violation",
        "warning",
        r"system understand(?:s)?|tool understand(?:s)?|模型理解用户|系统理解用户|工具理解用户",
        "Anthropomorphized software descriptions blur actual system behavior.",
        "Describe the operation: classify, parse, predict, rank, match, or generate.",
        None,
        ("serious-review", "document-safe"),
    ),
    Rule(
        "style-content-leak",
        "mixed",
        "style-content-leak",
        "warning",
        r"reuse.{0,40}(customer|client|company|metric|facts)|copy.{0,40}(facts|names|example)|沿用.{0,20}(事实|客户名|公司名|数据|情节)",
        "Style samples must not donate facts, names, metrics, quotes, or plot events.",
        "Extract style traits only; use target-document facts for content.",
        None,
        MODE_CHOICES,
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


def rule_applies_to_mode(rule: Rule, mode: str) -> bool:
    return not rule.modes or mode in rule.modes


def should_skip_rule(rule: Rule, line: str, mode: str) -> bool:
    if mode == "document-safe" and rule.id == "en-tricolon-padding":
        has_formal_context = re.search(
            r"risk|cost|scope|speed|scale|security|accuracy|latency|inputs?|outputs?",
            line,
            flags=re.IGNORECASE,
        )
        if has_formal_context:
            return True

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


def lint_text(
    text: str,
    min_severity: str = "info",
    mode: str = "document-safe",
) -> list[dict[str, object]]:
    issues: list[dict[str, object]] = []
    protected = protected_lines(text)
    threshold = SEVERITY_ORDER[min_severity]
    for line_no, line in enumerate(text.splitlines(), start=1):
        if line_no in protected:
            continue
        for rule in RULES:
            if not rule_applies_to_mode(rule, mode):
                continue
            if SEVERITY_ORDER[rule.severity] < threshold:
                continue
            if should_skip_rule(rule, line, mode):
                continue
            if re.search(rule.pattern, line, flags=re.IGNORECASE):
                issues.append(
                    {
                        "line": line_no,
                        "rule": rule.id,
                        "severity": rule.severity,
                        "language": rule.language,
                        "category": rule.category,
                        "mode": mode,
                        "message": rule.message,
                        "suggestion": rule.suggestion,
                        "text": line.strip(),
                    }
                )
    return issues


def apply_fixes(text: str, mode: str = "document-safe") -> str:
    lines = text.splitlines()
    protected = protected_lines(text)
    fixed_lines: list[str] = []
    for line_no, line in enumerate(lines, start=1):
        fixed = line
        if line_no not in protected:
            for rule in RULES:
                if not rule_applies_to_mode(rule, mode):
                    continue
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
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Lint common AI-style phrases in text.")
    parser.add_argument("input", help="Markdown or text file to inspect.")
    parser.add_argument("--fix", action="store_true", help="Apply conservative removals/replacements.")
    parser.add_argument("--no-fix", action="store_true", help="Explicitly disable fixes. This is the default.")
    parser.add_argument("--output", "-o", help="Write fixed text to this file. Defaults to stdout with --fix.")
    parser.add_argument("--format", choices=["json", "text"], default="json", help="Output format.")
    parser.add_argument(
        "--mode",
        choices=MODE_CHOICES,
        default="document-safe",
        help="Anti-slop mode. Defaults to document-safe.",
    )
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
    issues = lint_text(text, min_severity=args.min_severity, mode=args.mode)

    if args.fix and not args.no_fix:
        fixed = apply_fixes(text, mode=args.mode)
        if args.output:
            Path(args.output).write_text(fixed, encoding="utf-8", newline="\n")
        else:
            sys.stdout.write(fixed)
        return 1 if issues else 0

    result = {"ok": not issues, "mode": args.mode, "issue_count": len(issues), "issues": issues}
    if args.format == "text":
        print(format_text(result))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
