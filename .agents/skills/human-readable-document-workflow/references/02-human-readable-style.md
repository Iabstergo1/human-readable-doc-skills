# Human Readable Style

Human-readable writing lets the intended reader understand the document's
purpose, claims, evidence, structure, and next action without decoding filler or
template rhythm.

## What It Is

| Quality | Rule | Example |
| --- | --- | --- |
| Concrete | Name the object, action, constraint, and consequence. | "OCR failures keep the page id and retry state." |
| Contextual | Explain why the point matters for this reader. | "Implementers need the failure state because indexing is asynchronous." |
| Bounded | State assumptions and missing evidence. | "No benchmark is available yet, so latency is a design risk." |
| Well paced | Mix paragraphs, lists, and examples according to the job. | Use a list for options; use paragraphs for argument. |
| Renderable | Structure survives Markdown, Word, and PDF export. | Stable headings, captions, and fenced code blocks. |

## What It Is Not

| Misuse | Why it fails |
| --- | --- |
| Casual slang | It can reduce precision and professional fit. |
| Forced imperfection | Typos and awkward phrasing do not make writing human. |
| Overexplaining obvious facts | It slows readers and hides the important part. |
| Decorative structure | Empty tables, icons, or excessive bullets add effort. |
| Vague warmth | Compliments and enthusiasm do not replace evidence. |

## Professional Terms

- Keep technical or academic terms when they are the correct terms.
- Define a term on first use if the reader may not know it.
- Avoid replacing precise terms with simpler but wrong words.
- For mixed-language documents, keep established English terms when a Chinese
  translation would be less recognizable, then explain them once.

## Paragraphs

- One paragraph should carry one main move: context, claim, evidence, example,
  consequence, or limitation.
- Long paragraphs are acceptable when the reasoning is continuous; split when a
  new reader question starts.
- Avoid single-sentence paragraphs used only for dramatic emphasis in technical
  or academic documents.

## Lists

Use lists for scanning, comparison, steps, decisions, risks, and action items.
Prefer paragraphs when the goal is explanation or argument.

| Good list use | Weak list use |
| --- | --- |
| Inputs, outputs, error states, owners, dates. | Every sentence forced into bullets. |
| A checklist before export. | A conclusion split into three vague bullets. |
| Alternatives with tradeoffs. | Decorative "first, second, finally" rhythm. |

## Transitions

Transitions should reflect real logic:

- cause: "Because the OCR path is slower..."
- contrast: "This works for text PDFs, but scanned pages need..."
- boundary: "This does not cover layout recovery."
- sequence: "After extraction, normalization adds..."

Avoid transitions that only announce structure: "It is worth mentioning",
"Furthermore", "In conclusion", "综上所述".

## Examples

Use examples when they reduce ambiguity. A useful example names the input,
operation, and expected result.

Bad: "The system handles documents intelligently."

Better: "For a scanned PDF, the pipeline stores the page image, OCR text,
confidence score, and retry status before indexing."

## Limitations

Useful limitations say what is not known or not covered.

Bad: "There are still some limitations."

Better: "The draft does not include OCR latency data; the throughput estimate
should be treated as a design assumption until benchmarked."

## Language Modes

| Language | Style rule |
| --- | --- |
| Chinese | Prefer clear subject-action sentences. Avoid empty significance claims and padded openings. |
| English | Prefer plain verbs and concrete nouns. Avoid corporate filler and template conclusions. |
| Mixed | Keep terms consistent. Do not translate names, APIs, or citations destructively. |

## Rewrite Contrasts

| From | To | Strategy |
| --- | --- | --- |
| vague | concrete | Replace "improve efficiency" with the measured or observable change. |
| preachy | useful | Replace moralizing with a decision, caveat, or next step. |
| overstructured | readable | Merge shallow bullets into paragraphs when logic matters. |
| marketing | factual | Replace "leading, seamless, robust" with mechanism and scope. |
| academic but obscure | academic and clear | Define concepts before claims and keep notation stable. |

## Boundaries

Do not simplify legal, medical, financial, academic, or technical wording beyond
the available evidence. When precision and readability conflict, preserve
precision and add explanation.
