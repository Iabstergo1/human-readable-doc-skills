# Human Readable Document Workflow

This project provides a Codex skill for reusable document work. It helps an
agent route a request, load the right references, draft Markdown, check style,
and verify the result before delivery.

## What This Solves

- Routes document tasks by type instead of applying one generic outline.
- Keeps Markdown as the editable source for substantial documents.
- Adds checks for style, Markdown structure, and generated artifacts.
- Keeps long rules in references so `SKILL.md` stays small.

## What It Does Not Solve

- It does not verify legal, medical, financial, or academic claims by itself.
- It does not invent citations, benchmark data, authors, or sources.
- It does not replace a dedicated Word or PDF repair workflow.

## Installation

Copy the skill into the target repository:

```powershell
Copy-Item -Recurse -Force D:\human-readable-doc-skills\.agents .\.agents
```

## Quick Start

Use the skill for a reusable document request:

```text
$human-readable-document-workflow 帮我写一份技术设计文档，输出 Markdown。
```

## Validation

Run the package validator:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\validate_skill.py --pretty
```

Run a routing smoke test:

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\detect_doc_intent.py `
  --file .\tests\fixtures\doc-intent-technical-zh.txt --pretty
```

## Limitations

Word and PDF are optional export adapters. Load those references only when the
user explicitly asks for those artifacts.
