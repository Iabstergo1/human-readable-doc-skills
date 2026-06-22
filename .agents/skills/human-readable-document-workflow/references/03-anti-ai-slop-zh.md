# 中文去 AI 腔规则

目标是减少模板化、说教感和空泛拔高，不是把文字改得口语化、
随意化，或故意加入错别字。技术文档和学术文档需要正式表达时，
保留必要的术语、定义、限制和推理链。

## Preflight Gate / 门检

先判断输入是否可能是真人原文。去 AI 腔不是把所有文字改成平滑、
中性、无个人痕迹的说明文。

如果文本包含以下信号，应停手或只做格式清理：

- 访谈实录、口述稿、聊天记录、演讲逐字稿。
- 方言、口头停顿、自我修正、犹疑、重复、插入语。
- 强个人经历、情绪转折、生活细节、个人判断。
- 公共作者、品牌创始人、教师、研究者等明确个人声口。
- 明显不是 AI 模板，而是粗糙但真实的初稿。

如果用户明确要求改写，先区分请求类型：

- 改语体：从口述改成报告、从随笔改成说明文等。
- 简化：降低阅读难度，不等于去掉个性。
- 翻译：保留原意、语气和结构约束。
- 摘要：提炼信息，不执行风格消毒。
- 去 AI 腔：删除模板化和空泛拔高，不损伤事实和声口。

门检声明默认内部执行。只有在用户要求 review report、文本风险高、
或改写会明显损伤真人声口时，才显式说明：

```markdown
门检：该文本可能是真人原文。建议只清理格式和少量冗余，不执行大幅去 AI 腔。
```

门检优先级：

1. 事实和引用边界。
2. 真人声口和用户明确保留的语气。
3. 文档类型和语体。
4. 去 AI 腔规则。
5. 表面词语替换。

## Register Matrix / 语体矩阵

为每个任务先选语体，再决定去 AI 强度。

### `technical-design`

- Intensity: medium.
- 正式连接词: 允许，用于流程、边界、依赖和风险。
- 列表: 允许，适合 I/O、风险、步骤和接口。
- 第一人称: 通常不使用。
- 口语化: 不主动添加。
- 行业术语: 保留，并保持一致。
- 高风险误杀点: 把严谨定义改成松散口语；删除错误处理和边界条件。

### `academic-paper`

- Intensity: low to medium.
- 正式连接词: 允许，尤其是论证、假设、限制和文献关系。
- 列表: 少用，除非列变量、假设或研究问题。
- 第一人称: 按学科惯例处理。
- 口语化: 通常不允许。
- 行业术语: 保留，必要时定义。
- 高风险误杀点: 为了像人而删掉限定词、变量关系、引用边界。

### `README`

- Intensity: medium.
- 正式连接词: 允许，但避免营销式铺垫。
- 列表: 允许，适合安装、使用、配置和限制。
- 第一人称: 通常不需要。
- 口语化: 可轻微，但不损伤可操作性。
- 行业术语: 保留。
- 高风险误杀点: 把项目说明改成产品广告或泛泛介绍。

### `meeting-notes`

- Intensity: low.
- 正式连接词: 允许，用于决策、分歧和行动项。
- 列表: 允许，通常是默认结构。
- 第一人称: 只保留原文发言归属。
- 口语化: 可保留必要原话。
- 行业术语: 保留。
- 高风险误杀点: 擅自补决策、负责人、日期或共识。

### `SOP`

- Intensity: low to medium.
- 正式连接词: 允许，用于步骤和前置条件。
- 列表: 允许，编号步骤通常必要。
- 第一人称: 不使用。
- 口语化: 不主动添加。
- 行业术语: 保留。
- 高风险误杀点: 删除警告、回滚、验证和异常处理。

### `business-report`

- Intensity: medium.
- 正式连接词: 允许，用于发现、选项、建议和风险。
- 列表: 允许，适合指标、选项和行动。
- 第一人称: 通常不用。
- 口语化: 少量可用，但不影响决策语气。
- 行业术语: 保留，避免空泛商业词。
- 高风险误杀点: 用增长、赋能、闭环替代证据和选择。

### `general-article`

- Intensity: medium to high.
- 正式连接词: 允许，但不应机械堆叠。
- 列表: 适量使用。
- 第一人称: 可按主题使用。
- 口语化: 允许适度自然表达。
- 行业术语: 按读者解释。
- 高风险误杀点: 结尾拔高、标题党、强行金句化。

### `social/content-copy`

- Intensity: high, unless the sample is clearly human-authored.
- 正式连接词: 少用。
- 列表: 可用，但避免模板化清单。
- 第一人称: 允许。
- 口语化: 允许，需匹配平台和人设。
- 行业术语: 只保留读者会懂的术语。
- 高风险误杀点: 把平台文案改成报告腔；虚构体验和效果。

### `public-formal/policy-like`

- Intensity: low.
- 正式连接词: 允许，体例需要时保留。
- 列表: 允许，适合责任、范围和程序。
- 第一人称: 不使用。
- 口语化: 不允许。
- 行业术语: 保留，并避免随意替换。
- 高风险误杀点: 把公文体例误判成 AI 腔；删除必要套语和责任边界。

## 总规则

| Rule | Use |
| --- | --- |
| 先保事实 | 不为“更像人”而添加未经用户提供的事实、数据、引用或承诺。 |
| 先判文档类型 | README、论文、SOP、会议纪要的语气不一样。 |
| 保留必要正式性 | 严谨、清楚、可验证，比口语化更重要。 |
| 改机制不改噪音 | 删除空泛词，补具体对象、条件、机制、结果。 |
| 保护结构 | 不破坏 Markdown、表格、引用、代码块和术语一致性。 |

## 词语分类

| Class | Treatment |
| --- | --- |
| 事实禁区 | 不得虚构事实、引用、数据、输出文件、用户意图或验证结果。 |
| 高风险套话 | `具有重要意义`, `赋能`, `闭环`, `革命性` 等通常需要删除或改写。 |
| 场景敏感 | `首先/其次/最后`, `综上所述`, `不是...而是...` 需要看文档类型和作用。 |
| 正式表达保留 | 学术、公文、SOP 中承担定义、顺序、边界或小结功能的正式表达可以保留。 |

## 1. 宏大开头

- Pattern name: `zh-grand-opening`
- Risk: 用时代背景替代具体背景，读者需要等很久才知道问题是什么。
- Common phrases: `随着时代发展`, `在当今社会`, `在数字化浪潮下`,
  `随着技术不断进步`
- Keep when: 文档确实需要宏观背景，并且后面紧接可验证数据或范围。
- Rewrite strategy: 直接写对象、场景、痛点、约束。
- Bad example: 随着数字化转型的不断深入，PDF 预处理越来越重要。
- Better example: 当前系统需要同时处理文本型 PDF、扫描件和混合 PDF，
  预处理层负责把它们转换成统一的页面文本、图片和元数据。

## 2. 空泛意义句

- Pattern name: `zh-empty-significance`
- Risk: 只有价值判断，没有说明对谁、在什么条件下、产生什么影响。
- Common phrases: `具有重要意义`, `意义重大`, `价值深远`,
  `为未来发展奠定基础`
- Keep when: 学术摘要或项目背景需要说明研究意义，但必须接具体对象。
- Rewrite strategy: 改成具体收益、适用边界或待验证假设。
- Bad example: 该架构对业务发展具有重要意义。
- Better example: 该架构减少后续索引模块对 PDF 类型的判断分支，
  但 OCR 成本仍需要通过批量测试确认。

## 3. 机械三段式

- Pattern name: `zh-mechanical-three-part`
- Risk: `首先/其次/最后` 掩盖真实逻辑，段落像模板。
- Common phrases: `首先`, `其次`, `最后`, `一方面`, `另一方面`
- Keep when: 步骤说明、会议纪要、SOP、变量定义、模型说明或证明过程需要
  明确顺序。
- Rewrite strategy: 用因果、约束、对比、依赖关系连接。
- Bad example: 首先分析需求，其次设计架构，最后完成落地。
- Better example: 输入格式和并发规模决定架构边界；错误恢复方式决定
  任务队列和重试策略。

## 4. 伪深刻二分法

- Pattern name: `zh-false-depth-contrast`
- Risk: 制造“不是 A，而是 B”的戏剧感，但没有解释机制。
- Common phrases: `不仅是工具，更是理念`, `不仅关乎效率，更关乎生态`,
  `不是简单的技术问题，而是系统性工程`
- Keep when: 对比能准确区分概念边界、目标与非目标、输入与输出、
  职责与非职责。
- Rewrite strategy: 写清 A 和 B 的实际差异、证据或后果。
- Bad example: PDF 预处理不仅是工具，更是文档智能的基础设施。
- Better example: PDF 预处理既包含抽取工具，也包含错误记录、重试和
  字段标准化；这些状态决定后续索引能否稳定运行。

## 5. 营销腔和产品腔

- Pattern name: `zh-marketing-tone`
- Risk: 像宣传材料，削弱技术或业务判断的可信度。
- Common phrases: `赋能`, `打造闭环`, `极致体验`, `全方位`,
  `革命性`, `领先`
- Keep when: 用户明确要求营销文案，并且词语符合品牌语气。
- Rewrite strategy: 改成事实、指标、功能边界或用户动作。
- Bad example: 该方案将全方位赋能业务闭环。
- Better example: 该方案把抽取、OCR、字段校验和失败重试放在同一条
  处理链中，便于追踪每页的处理状态。

## 6. 谄媚和客服腔

- Pattern name: `zh-flattery-service-tone`
- Risk: 把文档写成客服话术，影响专业性。
- Common phrases: `您提出的问题非常重要`, `非常荣幸为您`,
  `希望能够帮助到您`, `感谢您的信任`
- Keep when: 客服邮件、外部服务回复或礼貌通知确实需要。
- Rewrite strategy: 删除多余客套，直接交代处理结果或建议。
- Bad example: 您提出的 PDF 处理问题非常重要，下面我将为您详细展开。
- Better example: 下面的设计把 PDF 处理拆成识别、抽取、OCR、校验和
  错误记录五个阶段。

## 7. 公文腔误用

- Pattern name: `zh-bureaucratic-misuse`
- Risk: 用行政套话替代具体责任、动作和结果。
- Common phrases: `高度重视`, `扎实推进`, `统筹协调`, `落实落细`,
  `形成合力`
- Keep when: 正式公文、会议通报或政策材料需要保持体例。
- Rewrite strategy: 写清执行者、动作、时间、交付物。
- Bad example: 后续需要统筹协调各方资源，扎实推进方案落地。
- Better example: 后续需要确定 OCR 服务、队列组件和字段校验规则的
  负责人，并在联调前完成错误码表。

## 8. 学术腔误用

- Pattern name: `zh-academic-misuse`
- Risk: 把普通判断包装成抽象概念，反而不严谨。
- Common phrases: `内在逻辑`, `理论意涵`, `范式转换`, `多维度`,
  `系统性阐释`
- Keep when: 学术论文确实需要概念界定、理论位置和论证链。
- Rewrite strategy: 先定义概念，再说明变量、关系、证据和限制。
- Bad example: 本文系统性阐释 PDF 预处理的内在逻辑。
- Better example: 本章把 PDF 预处理定义为输入识别、内容抽取、质量校验
  和失败恢复的组合过程。

## 9. 过度排比

- Pattern name: `zh-over-parallelism`
- Risk: 看似有节奏，实际没有区分优先级。
- Common phrases: `提升效率、优化体验、降低成本、赋能增长`,
  `更高效、更智能、更可靠`
- Keep when: 摘要或汇报需要列出并列目标，且每项后文会展开。
- Rewrite strategy: 只保留可验证的收益，并说明条件。
- Bad example: 该方案提升效率、优化体验、降低成本。
- Better example: 对文本型 PDF，直接抽取可减少 OCR 调用；对扫描件，
  成本仍取决于页数和识别精度要求。

## 10. 抽象名词堆叠

- Pattern name: `zh-noun-stack`
- Risk: 名词越堆越空，读者看不到动作。
- Common phrases: `能力建设`, `体系化支撑`, `流程优化能力`,
  `价值释放路径`
- Keep when: 组织管理或政策文件有固定术语，但仍需解释。
- Rewrite strategy: 把抽象名词拆成动词和对象。
- Bad example: 构建文档智能能力体系，释放数据价值。
- Better example: 把每页的文本、图片、字段和错误状态保存为统一记录，
  让检索模块可以按页追踪来源。

## 11. 无来源判断

- Pattern name: `zh-unsourced-claim`
- Risk: 让未验证判断看起来像事实。
- Common phrases: `显然`, `众所周知`, `业界普遍认为`, `大量实践表明`
- Keep when: 紧跟来源、数据、实验结果或用户提供的事实。
- Rewrite strategy: 加来源；没有来源时改成假设或待验证项。
- Bad example: 业界普遍认为 OCR 是 PDF 智能处理的最佳路径。
- Better example: 对扫描页，OCR 是必要路径；对文本型 PDF，直接抽取
  通常成本更低。具体比例需要用样本集验证。

## 12. 泛化结尾

- Pattern name: `zh-generic-ending`
- Risk: 结尾没有决策、限制或下一步。
- Common phrases: `总而言之`, `综上所述`, `未来可期`,
  `具有广阔前景`
- Keep when: 需要论文式小结，但必须总结具体论点。
- Rewrite strategy: 用结论、风险、下一步或未解决问题收束。
- Bad example: 总而言之，该方案前景广阔，值得持续探索。
- Better example: 下一步应先验证 100 份混合 PDF 的抽取成功率，再决定
  OCR 队列的并发上限。

## 13. 标题党

- Pattern name: `zh-clickbait-heading`
- Risk: 标题承诺过大或情绪化，正文无法兑现。
- Common phrases: `彻底解决`, `一文看懂`, `终极指南`, `必看`,
  `颠覆式`
- Keep when: 面向大众传播且用户明确需要强标题。
- Rewrite strategy: 标题写清对象、范围和动作。
- Bad example: 一文彻底搞懂 PDF 智能处理的终极方案。
- Better example: PDF 预处理架构：输入识别、抽取、OCR 与错误恢复。

## 14. 粗体和符号滥用

- Pattern name: `zh-formatting-overuse`
- Risk: 用视觉强调代替结构，Markdown 渲染后显得嘈杂。
- Common phrases: 大量 `**重点**`, `!!!`, `✅`, `🚀`, 连续感叹号。
- Keep when: 清单、警告或操作步骤需要少量强调。
- Rewrite strategy: 用标题、段落和表格承载层级，减少装饰符号。
- Bad example: **非常重要！！！** 必须立刻完成所有优化！！！
- Better example: 必须先完成字段校验，否则错误数据会进入索引。

## 15. 过度列表化

- Pattern name: `zh-over-listing`
- Risk: 文档像提纲，不像可读说明；论证关系断裂。
- Common phrases: 每句话都是项目符号；大量二级、三级列表。
- Keep when: SOP、会议纪要、检查清单和参数说明需要扫描。
- Rewrite strategy: 合并解释性内容为段落，只保留真正需要扫描的条目。
- Bad example:
  - 背景
  - 问题
  - 方案
  - 风险
- Better example: 当前问题来自输入类型不稳定。文本型 PDF、扫描件和
  混合 PDF 需要不同处理路径，因此预处理层必须先识别文件和页面类型。

## Markdown Protection

Do not rewrite these destructively:

- YAML frontmatter.
- Code fences.
- Tables.
- URLs and file paths.
- Quoted source material unless the user asks.
- Citations, bibliography entries, variable names, formulas, and API names.

## Boundaries

去 AI 腔不是把严谨内容改随意。学术论文可以正式，技术设计可以密集，
SOP 可以列表化，会议纪要可以动作导向。判断标准是读者是否更容易理解
具体事实、关系、限制和下一步。
