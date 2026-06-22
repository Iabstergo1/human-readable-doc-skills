# Upstream Source Access

Checked on 2026-06-22 with GitHub raw URLs through the user-provided proxy
`http://127.0.0.1:10808`.

This file records which referenced upstream skill sources were directly
reachable when refining the local references. The local repository still uses
rewritten methodology only; it does not vendor upstream skill text.

## Skill Source Results

| Upstream source | Raw URL | Status | Checked date | Source use | Note |
| --- | --- | --- | --- | --- | --- |
| Codex manual, Agent Skills section | local cache from https://developers.openai.com/codex/codex-manual.md | 200 OK | 2026-06-22 | summarized | Confirms skill directory, `SKILL.md`, optional scripts and references. |
| Codex manual, AGENTS.md section | local cache from https://developers.openai.com/codex/codex-manual.md | 200 OK | 2026-06-22 | summarized | Confirms repo guidance belongs in `AGENTS.md`. |
| Writer's Loop `SKILL.md` | https://raw.githubusercontent.com/xxsang/writers-loop/main/skills/writers-loop/SKILL.md | 200 OK | 2026-06-22 | summarized | 186 lines; workflow entrypoint. |
| Writer's Loop `checkpoints.md` | https://raw.githubusercontent.com/xxsang/writers-loop/main/skills/writers-loop/references/checkpoints.md | 200 OK | 2026-06-22 | summarized | 137 lines; checkpoint behavior. |
| Writer's Loop `critique-rubrics.md` | https://raw.githubusercontent.com/xxsang/writers-loop/main/skills/writers-loop/references/critique-rubrics.md | 200 OK | 2026-06-22 | summarized | 115 lines; critique dimensions. |
| Writer's Loop `preference-signals.md` | https://raw.githubusercontent.com/xxsang/writers-loop/main/skills/writers-loop/references/preference-signals.md | 200 OK | 2026-06-22 | summarized | 130 lines; preference evidence boundary. |
| Writer's Loop `style-distillation.md` | https://raw.githubusercontent.com/xxsang/writers-loop/main/skills/writers-loop/references/style-distillation.md | 200 OK | 2026-06-22 | summarized | 305 lines; style pack boundary. |
| Writer's Loop `technical-writing.md` | https://raw.githubusercontent.com/xxsang/writers-loop/main/skills/writers-loop/references/technical-writing.md | 200 OK | 2026-06-22 | summarized | 99 lines; technical checklist. |
| Writer's Loop `business-writing.md` | https://raw.githubusercontent.com/xxsang/writers-loop/main/skills/writers-loop/references/business-writing.md | 200 OK | 2026-06-22 | summarized | 137 lines; business checklist. |
| Writer's Loop `translation.md` | https://raw.githubusercontent.com/xxsang/writers-loop/main/skills/writers-loop/references/translation.md | 200 OK | 2026-06-22 | summarized | 260 lines; document-level translation boundary. |
| Writer's Loop `validation-scenarios.md` | https://raw.githubusercontent.com/xxsang/writers-loop/main/skills/writers-loop/references/validation-scenarios.md | 200 OK | 2026-06-22 | summarized | 336 lines; scenario coverage. |
| codex-be-serious main skill | https://raw.githubusercontent.com/lulucatdev/codex-be-serious/main/skills/be-serious/SKILL.md | 200 OK | 2026-06-22 | summarized | 125 lines; serious register. |
| codex-be-serious review skill | https://raw.githubusercontent.com/lulucatdev/codex-be-serious/main/skills/be-serious-review/SKILL.md | 200 OK | 2026-06-22 | summarized | 91 lines; review shape. |
| unslop main skill | https://raw.githubusercontent.com/MohamedAbdallah-14/unslop/main/skills/unslop/SKILL.md | 200 OK | 2026-06-22 | summarized | 148 lines; document-safe subset. |
| unslop review skill | https://raw.githubusercontent.com/MohamedAbdallah-14/unslop/main/skills/unslop-review/SKILL.md | 200 OK | 2026-06-22 | summarized | 91 lines; review behavior is not default. |
| anti-slop-writing English skill | https://raw.githubusercontent.com/adenaufal/anti-slop-writing/main/english/SKILL.md | 200 OK | 2026-06-22 | summarized | 341 lines; mode split. |
| anti-slop-writing vocabulary banlist | https://raw.githubusercontent.com/adenaufal/anti-slop-writing/main/english/references/vocabulary-banlist.md | 200 OK | 2026-06-22 | summarized | 371 lines; risk list, not global ban. |
| anti-slop-writing structural patterns | https://raw.githubusercontent.com/adenaufal/anti-slop-writing/main/english/references/structural-patterns.md | 200 OK | 2026-06-22 | summarized | 450 lines; structural pattern risks. |
| qu-ai-wei `SKILL.md` | https://raw.githubusercontent.com/LifelongLazyLearner/qu-ai-wei/main/SKILL.md | 200 OK | 2026-06-22 | summarized | 936 lines; zh workflow. |
| qu-ai-wei `patterns.md` | https://raw.githubusercontent.com/LifelongLazyLearner/qu-ai-wei/main/references/patterns.md | 200 OK | 2026-06-22 | summarized | 986 lines; full taxonomy not vendored. |
| qu-ai-wei `whitelists.md` | https://raw.githubusercontent.com/LifelongLazyLearner/qu-ai-wei/main/references/whitelists.md | 200 OK | 2026-06-22 | summarized | 134 lines; out of scope for generic repo. |
| qu-ai-wei `brand-voice.md` | https://raw.githubusercontent.com/LifelongLazyLearner/qu-ai-wei/main/references/brand-voice.md | 200 OK | 2026-06-22 | summarized | 190 lines; out of scope without brand input. |
| qu-ai-wei `platform-patterns.md` | https://raw.githubusercontent.com/LifelongLazyLearner/qu-ai-wei/main/references/platform-patterns.md | 200 OK | 2026-06-22 | summarized | 266 lines; out of scope without platform target. |
| qu-ai-wei `punctuation.md` | https://raw.githubusercontent.com/LifelongLazyLearner/qu-ai-wei/main/references/punctuation.md | 200 OK | 2026-06-22 | summarized | 118 lines; safe subset only. |
| qu-ai-wei `syntax.md` | https://raw.githubusercontent.com/LifelongLazyLearner/qu-ai-wei/main/references/syntax.md | 200 OK | 2026-06-22 | summarized | 60 lines; safe subset only. |
| qu-ai-wei `reference-models.md` | https://raw.githubusercontent.com/LifelongLazyLearner/qu-ai-wei/main/references/reference-models.md | 200 OK | 2026-06-22 | summarized | 71 lines; not copied. |
| qu-ai-wei `sources.md` | https://raw.githubusercontent.com/LifelongLazyLearner/qu-ai-wei/main/references/sources.md | 200 OK | 2026-06-22 | summarized | 56 lines; not copied. |
| Humanizer-zh `SKILL.md` | https://raw.githubusercontent.com/op7418/humanizer-zh/main/SKILL.md | 200 OK | 2026-06-22 | summarized | 485 lines; zh preservation. |
| writing-humanizer `SKILL.md` | https://raw.githubusercontent.com/shyuan/writing-humanizer/main/skills/writing-humanizer/SKILL.md | 200 OK | 2026-06-22 | summarized | 157 lines; two-pass cleanup. |
| ChatGPT Prompts for Academic Writing README | https://raw.githubusercontent.com/ahmetbersoz/chatgpt-prompts-for-academic-writing/main/README.md | 200 OK | 2026-06-22 | summarized | 412 lines; academic task categories. |

No required source in the current whitelist failed to fetch.

## Non-Skill Repository References

The following entries are repository-level methodology references in this
project, not specific upstream skill files:

- prompts.chat
- ChatGPT Prompts for Academic Writing

They remain attribution references for prompt modularity and academic writing
categories, but they were not treated as directly importable Codex skill
sources in this audit.

`prompts.chat` was treated as an organization-pattern reference only. Its
prompt collection was not copied into this repository.
