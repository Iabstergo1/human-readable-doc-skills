# English Anti-Slop Rules

Clean up generic AI phrasing without making the prose casual, imprecise, or
unfaithful to the source. Preserve structure and meaning before improving tone.

## Modes

Choose the mode from the document profile before editing.

### Document-Safe Mode

Use for technical design, academic writing, README files, business reports,
SOPs, proposals, formal email, and policy-like documents.

Rules:

- Do not optimize for AI detectors.
- Do not force sentence fragments, first person, confessional tone, or
  emotional texture into formal prose.
- Do not absolutely ban em dashes; limit overuse and repeated rhythm.
- Do not replace formal terminology with casual wording.
- Protect facts, structure, technical terms, citations, code, URLs, tables, and
  Markdown.
- Prefer concrete mechanisms, constraints, evidence, and next actions over
  stock enthusiasm.

### Creative/Blog Mode

Use for blogs, essays, social posts, newsletters, and content copy when the
user wants a more natural or voice-led public style.

Rules:

- Increase rhythm variation when it improves readability.
- First person is allowed when it fits the speaker and task.
- Reduce overly smooth transitions and formulaic sequencing.
- Avoid rule-of-three padding when it sounds automatic.
- Avoid generic conclusions that repeat the opening.
- Add viewpoints or concrete scenes only when the user supplied the underlying
  facts.
- Do not invent facts, anecdotes, metrics, quotes, or experience.

## Pattern Catalog

### Generic Openings

- Risk: delays the actual problem.
- Common phrases: `In today's fast-paced world`,
  `In the ever-evolving landscape`.
- Keep when: a public essay genuinely needs broad context.
- Rewrite: start with the object, constraint, or reader problem.

### Corporate Filler

- Risk: sounds polished but says little.
- Common phrases: `robust`, `seamless`, `leverage`, `streamline`.
- Keep when: the term is defined by product or domain vocabulary.
- Rewrite: replace with mechanism, measurable effect, or boundary.

### Empty Enthusiasm

- Risk: overpromises without evidence.
- Common phrases: `game-changer`, `unlock the full potential`,
  `revolutionary`.
- Keep when: marketing copy is explicitly requested.
- Rewrite: state the observable improvement and condition.

### Over-Hedging

- Risk: weakens clear claims.
- Common phrases: `it is important to note that`, `may potentially`,
  `could possibly`.
- Keep when: uncertainty is real and material.
- Rewrite: name the condition directly.

### Repetitive Transitions

- Risk: creates template rhythm.
- Common phrases: `firstly`, `secondly`, `lastly`, `moreover`.
- Keep when: step-by-step instructions need sequence markers.
- Rewrite: use causal, contrastive, or dependency transitions.

### Em Dash Overuse

- Risk: makes every sentence sound the same.
- Common phrases: repeated dashes used as default connectors.
- Keep when: a dash clarifies a true interruption or apposition.
- Rewrite: use a period, colon, comma, or split sentence.

### Vague Intensifiers

- Risk: adds emphasis without information.
- Common phrases: `very`, `highly`, `significantly`, `deeply`.
- Keep when: backed by a metric or explicit comparison.
- Rewrite: replace with a number, comparison, or remove.

### Preachy Endings

- Risk: turns the document into advice theater.
- Common phrases: `Ultimately`, `It is essential to remember`.
- Keep when: writing a speech or reflective essay.
- Rewrite: end with a decision, risk, or next step.

### Template Conclusions

- Risk: repeats the introduction generically.
- Common phrases: `In conclusion`, `This highlights...`.
- Keep when: academic conventions require a conclusion section.
- Rewrite: summarize actual findings and open questions.

## Structure Preservation Rules

- Preserve the user's heading hierarchy unless it is broken or conflicts with
  the requested output.
- Preserve quoted claims and cited statements unless the user asks for a
  paraphrase.
- Preserve technical terms, variable names, command names, file paths, and API
  names.
- Preserve meaning before improving rhythm.
- Do not flatten a document into bullet points unless scanning is the goal.

## Markdown Protection Rules

Do not rewrite destructively:

- YAML frontmatter.
- Code fences.
- URLs.
- Tables.
- Quoted source material unless the user asks.
- Citations, footnotes, and bibliography entries.
- Math, formulas, variables, and symbols.

When a protected block contains weak prose, report it as a note instead of
changing it automatically.

## Examples

Bad:

```markdown
In today's fast-paced digital landscape, a robust PDF preprocessing pipeline is
essential for unlocking seamless document intelligence.
```

Better:

```markdown
A PDF preprocessing pipeline should make extraction, OCR, metadata cleanup, and
downstream indexing predictable.
```

Bad:

```markdown
It is important to note that this approach may potentially improve scalability.
```

Better:

```markdown
This approach improves scalability when large files are split into independent
page-level jobs.
```

Bad:

```markdown
This solution empowers teams to streamline workflows and drive better outcomes.
```

Better:

```markdown
This solution reduces manual cleanup by validating extracted fields before
indexing.
```

## Boundaries

Do not remove necessary caution from academic, legal, medical, or financial
writing. Hedging is appropriate when evidence is incomplete, causal direction is
uncertain, or the user supplied tentative source material.
