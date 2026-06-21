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

### Trigger Keywords

技术设计, 架构, architecture, design doc, API, pipeline, data flow,
error handling.

### Recommended Structure

- Background and problem.
- Goals and non-goals.
- Inputs and outputs.
- Architecture and data flow.
- Processing flow.
- Error handling.
- Performance and scalability.
- Validation plan.
- Risks and next steps.

### Default Tone

Direct, concrete, implementation-oriented.

### References To Load

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- Language-specific anti-slop reference.
- `references/06-document-layout.md`
- `references/07-markdown-authoring.md`
- `references/08-word-export.md` only when Word export is explicitly requested.
- `references/09-pdf-export.md` only when PDF export is explicitly requested.
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Do Not

- Add marketing claims.
- Skip failure modes.
- Hide assumptions.
- Use diagrams without explanation.

### Markdown And Export Notes

Prefer Markdown source with tables for I/O and risks. Code blocks need language
labels. Word and PDF should render from the same source only when requested.

### Example Outline

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

### Trigger Keywords

README, repo docs, GitHub 项目主页, installation, usage, quickstart.

### Recommended Structure

- What it is.
- What problem it solves.
- Installation.
- Quick start.
- Examples.
- Configuration.
- Tests.
- Limitations.
- Roadmap.
- License or attribution.

### Default Tone

Practical, concise, project-facing.

### References To Load

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- `references/04-anti-ai-slop-en.md` for English.
- `references/03-anti-ai-slop-zh.md` for Chinese.
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Do Not

- Turn README into a sales page.
- Omit setup commands.
- Bury limitations.

### Markdown And Export Notes

Markdown is usually the final format. Tables must render cleanly on GitHub.

### Example Outline

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

### Trigger Keywords

论文, thesis, academic paper, model, variables, formula, citation.

### Recommended Structure

- Concept definitions.
- Research question.
- Literature position.
- Method.
- Model, variables, and symbols.
- Argument chain.
- Limitations.
- Citation placeholders.

### Default Tone

Formal, precise, source-bounded.

### References To Load

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- `references/03-anti-ai-slop-zh.md` or `references/04-anti-ai-slop-en.md`.
- `references/05-academic-writing.md`
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Do Not

- Invent literature, authors, years, journals, DOI, data, or findings.
- Flatten model logic into generic prose.
- Remove necessary formal terms only to sound casual.

### Markdown And Export Notes

Use YAML frontmatter when useful. Formulas need explanation. Citations must come
from supplied sources or remain as `[citation needed]`.

### Example Outline

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

### Trigger Keywords

文献综述, literature review, research background, prior work.

### Recommended Structure

- Scope.
- Search or source boundary.
- Thematic map.
- Methodological comparison.
- Findings.
- Gaps.
- Relation to current work.

### Default Tone

Synthetic, careful, non-inventive.

### References To Load

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- `references/05-academic-writing.md`
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Do Not

- Pretend to have read papers not provided.
- Fabricate citation clusters.
- Treat a list of paper summaries as synthesis.

### Markdown And Export Notes

Use tables only for real comparisons. Keep placeholders visible when sources are
missing.

### Example Outline

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

### Trigger Keywords

business report, 汇报, 经营分析, 市场, strategy, memo.

### Recommended Structure

- Executive summary.
- Context.
- Findings.
- Evidence.
- Options.
- Recommendation.
- Risks.
- Next actions.

### Default Tone

Clear, decision-oriented, factual.

### References To Load

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- Language-specific anti-slop reference.
- `references/06-document-layout.md`
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Do Not

- Add unsupported market claims.
- Use generic growth language.
- Hide the decision the reader needs to make.

### Markdown And Export Notes

Tables are useful for options, costs, risks, and owners.

### Example Outline

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

### Trigger Keywords

proposal, 方案, 计划书, project plan, grant, pitch.

### Recommended Structure

- Problem.
- Goal.
- Proposed approach.
- Scope.
- Timeline.
- Resources.
- Risks.
- Expected outcomes.
- Decision needed.

### Default Tone

Persuasive but concrete.

### References To Load

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- Language-specific anti-slop reference.
- `references/06-document-layout.md`
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Do Not

- Overpromise impact.
- Hide cost.
- Use vague benefit language.

### Markdown And Export Notes

Word or PDF may be needed for stakeholder delivery, but only when explicitly
requested. Keep Markdown as the source.

### Example Outline

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

### Trigger Keywords

SOP, manual, 操作手册, 指南, runbook, procedure.

### Recommended Structure

- Purpose.
- Scope.
- Prerequisites.
- Roles.
- Procedure.
- Verification.
- Rollback.
- Troubleshooting.
- Change log.

### Default Tone

Procedural, unambiguous, compact.

### References To Load

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- Language-specific anti-slop reference.
- `references/06-document-layout.md`
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Do Not

- Use vague advice.
- Omit prerequisites.
- Mix rationale with action steps.

### Markdown And Export Notes

Lists and tables are appropriate. Steps need stable numbering.

### Example Outline

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

### Trigger Keywords

会议纪要, meeting notes, minutes, action items, decisions.

### Recommended Structure

- Context.
- Attendees.
- Decisions.
- Discussion summary.
- Risks.
- Action items.
- Open questions.

### Default Tone

Neutral, concise, accountable.

### References To Load

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- Language-specific anti-slop reference.
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Do Not

- Invent decisions.
- Assign owners not present in source.
- Over-polish disagreements.

### Markdown And Export Notes

Tables work well for action items with owner and due date.

### Example Outline

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

### Trigger Keywords

email, 邮件, 通知, follow-up, outreach.

### Recommended Structure

- Subject.
- Opening context.
- Main request or update.
- Details.
- Deadline or action.
- Close.

### Default Tone

Professional, direct, appropriately polite.

### References To Load

- `references/00-routing-policy.md`
- `references/01-writing-loop.md` in compressed form.
- `references/02-human-readable-style.md`
- Language-specific anti-slop reference.
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Do Not

- Add exaggerated flattery.
- Bury the ask.
- Invent relationship context.

### Markdown And Export Notes

Usually chat output. Use Markdown only when the email must be archived or
reused.

### Example Outline

```markdown
Subject: Review request for PDF preprocessing design

Hi [Name],

Context...

Request...

Deadline...
```

## General Article

### Trigger Keywords

article, blog, 文章, explanation, guide with no narrower type.

### Recommended Structure

- Reader question.
- Context.
- Main explanation.
- Examples.
- Limitations.
- Conclusion.

### Default Tone

Clear, explanatory, reader-friendly.

### References To Load

- `references/00-routing-policy.md`
- `references/01-writing-loop.md`
- `references/02-human-readable-style.md`
- Language-specific anti-slop reference.
- `references/07-markdown-authoring.md`
- `references/10-quality-gates.md`
- `references/12-document-type-profiles.md`

### Do Not

- Use clickbait titles.
- Overgeneralize.
- End with generic inspiration.

### Markdown And Export Notes

Markdown is default. Use Word or PDF only when requested.

### Example Outline

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
