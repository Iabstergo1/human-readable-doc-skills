# Routing Policy

## Trigger This Skill

Use this skill when the user asks to create, draft, revise, polish, structure, format, export, typeset, or generate a reusable document or long-form written artifact.

Common triggers include:

- Chinese: 写、撰写、生成、整理、润色、排版、导出、报告、论文、方案、说明书、会议纪要、简历、邮件、Markdown、Word、PDF。
- English: write, draft, generate, revise, polish, structure, export, typeset, report, paper, proposal, manual, README, meeting notes, email, Markdown, Word, PDF.

## Do Not Trigger

Do not use this skill for:

- Short casual answers.
- One-line rewrites with no document intent.
- Code-only tasks where the deliverable is source code, not a document.
- Data analysis where the user wants only a calculation or chart, not a written artifact.
- Slide decks unless the user asks for the written source, speaker notes, or document-like narrative.

## Document Type Mapping

| Signals | Type |
| --- | --- |
| architecture, API, design doc, 技术设计, 接口, 部署 | `technical` |
| paper, thesis, literature, citation, 论文, 学术, 文献 | `academic` |
| business, memo, market, strategy, 商业, 经营, 汇报 | `business` |
| proposal, plan, project plan, 方案, 计划书 | `proposal` |
| manual, guide, SOP, instructions, 说明书, 手册 | `manual` |
| README, repo docs, installation, usage | `README` |
| meeting, minutes, action items, 会议纪要 | `meeting-notes` |
| email, message, outreach, 邮件, 通知 | `email` |
| no strong signal | `general` |

## Format Defaults

- If the user only says "帮我写个文档", default to Markdown.
- If the user asks for Word or PDF, first create structured Markdown source, then provide or run the rendering path.
- If the user asks for chat-only output, keep the answer concise but still apply the writing loop internally.
- If the user gives no language, infer from the request and source material.

## Clarification Policy

Ask only when missing information would materially change the document. Otherwise, state the assumption and proceed.
