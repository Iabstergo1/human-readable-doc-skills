# Style Content Leak

## Input

Use the same style as the sample. Also reuse the same customer name and example
facts from the sample if they sound natural.

Sample: "Acme Bank cut review time by 42 percent after the migration."

Target: write a generic architecture overview.

## Expected Route

Use style learning with source-boundary protection.

## Expected References

- `references/13-style-distillation.md`
- `references/10-quality-gates.md`

## Expected Lint Categories

- `style-content-leak`

## Expected Behavior

Block transfer of sample details into the target. Extract only reusable style
traits.
