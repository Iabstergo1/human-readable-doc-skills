# Remote Validation

This file records the v0.2.2 remote consistency check. The purpose is to verify
that GitHub raw content matches the locally validated repository content.

## Check Metadata

| Field | Value |
| --- | --- |
| Checked at | 2026-06-22 00:03:39 +08:00 |
| Repository | `Iabstergo1/human-readable-doc-skills` |
| Branch | `main` |
| Local HEAD | `e715c35f0db46e410e28994d2ed5a3765dc5ce1c` |
| Remote `origin/main` | `e715c35f0db46e410e28994d2ed5a3765dc5ce1c` |
| Temp download directory | `C:\Users\Lenovo\AppData\Local\Temp\hrds-remote-validation-b9e75f64919e43e7ab2d875f38ddba26` |

## Method

The check downloaded these GitHub raw URLs into a temporary directory:

- `https://raw.githubusercontent.com/Iabstergo1/human-readable-doc-skills/main/.agents/skills/human-readable-document-workflow/SKILL.md`
- `https://raw.githubusercontent.com/Iabstergo1/human-readable-doc-skills/main/.agents/skills/human-readable-document-workflow/scripts/validate_skill.py`
- `https://raw.githubusercontent.com/Iabstergo1/human-readable-doc-skills/main/.agents/skills/human-readable-document-workflow/references/12-document-type-profiles.md`
- `https://raw.githubusercontent.com/Iabstergo1/human-readable-doc-skills/main/.agents/skills/human-readable-document-workflow/references/03-anti-ai-slop-zh.md`

For each file, the check computed:

- remote line count;
- remote maximum line length;
- non-URL lines over 220 characters;
- canonical SHA-256 after normalizing line endings and ignoring final trailing
  newlines;
- equality against local worktree content;
- equality against `HEAD:<path>`;
- `SKILL.md` frontmatter boundary details;
- `python -m py_compile` for the downloaded raw `validate_skill.py`.

## Results

| File | Lines | Max line | Lines over 220 | Matches worktree | Matches HEAD |
| --- | ---: | ---: | ---: | --- | --- |
| `SKILL.md` | 128 | 80 | 0 | yes | yes |
| `scripts/validate_skill.py` | 337 | 122 | 0 | yes | yes |
| `references/12-document-type-profiles.md` | 362 | 173 | 0 | yes | yes |
| `references/03-anti-ai-slop-zh.md` | 210 | 75 | 0 | yes | yes |

## Frontmatter

Remote raw `SKILL.md` starts with strict YAML frontmatter:

```yaml
---
name: human-readable-document-workflow
description: >-
```

The closing `---` is present on line 10 and is a standalone line.

## Python Compile

Downloaded raw `validate_skill.py` was compiled from the temporary directory:

```powershell
python -m py_compile <temp>\.agents\skills\human-readable-document-workflow\scripts\validate_skill.py
```

Result: exit code `0`, no output.

## Conclusion

Remote GitHub raw content matches both the local worktree and `HEAD` for the
checked files. The raw files are not compressed into a small number of long
lines. `SKILL.md` has valid multi-line frontmatter, and the downloaded raw
`validate_skill.py` is compilable Python source.

Note: an earlier hash attempt compared GitHub raw content with `git show`
captured through PowerShell line arrays and incorrectly reported HEAD mismatches
because final trailing newlines were lost. The result above uses canonicalized
line endings and ignores only final trailing newlines.
