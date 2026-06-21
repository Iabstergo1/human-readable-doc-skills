# Document Type Profiles

Use profiles to avoid applying one generic anti-AI rule set to every document.
Each profile defines structure, tone, references, export notes, and boundaries.

## Profile Index

| Profile | Use for |
| --- | --- |
| `technical-design` | Architecture, design docs, APIs, data flow, implementation plans. |
| `README` | GitHub project homepages and repository documentation. |
| `academic-paper` | Papers, thesis sections, model descriptions, scholarly arguments. |
| `literature-review` | Research background and synthesis of existing work. |
| `business-report` | Operational, market, strategy, and management reports. |
| `proposal` | Project plans, grant proposals, and persuasive plans. |
| `manual / SOP` | Step-by-step operating procedures and repeatable workflows. |
| `meeting-notes` | Meeting summaries, decisions, risks, and action items. |
| `email` | Professional emails, announcements, outreach, and follow-ups. |
| `general-article` | Essays, explanatory articles, blog-like documents. |

## Technical Design

| Field | Guidance |
| --- | --- |
| Trigger keywords | 技术设计, 架构, architecture, design doc, API, pipeline, data flow, error handling. |
| Recommended structure | Use the outline below. |
| Default tone | Direct, concrete, implementation-oriented. |
| References to load | 00, 01, 02, language anti-slop, 06, 07, 08/09 if export requested, 10, 12. |
| Do not | Add marketing claims, skip failure modes, hide assumptions, use diagrams without explanation. |
| Markdown/Word/PDF notes | Prefer Markdown source with tables for I/O and risks; code blocks need language labels; Word/PDF should render from the same source. |

Example outline:

```markdown

# PDF Preprocessing Architecture

## Background And Problem

## Goals And Non-Goals

## Inputs And Outputs

## Architecture

## Processing Flow

## Error Handling

## Performance And Scalability

## Validation Plan

## Risks And Next Steps

```

Structure notes:

- Background and problem.
- Goals and non-goals.
- Inputs and outputs.
- Architecture and data flow.
- Error handling.
- Performance and scalability.
- Validation plan.
- Risks and next steps.

## README

| Field | Guidance |
| --- | --- |
| Trigger keywords | README, repo docs, GitHub 项目主页, installation, usage, quickstart. |
| Recommended structure | What it is; what problem it solves; installation; quick start; examples; configuration; tests; limitations; roadmap; license/attribution. |
| Default tone | Practical, concise, project-facing. |
| References to load | 00, 01, 02, 04 for English or 03 for Chinese, 07, 10, 12. |
| Do not | Turn README into a sales page, omit setup commands, bury limitations. |
| Markdown/Word/PDF notes | Markdown is usually the final format; tables must render on GitHub. |

Example outline:

```markdown

# Project Name

## What This Solves

## What It Does Not Solve

## Installation

## Quick Start

## Directory Structure

## Validation

## Attribution

## Roadmap

```

## Academic Paper

| Field | Guidance |
| --- | --- |
| Trigger keywords | 论文, thesis, academic paper, model, variables, formula, citation. |
| Recommended structure | Concept definitions; research question; literature position; method; model/variables/symbols; argument chain; limitations; citation placeholders. |
| Default tone | Formal, precise, source-bounded. |
| References to load | 00, 01, 02, 03/04, 05, 07, 10, 12. |
| Do not | Invent literature, authors, years, journals, DOI, data, or findings. |
| Markdown/Word/PDF notes | Use YAML frontmatter when useful; formulas need explanation; citations only from supplied sources or `[citation needed]`. |

Example outline:

```markdown

# Chapter 3 Model Specification

## Concept Definitions

## Research Question

## Model Setup

## Variable Definitions

## Identification Assumptions

## Expected Relationships

## Limitations

```

## Literature Review

| Field | Guidance |
| --- | --- |
| Trigger keywords | 文献综述, literature review, research background, prior work. |
| Recommended structure | Scope; search/source boundary; thematic map; methodological comparison; findings; gaps; relation to current work. |
| Default tone | Synthetic, careful, non-inventive. |
| References to load | 00, 01, 02, 05, 07, 10, 12. |
| Do not | Pretend to have read papers not provided; fabricate citation clusters. |
| Markdown/Word/PDF notes | Use tables only for real comparison; keep placeholders visible. |

Example outline:

```markdown

# Literature Review

## Scope And Source Boundary

## Theme 1

## Theme 2

## Methodological Comparison

## Gaps

## Position Of This Study

```

## Business Report

| Field | Guidance |
| --- | --- |
| Trigger keywords | business report, 汇报, 经营分析, 市场, strategy, memo. |
| Recommended structure | Executive summary; context; findings; evidence; options; recommendation; risks; next actions. |
| Default tone | Clear, decision-oriented, factual. |
| References to load | 00, 01, 02, language anti-slop, 06, 07, 10, 12. |
| Do not | Add unsupported market claims or generic growth language. |
| Markdown/Word/PDF notes | Tables are useful for options, costs, risks, and owners. |

Example outline:

```markdown

# Business Report

## Executive Summary

## Context

## Findings

## Options

## Recommendation

## Risks

## Next Actions

```

## Proposal

| Field | Guidance |
| --- | --- |
| Trigger keywords | proposal, 方案, 计划书, project plan, grant, pitch. |
| Recommended structure | Problem; goal; proposed approach; scope; timeline; resources; risks; expected outcomes; decision needed. |
| Default tone | Persuasive but concrete. |
| References to load | 00, 01, 02, language anti-slop, 06, 07, 10, 12. |
| Do not | Overpromise impact, hide cost, or use vague benefit language. |
| Markdown/Word/PDF notes | Word/PDF may be needed for stakeholder delivery; keep Markdown source. |

Example outline:

```markdown

# Proposal

## Problem

## Goal

## Proposed Approach

## Scope

## Timeline

## Resources

## Risks

## Decision Needed

```

## Manual / SOP

| Field | Guidance |
| --- | --- |
| Trigger keywords | SOP, manual, 操作手册, 指南, runbook, procedure. |
| Recommended structure | Purpose; scope; prerequisites; roles; steps; checks; rollback; troubleshooting; change log. |
| Default tone | Procedural, unambiguous, compact. |
| References to load | 00, 01, 02, language anti-slop, 06, 07, 10, 12. |
| Do not | Use vague advice, omit prerequisites, or mix rationale with action steps. |
| Markdown/Word/PDF notes | Lists and tables are appropriate; steps need stable numbering. |

Example outline:

```markdown

# SOP Title

## Purpose

## Scope

## Prerequisites

## Roles

## Procedure

## Verification

## Troubleshooting

## Change Log

```

## Meeting Notes

| Field | Guidance |
| --- | --- |
| Trigger keywords | 会议纪要, meeting notes, minutes, action items, decisions. |
| Recommended structure | Context; attendees; decisions; discussion summary; risks; action items; open questions. |
| Default tone | Neutral, concise, accountable. |
| References to load | 00, 01, 02, language anti-slop, 07, 10, 12. |
| Do not | Invent decisions, assign owners not present in source, or over-polish disagreements. |
| Markdown/Word/PDF notes | Tables work well for action items with owner and due date. |

Example outline:

```markdown

# Meeting Notes

## Context

## Decisions

## Discussion Summary

## Risks

## Action Items

## Open Questions

```

## Email

| Field | Guidance |
| --- | --- |
| Trigger keywords | email, 邮件, 通知, follow-up, outreach. |
| Recommended structure | Subject; opening context; main request or update; details; deadline or action; close. |
| Default tone | Professional, direct, appropriately polite. |
| References to load | 00, 01 compressed, 02, language anti-slop, 10, 12. |
| Do not | Add exaggerated flattery, bury the ask, or invent relationship context. |
| Markdown/Word/PDF notes | Usually chat output; Markdown only when archived or reused. |

Example outline:

```markdown
Subject: Review request for PDF preprocessing design

Hi [Name],

Context...

Request...

Deadline...
```

## General Article

| Field | Guidance |
| --- | --- |
| Trigger keywords | article, blog, 文章, explanation, guide with no narrower type. |
| Recommended structure | Reader question; context; main explanation; examples; limitations; conclusion. |
| Default tone | Clear, explanatory, reader-friendly. |
| References to load | 00, 01, 02, language anti-slop, 07, 10, 12. |
| Do not | Use clickbait titles, overgeneralize, or end with generic inspiration. |
| Markdown/Word/PDF notes | Markdown is default; use Word/PDF only when requested. |

Example outline:

```markdown

# Article Title

## Reader Question

## Context

## Main Explanation

## Example

## Limitations

## Takeaway

```

## Boundaries

Profiles guide defaults; user instructions override them when explicit. If a
document spans profiles, pick a primary profile and load secondary references
only for the sections that need them.
