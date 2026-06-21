# Upstream Source Access

Checked on 2026-06-22 with GitHub raw URLs through the user-provided proxy
`http://127.0.0.1:10808`.

This file records which referenced upstream skill sources were directly
reachable when refining the local references. The local repository still uses
rewritten methodology only; it does not vendor upstream skill text.

## Skill Source Results

| Upstream source | Raw access result |
| --- | --- |
| Writer's Loop `skills/writers-loop/SKILL.md` | 200 OK, 186 lines. |
| codex-be-serious `skills/be-serious/SKILL.md` | 200 OK, 125 lines. |
| codex-be-serious `skills/be-serious-review/SKILL.md` | 200 OK, 91 lines. |
| unslop `skills/unslop/SKILL.md` | 200 OK, 148 lines. |
| unslop `skills/humanize/SKILL.md` | 404 Not Found. |
| unslop `skills/unslop-review/SKILL.md` | 200 OK, 91 lines. |
| anti-slop-writing `english/SKILL.md` | 200 OK, 341 lines. |
| qu-ai-wei `SKILL.md` | 200 OK, 936 lines. |
| Humanizer-zh `SKILL.md` | 200 OK, 485 lines. |
| writing-humanizer `skills/writing-humanizer/SKILL.md` | 200 OK, 157 lines. |

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
