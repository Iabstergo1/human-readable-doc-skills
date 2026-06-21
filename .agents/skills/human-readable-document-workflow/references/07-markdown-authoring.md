# Markdown Authoring

Use Markdown as the canonical source for document generation. Good Markdown is
readable in raw form, reviewable in Git, and renderable to Word or PDF.

## Supported Structure

| Feature | Rule |
| --- | --- |
| YAML frontmatter | Use for title, author, date, abstract, keywords, and renderer hints. |
| Headings | Start with H1; do not skip levels. |
| Paragraphs | Wrap naturally; avoid single-line mega paragraphs. |
| Lists | Keep nesting shallow. |
| Code blocks | Use fenced blocks with language labels. |
| Tables | Keep simple and add surrounding blank lines. |
| Links | Use inline links for one-off sources, reference links for repeated sources. |
| Quotes | Use block quotes for source material and preserve wording. |
| Footnotes | Use when notes would interrupt the main argument. |
| Images | Add alt text and a caption or explanation. |
| Formulas | Use renderer-compatible math and explain symbols. |

## YAML Frontmatter

Example:

```yaml
---
title: "PDF Preprocessing Architecture"
author: "Team Name"
date: "2026-06-21"
keywords:
  - PDF
  - OCR
  - preprocessing
---
```

Rules:

- Frontmatter must start at the first line.
- Frontmatter must close with a second `---`.
- Do not use single-line frontmatter.
- Do not rewrite frontmatter during style cleanup unless the user asks.

## Markdown Hygiene

- Do not use manual spaces to align layout.
- Do not use tables for two-column page design.
- Do not leave unclosed code fences.
- Do not omit code fence languages when the language is known.
- Do not rely on embedded HTML unless the renderer route requires it.
- Keep renderer-specific syntax documented near the command or in the file.

## PowerShell Commands

Check a Markdown file:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\normalize_markdown.py `
  .\draft.md --check --report .\tmp\markdown-report.json
```

Write a normalized copy:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\normalize_markdown.py `
  .\draft.md --fix --output .\draft.normalized.md
```

## Examples

Good:

````markdown

# PDF Preprocessing Architecture

## Inputs

The pipeline accepts text PDFs, scanned PDFs, and mixed PDFs.

```powershell

python .\scripts\preprocess.py --input .\sample.pdf

```
````

Bad:

````markdown

# PDF Preprocessing Architecture

### Inputs

````

The bad version skips heading levels and gives no body content.

## Boundaries

Markdown is not a full layout language. Put page size, margins, fonts, and
headers in Word reference documents, Quarto config, Typst templates, or Pandoc
options.
