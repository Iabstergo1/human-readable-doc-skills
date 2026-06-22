# Parity Test Fixtures

These are manual parity fixtures for the human-readable document skill. They do
not require pytest. Use them when changing routing, style learning, anti-slop
modes, or serious-register review.

Suggested checks:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\parity\zh-real-human-stop-gate.txt --mode zh-source-safe --pretty

python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\parity\en-document-safe-mode.md --mode document-safe --pretty

python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\parity\en-creative-blog-mode.md --mode creative-blog --pretty

python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\parity\serious-register-review.md --mode serious-review --pretty

python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\parity\style-content-leak.md --mode document-safe --pretty
```

Expected nonzero exit codes are acceptable when a fixture intentionally
contains lint issues.
