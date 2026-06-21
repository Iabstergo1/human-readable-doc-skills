# Word Export

Use Markdown source plus a Word reference template. A `.docx` file is a rendered
artifact; the Markdown source remains the editable canonical document.

## When To Generate Word

| Situation | Output |
| --- | --- |
| User asks for Word/docx and local renderer is available. | Generate `.docx` and keep `.md`. |
| User asks for Word but renderer is missing. | Provide `.md` and render command. |
| User only asks for Markdown. | Do not generate Word. |
| User supplies a corporate template. | Pass it as `--reference-doc` or replace `assets/reference.docx`. |

## Reference Document

`assets/reference.docx` controls Word styles such as:

- Heading appearance.
- Body font and spacing.
- Table style.
- Caption style.
- Margins and page defaults.

Replace it with a real template when production styling matters. Keep the same
path when possible so commands stay stable.

## Markdown Requirements Before Word

- One H1.
- No skipped heading levels.
- Tables have blank lines before and after.
- Code fences have language labels.
- Images and tables have captions or explanatory lead-in text.
- YAML frontmatter is valid when present.

## PowerShell Commands

Validate the source:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\normalize_markdown.py `
  .\draft.md --check --report .\tmp\markdown-report.json
```

Render through the wrapper:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\render_with_pandoc.py `
  .\draft.md --to docx --output .\draft.docx `
  --reference-doc .\.agents\skills\human-readable-document-workflow\assets\reference.docx
```

Equivalent direct Pandoc command:

```powershell
pandoc .\draft.md --to docx `
  --reference-doc .\.agents\skills\human-readable-document-workflow\assets\reference.docx `
  -o .\draft.docx
```

Validate the artifact:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\validate_outputs.py `
  .\draft.docx --markdown .\draft.md --pretty
```

## Examples

Good workflow:

1. Draft `draft.md`.
2. Normalize and check Markdown.
3. Render `draft.docx`.
4. Validate the `.docx` zip structure.

Bad workflow:

1. Ask the model to "output a Word file" without creating a real artifact.
2. Use manual spaces in Markdown to imitate page alignment.

## Boundaries

This skill does not edit tracked changes or comments inside existing Word files.
Use a dedicated docx workflow when the task requires preserving Word-specific
review metadata.
