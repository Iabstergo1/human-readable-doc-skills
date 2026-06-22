# Writing Loop

Use a loop instead of jumping from prompt to final draft. This reference adapts
the Writer's Loop method for this skill's narrower job: produce or revise clean
Markdown source for human-readable documents.

Important documents must pass through at least `frame -> plan -> draft ->
critique -> revise -> finalize`. Short tasks may compress the visible process,
but they still need a source-boundary check.

## Core Rule

Preserve the user's source boundary before improving structure or style:

- Do not invent facts, citations, data, decisions, file artifacts, or user
  preferences.
- Treat the user's current instruction as a task constraint unless they say it
  should apply in future work.
- Learn writing preferences only from explicit decisions: accepted plans,
  rejected plans with reasons, accepted edits, rejected edits, undone edits,
  manual rewrites that change style, or explicit standing preferences.
- Do not learn from unreviewed drafts, generated text, fact corrections,
  one-off comments, or current-task constraints.

## Phase Overview

| Phase | Required output |
| --- | --- |
| Intake | Task brief and source boundary. |
| Frame | Reader problem and delivery boundary. |
| Question gate | Only blocking questions, or stated assumptions. |
| Plan | Stable section structure. |
| Plan checkpoint | Approval point for high-risk or substantial new documents. |
| Draft | Complete first version. |
| Critique | Specific issues across facts, structure, style, and source quality. |
| Propose | Targeted changes with reasons when revising existing text. |
| Decide | Apply only accepted changes when user review is required. |
| Revise | Final source draft. |
| Layout normalize | Handoff-ready Markdown source. |
| Evaluate | Check against original goal and quality gates. |
| Finalize | Markdown source, summary, and handoff note if needed. |

## Entry Modes

### New Artifact

Start at `Intake`, then `Frame`, `Question gate`, and `Plan`. For substantial
new documents, do not draft before the plan is either approved or safe to
proceed under stated assumptions.

### Fast Draft

Use only when the user clearly wants an immediate draft or the task is low
risk. Still include an internal frame and compact plan. End with any missing
sources or handoff limitations.

### Existing Draft

Start at `Intake`, then `Critique`. Preserve user intent, facts, voice,
protected wording, citations, and continuity. Plan only when the structure is
unclear or the user asked for section-level rewriting.

### Targeted Revision

Start at `Intake`, then `Propose` or make a small direct edit. Keep changes at
sentence or paragraph level unless the user asked for restructuring.

### Style Learning

Use only when the user asks to learn a reusable style or supplies approved
style samples. Separate style from content facts. Do not copy passages from the
sample into a reusable style note.

### Translation

Use this skill only when the translation must become a reusable document. Keep
formatting, terminology, names, citations, code, file paths, URLs, and IDs
stable.

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

### 3. Question Gate

- Purpose: ask only questions that materially change the document.
- Input: frame, source boundary, risk level.
- Output: blocking questions or stated assumptions.
- Skip or compress: ask nothing when assumptions are safe and reversible.
- Failure modes: interrogating the user for optional details; drafting while a
  blocking source is missing.
- Quality check: would the answer change the outline, facts, audience,
  citation boundary, or file handoff?

### 4. Plan

- Purpose: build the structure before drafting.
- Input: frame, profile, required sections.
- Output: headings, section order, and expected evidence.
- Skip or compress: very short rewrites under one page.
- Failure modes: shallow outline, skipped sections, too many heading levels.
- Quality check: does each section answer a reader question?

### 5. Plan Checkpoint

- Purpose: prevent premature drafting when structure or risk matters.
- Input: plan, user constraints, risk level.
- Output: user approval, explicit requested change, or safe proceed note.
- Skip or compress: low-risk short tasks and user-waived fast drafts.
- Failure modes: treating a decorative outline as approval; bypassing the
  checkpoint because the draft is easy to write.
- Quality check: is it clear whether the user approved, requested changes, or
  waived review?

For substantial new documents, expose the checkpoint in this compact shape:

```markdown
Plan checkpoint:
- Proposed structure:
- Source gaps:
- Risky assumptions:
- Need your decision: approve, adjust, or skip checkpoint.
```

If the user response is ambiguous, ask whether they approve the plan or want
changes. Do not treat "looks good" as a durable style preference.

### 6. Draft

- Purpose: produce the first coherent version.
- Input: plan and source material.
- Output: complete draft in the requested language.
- Skip or compress: never skip for new documents.
- Failure modes: polished filler, unsupported claims, list-only writing.
- Quality check: does every paragraph move the document forward?

### 7. Critique

- Purpose: find defects before the user sees the draft.
- Input: draft and quality gates.
- Output: issue list or internal edit targets.
- Skip or compress: compress for low-risk tasks.
- Failure modes: missing facts, overfocusing on style, rewriting protected text.
- Quality check: are fact, structure, style, Markdown source quality, and
  handoff readiness all checked?

Critique must point to specific locations or sections. Avoid generic comments
such as "make it clearer" unless paired with a concrete defect.

### 8. Propose

- Purpose: separate diagnosis from edits when revising user-owned text.
- Input: critique and source boundary.
- Output: targeted change proposals with reason and expected improvement.
- Skip or compress: direct fixes are acceptable when the user asked for an
  edited final draft and no approval checkpoint is needed.
- Failure modes: broad rewrite when a sentence-level fix preserves intent.
- Quality check: does each proposal name what changes and why?

### 9. Decide

- Purpose: avoid learning or applying preferences from weak signals.
- Input: user response to plan or proposed changes.
- Output: accepted, rejected, adjusted, or unresolved decision.
- Skip or compress: only when no user checkpoint was created.
- Failure modes: treating silence, praise, or a fact correction as a durable
  style preference.
- Quality check: are rejected changes kept out of the final draft?

For revision proposals that require user review, use one decision per item:

```markdown
Decision record:
- Proposal:
- User decision: apply / reject / adjust / undo / unresolved.
- Durable preference: yes only if the user explicitly says so.
```

### 10. Revise

- Purpose: improve the draft based on critique.
- Input: draft and issues.
- Output: final source draft.
- Skip or compress: minor formatting-only tasks.
- Failure modes: cosmetic edits only, tone drift, new unsupported claims.
- Quality check: did the revision solve the critique without adding noise?

### 11. Layout Normalize

- Purpose: make the Markdown source stable for reading and handoff.
- Input: final source draft.
- Output: clean Markdown source.
- Skip or compress: chat-only output.
- Failure modes: broken headings, unclosed fences, table spacing errors.
- Quality check: run or follow `normalize_markdown.py`.

### 12. Evaluate

- Purpose: check the revised source against the original goal.
- Input: final source draft and quality gates.
- Output: pass/fail notes or final edit targets.
- Skip or compress: never skip internally.
- Failure modes: validating style while missing source gaps or handoff limits.
- Quality check: do `references/10-quality-gates.md` and the selected profile
  both pass?

### 13. Finalize

- Purpose: deliver the Markdown source and tell the user what remains.
- Input: source, target format, and handoff requirement.
- Output: Markdown source path or text, concise summary, and handoff note.
- Skip or compress: never skip.
- Failure modes: claiming Word, PDF, slides, or other files exist when this
  skill only produced source.
- Quality check: state whether the output is source-only or ready for official
  document-generation handoff.

## Reference Coordination

Load references as a staged control system, not as independent advice:

| Decision | Primary reference | Follow-up reference |
| --- | --- | --- |
| Should this skill run? | `00-routing-policy.md` | `12-document-type-profiles.md` |
| What loop path is needed? | `01-writing-loop.md` | `10-quality-gates.md` |
| What structure fits? | `12-document-type-profiles.md` | `06-document-layout.md` |
| How should prose read? | `02-human-readable-style.md` | `03` or `04` anti-slop |
| Is this academic? | `05-academic-writing.md` | `12-document-type-profiles.md` |
| Is source handoff ready? | `07-markdown-authoring.md` | `validate_markdown_source.py` |

When references disagree, follow the narrower context:

- User instruction beats profile defaults.
- Source boundary beats style cleanup.
- Academic safeguards beat anti-slop simplification.
- Markdown source rules beat decorative layout preferences.
- Official document-generation handoff beats local rendering attempts.

## Operating Rules

- Preserve user-provided facts and boundaries. Mark gaps instead of filling them
  with plausible detail.
- Keep the visible process proportional to the task. Do not expose internal
  critique unless the user asks for reasoning, review notes, or a change log.
- Use examples as style references only when the user supplied or approved them.
- Do not learn from weak AI drafts except as negative examples.
- Do not treat anti-AI editing as casualization. Professional and academic
  documents may need formal language.
- Do not turn a one-time tone instruction into a future preference.
- Do not copy source passages into a style rule.
- Do not use multi-agent validation by default. Use it only for high-stakes,
  long, ambiguous, or multi-audience documents.

## Common Loopholes

| Loophole | Correction |
| --- | --- |
| "The user asked for speed, so skip the frame." | Compress the frame; do not skip it. |
| "The outline is obvious, so draft directly." | Write at least an internal plan. |
| "This is only style cleanup." | Preserve facts, citations, variables, and protected blocks first. |
| "The source is weak, so improve the facts." | Mark gaps; do not invent evidence. |
| "The user liked it, so learn the style." | Learn only from explicit decisions or manual rewrites. |
| "PDF was mentioned, so generate a PDF." | Produce Markdown source and hand off if an artifact is requested. |
| "Anti-AI rules ban formal words." | Keep formal wording when the document type needs it. |

## Examples

Technical design request:

1. Intake: target is Markdown, later Word/PDF, reader is implementers.
2. Frame: preprocessing must make PDF inputs predictable for downstream use.
3. Plan: background, goals, non-goals, inputs, pipeline, errors, validation.
4. Draft and critique: check concrete I/O, failure handling, and source
   handoff readiness.

Short polish request:

1. Intake: preserve facts and language.
2. Compress frame and plan.
3. Revise for clarity.
4. Run style lint if the text is file-based.

## Boundaries

The loop is not a requirement to show every step to the user. It is a control
process for the agent. For sensitive domains, add domain-specific verification
outside this skill rather than relying on writing quality alone.
