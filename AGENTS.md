# AGENTS.md

## Project Scope

This repository is a Codex Skills project, not a general document repository. Keep changes focused on making the skill easier for another Codex agent to discover, load, and use.

## Skill Structure

- Do not merge every rule into one oversized `SKILL.md`.
- Keep `SKILL.md` as the orchestration layer: routing, workflow, and when to load references.
- Put longer style rules, document-type guidance, export policy, and quality gates in `references/`.
- Put deterministic checks, normalization, and rendering wrappers in `scripts/`.
- Put templates and examples in `assets/`.

## Attribution And Licenses

- Do not copy complete protected text from third-party open-source projects without explicit permission.
- It is acceptable to abstract, rewrite, and summarize public methodology such as writing loops, anti-slop review patterns, or document-rendering workflows.
- Preserve attribution and license notes in `README.md` when a third-party method or project materially informs this repository.
- Use only the upstream projects listed in `README.md` as methodology references. Do not invent skill names, repository paths, or replacement URLs.
- If a listed upstream URL becomes unavailable, mark that exact URL as unavailable and continue with the remaining verified references.
- When refreshing upstream GitHub references in this workspace, use the user-provided proxy `http://127.0.0.1:10808` unless a newer instruction changes it.

## Platform Rules

- All new scripts must run on Windows 11 with PowerShell 7.
- Prefer PowerShell-compatible examples in docs.
- Python scripts should avoid heavy dependencies. If a dependency becomes necessary, document it in `README.md` with installation and fallback notes.

## Verification

After each meaningful change, check:

- Directory structure still matches the intended skill layout.
- `SKILL.md` has YAML frontmatter with `name` and `description`.
- Reference files remain split by topic and are linked from `SKILL.md`.
- Python scripts have an `argparse` CLI and can show `--help`.
- Markdown files are readable and free of accidental placeholder-only sections.

## Language

When producing user-facing output for Chinese users, default to Simplified Chinese unless the task, source material, or deliverable clearly requires another language.
