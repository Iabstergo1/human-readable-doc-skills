# Document Layout

Layout should make the source readable and the rendered artifact predictable.
Markdown is the canonical source; Word and PDF are rendered artifacts.

## Layout Rules

| Area | Rule | Why |
| --- | --- | --- |
| Headings | Start with one H1 and do not skip levels. | Renderers use headings for TOC and styles. |
| Paragraphs | Keep paragraphs focused but not artificially short. | Readers need continuity. |
| Lists | Use for steps, checks, options, owners, or action items. | Lists should improve scanning. |
| Tables | Use only for real comparison or structured data. | Tables are fragile in Word/PDF when used for layout. |
| Code | Use fenced code blocks with language labels. | Renderers and readers need syntax context. |
| Figures | Add caption or explanatory lead-in text. | Images need context and accessibility. |
| Formulas | Explain symbols before or after the formula. | Mathematical notation should not stand alone. |
| Spacing | Do not align with manual spaces or repeated blank lines. | Rendered output will drift. |

## Source And Artifact Policy

- `.md` is the editable source of truth.
- `.docx` and `.pdf` are generated artifacts.
- Do not ask the model to imitate binary file formats.
- If render tools are missing, deliver the Markdown source and the command the
  user can run locally.

## Format-Specific Boundaries

| Target | Use | Avoid |
| --- | --- | --- |
| Markdown | Default for drafting, review, and version control. | Renderer-specific syntax without a note. |
| Word | Stakeholder review, comments, templates, corporate styles. | Manual page layout in Markdown. |
| PDF | Fixed-layout sharing, academic or formal distribution. | Complex page design without a renderer/toolchain. |

## Examples

Good table use:

```markdown

| Input type | Default path | Failure record |
| --- | --- | --- |
| Text PDF | Text extraction | Extractor error and page id |
| Scanned PDF | OCR queue | OCR confidence and retry state |

```

Poor table use:

```markdown

| Left column paragraph | Right column paragraph |
| --- | --- |
| Long body text used only for page layout. | More long body text. |

```

## Boundaries

This reference does not replace a design system, journal template, or corporate
brand guide. When a template exists, keep Markdown structure clean and put visual
styling in the renderer configuration or reference document.
