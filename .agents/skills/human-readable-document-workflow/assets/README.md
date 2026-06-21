# Assets

Assets are files used by the skill at output time. They should not become a
second instruction system; durable rules belong in `references/`.

## Files

| Path | Purpose | Maintenance note |
| --- | --- | --- |
| `reference.docx` | Minimal Word reference document for Pandoc. | Replace with a real template when production styling matters. |
| `templates/report.typ` | Typst template placeholder. | Expand only when a Typst route is actively used. |
| `quarto/_quarto.yml` | Quarto configuration placeholder. | Keep small and renderer-focused. |
| `examples/` | Good and bad prose samples for style checks. | Keep examples short and clearly labeled. |

## Replacing The Word Template

1. Create a Word document with heading, paragraph, table, code, and caption
   styles.
2. Save it as `reference.docx`.
3. Keep the path `assets/reference.docx`, or pass another path to
   `render_with_pandoc.py --reference-doc`.

## Boundaries

Do not store private client templates, credentials, or large generated outputs
in this directory. If a template comes from a third party, document its license
and origin before committing it.
