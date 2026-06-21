# Markdown Authoring

Use Markdown as the canonical source for document generation.

## Supported Structure

- YAML frontmatter for title, author, date, abstract, keywords, and output hints.
- Table of contents markers when the renderer supports them.
- Headings from H1 downward without skipped levels.
- Footnotes when needed.
- Block quotes for quoted source material.
- Fenced code blocks with language names.
- Pipe tables for simple comparisons.
- Reference-style links for repeated sources.

## Avoid

- Complex embedded HTML.
- Manual page breaks unless the target renderer requires them.
- Deeply nested lists.
- Tables used for page layout.
- Renderer-specific syntax in a general-purpose source file unless documented.

## Renderer Compatibility

Keep source compatible with Pandoc, Quarto, and Typst when possible. If a feature is renderer-specific, add a short note near the source or in the render instructions.
