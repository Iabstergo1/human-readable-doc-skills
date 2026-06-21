# Academic Writing

Academic writing should make concepts, evidence, assumptions, notation, and
argument structure explicit. It must not fabricate sources, claims, citations,
metrics, quotations, or bibliography entries.

## Core Rules

| Area | Rule | Failure to avoid |
| --- | --- | --- |
| Sources | Use only user-provided sources or clearly marked placeholders. | Invented authors, years, journals, DOIs, or quotations. |
| Concepts | Define concepts before using them analytically. | Treating broad terms as self-evident. |
| Variables | Keep variable names and symbols consistent. | Switching from `x_i` to `X_i` without explanation. |
| Formulas | Keep subscripts, superscripts, and indexing conventions stable. | Changing `t` from time to treatment in the same section. |
| Argument | Separate definitions, assumptions, claims, evidence, and implications. | Paragraphs that state conclusions without support. |
| Literature | Distinguish prior work from the author's contribution. | Presenting a literature summary as original analysis. |
| Limitations | State boundary conditions and unresolved issues. | Overclaiming external validity. |

## Citation Policy

- Never invent references.
- If the user has not supplied a source, use `[citation needed]`.
- If the user supplied partial citation information, preserve it and mark the
  missing part rather than guessing.
- Do not normalize citation style beyond the information provided unless the
  user supplies a bibliography or citation manager export.
- Do not fabricate a bibliography to make a draft look complete.

Example:

```markdown
Prior work on platform labor argues that algorithmic management changes how
workers experience autonomy [citation needed].
```

## Concepts And Boundaries

Define a concept by naming:

1. The object or phenomenon.
2. What is included.
3. What is excluded.
4. Why the distinction matters for the argument.

Example:

```markdown
This chapter uses "algorithmic management" to refer to allocation, pricing,
rating, and sanction mechanisms mediated by platform software. It does not
refer to ordinary digital record keeping unless those records directly affect
worker evaluation or pay.
```

## Variables And Symbols

Before using notation, create a small symbol inventory when the section has more
than two variables.

| Symbol | Meaning | Notes |
| --- | --- | --- |
| `i` | Unit, worker, firm, or document. | Do not change unit mid-section. |
| `t` | Time period. | State whether discrete or continuous. |
| `Y_i` | Outcome variable. | Define scale and measurement source. |
| `X_i` | Explanatory variable. | Define whether observed or constructed. |

Rules:

- Define before use.
- Use the same case, subscript, and superscript conventions throughout.
- Explain formula terms in prose immediately before or after the formula.
- Do not add formulas for decoration.

## Paragraph Argument Chain

Each analytical paragraph should usually include:

1. A local claim.
2. A definition or assumption needed for the claim.
3. Evidence, source, model relationship, or reasoning.
4. A limitation or boundary when relevant.
5. A sentence that connects to the section's larger argument.

Weak:

```markdown
This issue has important theoretical significance and practical value.
```

Better:

```markdown
This distinction matters because platform rules can alter workers' expected
income even when task demand is unchanged. Without separating demand shocks from
rule changes, the model may attribute income volatility to worker behavior
rather than platform governance [citation needed].
```

## Literature Review Versus Original Argument

| Section | Primary job | Do not |
| --- | --- | --- |
| Literature review | Map existing debates, methods, findings, and gaps. | Pretend cited work says more than the user supplied. |
| Theory section | Define concepts and expected relationships. | Use abstract labels without definitions. |
| Method section | Explain data, model, identification, and limits. | Hide assumptions in technical notation. |
| Results discussion | Interpret evidence within scope. | Claim causality without design support. |
| Original argument | State what this paper adds. | Repackage literature summary as contribution. |

## Chinese Academic Writing

Avoid empty significance formulas:

- `具有重要意义`
- `填补研究空白`
- `为后续研究提供参考`
- `具有理论价值和现实意义`

Use them only when the exact contribution and evidence are stated.

Better pattern:

```markdown
本文的贡献在于把平台派单规则与收入波动放在同一分析框架中。
这一处理能区分需求变化和规则变化，但仍依赖平台日志数据的可得性。
```

## Examples

Bad:

```markdown
Smith (2021) proves that algorithmic management always improves efficiency.
```

Better:

```markdown
The draft needs a source for the claim that algorithmic management improves
efficiency [citation needed]. Without that source, the safer claim is that the
effect depends on how allocation and evaluation rules are designed.
```

## Boundaries

This reference supports academic clarity; it does not verify the truth of
domain claims. For high-stakes or current claims, verify sources through the
appropriate research workflow before final delivery.
