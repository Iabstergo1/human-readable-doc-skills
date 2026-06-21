# Writing Loop

Use a loop instead of jumping from prompt to final draft. Important documents
must pass through at least `plan -> draft -> critique -> revise`. Short tasks
may compress the visible process, but they still need a fact-boundary check.

## Phase Overview

| Phase | Required output |
| --- | --- |
| Intake | Task brief and source boundary. |
| Frame | Reader problem and delivery boundary. |
| Plan | Stable section structure. |
| Draft | Complete first version. |
| Critique | Issues across facts, structure, style, and renderability. |
| Revise | Final source draft. |
| Layout normalize | Render-ready Markdown. |
| Finalize | Requested artifact or render path. |

## Phase Details

### 1. Intake

- Purpose: determine what must be written and what must be preserved.
- Input: request, source text, files, audience, format, tone, and constraints.
- Output: compact task brief and source boundary.
- Skip or compress: never skip; compress for short edits.
- Failure modes: invented facts, missing format, changed protected content.
- Quality check: can you state goal, reader, format, language, and gaps?

### 2. Frame

- Purpose: define the document's problem and reader questions.
- Input: task brief and document type.
- Output: one framing sentence or internal framing note.
- Skip or compress: short emails or meeting notes.
- Failure modes: generic openings, wrong audience, vague purpose.
- Quality check: does the frame explain why the document exists?

### 3. Plan

- Purpose: build the structure before drafting.
- Input: frame, profile, required sections.
- Output: headings, section order, and expected evidence.
- Skip or compress: very short rewrites under one page.
- Failure modes: shallow outline, skipped sections, too many heading levels.
- Quality check: does each section answer a reader question?

### 4. Draft

- Purpose: produce the first coherent version.
- Input: plan and source material.
- Output: complete draft in the requested language.
- Skip or compress: never skip for new documents.
- Failure modes: polished filler, unsupported claims, list-only writing.
- Quality check: does every paragraph move the document forward?

### 5. Critique

- Purpose: find defects before the user sees the draft.
- Input: draft and quality gates.
- Output: issue list or internal edit targets.
- Skip or compress: compress for low-risk tasks.
- Failure modes: missing facts, overfocusing on style, rewriting protected text.
- Quality check: are fact, structure, style, and renderability all checked?

### 6. Revise

- Purpose: improve the draft based on critique.
- Input: draft and issues.
- Output: final source draft.
- Skip or compress: minor formatting-only tasks.
- Failure modes: cosmetic edits only, tone drift, new unsupported claims.
- Quality check: did the revision solve the critique without adding noise?

### 7. Layout Normalize

- Purpose: make the source renderable.
- Input: final source draft.
- Output: clean Markdown or render-ready source.
- Skip or compress: chat-only output.
- Failure modes: broken headings, unclosed fences, table spacing errors.
- Quality check: run or follow `normalize_markdown.py`.

### 8. Finalize

- Purpose: deliver the requested artifact or render path.
- Input: source and target format.
- Output: Markdown, docx, pdf, or command instructions.
- Skip or compress: never skip.
- Failure modes: claiming rendered files exist when tools were not run.
- Quality check: run quality gates and state missing tool/source limitations.

## Operating Rules

- Preserve user-provided facts and boundaries. Mark gaps instead of filling them
  with plausible detail.
- Keep the visible process proportional to the task. Do not expose internal
  critique unless the user asks for reasoning, review notes, or a change log.
- Use examples as style references only when the user supplied or approved them.
- Do not learn from weak AI drafts except as negative examples.
- Do not treat anti-AI editing as casualization. Professional and academic
  documents may need formal language.

## Examples

Technical design request:

1. Intake: target is Markdown, later Word/PDF, reader is implementers.
2. Frame: preprocessing must make PDF inputs predictable for downstream use.
3. Plan: background, goals, non-goals, inputs, pipeline, errors, validation.
4. Draft and critique: check concrete I/O, failure handling, and renderability.

Short polish request:

1. Intake: preserve facts and language.
2. Compress frame and plan.
3. Revise for clarity.
4. Run style lint if the text is file-based.

## Boundaries

The loop is not a requirement to show every step to the user. It is a control
process for the agent. For sensitive domains, add domain-specific verification
outside this skill rather than relying on writing quality alone.
