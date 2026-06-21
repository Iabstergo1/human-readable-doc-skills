#!/usr/bin/env python3
"""Rule-based document-intent detector for the human-readable document workflow."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


BASE_REFERENCES = [
    "references/00-routing-policy.md",
    "references/01-writing-loop.md",
    "references/02-human-readable-style.md",
]

DOCUMENT_TRIGGERS = [
    "写",
    "撰写",
    "生成",
    "整理",
    "润色",
    "改写",
    "排版",
    "导出",
    "文档",
    "报告",
    "论文",
    "方案",
    "说明书",
    "会议纪要",
    "邮件",
    "write",
    "draft",
    "generate",
    "revise",
    "polish",
    "structure",
    "export",
    "typeset",
    "document",
    "report",
    "paper",
    "proposal",
    "manual",
    "readme",
    "meeting notes",
    "email",
]

FORMAT_RULES = {
    "Markdown": ["markdown", "md", ".md", "markdown 源稿", "输出 markdown"],
    "docx": ["docx", "word", ".docx", "word 文档"],
    "pdf": ["pdf", ".pdf"],
    "html": ["html", ".html", "网页"],
    "slides": ["slides", "ppt", "pptx", "deck", "幻灯片", "演示文稿"],
    "chat answer": ["直接回答", "聊天里", "chat answer"],
}

PROFILE_RULES = {
    "technical-design": [
        "技术设计",
        "架构",
        "architecture",
        "design doc",
        "pipeline",
        "data flow",
        "接口",
        "错误处理",
        "性能",
        "扩展性",
        "预处理",
    ],
    "README": ["readme", "github 项目主页", "repo docs", "installation", "usage", "quickstart"],
    "academic-paper": ["学术", "论文", "thesis", "academic paper", "模型", "变量", "符号", "citation"],
    "literature-review": ["文献综述", "literature review", "研究现状", "prior work"],
    "business-report": ["商业", "经营", "市场", "汇报", "business report", "strategy", "memo"],
    "proposal": ["方案", "计划书", "proposal", "project plan", "grant", "pitch"],
    "manual / SOP": ["sop", "manual", "说明书", "手册", "指南", "runbook", "procedure"],
    "meeting-notes": ["会议纪要", "会议记录", "meeting notes", "minutes", "action items"],
    "email": ["邮件", "email", "mail", "通知", "outreach", "follow-up"],
    "general-article": ["文章", "article", "blog", "explanation", "guide"],
}

EXPLICIT_FORMAT_TERMS = {
    "Markdown": r"markdown|md|\.md|markdown 源稿",
    "docx": r"word|docx|\.docx|word 文档",
    "pdf": r"pdf|\.pdf",
    "html": r"html|\.html|网页",
    "slides": r"slides|ppt|pptx|deck|幻灯片|演示文稿",
}

EXPORT_VERBS = (
    r"输出|导出|生成|产出|保存为|写成|整理成|"
    r"转成|转换为|渲染为|output|export|write as|save as|convert to|render to"
)

FUTURE_EXPORT_MARKERS = r"后续|之后|随后|later|afterward"


def read_text(args: argparse.Namespace) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8")
    if args.text:
        return " ".join(args.text)
    return sys.stdin.read()


def has_cjk(value: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", value))


def matched_terms(text: str, terms: list[str]) -> list[str]:
    lowered = text.lower()
    found: list[str] = []
    for term in terms:
        haystack = text if has_cjk(term) else lowered
        needle = term if has_cjk(term) else term.lower()
        if needle in haystack:
            found.append(term)
    return found


def choose_from_rules(text: str, rules: dict[str, list[str]], default: str) -> tuple[str, list[str]]:
    best_name = default
    best_matches: list[str] = []
    for name, terms in rules.items():
        matches = matched_terms(text, terms)
        if len(matches) > len(best_matches):
            best_name = name
            best_matches = matches
    return best_name, best_matches


def explicit_format_requested(text: str, name: str) -> bool:
    terms = EXPLICIT_FORMAT_TERMS[name]
    patterns = [
        rf"({EXPORT_VERBS})\s*(为|成|as|to)?\s*.{{0,16}}({terms})",
        rf"({FUTURE_EXPORT_MARKERS}).{{0,30}}({EXPORT_VERBS}).{{0,24}}({terms})",
        rf"({terms})\s*(文件|文档|版本|artifact|output)",
    ]
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def detect_target_format(text: str) -> tuple[str, list[str]]:
    for name in ["Markdown", "docx", "pdf", "html", "slides"]:
        if explicit_format_requested(text, name):
            return name, matched_terms(text, FORMAT_RULES[name])
    return "unknown", []


def detect_language(text: str) -> str:
    zh_chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    en_words = len(re.findall(r"[A-Za-z]{2,}", text))
    if zh_chars and en_words and zh_chars >= en_words * 2:
        return "zh-CN"
    if zh_chars and en_words:
        return "mixed"
    if zh_chars:
        return "zh-CN"
    if en_words:
        return "en"
    return "unknown"


def mentions_word(text: str) -> bool:
    return explicit_format_requested(text, "docx")


def mentions_pdf(text: str) -> bool:
    return explicit_format_requested(text, "pdf")


def recommended_references(
    *,
    language: str,
    document_type: str,
    target_format: str,
    text: str,
) -> list[str]:
    refs = list(BASE_REFERENCES)
    if language in {"zh-CN", "mixed"}:
        refs.append("references/03-anti-ai-slop-zh.md")
    if language in {"en", "mixed"}:
        refs.append("references/04-anti-ai-slop-en.md")
    if document_type in {"academic-paper", "literature-review"} or any(
        term in text for term in ["符号", "变量", "引用", "citation", "model"]
    ):
        refs.append("references/05-academic-writing.md")
    if target_format != "chat answer":
        refs.extend(
            [
                "references/06-document-layout.md",
                "references/07-markdown-authoring.md",
            ]
        )
    if target_format == "docx" or mentions_word(text):
        refs.append("references/08-word-export.md")
    if target_format == "pdf" or mentions_pdf(text):
        refs.append("references/09-pdf-export.md")
    refs.extend(
        [
            "references/10-quality-gates.md",
            "references/12-document-type-profiles.md",
        ]
    )
    return list(dict.fromkeys(refs))


def recommended_scripts(text: str, target_format: str) -> list[str]:
    scripts = ["scripts/detect_doc_intent.py"]
    if any(term in text.lower() for term in ["润色", "改写", "polish", "revise", "ai 味"]):
        scripts.append("scripts/lint_ai_style.py")
    if target_format in {"Markdown", "docx", "pdf"} or mentions_word(text) or mentions_pdf(text):
        scripts.append("scripts/normalize_markdown.py")
    if target_format in {"docx", "pdf"} or mentions_word(text) or mentions_pdf(text):
        scripts.append("scripts/render_with_pandoc.py")
    if target_format != "chat answer":
        scripts.append("scripts/validate_outputs.py")
    return list(dict.fromkeys(scripts))


def needs_markdown_source(is_document_task: bool, document_type: str, target_format: str, text: str) -> bool:
    if not is_document_task:
        return False
    if target_format in {"Markdown", "docx", "pdf", "html", "slides"}:
        return True
    if mentions_word(text) or mentions_pdf(text):
        return True
    return document_type not in {"email"} and target_format != "chat answer"


def confidence_score(
    text: str,
    trigger_matches: list[str],
    format_matches: list[str],
    type_matches: list[str],
) -> float:
    if not text.strip():
        return 0.0
    score = 0.18
    score += min(0.42, 0.08 * len(trigger_matches))
    score += min(0.2, 0.1 * len(format_matches))
    score += min(0.2, 0.08 * len(type_matches))
    if "文档" in text or "document" in text.lower():
        score += 0.08
    return round(min(score, 0.97), 2)


def detect(text: str) -> dict[str, object]:
    trigger_matches = matched_terms(text, DOCUMENT_TRIGGERS)
    target_format, format_matches = detect_target_format(text)
    document_type, type_matches = choose_from_rules(text, PROFILE_RULES, "general-article")
    is_document_task = bool(trigger_matches or format_matches or type_matches)
    if is_document_task and target_format == "unknown":
        target_format = "Markdown"
    language = detect_language(text)

    refs = recommended_references(
        language=language,
        document_type=document_type,
        target_format=target_format,
        text=text,
    )
    scripts = recommended_scripts(text, target_format)

    return {
        "is_document_task": is_document_task,
        "document_type": document_type,
        "language": language,
        "target_format": target_format,
        "confidence": confidence_score(text, trigger_matches, format_matches, type_matches),
        "matched_triggers": sorted(set(trigger_matches + format_matches + type_matches)),
        "recommended_references": refs,
        "recommended_scripts": scripts,
        "needs_markdown_source": needs_markdown_source(
            is_document_task, document_type, target_format, text
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect whether a user request is a document task.")
    parser.add_argument("text", nargs="*", help="Request text. If omitted, stdin is used.")
    parser.add_argument("--file", "-f", help="Read request text from a UTF-8 file.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    args = parser.parse_args()

    result = detect(read_text(args))
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
