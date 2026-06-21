# Replay Tests

These replay tests use realistic document requests instead of short fixtures.
They record the input, routed references, draft output path, lint result, and
manual critique. The goal is to check whether the skill improves real document
work, not only whether keyword fixtures pass.

## Replay Index

| Replay | Input focus | Draft |
| --- | --- | --- |
| `pdf-preprocessing-technical-design` | Technical design for PDF preprocessing. | `outputs/pdf-preprocessing-technical-design.md` |
| `academic-chapter-model` | Academic chapter model explanation. | `outputs/academic-chapter-model.md` |
| `readme-rewrite` | GitHub README rewrite. | `outputs/readme-rewrite.md` |

## Commands

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\detect_doc_intent.py `
  '帮我写一份关于 PDF 预处理架构的技术设计文档，输出 Markdown。' --pretty

python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\replays\outputs\pdf-preprocessing-technical-design.md --pretty

python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\replays\outputs\academic-chapter-model.md --pretty

python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\replays\outputs\readme-rewrite.md --pretty
```

## Replay 1: PDF Preprocessing Technical Design

### Input

```text
帮我写一份关于 PDF 预处理架构的技术设计文档，输出 Markdown。
```

### Triggered References

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- `references/03-anti-ai-slop-zh.md`
- `references/06-document-layout.md`
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Lint Result

Command:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\replays\outputs\pdf-preprocessing-technical-design.md --pretty
```

Result after v0.5 refinement: `ok: true`, `issue_count: 0`.

Pre-refinement finding: `zh-false-depth` flagged a boundary sentence using
`不是...而是...`. Manual review kept it because the sentence defined the
preprocessing layer's responsibility.

### Manual Critique

- The output should describe PDF as the problem domain, not as an export target.
- The draft should name inputs, outputs, failure states, and validation data.
- It should avoid marketing words such as `赋能` and unsupported success claims.

## Replay 2: Academic Chapter Model

### Input

```text
帮我生成一篇学术论文第三章的模型说明，注意变量命名、符号统一和引用占位。
```

### Triggered References

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- `references/03-anti-ai-slop-zh.md`
- `references/05-academic-writing.md`
- `references/06-document-layout.md`
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Lint Result

Command:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\replays\outputs\academic-chapter-model.md --pretty
```

Result after v0.5 refinement: `ok: true`, `issue_count: 0`.

Pre-refinement finding: `zh-mechanical-transition` flagged `首先/其次`.
Manual review kept it because the phrase marked ordered variable definitions,
not template filler.

### Manual Critique

- Ordered transitions are acceptable in formal model exposition.
- Variable definitions need stable symbols and source boundaries.
- Citation placeholders must remain visible instead of invented citations.

## Replay 3: README Rewrite

### Input

```text
把 README 改写得更清楚，适合 GitHub 项目主页，保留安装和验证命令。
```

### Triggered References

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- `references/03-anti-ai-slop-zh.md`
- `references/06-document-layout.md`
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Lint Result

Command:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\replays\outputs\readme-rewrite.md --pretty
```

Result after v0.5 refinement: `ok: true`, `issue_count: 0`.

### Manual Critique

- The README draft should lead with purpose, scope, and commands.
- It should not become a landing page or sales page.
- Limitations and verification commands should remain visible.
