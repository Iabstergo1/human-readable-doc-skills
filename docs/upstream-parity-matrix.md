# Upstream Parity Matrix

This audit records capability parity against the upstream projects used as
methodology references. The local project is not an upstream mirror: copied
skill trigger behavior, persistent modes, hooks, and long upstream rule text
must be intentionally rewritten or marked out of scope.

Allowed status values:

- `implemented`
- `partially implemented`
- `intentionally out of scope`
- `missing`
- `needs source text`

## Matrix

| Upstream project | Upstream capability | Local implementation | Status | Action |
| --- | --- | --- | --- | --- |
| Codex official docs | Repo skill structure: `SKILL.md` plus optional scripts and references. | `.agents/skills/...` follows this layout. | implemented | Keep `SKILL.md` as entrypoint. |
| Codex official docs | Progressive disclosure through concise skill descriptions. | `SKILL.md` routes to focused references. | implemented | Do not merge long rules into `SKILL.md`. |
| Codex official docs | Repository guidance belongs in `AGENTS.md`. | Project rules stay in root `AGENTS.md`. | implemented | Keep skill behavior out of `AGENTS.md`. |
| Writer's Loop | Frame, question gate, plan, checkpoint, draft, critique, propose, decide, revise, evaluate. | `01-writing-loop.md` covers the core loop. | implemented | Keep as workflow layer. |
| Writer's Loop | Plan checkpoint pause. | `01-writing-loop.md` requires a checkpoint for substantial or risky drafts. | implemented | Use before drafting high-risk documents. |
| Writer's Loop | Revision proposal one-by-one decision. | `01-writing-loop.md` has propose and decide phases. | partially implemented | Keep proposals explicit when user review is required. |
| Writer's Loop | Preference signal extraction. | `01-writing-loop.md` defines strong and weak signals. | implemented | Do not learn from praise, silence, or fact corrections. |
| Writer's Loop | Style distillation and style pack. | `13-style-distillation.md` defines session-only style packs. | implemented | Load only for style learning or voice matching. |
| Writer's Loop | Style-versus-content boundary. | `13-style-distillation.md` separates extractable style from facts. | implemented | Enforce before using samples. |
| Writer's Loop | Style match review. | `13-style-distillation.md` adds a style-match review pass. | implemented | Run after applying a style pack. |
| Writer's Loop | Technical writing checklist. | `12-document-type-profiles.md` and `10-quality-gates.md` cover technical docs. | implemented | Keep concrete I/O, risks, and validation. |
| Writer's Loop | Business writing checklist. | `12-document-type-profiles.md` covers reports and proposals. | implemented | Keep evidence, options, risks, and decisions. |
| Writer's Loop | Translation workflow. | `01-writing-loop.md` treats document translation as a mode. | partially implemented | Use only for reusable document transformation. |
| Writer's Loop | Multi-agent validation. | `01-writing-loop.md` limits this to high-stakes, long, or ambiguous docs. | implemented | Do not default to subagents. |
| Writer's Loop | Durable preference journal and local style storage. | This repo does not manage durable memory. | intentionally out of scope | Require explicit user request. |
| qu-ai-wei | Simplified Chinese scope. | `03-anti-ai-slop-zh.md` is zh-CN-specific. | implemented | Keep separate from English rules. |
| qu-ai-wei | Real-human stop gate. | `03-anti-ai-slop-zh.md` now has a preflight gate. | implemented | Stop or format-only when human voice is at risk. |
| qu-ai-wei | Gate declaration. | `03-anti-ai-slop-zh.md` keeps it internal by default. | partially implemented | Show only in review reports or high-risk edits. |
| qu-ai-wei | Register identification. | `03-anti-ai-slop-zh.md` has a register matrix. | implemented | Select intensity before rewriting. |
| qu-ai-wei | Register matrix. | `03-anti-ai-slop-zh.md` covers core document and content registers. | implemented | Extend only when new profiles are needed. |
| qu-ai-wei | Conflict arbitration order. | `03-anti-ai-slop-zh.md` adds source-first ordering. | implemented | Preserve facts before style. |
| qu-ai-wei | No invented facts. | Source-boundary gates and zh rules enforce it. | implemented | Keep in every polish pass. |
| qu-ai-wei | Register downgrade protection. | Zh preflight and serious gates protect formal text. | implemented | Do not casualize technical or academic prose. |
| qu-ai-wei | Over-sanitization countermeasure. | Zh preflight and second-pass gate check for voice loss. | implemented | Preserve human hesitation and voice where valid. |
| qu-ai-wei | 51 AI-slop pattern classes. | Local rules cover the common document-safe subset only. | partially implemented | Source is reachable, but the full taxonomy is not vendored. |
| qu-ai-wei | Active polish rules. | Local lint and references support conservative polish. | partially implemented | Avoid platform-specific overreach. |
| qu-ai-wei | Whitelists. | Not carried as reusable whitelist files. | intentionally out of scope | Add only for a defined brand or corpus. |
| qu-ai-wei | Brand voice. | Not a generic document workflow concern. | intentionally out of scope | Add per user-provided brand style. |
| qu-ai-wei | Platform patterns. | Social/content-copy is recognized but not platform-specific. | intentionally out of scope | Add only for a platform-focused skill. |
| qu-ai-wei | Punctuation rules. | Markdown and style rules cover safe basics. | partially implemented | Add exact source text if parity is required. |
| qu-ai-wei | Final polish report. | Not default output. | intentionally out of scope | Use only for requested review reports. |
| Humanizer-zh | Content, language, style, exchange, structure modes. | `02` and `03` split these across readability and zh anti-slop. | partially implemented | Keep mode categories in zh review. |
| Humanizer-zh | Second-round self-review. | `10-quality-gates.md` adds a second-pass humanization gate. | implemented | Enable for polish and humanize tasks. |
| Humanizer-zh | Scoring output. | This project does not default to scores. | intentionally out of scope | Use only for review reports. |
| Humanizer-zh | Avoid sterile neutral rewriting. | Zh preflight and second-pass gates protect voice. | implemented | Stop when human voice would be damaged. |
| Humanizer-zh | Preserve tone and meaning. | Source boundary and humanization gates enforce this. | implemented | Keep before anti-slop cleanup. |
| writing-humanizer | Content, language, style, exchange, structure modes. | Local rules cover the shared subset. | partially implemented | No full upstream mode taxonomy. |
| writing-humanizer | Second-round self-review. | `10-quality-gates.md` now defines it. | implemented | Apply after first rewrite. |
| writing-humanizer | Scoring output. | Not default behavior. | intentionally out of scope | Use only when user asks for scoring. |
| writing-humanizer | Preserve tone and meaning. | Source-boundary and voice-loss checks cover this. | implemented | Do not over-sanitize. |
| unslop | Sycophancy cleanup. | Zh, English, and serious-register checks flag it. | implemented | Keep as lint category. |
| unslop | Stock vocabulary cleanup. | English and zh rules flag common stock terms. | implemented | Preserve domain terms. |
| unslop | Hedging stacks. | English rules flag over-hedging. | implemented | Keep real uncertainty. |
| unslop | Tricolon padding. | `lint_ai_style.py` flags rule-of-three padding. | implemented | Use mode-sensitive severity. |
| unslop | Em-dash overuse. | English rules limit overuse, not legitimate dashes. | implemented | Do not use an absolute ban. |
| unslop | Bullet-soup. | Layout and zh rules discourage excessive lists. | partially implemented | Detect structurally in future if needed. |
| unslop | Subtract, do not add. | English and quality gates require source-boundary preservation. | implemented | Remove filler without adding claims. |
| unslop | Style and stance separation. | `13-style-distillation.md` separates style from content. | implemented | Do not import sample stance as fact. |
| unslop | Technical preservation. | Markdown and source-boundary rules protect code and terms. | implemented | Never rewrite protected blocks destructively. |
| unslop | Preserve real uncertainty. | `10-quality-gates.md` protects assumptions and uncertainty. | implemented | Do not convert caveats into fake confidence. |
| unslop | Fact verification boundary after rewriting. | Source Boundary Gate applies after style cleanup. | implemented | Re-check claims after edits. |
| unslop | Voice matching. | `13-style-distillation.md` supports session style packs. | partially implemented | Durable voice memory is out of scope. |
| unslop | Mode concepts. | Local `--mode` supports document-safe, creative-blog, serious-review, zh-source-safe. | partially implemented | Do not copy session-wide slash modes. |
| unslop | Slash modes. | Slash command modes are not supported here. | intentionally out of scope | This is not a session-wide mode plugin. |
| unslop | Session-wide persistence. | Not supported. | intentionally out of scope | Use explicit task scope only. |
| unslop | Hooks and statusline. | Not supported. | intentionally out of scope | Avoid plugin behavior in this skill. |
| unslop | Review comments preserve exact identifiers and line references. | Not a default document workflow. | intentionally out of scope | Use only for code-review prose tasks. |
| anti-slop-writing | Detector-oriented perplexity, burstiness, stylometry. | Split into document-safe and creative/blog modes. | partially implemented | Do not use detector rules on formal docs. |
| anti-slop-writing | Hard vocabulary banlist. | Local rules use warnings, not absolute bans. | intentionally out of scope | Preserve domain language and user voice. |
| anti-slop-writing | Structural pattern avoidance. | English rules flag generic openings and template endings. | implemented | Use mode-specific intensity. |
| anti-slop-writing | Rule of three. | `lint_ai_style.py` flags tricolon padding. | implemented | Stronger in creative/blog mode. |
| anti-slop-writing | Negative parallelisms. | `lint_ai_style.py` flags detector-style negative pairs. | implemented | Use mainly in creative/blog mode. |
| anti-slop-writing | False ranges. | `lint_ai_style.py` flags vague binary or range claims. | implemented | Replace with real boundary or evidence. |
| anti-slop-writing | Formulaic conclusions. | English rules flag template conclusions. | implemented | Keep academic conclusions when needed. |
| anti-slop-writing | Vertical list with bold header avoidance. | Markdown/layout rules discourage over-formatting. | partially implemented | Add structural lint only if needed. |
| anti-slop-writing | Em dash ban. | Replaced with overuse check. | intentionally out of scope | Absolute bans break valid prose. |
| anti-slop-writing | First-person, register shift, human imperfection. | Creative/blog mode allows these. | partially implemented | Not allowed by default in formal docs. |
| anti-slop-writing | Vague attribution cleanup. | Source-boundary and unsourced-claim checks cover it. | implemented | Keep source caveats visible. |
| codex-be-serious | Serious scholarly register. | `10-quality-gates.md` adds Serious Register Gate. | implemented | Enable for formal documents. |
| codex-be-serious | No slang. | Serious mode flags slang and internet vernacular. | implemented | Use in formal review. |
| codex-be-serious | No sycophancy. | Zh and serious rules flag flattery. | implemented | Remove from professional prose. |
| codex-be-serious | No emoji. | Serious mode flags emoji. | implemented | Keep out of formal docs. |
| codex-be-serious | No marketing adjectives. | Zh and English rules flag marketing tone. | implemented | Preserve only for marketing copy. |
| codex-be-serious | No anthropomorphized software descriptions. | Serious mode flags tool personification. | implemented | Describe systems by behavior. |
| codex-be-serious | No forced informality. | Serious gate flags forced casual tone. | implemented | Keep formal register when required. |
| codex-be-serious | Chinese internet vernacular cleanup. | Serious mode flags common workplace and internet slang. | implemented | Enable for formal zh documents. |
| codex-be-serious | Review output shape. | Formal review shape is documented but not default. | partially implemented | Use Assessment / Findings / Revision when requested. |
| codex-be-serious | Session-wide register persistence. | Not supported. | intentionally out of scope | Apply only to the current document task. |
| prompts.chat | Prompt library organization. | Examples and parity fixtures are grouped by workflow. | partially implemented | Do not copy prompt catalogs. |
| prompts.chat | Runtime skill source. | Not treated as a runtime skill source. | intentionally out of scope | Use only for organization methodology. |
| ChatGPT Prompts for Academic Writing | Academic task decomposition. | `05-academic-writing.md` and profiles cover paper sections. | implemented | Keep section boundaries explicit. |
| ChatGPT Prompts for Academic Writing | Citation formatting for user-provided sources. | Academic and source gates forbid fabricated citations. | implemented | Format only supplied or verified sources. |
| ChatGPT Prompts for Academic Writing | Prompt catalog mirroring. | Not copied into this project. | intentionally out of scope | Keep as methodology reference only. |

## Summary

Implemented capabilities cluster around document routing, writing loop control,
source boundaries, common zh/en anti-slop cleanup, Markdown protection, serious
register review, and session-only style matching.

Partially implemented capabilities are mostly upstream features that need a
heavier taxonomy or richer report format than this focused document skill
should load by default.

Intentionally out-of-scope capabilities are session-wide modes, hooks,
statusline behavior, durable preference memory, brand/platform-specific voice
systems, detector-first rewriting, and code-review-specific workflows.

No current item is marked `needs source text`. Long upstream taxonomies are
reachable, but this project intentionally rewrites only the document-safe
subset instead of vendoring full upstream rule catalogs.
