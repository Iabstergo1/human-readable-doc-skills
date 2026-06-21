#!/usr/bin/env python3
"""Rule-based document-intent detector for the human-readable document workflow."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


TRIGGERS = [
    "写",
    "撰写",
    "生成",
    "整理",
    "润色",
    "排版",
    "导出",
    "文档",
    "报告",
    "论文",
    "方案",
    "说明书",
    "会议纪要",
    "简历",
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
    "Markdown": ["markdown", "md", ".md"],
    "docx": ["docx", "word", ".docx"],
    "pdf": ["pdf", ".pdf"],
    "html": ["html", ".html", "网页"],
    "slides": ["slides", "ppt", "pptx", "deck", "幻灯片", "演示文稿"],
    "chat answer": ["直接回答", "聊天里", "chat answer"],
}

TYPE_RULES = {
    "technical": ["技术", "架构", "接口", "API", "部署", "design doc", "architecture"],
    "academic": ["学术", "论文", "文献", "citation", "paper", "thesis"],
    "business": ["商业", "经营", "市场", "汇报", "business", "strategy", "memo"],
    "proposal": ["方案", "计划书", "proposal", "project plan"],
    "manual": ["说明书", "手册", "指南", "SOP", "manual", "guide"],
    "README": ["README", "readme", "安装", "usage", "repository"],
    "meeting-notes": ["会议纪要", "会议记录", "meeting notes", "minutes", "action items"],
    "email": ["邮件", "email", "mail", "通知"],
}


def read_text(args: argparse.Namespace) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8")
    if args.text:
        return " ".join(args.text)
    return sys.stdin.read()


def matched_terms(text: str, terms: list[str]) -> list[str]:
    lowered = text.lower()
    found: list[str] = []
    for term in terms:
        haystack = text if re.search(r"[\u4e00-\u9fff]", term) else lowered
        needle = term if re.search(r"[\u4e00-\u9fff]", term) else term.lower()
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


def detect_target_format(text: str) -> tuple[str, list[str]]:
    lowered = text.lower()
    explicit_patterns = [
        ("Markdown", r"(输出|导出|生成|产出|保存为|output|export|write as)\s*(为|成|as)?\s*(markdown|md|\.md)"),
        ("docx", r"(输出|导出|生成|产出|保存为|output|export|write as)\s*(为|成|as)?\s*(word|docx|\.docx)"),
        ("pdf", r"(输出|导出|生成|产出|保存为|output|export|write as)\s*(为|成|as)?\s*(pdf|\.pdf)"),
        ("html", r"(输出|导出|生成|产出|保存为|output|export|write as)\s*(为|成|as)?\s*(html|\.html|网页)"),
    ]
    for name, pattern in explicit_patterns:
        if re.search(pattern, lowered, flags=re.IGNORECASE):
            return name, matched_terms(text, FORMAT_RULES[name])
    return choose_from_rules(text, FORMAT_RULES, "unknown")


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


def detect(text: str) -> dict[str, object]:
    trigger_matches = matched_terms(text, TRIGGERS)
    target_format, format_matches = detect_target_format(text)
    document_type, type_matches = choose_from_rules(text, TYPE_RULES, "general")

    is_document_task = bool(trigger_matches or format_matches or type_matches)
    score = 0.15
    if trigger_matches:
        score += min(0.45, 0.12 * len(trigger_matches))
    if format_matches:
        score += 0.2
    if type_matches:
        score += 0.15
    if not text.strip():
        score = 0.0

    return {
        "is_document_task": is_document_task,
        "document_type": document_type,
        "language": detect_language(text),
        "target_format": target_format,
        "confidence": round(min(score, 0.95), 2),
        "matched_triggers": sorted(set(trigger_matches + format_matches + type_matches)),
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
