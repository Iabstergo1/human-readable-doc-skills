# Human Readable Doc Skills

This repository provides a Codex skill for document generation and revision. It
turns broad requests such as "write a technical design", "polish this report",
or "make this README clearer" into a controlled workflow: route the document
type, load focused references, produce Markdown as the source of truth, and
verify the result before delivery.

## Core Capability

- Keeps `SKILL.md` small while giving Codex deeper rules through references.
- Separates writing workflow, human-readable style, document structure, and
  Markdown layout rules.
- Provides standard-library scripts for deterministic checks.
- Treats Markdown as the canonical source for substantial document work.
- Preserves attribution for methodology references without vendoring upstream
  projects.

The core skill is a human-readable document workflow. It improves planning,
drafting, revision, structure, Markdown authoring, style review, and final
quality checks. It is not a full Word or PDF rendering system.

## Optional Export Adapter

Word and PDF support are optional adapters used only when the user explicitly
requests those artifacts. The skill first creates or updates Markdown, then
renders through local tools when available or provides a reproducible command
when they are not.

- Word output uses `references/08-word-export.md`,
  `assets/reference.docx`, and `render_with_pandoc.py`.
- PDF output uses `references/09-pdf-export.md` and local routes such as
  Pandoc, Quarto, or Typst.
- Markdown-only tasks should not load Word or PDF export rules.
- Do not claim a `.docx` or `.pdf` exists unless a command created it.

## What This Does Not Solve

- It does not replace domain verification for legal, medical, financial, or
  academic claims.
- It does not fabricate citations, benchmark data, authors, DOIs, or sources.
- It does not directly edit Word tracked changes or repair binary PDFs.
- It does not copy upstream skill text, prompts, templates, or repositories.
- It does not introduce heavy dependencies; scripts use Python standard library.

## Architecture

```text
human-readable-doc-skills/
├── AGENTS.md
├── README.md
├── tests/
│   ├── README.md
│   └── fixtures/
└── .agents/
    └── skills/
        └── human-readable-document-workflow/
            ├── SKILL.md
            ├── references/
            ├── scripts/
            └── assets/
```

## Four-Layer Framework

1. Writing workflow:
   intake, frame, plan, draft, critique, revise, normalize, finalize.
   Main file: `references/01-writing-loop.md`.

2. Human-readable style and anti-AI:
   keep prose concrete, source-bounded, and non-template.
   Main files: `references/02-human-readable-style.md`,
   `references/03-anti-ai-slop-zh.md`,
   `references/04-anti-ai-slop-en.md`.

3. Document structure:
   route by document type instead of applying one generic outline.
   Main files: `references/05-academic-writing.md`,
   `references/12-document-type-profiles.md`.

4. Rendering and layout:
   keep Markdown source readable and renderable; load Word/PDF export guidance
   only when those artifacts are explicitly requested.
   Main files: `references/06-document-layout.md`,
   `references/07-markdown-authoring.md`,
   `references/08-word-export.md`,
   `references/09-pdf-export.md`.

## Install To Repo Scope

Copy `.agents` into the repository where Codex should discover the skill.

```powershell
cd C:\path\to\target-repo
Copy-Item -Recurse -Force D:\human-readable-doc-skills\.agents .\.agents
Get-ChildItem .\.agents\skills\human-readable-document-workflow
```

## Install To User Scope

Use this when your Codex setup loads user-level skills.

```powershell
$source = "D:\human-readable-doc-skills\.agents\skills\human-readable-document-workflow"
$target = "$env:USERPROFILE\.codex\skills\human-readable-document-workflow"
Copy-Item -Recurse -Force $source $target
```

## Explicit Invocation

```text
$human-readable-document-workflow 帮我写一份 PDF 预处理架构技术设计文档，输出 Markdown，后续转 Word 和 PDF。
```

## Implicit Triggering

The skill should trigger when the user asks to create, draft, revise, polish,
structure, export, typeset, or generate a reusable document. Typical signals
include document, report, article, paper, proposal, README, Word, PDF, academic
writing, technical documentation, business document, meeting notes, and email.

Short casual answers and code-only tasks should not trigger it unless the user
explicitly asks for a reusable document artifact.

## Maintain References

- Keep `SKILL.md` as the orchestration layer.
- Put long-form rules in `references/`.
- Keep each reference focused on one topic.
- Add a new reference only when a stable topic would otherwise bloat another
  file.
- Keep upstream attribution in both `README.md` and
  `references/11-upstream-attribution.md`.

## Maintain Scripts

Scripts live in:

```text
.agents\skills\human-readable-document-workflow\scripts
```

Rules:

- Use Python standard library first.
- Provide `argparse` CLIs and working `--help`.
- Prefer JSON output for automation.
- Keep conservative fixes separate from lint findings.
- Protect Markdown frontmatter, code fences, tables, URLs, quotes, citations,
  and bibliography entries during style cleanup.

## Replace The Word Template

This section applies only to explicit Word export requests.
`assets/reference.docx` is the Word reference document path used by the Pandoc
wrapper. Replace it with your own template when production styling matters.

```powershell
Copy-Item -Force C:\path\to\your-template.docx `
  .\.agents\skills\human-readable-document-workflow\assets\reference.docx
```

Render Word:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\render_with_pandoc.py `
  .\draft.md --to docx --output .\draft.docx `
  --reference-doc .\.agents\skills\human-readable-document-workflow\assets\reference.docx
```

## Configure PDF Routes

This section applies only to explicit PDF export requests. The PDF layer
supports three routes:

| Route | Command family | Use when |
| --- | --- | --- |
| Pandoc | `render_with_pandoc.py --to pdf` | General Markdown to PDF. |
| Quarto | `quarto render` | Computational reports or Quarto projects. |
| Typst | `typst compile` | Typst-native layouts. |

If the renderer is unavailable, deliver clean Markdown and the command needed to
render locally. Do not claim a PDF exists unless a command created it.

## Validation

Run the skill package validator:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\validate_skill.py --pretty
```

Run routing:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\detect_doc_intent.py `
  --file .\tests\fixtures\doc-intent-technical-zh.txt --pretty
```

Run style lint:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py `
  .\tests\fixtures\ai-slop-zh.md --pretty
```

Run Markdown checks:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\normalize_markdown.py `
  .\tests\fixtures\bad-markdown.md --check --report .\tmp\markdown-report.json
```

## Upstream Projects

This repository uses the following upstream projects as methodology references
only. Rules and scripts in this repository are rewritten locally.

| Project | URL | License note |
| --- | --- | --- |
| Writer's Loop | https://github.com/xxsang/writers-loop | GitHub metadata previously observed as MIT. |
| Writer's Loop skill | https://github.com/xxsang/writers-loop/tree/main/skills/writers-loop | Methodology reference only. |
| codex-be-serious | https://github.com/lulucatdev/codex-be-serious | GitHub metadata previously observed as MIT. |
| codex-be-serious main skill | https://github.com/lulucatdev/codex-be-serious/tree/main/skills/be-serious | Methodology reference only. |
| codex-be-serious review skill | https://github.com/lulucatdev/codex-be-serious/tree/main/skills/be-serious-review | Methodology reference only. |
| unslop | https://github.com/MohamedAbdallah-14/unslop | GitHub metadata previously observed as MIT. |
| unslop main skill | https://github.com/MohamedAbdallah-14/unslop/tree/main/skills/unslop | Methodology reference only. |
| unslop review skill | https://github.com/MohamedAbdallah-14/unslop/tree/main/skills/unslop-review | Methodology reference only. |
| anti-slop-writing | https://github.com/adenaufal/anti-slop-writing | GitHub metadata previously observed as MIT. |
| anti-slop-writing English directory | https://github.com/adenaufal/anti-slop-writing/tree/main/english | Methodology reference only. |
| anti-slop-writing English SKILL.md | https://github.com/adenaufal/anti-slop-writing/blob/main/english/SKILL.md | Methodology reference only. |
| qu-ai-wei | https://github.com/LifelongLazyLearner/qu-ai-wei | GitHub metadata previously observed as MIT. |
| qu-ai-wei SKILL.md | https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/SKILL.md | Methodology reference only. |
| qu-ai-wei references | https://github.com/LifelongLazyLearner/qu-ai-wei/tree/main/references | Methodology reference only. |
| qu-ai-wei scripts | https://github.com/LifelongLazyLearner/qu-ai-wei/tree/main/scripts | Methodology reference only. |
| Humanizer-zh | https://github.com/op7418/humanizer-zh | GitHub metadata previously observed as MIT. |
| Humanizer-zh SKILL.md | https://github.com/op7418/humanizer-zh/blob/main/SKILL.md | Methodology reference only. |
| writing-humanizer | https://github.com/shyuan/writing-humanizer | GitHub metadata previously observed as MIT. |
| writing-humanizer skill | https://github.com/shyuan/writing-humanizer/tree/main/skills/writing-humanizer | Methodology reference only. |
| prompts.chat | https://github.com/f/prompts.chat | GitHub metadata previously observed as Other / NOASSERTION. |
| ChatGPT Prompts for Academic Writing | https://github.com/ahmetbersoz/chatgpt-prompts-for-academic-writing | License metadata previously observed as unknown. |

Do not invent unavailable paths. The requested `unslop` path
`skills/humanize` is treated as unavailable unless verified later.

## License Notes

This repository does not vendor upstream repositories. If future work copies
code, templates, long examples, or protected text from an upstream project,
re-check that project's license file, preserve required notices, and document
the import in `references/11-upstream-attribution.md`.

## Roadmap

- Add more document profiles only when repeated tasks justify them.
- Add renderer-specific templates after real user documents expose layout needs.
- Add optional forward tests using realistic document prompts.
- Add stricter validation for citations and bibliography files when a citation
  workflow is introduced.
