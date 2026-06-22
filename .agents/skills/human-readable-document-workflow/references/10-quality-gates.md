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
| Serious register | Formal documents avoid slang, hype, and forced friendliness. | `lint_ai_style.py --mode serious-review`. |
| Second-pass humanization | Humanize tasks preserve voice while removing AI residue. | `lint_ai_style.py` with the selected mode. |

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
- Do not turn guesses into facts.
- Do not add fake citations, authors, years, DOI values, data, or validation
  results.
- Do not import facts from a style sample into the target document.
- Do not treat a tone sample as evidence for claims.
- After anti-slop or humanization edits, re-check factual claims because style
  cleanup can accidentally remove uncertainty or add confidence.

## Source Boundary Gate

Pass only when:

- Every factual claim comes from the user, attached sources, verified tooling,
  or an explicit assumption label.
- Missing evidence remains visible instead of being smoothed away.
- Style samples influence form only, not facts, names, metrics, quotes, or
  examples.
- Citations and quoted material remain protected unless the user asked for
  paraphrase.

Fail when the draft invents a source, hides uncertainty, or uses sample content
as if it belonged to the target document.

## Style

- Remove generic openings, empty endings, and unsupported broad claims.
- Keep professional terminology when it improves precision.
- Use lists only when scanning or comparison helps.
- Avoid marketing tone unless the document is explicitly marketing material.
- Avoid academic abstraction unless the document needs scholarly framing.

## Serious Register Gate

Enable this gate for technical, academic, formal report, proposal, SOP,
policy-like, and other formal documents.

Check for:

- slang and internet vernacular
- sycophancy and praise that does not serve the document
- emoji and decorative symbols
- marketing adjectives and empty enthusiasm
- forced informality
- anthropomorphized software descriptions
- Chinese internet workplace jargon

Typical failures:

- "the system understands the user's intent" when the system classifies,
  predicts, parses, or matches.
- "awesome", "super", "magic", "game-changing", or "crush it" in a formal
  technical document.
- "绝绝子", "YYDS", "拿捏", "打工人", or similar phrasing in formal Chinese
  prose.

For requested formal review reports, use:

```markdown
Assessment:
Findings:
Revision:
```

Do not expose this review shape by default during ordinary drafting.

## Second-Pass Humanization Gate

Enable this gate for polishing, humanize, anti-AI-style cleanup, and similar
tasks.

Check after the first rewrite:

- Does any generic AI phrasing still remain?
- Did the revision over-sanitize the original voice?
- Was likely human speech, hesitation, dialect, or personal texture damaged?
- Did the edit only swap words without improving structure or fact density?
- Did the text become more casual than the document type allows?
- Did the edit add new claims instead of subtracting filler?

If the second pass finds voice loss, restore the user's tone and limit the edit
to concrete defects: empty claims, unsupported exaggeration, template openings,
mechanical transitions, and format noise.

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
