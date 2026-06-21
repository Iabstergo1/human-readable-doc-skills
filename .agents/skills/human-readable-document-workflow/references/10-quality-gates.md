# Quality Gates

Use these gates before final delivery. They are not a replacement for domain
verification; they ensure the document is coherent, readable, source-bounded,
and ready for Markdown-source handoff.

## Gate Summary

| Gate | Pass condition | Useful script |
| --- | --- | --- |
| Goal and reader | The document answers the requested task for the intended audience. | `detect_doc_intent.py` for routing. |
| Source boundary | Facts, citations, and claims stay inside provided evidence. | Manual check. |
| Structure | Headings, sections, and order match the document type. | `normalize_markdown.py`. |
| Style | Obvious AI phrasing is removed without casualizing precise text. | `lint_ai_style.py`. |
| Markdown | Source is raw-readable and handoff-ready. | `normalize_markdown.py`. |
| Source validation | Placeholders, heading issues, and code-fence issues are visible. | `validate_markdown_source.py`. |

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

## Handoff Path

Apply file-artifact checks outside this skill. A task about PDF content, PDF
preprocessing, or Word-related prose is not automatically a rendered file
request.

| Requested output | Required evidence |
| --- | --- |
| Markdown | Source file or Markdown text passes readability checks. |
| Word, PDF, or slides | Markdown source is clean and ready for handoff. |
| Chat answer | Response stays source-bounded and does not claim file creation. |

## Suggested Commands

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\normalize_markdown.py `
  .\draft.md --check --report .\tmp\markdown-report.json

python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\draft.md --format json --pretty

python .\.agents\skills\human-readable-document-workflow\scripts\validate_markdown_source.py `
  .\draft.md --pretty
```

## Boundaries

For high-stakes medical, legal, financial, academic citation, or current factual
claims, use the appropriate verification workflow. Passing these gates means the
document is structurally and stylistically controlled, not that every external
claim is independently true.
