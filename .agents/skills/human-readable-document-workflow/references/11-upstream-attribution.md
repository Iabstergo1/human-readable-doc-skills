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
Capability parity is recorded in `docs/upstream-parity-matrix.md`.

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
- Borrowed capability: iterative writing workflow, checkpoints, revision
  decisions, preference signals, style distillation, and style matching.
- Local equivalent: `references/01-writing-loop.md`,
  `references/13-style-distillation.md`, and `SKILL.md`.
- Parity status: implemented for document workflow and session-only style
  packs; durable preference storage is intentionally out of scope.
- Out-of-scope parts: durable preference journal and local style pack storage
  unless the user explicitly asks for storage.
- Source access status: raw `SKILL.md` was accessible on 2026-06-22; source
  text is summarized and rewritten locally.
- License note: GitHub metadata previously observed as MIT.

### codex-be-serious

- Repo: https://github.com/lulucatdev/codex-be-serious
- Main skill: https://github.com/lulucatdev/codex-be-serious/tree/main/skills/be-serious
- Review skill: https://github.com/lulucatdev/codex-be-serious/tree/main/skills/be-serious-review
- Borrowed capability: serious register, anti-sycophancy, anti-marketing,
  no-slang review, and sober revision shape.
- Local equivalent: Serious Register Gate in `references/10-quality-gates.md`
  and `lint_ai_style.py --mode serious-review`.
- Parity status: implemented for formal document review; session-wide register
  persistence is intentionally out of scope.
- Out-of-scope parts: global conversation register control.
- Source access status: raw main and review skills were accessible on
  2026-06-22; source text is summarized and rewritten locally.
- License note: GitHub metadata previously observed as MIT.

### unslop

- Repo: https://github.com/MohamedAbdallah-14/unslop
- Main skill: https://github.com/MohamedAbdallah-14/unslop/tree/main/skills/unslop
- Review skill: https://github.com/MohamedAbdallah-14/unslop/tree/main/skills/unslop-review
- Unavailable path: `skills/humanize` returned 404 on 2026-06-22.
- Borrowed capability: conservative anti-template cleanup, voice preservation,
  stock vocabulary cleanup, hedging cleanup, tricolon cleanup, and technical
  preservation.
- Local equivalent: `references/03-anti-ai-slop-zh.md`,
  `references/04-anti-ai-slop-en.md`, `references/13-style-distillation.md`,
  and `lint_ai_style.py`.
- Parity status: implemented for document-safe cleanup; voice matching is
  partially implemented through session-only style packs.
- Out-of-scope parts: slash modes, anti-detector mode, hooks, statusline,
  session-wide persistence, and PR comment workflows.
- Source access status: raw main and review skills were accessible on
  2026-06-22; `skills/humanize` is unavailable.
- License note: GitHub metadata previously observed as MIT.

### anti-slop-writing

- Repo: https://github.com/adenaufal/anti-slop-writing
- English directory: https://github.com/adenaufal/anti-slop-writing/tree/main/english
- English SKILL.md: https://github.com/adenaufal/anti-slop-writing/blob/main/english/SKILL.md
- Borrowed capability: English filler cleanup, structure-pattern avoidance,
  formulaic conclusion cleanup, and detector-aware risk framing.
- Local equivalent: `references/04-anti-ai-slop-en.md`, anti-slop mode map in
  `references/12-document-type-profiles.md`, and `lint_ai_style.py --mode`.
- Parity status: partially implemented. This project separates document-safe
  cleanup from creative/blog cleanup.
- Out-of-scope parts: hard detector-first rewriting, absolute vocabulary bans,
  forced imperfection, and absolute em-dash bans.
- Source access status: raw English `SKILL.md` was accessible on 2026-06-22;
  source text is summarized and rewritten locally.
- License note: GitHub metadata previously observed as MIT.

### qu-ai-wei

- Repo: https://github.com/LifelongLazyLearner/qu-ai-wei
- SKILL.md: https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/SKILL.md
- References: https://github.com/LifelongLazyLearner/qu-ai-wei/tree/main/references
- Scripts: https://github.com/LifelongLazyLearner/qu-ai-wei/tree/main/scripts
- Borrowed capability: Chinese anti-AI stance, real-human stop gate, register
  selection, conflict arbitration, no-fact-invention, and anti-sanitization.
- Local equivalent: `references/03-anti-ai-slop-zh.md`,
  `references/10-quality-gates.md`, and zh lint categories.
- Parity status: implemented for the shared document-safe subset; full 51-rule
  taxonomy and reference files need source text for fuller migration.
- Out-of-scope parts: generic brand voice, platform-specific playbooks, and
  reusable whitelists unless the user supplies a target brand or platform.
- Source access status: raw main `SKILL.md` was accessible on 2026-06-22, but
  long reference files were not fully migrated.
- License note: GitHub metadata previously observed as MIT.

### Humanizer-zh

- Repo: https://github.com/op7418/humanizer-zh
- SKILL.md: https://github.com/op7418/humanizer-zh/blob/main/SKILL.md
- Borrowed capability: Chinese human-readable prose, formula cleanup, voice
  preservation, and avoiding sterile neutral rewrites.
- Local equivalent: `references/02-human-readable-style.md`,
  `references/03-anti-ai-slop-zh.md`, and Second-Pass Humanization Gate.
- Parity status: implemented for preservation and second-pass review; scoring
  output is intentionally out of scope.
- Out-of-scope parts: default score reports.
- Source access status: raw `SKILL.md` was accessible on 2026-06-22; source
  text is summarized and rewritten locally.
- License note: GitHub metadata previously observed as MIT.

### writing-humanizer

- Repo: https://github.com/shyuan/writing-humanizer
- Skill directory: https://github.com/shyuan/writing-humanizer/tree/main/skills/writing-humanizer
- Borrowed capability: two-pass humanization, cleanup boundaries, and voice
  preservation.
- Local equivalent: `references/02-human-readable-style.md`,
  `references/10-quality-gates.md`, and `SKILL.md` routing.
- Parity status: partially implemented for mode taxonomy; implemented for
  second-pass review behavior.
- Out-of-scope parts: mandatory score output and persistent mode behavior.
- Source access status: raw skill was accessible on 2026-06-22; source text is
  summarized and rewritten locally.
- License note: GitHub metadata previously observed as MIT.

### prompts.chat

- Repo: https://github.com/f/prompts.chat
- Reference path: repository root.
- Borrowed capability: prompt modularity and attribution discipline.
- Local equivalent: README attribution and reference-split project structure.
- Parity status: partially implemented as methodology only.
- Out-of-scope parts: prompt catalog mirroring.
- Source access status: repository-level reference; not treated as a Codex
  skill source in this audit.
- License note: GitHub metadata previously observed as Other / NOASSERTION.

### ChatGPT Prompts for Academic Writing

- Repo: https://github.com/ahmetbersoz/chatgpt-prompts-for-academic-writing
- Reference path: repository root.
- Borrowed capability: academic writing prompt categories and task framing.
- Local equivalent: `references/05-academic-writing.md` and
  `references/12-document-type-profiles.md`.
- Parity status: partially implemented as document profiles, not prompt
  catalog mirroring.
- Out-of-scope parts: copying prompt lists or treating prompts as citations.
- Source access status: repository-level reference; not treated as a Codex
  skill source in this audit.
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
| `references/10-quality-gates.md` | Serious review and second-pass gates. | Rewritten locally. |
| `references/13-style-distillation.md` | Session-only style pack handling. | Rewritten locally. |
| `scripts/*.py` | Deterministic helper concept. | Original standard-library code. |

## Boundaries

This file records methodology attribution; it is not legal advice. Re-check the
specific upstream license file before copying code, templates, examples, or long
text. If an upstream URL becomes unavailable, keep the exact URL and mark it
unavailable with the check date.
