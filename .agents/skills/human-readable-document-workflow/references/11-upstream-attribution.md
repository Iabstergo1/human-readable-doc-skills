# Upstream Attribution

This project extracts and rewrites methodology only. Do not vendor upstream
repositories, copy long protected text, or invent replacement paths. Keep
attribution in this file and in the repository README.

## Import Policy

| Policy | Rule |
| --- | --- |
| Text | Summarize and rewrite methodology in this project's own words. |
| Code | Do not copy upstream code unless the license is checked and notices are preserved. |
| Templates | Do not import templates without explicit need and license review. |
| Missing paths | Mark the exact URL unavailable instead of fabricating alternatives. |
| Scope | Use only the upstream projects listed below. |

Raw source access checks are recorded in `docs/upstream-source-access.md`.

## Skill-To-Reference Boundary

Upstream `SKILL.md` files are methodology sources here, not active local skill
entrypoints. The active entrypoint is this repository's local `SKILL.md`; it
must route tasks to the relevant files in `references/`.

This does not inherently make the workflow weaker. It can make the workflow
more controllable because one local orchestration layer decides which rewritten
rules to load. The risk is different: upstream trigger metadata, tool guidance,
or entrypoint behavior has no effect unless it is intentionally rewritten into
local `SKILL.md`, `references/`, or `scripts/`.

## Upstream Map

### Writer's Loop

- Repo: https://github.com/xxsang/writers-loop
- Skill directory: https://github.com/xxsang/writers-loop/tree/main/skills/writers-loop
- Borrowed method: iterative writing workflow.
- Local impact: `references/01-writing-loop.md`, `SKILL.md`.
- License note: GitHub metadata previously observed as MIT.

### codex-be-serious

- Repo: https://github.com/lulucatdev/codex-be-serious
- Main skill: https://github.com/lulucatdev/codex-be-serious/tree/main/skills/be-serious
- Review skill: https://github.com/lulucatdev/codex-be-serious/tree/main/skills/be-serious-review
- Borrowed method: rigorous critique of vague claims and missing evidence.
- Local impact: `references/10-quality-gates.md`, `SKILL.md`.
- License note: GitHub metadata previously observed as MIT.

### unslop

- Repo: https://github.com/MohamedAbdallah-14/unslop
- Main skill: https://github.com/MohamedAbdallah-14/unslop/tree/main/skills/unslop
- Review skill: https://github.com/MohamedAbdallah-14/unslop/tree/main/skills/unslop-review
- Unavailable path: `skills/humanize` returned 404 on 2026-06-22.
- Borrowed method: conservative anti-template editing.
- Local impact: Chinese and English anti-slop references, `lint_ai_style.py`.
- License note: GitHub metadata previously observed as MIT.

### anti-slop-writing

- Repo: https://github.com/adenaufal/anti-slop-writing
- English directory: https://github.com/adenaufal/anti-slop-writing/tree/main/english
- English SKILL.md: https://github.com/adenaufal/anti-slop-writing/blob/main/english/SKILL.md
- Borrowed method: English filler and template-conclusion categories.
- Local impact: `references/04-anti-ai-slop-en.md`, `lint_ai_style.py`.
- License note: GitHub metadata previously observed as MIT.

### qu-ai-wei

- Repo: https://github.com/LifelongLazyLearner/qu-ai-wei
- SKILL.md: https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/SKILL.md
- References: https://github.com/LifelongLazyLearner/qu-ai-wei/tree/main/references
- Scripts: https://github.com/LifelongLazyLearner/qu-ai-wei/tree/main/scripts
- Borrowed method: Chinese anti-AI writing stance and reference-split structure.
- Local impact: `references/03-anti-ai-slop-zh.md`, `references/`.
- License note: GitHub metadata previously observed as MIT.

### Humanizer-zh

- Repo: https://github.com/op7418/humanizer-zh
- SKILL.md: https://github.com/op7418/humanizer-zh/blob/main/SKILL.md
- Borrowed method: Chinese human-readable prose direction.
- Local impact: `references/02-human-readable-style.md`,
  `references/03-anti-ai-slop-zh.md`.
- License note: GitHub metadata previously observed as MIT.

### writing-humanizer

- Repo: https://github.com/shyuan/writing-humanizer
- Skill directory: https://github.com/shyuan/writing-humanizer/tree/main/skills/writing-humanizer
- Borrowed method: humanizer skill packaging and cleanup boundaries.
- Local impact: `SKILL.md`, `references/02-human-readable-style.md`.
- License note: GitHub metadata previously observed as MIT.

### prompts.chat

- Repo: https://github.com/f/prompts.chat
- Reference path: repository root.
- Borrowed method: prompt modularity and attribution discipline.
- Local impact: README attribution and roadmap.
- License note: GitHub metadata previously observed as Other / NOASSERTION.

### ChatGPT Prompts for Academic Writing

- Repo: https://github.com/ahmetbersoz/chatgpt-prompts-for-academic-writing
- Reference path: repository root.
- Borrowed method: academic writing prompt categories.
- Local impact: `references/05-academic-writing.md`,
  `references/12-document-type-profiles.md`.
- License note: license metadata previously observed as unknown.

## Local Files Influenced

| Local file | Upstream influence | Import status |
| --- | --- | --- |
| `SKILL.md` | Skill orchestration and progressive reference loading. | Rewritten locally. |
| `references/01-writing-loop.md` | Iterative writing loop methodology. | Rewritten locally. |
| `references/02-human-readable-style.md` | Human-readable prose criteria. | Rewritten locally. |
| `references/03-anti-ai-slop-zh.md` | Chinese anti-template categories. | Rewritten locally. |
| `references/04-anti-ai-slop-en.md` | English anti-slop categories and protected blocks. | Rewritten locally. |
| `references/05-academic-writing.md` | Academic writing prompt categories. | Rewritten locally. |
| `scripts/*.py` | Deterministic helper concept. | Original standard-library code. |

## Boundaries

This file records methodology attribution; it is not legal advice. Re-check the
specific upstream license file before copying code, templates, examples, or long
text. If an upstream URL becomes unavailable, keep the exact URL and mark it
unavailable with the check date.
