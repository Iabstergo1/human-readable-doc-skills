# Tests

This repository uses manual smoke tests with Python standard-library scripts.
No pytest dependency is required.

## Skill Package Validation

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\validate_skill.py --pretty
```

## Intent Detection

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\detect_doc_intent.py `
  --file .\tests\fixtures\doc-intent-technical-zh.txt --pretty
```

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\detect_doc_intent.py `
  --file .\tests\fixtures\doc-intent-academic-zh.txt --pretty
```

## AI-Style Lint

The following commands are expected to report issues and return a non-zero exit
code because the fixtures intentionally contain weak phrases.

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\fixtures\ai-slop-zh.md --pretty
```

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\fixtures\ai-slop-en.md --format text
```

## Markdown Normalization

Good Markdown should pass:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\normalize_markdown.py `
  .\tests\fixtures\good-markdown.md --check --report .\tmp\good-markdown-report.json
```

Bad Markdown should report issues:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\normalize_markdown.py `
  .\tests\fixtures\bad-markdown.md --check --report .\tmp\markdown-report.json
```

## Output Validation

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\validate_outputs.py `
  .\tests\fixtures\good-markdown.md --markdown .\tests\fixtures\good-markdown.md --pretty
```
