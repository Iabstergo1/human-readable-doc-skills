# Workflow Examples

These examples show how the skill routes common requests and chooses references.
They are routing examples, not templates to copy verbatim into user output.

## Example 1: PDF Preprocessing Technical Design

User request:

```text
帮我写一份 PDF 预处理架构技术设计文档，输出 Markdown，后续转 Word 和 PDF。
```

| Field | Detected value |
| --- | --- |
| detected intent | Create a reusable technical design document. |
| document type | `technical-design` |
| target format | `Markdown`; later Word and PDF. |
| language | `zh-CN` |
| needs Markdown source | `true` |

References to load:

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- `references/03-anti-ai-slop-zh.md`
- `references/06-document-layout.md`
- `references/07-markdown-authoring.md`
- `references/08-word-export.md`
- `references/09-pdf-export.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

Scripts to run if file-based:

- `detect_doc_intent.py --pretty`
- `normalize_markdown.py --check --report`
- `validate_outputs.py --markdown`

Expected output shape:

```markdown

# PDF 预处理架构技术设计

## 背景与问题

## 目标与非目标

## 输入与输出

## 架构方案

## 处理流程

## 错误处理

## 性能与扩展性

## 验证计划

## 风险与下一步

```

## Example 2: Chinese AI-Style Report Revision

User request:

```text
把这段 AI 味很重的中文报告润色成人类更容易读懂的版本。
```

| Field | Detected value |
| --- | --- |
| detected intent | Revise and polish existing report text. |
| document type | `business-report` or `general-article`, depending on source content. |
| target format | Usually chat answer or Markdown. |
| language | `zh-CN` |
| needs Markdown source | `false` unless file-based or reusable output requested. |

References to load:

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- `references/03-anti-ai-slop-zh.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

Scripts to run if file-based:

- `lint_ai_style.py input.md --format json --pretty`
- `normalize_markdown.py input.md --check --report .\tmp\markdown-report.json`

Expected output shape:

- Revised text.
- Short note on preserved facts and any unsupported claims left unresolved.

## Example 3: Academic Model Explanation

User request:

```text
帮我生成一篇学术论文第三章的模型说明，注意符号统一。
```

| Field | Detected value |
| --- | --- |
| detected intent | Draft academic paper section. |
| document type | `academic-paper` |
| target format | Markdown by default. |
| language | `zh-CN` |
| needs Markdown source | `true` |

References to load:

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- `references/03-anti-ai-slop-zh.md`
- `references/05-academic-writing.md`
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

Scripts to run if file-based:

- `normalize_markdown.py --check --report`
- `validate_outputs.py --markdown`

Expected output shape:

```markdown

# 第三章 模型设定

## 概念界定

## 研究问题

## 符号与变量定义

## 模型设定

## 假设条件

## 机制解释

## 局限与待补充来源

```

## Example 4: GitHub README Rewrite

User request:

```text
把 README 写得更清楚，适合 GitHub 项目主页。
```

| Field | Detected value |
| --- | --- |
| detected intent | Rewrite project README. |
| document type | `README` |
| target format | Markdown. |
| language | Infer from source or user request. |
| needs Markdown source | `true` |

References to load:

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- language-specific anti-slop reference
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

Scripts to run if file-based:

- `normalize_markdown.py README.md --check --report .\tmp\readme-report.json`
- `lint_ai_style.py README.md --format json --pretty`

Expected output shape:

```markdown

# Project Name

## What This Solves

## What It Does Not Solve

## Installation

## Quick Start

## Usage

## Validation

## Limitations

## License

```

## Example 5: Meeting Notes

User request:

```text
输出一份会议纪要，包含决策、风险和 action items。
```

| Field | Detected value |
| --- | --- |
| detected intent | Create meeting notes. |
| document type | `meeting-notes` |
| target format | Markdown by default. |
| language | Mixed if the user wants `action items` retained. |
| needs Markdown source | `true` for reusable notes. |

References to load:

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- language-specific anti-slop reference
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

Scripts to run if file-based:

- `normalize_markdown.py --check --report`
- `validate_outputs.py --markdown`

Expected output shape:

```markdown

# 会议纪要

## 背景

## 决策

## 风险

## Action Items

## Open Questions

```

## Boundaries

Examples should not override the user's explicit instructions. If a request
contains source text, preserve its facts and mark missing information instead of
inventing details.
