# Human Readable Doc Skills

这是一个 Codex Skills 项目，用来处理“生成、撰写、整理、导出、排版、润色某种文档”的任务。它把文档工作拆成写作流程、去 AI 腔、文档结构和确定性排版四层，避免把所有提示词塞进一个超长文件。

## 项目结构

```text
human-readable-doc-skills/
├── AGENTS.md
├── README.md
└── .agents/
    └── skills/
        └── human-readable-document-workflow/
            ├── SKILL.md
            ├── references/
            ├── scripts/
            └── assets/
```

## 安装方式

把本项目放在目标仓库根目录，并保留 `.agents/skills/human-readable-document-workflow/` 结构。Codex 在该仓库工作时即可读取项目级 skill。

PowerShell 示例：

```powershell
cd C:\path\to\your-repo
Copy-Item -Recurse -Force .\human-readable-doc-skills\.agents .\.agents
Get-ChildItem .\.agents\skills\human-readable-document-workflow
```

如果你的 Codex 环境只加载全局 skills，可以把 skill 文件夹复制到用户级目录：

```powershell
$target = "$env:USERPROFILE\.codex\skills\human-readable-document-workflow"
Copy-Item -Recurse -Force .\.agents\skills\human-readable-document-workflow $target
```

## 调用方式

显式调用：

```text
$human-readable-document-workflow 帮我写一份技术设计文档，输出 Markdown，后续转 Word 和 PDF。
```

隐式触发：当用户请求创建、撰写、整理、润色、结构化、导出、排版文档、报告、论文、方案书、README、会议纪要、邮件、Word 或 PDF 时，`SKILL.md` 的 description 会引导 Codex 使用该 skill。短聊天回答默认不触发，除非用户明确要求可复用文档。

## 维护 References

- `SKILL.md` 只保留总控流程和加载指引。
- 写作循环规则放在 `references/01-writing-loop.md`。
- 中文去 AI 腔规则放在 `references/03-anti-ai-slop-zh.md`。
- 英文去 AI 腔规则放在 `references/04-anti-ai-slop-en.md`。
- 学术、Markdown、Word、PDF 和质量门禁分别维护在对应 reference 文件中。

新增规则时，优先放进已有主题文件；只有出现稳定的新主题时才新增 reference 文件。

## 替换 Word 和 PDF 模板

`assets/reference.docx` 是 Word 样式模板占位。实际使用时，用你自己的 Word 模板替换它，保留同名路径即可。

Pandoc 转 Word：

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\render_with_pandoc.py `
  .\draft.md --to docx --output .\draft.docx `
  --reference-doc .\.agents\skills\human-readable-document-workflow\assets\reference.docx
```

PDF 可以走 Pandoc、Quarto 或 Typst。项目提供 `assets/templates/report.typ` 和 `assets/quarto/_quarto.yml` 作为可扩展占位，默认不追求复杂版式。

## 脚本用法

检测用户请求是否为文档任务：

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\detect_doc_intent.py "帮我写一份技术设计文档，输出 Markdown"
```

检查 AI 腔：

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\lint_ai_style.py .\draft.md
```

规范化 Markdown：

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\normalize_markdown.py .\draft.md --output .\draft.normalized.md
```

渲染输出：

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\render_with_pandoc.py .\draft.md --to docx --output .\draft.docx
```

验证交付物：

```powershell
python .\.agents\skills\human-readable-document-workflow\scripts\validate_outputs.py .\draft.md .\draft.docx --markdown .\draft.md --pretty
```

所有脚本只使用 Python 标准库。

## Attribution And License Notes

本项目的方法论只参考下面列出的真实上游项目。规则内容为重新组织和重写的工作流方法，不直接复制第三方项目的受版权保护长文本。若后续引入特定开源项目的模板、代码或大段规则，应在本节补充许可证、来源链接和改动说明。

已在 2026-06-21 通过 `http://127.0.0.1:10808` 代理检查可访问性：

| Project | URL | Status |
| --- | --- | --- |
| Writer's Loop repo | https://github.com/xxsang/writers-loop | available |
| Writer's Loop skill | https://github.com/xxsang/writers-loop/tree/main/skills/writers-loop | available |
| codex-be-serious repo | https://github.com/lulucatdev/codex-be-serious | available |
| codex-be-serious main skill | https://github.com/lulucatdev/codex-be-serious/tree/main/skills/be-serious | available |
| codex-be-serious review skill | https://github.com/lulucatdev/codex-be-serious/tree/main/skills/be-serious-review | available |
| unslop repo | https://github.com/MohamedAbdallah-14/unslop | available |
| unslop main skill | https://github.com/MohamedAbdallah-14/unslop/tree/main/skills/unslop | available |
| unslop humanize skill | https://github.com/MohamedAbdallah-14/unslop/tree/main/skills/humanize | unavailable, 404 on 2026-06-21 |
| unslop review skill | https://github.com/MohamedAbdallah-14/unslop/tree/main/skills/unslop-review | available |
| anti-slop-writing repo | https://github.com/adenaufal/anti-slop-writing | available |
| anti-slop-writing English directory | https://github.com/adenaufal/anti-slop-writing/tree/main/english | available |
| anti-slop-writing English SKILL.md | https://github.com/adenaufal/anti-slop-writing/blob/main/english/SKILL.md | available |
| qu-ai-wei repo | https://github.com/LifelongLazyLearner/qu-ai-wei | available |
| qu-ai-wei SKILL.md | https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/SKILL.md | available |
| qu-ai-wei references | https://github.com/LifelongLazyLearner/qu-ai-wei/tree/main/references | available |
| qu-ai-wei scripts | https://github.com/LifelongLazyLearner/qu-ai-wei/tree/main/scripts | available |
| Humanizer-zh repo | https://github.com/op7418/humanizer-zh | available |
| Humanizer-zh SKILL.md | https://github.com/op7418/humanizer-zh/blob/main/SKILL.md | available |
| writing-humanizer repo | https://github.com/shyuan/writing-humanizer | available |
| writing-humanizer skill | https://github.com/shyuan/writing-humanizer/tree/main/skills/writing-humanizer | available |
| prompts.chat repo | https://github.com/f/prompts.chat | available |
| ChatGPT Prompts for Academic Writing repo | https://github.com/ahmetbersoz/chatgpt-prompts-for-academic-writing | available |

Do not invent replacement paths for unavailable entries. Use the remaining verified references or mark the missing path explicitly.

License metadata checked through the GitHub API on 2026-06-21 via the same proxy:

| Project | GitHub license metadata |
| --- | --- |
| Writer's Loop | MIT |
| codex-be-serious | MIT |
| unslop | MIT |
| anti-slop-writing | MIT |
| qu-ai-wei | MIT |
| Humanizer-zh | MIT |
| writing-humanizer | MIT |
| prompts.chat | Other / NOASSERTION |
| ChatGPT Prompts for Academic Writing | unknown |

Treat this table as metadata, not legal advice. If you copy code, templates, or long text from an upstream project later, re-check that repository's license file and preserve the required notice.
