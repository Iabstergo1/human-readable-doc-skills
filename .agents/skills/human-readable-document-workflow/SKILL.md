---
name: human-readable-document-workflow
description: >-
  Trigger when the user asks to create, draft, revise, polish, structure,
  export, typeset, or generate a document, report, article, paper, proposal,
  README, Markdown file, Word document, PDF, academic writing, technical
  documentation, business document, meeting notes, or other long-form written
  artifact. Do not trigger for short casual answers unless the user explicitly
  asks for a reusable document.
---

# Human Readable Document Workflow

Use this skill as the orchestration layer for long-form document work. Keep the
main file short: route the task, load only relevant references, use scripts for
deterministic checks, and deliver a readable source document before any rendered
artifact.

## Trigger Boundary

Use this skill when the user asks to create, draft, rewrite, polish, structure,
typeset, export, or validate a reusable document. Typical deliverables include
Markdown, Word, PDF, technical design docs, academic writing, reports,
proposals, README files, SOPs, meeting notes, and email drafts.

Do not use this skill for short casual answers, code-only implementation tasks,
or one-line rewrites unless the user explicitly wants a reusable document.

## Routing

First identify:

- `document_type`: use `references/12-document-type-profiles.md`.
- `language`: `zh-CN`, `en`, or `mixed`.
- `target_format`: `Markdown`, `docx`, `pdf`, `html`, `slides`, `chat answer`,
  or `unknown`.
- `source_boundary`: user-provided facts, missing sources, claims that need
  citation, and content that must not be changed.

Use `scripts/detect_doc_intent.py` when the request is file-based, ambiguous,
or likely to be repeated in automation.

## Reference Loading

Read only the references needed for the current task:

- Routing and defaults: `references/00-routing-policy.md`
- Writing loop: `references/01-writing-loop.md`
- General readability: `references/02-human-readable-style.md`
- Simplified Chinese anti-AI style: `references/03-anti-ai-slop-zh.md`
- English anti-AI style: `references/04-anti-ai-slop-en.md`
- Academic writing: `references/05-academic-writing.md`
- Layout rules: `references/06-document-layout.md`
- Markdown source rules: `references/07-markdown-authoring.md`
- Word export: `references/08-word-export.md`
- PDF export: `references/09-pdf-export.md`
- Final checks: `references/10-quality-gates.md`
- Upstream attribution: `references/11-upstream-attribution.md`
- Document type profiles: `references/12-document-type-profiles.md`
- Workflow examples: `references/13-workflow-examples.md`

## Four-Layer Framework

Apply these layers in order. Compress the visible process for short tasks, but
do not skip fact-boundary checks.

1. **Writing workflow layer**
   Load `references/01-writing-loop.md`. Important documents must pass through
   at least `plan -> draft -> critique -> revise`.

2. **Human-readable style and anti-AI layer**
   Load `references/02-human-readable-style.md` and the language-specific
   anti-slop reference:
   `references/03-anti-ai-slop-zh.md` for Chinese,
   `references/04-anti-ai-slop-en.md` for English, or both for mixed text.

3. **Document structure layer**
   Load the profile from `references/12-document-type-profiles.md`.
   Also load `references/05-academic-writing.md` for academic papers,
   literature reviews, thesis sections, model descriptions, citation work, or
   any text that uses scholarly claims, variables, symbols, or references.

4. **Rendering and layout layer**
   Load `references/06-document-layout.md`,
   `references/07-markdown-authoring.md`, and the export references needed for
   the requested artifacts:
   `references/08-word-export.md` for Word,
   `references/09-pdf-export.md` for PDF.

## Markdown Source Rule

Markdown is the canonical source for substantial documents. If the user asks for
Word or PDF, first produce or update a clean Markdown source draft, then render
or provide the render command. Do not treat `.docx` or `.pdf` as formats the
model should fake directly.

## Script Use

Use scripts when deterministic checks are useful:

- `scripts/detect_doc_intent.py`: classify document intent, type, language,
  target format, recommended references, and recommended scripts.
- `scripts/lint_ai_style.py`: scan file-based drafts for common AI-style
  patterns while protecting Markdown frontmatter, code fences, tables, URLs,
  quotes, and citations.
- `scripts/normalize_markdown.py`: check or fix Markdown spacing, frontmatter,
  headings, code fences, table spacing, long lines, and list density.
- `scripts/render_with_pandoc.py`: render Markdown to Word or PDF when Pandoc is
  available.
- `scripts/validate_outputs.py`: validate generated Markdown, docx, pdf, and
  obvious placeholders.
- `scripts/validate_skill.py`: validate this skill package after edits.

## Quality Gates

Before final delivery, load `references/10-quality-gates.md` and verify:

- The document matches the user's goal, reader, language, and target format.
- Facts, claims, citations, and assumptions stay inside the available source
  boundary.
- The prose is readable without forced casualness or obvious AI patterns.
- Markdown is renderable, with stable headings, tables, code blocks, captions,
  formulas, and links.
- Word/PDF requests have a Markdown source and either a rendered artifact or a
  clear local render command.

In the final answer, provide the artifact path, rendered output, or concise
summary the user needs. Do not expose the internal critique trace unless asked.
