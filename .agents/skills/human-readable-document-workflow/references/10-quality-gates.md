# Quality Gates

Use these gates before final delivery. They are not a replacement for domain
verification; they ensure the document is coherent, readable, source-bounded,
and renderable.

## Gate Summary

| Gate | Pass condition | Useful script |
| --- | --- | --- |
| Goal and reader | The document answers the requested task for the intended audience. | `detect_doc_intent.py` for routing. |
| Source boundary | Facts, citations, and claims stay inside provided evidence. | Manual check. |
| Structure | Headings, sections, and order match the document type. | `normalize_markdown.py`. |
| Style | Obvious AI phrasing is removed without casualizing precise text. | `lint_ai_style.py`. |
| Markdown | Source is raw-readable and renderable. | `normalize_markdown.py`. |
| Output artifacts | Explicitly requested files exist and have plausible file structure. | `validate_outputs.py`. |

## Goal And Reader

- Does the document match the user's stated goal?
- Is the target reader clear?
- Does the structure answer that reader's likely questions?
- Are non-goals or boundaries stated when they matter?

Example:

```markdown
Goal: technical design for implementers.
Non-goal: not a user-facing product overview.
```

## Facts And Sources

- Do not invent facts, sources, citations, metrics, or quotes.
- Label assumptions.
- Use `[citation needed]` where sources are missing.
- Keep user-provided wording intact when quoted.
- Do not alter bibliography entries during style cleanup.

## Style

- Remove generic openings, empty endings, and unsupported broad claims.
- Keep professional terminology when it improves precision.
- Use lists only when scanning or comparison helps.
- Avoid marketing tone unless the document is explicitly marketing material.
- Avoid academic abstraction unless the document needs scholarly framing.

## Structure

- One H1.
- No skipped heading levels.
- Paragraphs carry one main move.
- Tables compare real structured data.
- Code blocks have language labels.
- Figures, tables, and formulas have captions or explanations.

## Output Path

Apply Word and PDF checks only when the user explicitly asks for those exported
artifacts. A task about PDF content, PDF preprocessing, or Word-related prose is
not automatically a PDF or Word export request.

| Requested output | Required evidence |
| --- | --- |
| Markdown | Source file or Markdown text passes readability checks. |
| Word, explicitly requested | Markdown source exists and `.docx` is rendered or command is provided. |
| PDF, explicitly requested | Markdown source exists and `.pdf` is rendered or command is provided. |
| Word plus PDF | One canonical Markdown source drives both artifacts. |

## Suggested Commands

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\normalize_markdown.py `
  .\draft.md --check --report .\tmp\markdown-report.json

python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\draft.md --format json --pretty

python .\.agents\skills\human-readable-document-workflow\scripts\validate_outputs.py `
  .\draft.md --markdown .\draft.md --pretty
```

## Boundaries

For high-stakes medical, legal, financial, academic citation, or current factual
claims, use the appropriate verification workflow. Passing these gates means the
document is structurally and stylistically controlled, not that every external
claim is independently true.
