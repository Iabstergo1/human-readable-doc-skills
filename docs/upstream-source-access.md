# Upstream Source Access

Checked on 2026-06-22 with GitHub raw URLs through the user-provided proxy
`http://127.0.0.1:10808`.

This file records which referenced upstream skill sources were directly
reachable when refining the local references. The local repository still uses
rewritten methodology only; it does not vendor upstream skill text.

## Skill Source Results

| Upstream source | Raw URL | Status | Checked date | Source use | Note |
| --- | --- | --- | --- | --- | --- |
| Writer's Loop `skills/writers-loop/SKILL.md` | https://raw.githubusercontent.com/xxsang/writers-loop/main/skills/writers-loop/SKILL.md | 200 OK | 2026-06-22 | summarized | 186 lines; rewritten into local workflow and style references. |
| codex-be-serious `skills/be-serious/SKILL.md` | https://raw.githubusercontent.com/lulucatdev/codex-be-serious/main/skills/be-serious/SKILL.md | 200 OK | 2026-06-22 | summarized | 125 lines; rewritten into serious-register gates. |
| codex-be-serious `skills/be-serious-review/SKILL.md` | https://raw.githubusercontent.com/lulucatdev/codex-be-serious/main/skills/be-serious-review/SKILL.md | 200 OK | 2026-06-22 | summarized | 91 lines; review shape borrowed in rewritten form. |
| unslop `skills/unslop/SKILL.md` | https://raw.githubusercontent.com/MohamedAbdallah-14/unslop/main/skills/unslop/SKILL.md | 200 OK | 2026-06-22 | summarized | 148 lines; document-safe subset rewritten locally. |
| unslop `skills/humanize/SKILL.md` | https://raw.githubusercontent.com/MohamedAbdallah-14/unslop/main/skills/humanize/SKILL.md | 404 Not Found | 2026-06-22 | unavailable | Do not invent a replacement path. |
| unslop `skills/unslop-review/SKILL.md` | https://raw.githubusercontent.com/MohamedAbdallah-14/unslop/main/skills/unslop-review/SKILL.md | 200 OK | 2026-06-22 | summarized | 91 lines; PR-review behavior is out of scope. |
| anti-slop-writing `english/SKILL.md` | https://raw.githubusercontent.com/adenaufal/anti-slop-writing/main/english/SKILL.md | 200 OK | 2026-06-22 | summarized | 341 lines; split into document-safe and creative/blog modes. |
| qu-ai-wei `SKILL.md` | https://raw.githubusercontent.com/LifelongLazyLearner/qu-ai-wei/main/SKILL.md | 200 OK | 2026-06-22 | summarized | 936 lines; long reference taxonomy was not fully migrated. |
| Humanizer-zh `SKILL.md` | https://raw.githubusercontent.com/op7418/humanizer-zh/main/SKILL.md | 200 OK | 2026-06-22 | summarized | 485 lines; rewritten into zh style and second-pass gates. |
| writing-humanizer `skills/writing-humanizer/SKILL.md` | https://raw.githubusercontent.com/shyuan/writing-humanizer/main/skills/writing-humanizer/SKILL.md | 200 OK | 2026-06-22 | summarized | 157 lines; rewritten into two-pass and voice-preservation rules. |

## Unavailable Source

The only currently listed skill source that could not be fetched was:

https://raw.githubusercontent.com/MohamedAbdallah-14/unslop/main/skills/humanize/SKILL.md

Do not invent a replacement path for that source. Treat it as unavailable until
a later audit verifies a real upstream location.

## Non-Skill Repository References

The following entries are repository-level methodology references in this
project, not specific upstream skill files:

- prompts.chat
- ChatGPT Prompts for Academic Writing

They remain attribution references for prompt modularity and academic writing
categories, but they were not treated as directly importable Codex skill
sources in this audit.
