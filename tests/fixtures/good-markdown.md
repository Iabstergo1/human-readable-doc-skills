---
title: "PDF Preprocessing Architecture"
date: "2026-06-21"
---

# PDF Preprocessing Architecture

## Background

The preprocessing layer accepts text PDFs, scanned PDFs, and mixed PDFs. It
normalizes them into page text, page images, metadata, and error records for
downstream indexing.

## Inputs And Outputs

| Item | Description |
| --- | --- |
| Input | PDF file, source, task id. |
| Output | Page text, page image, metadata, error state. |

## Validation Command

```powershell
python .\scripts\validate_markdown_source.py .\draft.md
```
