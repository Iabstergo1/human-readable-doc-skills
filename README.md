# Human Readable Doc Skills

v1.0.0 provides a Codex skill for human-readable document source workflows. It
routes document requests, applies a writing loop, improves prose, organizes
structure, and produces clean Markdown source that can be reviewed or handed
off to official document-generation tooling.

This project does not render Word, PDF, slides, or other binary artifacts. File
rendering is delegated to external official document tooling.

## Core capability

- Document intent routing.
- Writing loop: intake, frame, plan, draft, critique, revise, finalize.
- Human-readable style rules.
- Simplified Chinese anti-AI-style cleanup.
- English anti-AI-style cleanup.
- Academic writing safeguards.
- Document type profiles.
- Markdown source authoring.
- Quality gates.

## Out of scope

- Direct Word/PDF binary generation.
- Pandoc / Quarto / Typst template system.
- Word tracked changes editing.
- PDF repair or layout editing.
- Fabricated citations.
- Claiming a rendered artifact exists when this skill only produced source
  text.

## Handoff policy

If the user requests Word, PDF, slides, or another concrete file artifact:

1. Use this skill to plan and produce the clean Markdown source.
2. Then hand off to Codex official docs/document skill or the appropriate
   file-generation tool.
3. Do not perform local rendering inside this skill.

## Architecture

```text
human-readable-doc-skills/
├── AGENTS.md
├── docs/
│   └── workflow-examples.md
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

4. Markdown source and handoff:
   keep Markdown source readable, source-bounded, and ready for external
   official document-generation tooling when a file artifact is requested.
   Main files: `references/06-document-layout.md`,
   `references/07-markdown-authoring.md`.

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

Run Markdown source validation:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\validate_markdown_source.py `
  .\tests\fixtures\good-markdown.md --pretty
```

## Upstream Projects

This repository uses the following upstream projects as methodology references
only. Rules and scripts in this repository are rewritten locally.
Raw source access checks are recorded in `docs/upstream-source-access.md`.
Capability parity is recorded in `docs/upstream-parity-matrix.md`.

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
