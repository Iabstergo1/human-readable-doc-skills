--- name: Broken Markdown description: This frontmatter is intentionally invalid. ---
### Skipped Heading
This line is intentionally very long because it is used to check the long-line detector in the Markdown normalization script and should produce a warning in the JSON report when the command is run from the tests README.
| Column A | Column B |
| --- | --- |
| A | B |
```
missing language and closing fence
