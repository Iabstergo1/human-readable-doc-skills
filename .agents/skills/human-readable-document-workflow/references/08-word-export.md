# Word Export

Use Markdown source plus a Word reference template.

## Principles

- Do not ask the model to fake a `.docx` structure.
- Keep the Markdown source as the editable canonical draft.
- Use `assets/reference.docx` for styles, fonts, heading appearance, margins, and table style.
- If the user supplies a corporate template, replace `assets/reference.docx` or pass its path at render time.

## Pandoc Command

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\render_with_pandoc.py `
  .\draft.md --to docx --output .\draft.docx `
  --reference-doc .\.agents\skills\human-readable-document-workflow\assets\reference.docx
```

Equivalent direct Pandoc command:

```powershell
pandoc .\draft.md --to docx --reference-doc .\assets\reference.docx -o .\draft.docx
```

## If Pandoc Is Missing

Provide the Markdown source and tell the user which command to run after installing Pandoc. Do not pretend a Word file was generated.
