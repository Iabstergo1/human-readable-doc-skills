---
name: human-readable-document-workflow
description: Trigger when the user asks to create, draft, revise, polish, structure, export, typeset, or generate a document, report, article, paper, proposal, README, Markdown file, Word document, PDF, academic writing, technical documentation, business document, meeting notes, or other long-form written artifact. Do not trigger for short casual answers unless the user explicitly asks for a reusable document.
---

# Human Readable Document Workflow

Use this skill as the orchestration layer for long-form document work. Keep detailed rules in `references/` and use scripts for deterministic checks or rendering steps.

## Reference Loading

Read only the references needed for the task:

- Routing and defaults: `references/00-routing-policy.md`
- Writing loop: `references/01-writing-loop.md`
- General readability: `references/02-human-readable-style.md`
- Simplified Chinese style cleanup: `references/03-anti-ai-slop-zh.md`
- English style cleanup: `references/04-anti-ai-slop-en.md`
- Academic writing: `references/05-academic-writing.md`
- Layout rules: `references/06-document-layout.md`
- Markdown source rules: `references/07-markdown-authoring.md`
- Word export: `references/08-word-export.md`
- PDF export: `references/09-pdf-export.md`
- Final checks: `references/10-quality-gates.md`

## 0. Detect Document Intent

Determine whether the user asks to generate, draft, organize, revise, export, typeset, or polish a document.

Identify:

- Target format: `chat answer`, `Markdown`, `docx`, `pdf`, `html`, `slides`, or `unknown`.
- Document type: `technical`, `academic`, `business`, `proposal`, `manual`, `README`, `meeting-notes`, `email`, or `general`.
- Language: `zh-CN`, `en`, or `mixed`.

If information is missing but work can start, choose reasonable defaults and continue. Do not repeatedly ask clarification questions.

Use `scripts/detect_doc_intent.py` when deterministic routing is useful.

## 1. Intake

Extract the user's goal, reader, use case, length, format, tone, source material, required content, and content that must not be changed.

If the user provides source text, preserve its facts and do not invent unsupported details. If the user asks for Word or PDF, first produce structured Markdown source, then use the layout/export path.

## 2. Frame

State the document's problem, reader concerns, and delivery boundary.

Avoid generic framing such as "本文将深入探讨" or "具有重要意义". For technical documents, prioritize `what / why / how / caveats / next steps`. For academic documents, prioritize concept definitions, consistent notation, and complete argument chains.

## 3. Plan

Create a short structure plan before drafting.

Keep heading depth shallow. Prefer paragraphs; use lists only when scanning is clearly better. For Markdown, Word, and PDF outputs, ensure headings, tables, code blocks, image captions, citations, and appendices can be rendered reliably.

## 4. Draft

Write clear, natural, readable prose.

Avoid obvious AI style: no preachy tone, empty grand conclusions, repeated `first / second / finally`, mechanical parallelism, or unsupported broad claims. For Chinese, default to concise and concrete paragraphs with natural sentence variation. For technical content, accuracy and actionability are primary. For academic content, conceptual clarity, rigor, and notation consistency are primary.

## 5. Critique

Check the draft for:

- Abstract filler or vague adjectives.
- Common AI cliches.
- Preachy endings.
- Clickbait or marketing tone.
- Excessive lists.
- Logical jumps.
- Unsupported factual expansion.
- Confusing Markdown hierarchy.
- Structures that Word/PDF renderers cannot handle reliably.

Use `scripts/lint_ai_style.py` for a deterministic style pass when the draft is file-based.

## 6. Revise

Revise based on the critique.

Prioritize clarity, structural continuity, factual fidelity, and reader usefulness. Do not add filler, typos, forced informality, or meaningless pauses just to make text seem "human".

## 7. Layout Normalize

For Markdown output, use or follow `scripts/normalize_markdown.py`.

For Word output, use Markdown source plus `assets/reference.docx` as the rendering base.

For PDF output, prefer Pandoc, Typst, or Quarto. Do not hand-write complex LaTeX unless the user explicitly asks and the project requires it.

If required tools are unavailable, produce clean Markdown and give the local render command needed to finish the export.

## 8. Quality Gates

Use `references/10-quality-gates.md` before final delivery.

For important documents, check structure, style, format, factual boundary, and target-format consistency. In the final answer, show only the artifact or summary the user needs; do not expose the full internal reasoning trace.
