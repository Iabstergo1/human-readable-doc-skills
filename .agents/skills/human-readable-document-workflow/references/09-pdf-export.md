# PDF Export

Prefer clear and stable PDF generation over decorative complexity.

## Supported Routes

1. Pandoc plus a LaTeX template or default PDF engine.
2. Quarto using `assets/quarto/_quarto.yml`.
3. Typst using `assets/templates/report.typ`.

## Pandoc Example

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\render_with_pandoc.py `
  .\draft.md --to pdf --output .\draft.pdf
```

With a PDF engine:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\render_with_pandoc.py `
  .\draft.md --to pdf --output .\draft.pdf --pdf-engine xelatex
```

## Quarto Example

```powershell
quarto render .\draft.qmd --to pdf --project .\.agents\skills\human-readable-document-workflow\assets\quarto
```

## Typst Example

```powershell
typst compile .\draft.typ .\draft.pdf
```

## Fallback

If local tools are missing, output clean Markdown and provide installation or render instructions. Do not claim that a PDF was created.
