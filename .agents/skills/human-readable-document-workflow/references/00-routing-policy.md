# Routing Policy

Use this file to decide whether the document workflow should run, how to choose
a document type, and which references to load first.

## Trigger Scope

Trigger when the user asks for a reusable written artifact rather than a short
chat answer.

| Signal group | Common triggers | Route |
| --- | --- | --- |
| Creation | 写, 撰写, 生成, draft, write, generate | Run intake and profile selection. |
| Revision | 润色, 改写, polish, revise, humanize | Preserve source facts and run style checks. |
| Structure | 结构化, 大纲, organize, outline | Load the document type profile before drafting. |
| Export | Word, docx, PDF, Markdown, render, typeset | Treat Markdown as canonical source. |
| Validation | 检查, 质量, lint, validate | Run deterministic scripts when a file exists. |

## Do Not Trigger

Do not trigger for tasks whose primary deliverable is not a document.

| Non-trigger | Boundary |
| --- | --- |
| Short answer | A one-paragraph explanation does not need this skill. |
| Code implementation | Use normal coding workflow unless the user asks for docs. |
| Data calculation | Use this skill only when a written report is requested. |
| Slide design | Use this skill only for speaker notes or document-like source. |
| Translation only | Use this skill only if the result needs document structure. |

## Document Type Mapping

Prefer the more specific type when multiple signals appear. Use
`references/12-document-type-profiles.md` for full profile rules.

| Signals | Type |
| --- | --- |
| architecture, design doc, 技术设计, 架构, 接口, 数据流 | `technical-design` |
| README, repo docs, installation, usage, 项目主页 | `README` |
| paper, thesis, 论文, 模型, 变量, citation | `academic-paper` |
| literature review, 文献综述, 研究现状 | `literature-review` |
| business report, 汇报, 经营分析, market | `business-report` |
| proposal, 方案, 计划书, grant, pitch | `proposal` |
| manual, SOP, 操作手册, 指南, runbook | `manual / SOP` |
| meeting notes, 会议纪要, action items | `meeting-notes` |
| email, 邮件, 通知, outreach | `email` |
| article, blog, 文章, no strong signal | `general-article` |

## Format Defaults

| Request | Default |
| --- | --- |
| No format specified | Markdown. |
| Word requested | Markdown source plus `.docx` render path or artifact. |
| PDF requested | Markdown source plus PDF render path or artifact. |
| Word and PDF requested | One Markdown source, then render both artifacts. |
| Chat-only requested | Concise answer, with internal fact-boundary checks. |

## Examples

User: "帮我写一份 PDF 预处理架构技术设计文档，输出 Markdown。"

Route: document task, `technical-design`, `zh-CN`, `Markdown`; load routing,
writing loop, readability, Chinese anti-slop, layout, Markdown, quality gates,
and document type profiles.

User: "这个变量名怎么改？"

Route: not a document task unless the user asks for a style guide or README
update.

## Boundaries

Ask a clarification only when the missing answer changes the document itself:
audience, required format, source material, citation source, legal/medical risk,
or whether a public-facing document may mention private facts. Otherwise state a
reasonable assumption and continue.
