# PDF Export

Prefer stable, auditable PDF generation over decorative complexity. A PDF is a
rendered artifact; Markdown remains the canonical source unless the user
explicitly asks for a renderer-native source such as Typst.

## Route Selection

| Route | Use when | Notes |
| --- | --- | --- |
| Pandoc | General Markdown to PDF conversion. | Needs Pandoc and usually a PDF engine. |
| Quarto | Reports with executable notebooks, citations, or project config. | Use `assets/quarto/_quarto.yml` as a starting point. |
| Typst | Controlled PDF layout with a Typst template. | Use `assets/templates/report.typ` when the source is Typst-ready. |
| Markdown only | Tools are missing or user asks only for source. | Provide commands and limitations plainly. |

## Markdown Requirements Before PDF

- Use one H1 and stable heading hierarchy.
- Keep tables simple and avoid layout tables.
- Add captions or explanatory text for figures, tables, and formulas.
- Mark code block languages.
- Avoid manual spaces for alignment.
- Use YAML frontmatter for title, author, date, abstract, and metadata when
  useful.

## Pandoc Commands

Dry-run command construction:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\render_with_pandoc.py `
  .\draft.md --to pdf --output .\draft.pdf --dry-run
```

Render with default PDF route:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\render_with_pandoc.py `
  .\draft.md --to pdf --output .\draft.pdf
```

Render with a PDF engine:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\render_with_pandoc.py `
  .\draft.md --to pdf --output .\draft.pdf --pdf-engine xelatex
```

## Quarto Route

Use Quarto when the document is closer to a computational report.

```powershell
quarto render .\draft.qmd --to pdf
```

If project-level config is needed, copy or adapt:

```text
.agents\skills\human-readable-document-workflow\assets\quarto\_quarto.yml
```

## Typst Route

Use Typst when layout control matters and the project already accepts Typst.

```powershell
typst compile .\draft.typ .\draft.pdf
```

The template placeholder is:

```text
.agents\skills\human-readable-document-workflow\assets\templates\report.typ
```

## Validate PDF

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\validate_outputs.py `
  .\draft.pdf --markdown .\draft.md --pretty
```

## Examples

Good: "Generate `draft.md`, then render `draft.pdf` with Pandoc and validate the
PDF header."

Bad: "Paste PDF-like text into chat and claim a PDF was created."

## Boundaries

This skill does not perform professional typesetting, OCR, or PDF repair. Use a
dedicated PDF workflow when the task requires merging, splitting, OCR, form
filling, or visual QA of an existing PDF.
