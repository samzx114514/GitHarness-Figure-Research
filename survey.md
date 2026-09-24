# GitHarness Figure 2：真实论文方法图的视觉调研

调研日期：2026-09-23。范围：2023–2026，共12篇，覆盖树搜索、经验复用、状态演化、推理/训练关系与高密度框架图。**本报告研究构图，不评判算法优劣，也不制作最终Figure 2。**

## 结论先行

GitHarness需要一个具有身份连续性的科学对象：**由成对(Q,W)节点构成的可恢复历史图，以及从选中v4产生v7的那条新枝**。当前图的内容已经较完整，但主图、需求面板和执行面板分别讲述了一遍过程，读者要自己把它们拼起来。减少边框有帮助，却不足以建立科学叙事。

最有价值的来源组合是：ToT Fig.2的**从真实节点引出局部机制**、ExpeL Fig.1的**宏观主图与A/B解释关系**、Voyager Fig.2的**中央工作对象接收不同来源的输入**、ACE Fig.4的**全局回线准确回到原对象**。AgenticRag-R1提供主线与多个展开的连接方式，但其密集小字不可照搬。它们贡献的是组织原则，不是一张可复制的完整模板。

下一轮优先比较[方向A：版本图主体](git_harness_design_directions.md)与[方向D：中央工作变换](git_harness_design_directions.md)。A回答“为何选v4而非HEAD”，D回答“历史工作如何安全地成为新工作”。另外两种方向分别检验Q/W对应关系和唯一策略闭环。

## 1. 技能发现与任务范围

检查了当前技能目录与会话技能清单，发现并阅读了：

| Skill | 本次使用方式 |
|---|---|
| drawio-diagram-builder | 来源角色区分、科学对象与箭头语义、渲染审查；本阶段按用户要求仅输出SVG研究草图，不制作draw.io定稿 |
| pdf | 下载原始PDF后渲染、截图、读图注和邻近方法；不凭文本推断布局 |
| research-paper-writing | 先明确科学命题，再检验图中主张与正文证据一致性 |
| systematic-literature-review | 分批独立提取后跨论文综合；用户明确要求原图和多源检索，故不套用仅arXiv摘要/单一报告输出模板 |
| pptx-generator、presentations | 已识别并读取入口；本次不启动PowerPoint制作 |

未发现单独名为TikZ的专用技能。imagegen与visualize在清单中存在，但本轮目标是证据调研和矢量结构草图，不需要生成式位图或互动模拟。详细路径记录见[技能记录](03_analysis/00_skills_and_scope.md)。

## 2. 检索与核验方法

这是有目的的视觉样本调研，不是PRISMA式穷尽综述。以用户的六篇种子论文为起点，补充ToT、Voyager、DS-Agent、Agent Lightning及两篇近期候选参考。优先会议正式PDF；无法取最终会议版时使用作者保存版本或arXiv原文，并注明版本。只用论文原图和原文判断视觉特征，没有用博客/自动摘要替代图像检查。

流程：确认论文身份和最终venue→下载PDF→定位真实方法图→渲染整页→查看清晰裁图→读图注和附近方法→查看约680px宽缩略图→记录A–H分析→归纳跨图规律。各来源JSON记录页码、图号、裁框、下载链接和核验状态；PDF另有SHA256留存。页码都是保存PDF的**1-based物理页码**，不能随意套用到另一个版本。

**12篇全部完成原图检查。** 共保留18张编号方法/概念图：12张主分析图，6张辅助图；另存整页和尺度预览。Verified只表示来源与图像已核验，不等于已同行评审或推荐整套构图。

身份校正：

- AWM最初2024预印本，最终为[ICML 2025](https://proceedings.mlr.press/v267/wang25bx.html)，不能据旧投稿PDF标成ICLR。
- Voyager为[TMLR 2024](https://rpl.cs.utexas.edu/publications/2024/03/14/wang-tmlr24-voyager/)，不是ICLR 2024。
- ACE有[ICLR 2026官方记录](https://iclr.cc/virtual/2026/poster/10008343)。
- [LoongReflect](https://arxiv.org/abs/2608.11967)、[AgenticRag-R1](https://arxiv.org/abs/2608.29622)仅按2026预印本处理；本次没有用户提及的两张原参考附件，不能确认检索出的图就是此前指定的图。LongReflect/LoongReflect拼写也未作无证据等同。
- ExpeL使用38页作者保存版本，Fig.1在PDF p3；不能假定11页会议版同页码。

## 3. 逐篇视觉证据索引

以下每条结论来自对应原图与正文，完整A–H分析在链接中。

| 论文 / 主图 / PDF页 | 观察到的构图机制 | 可迁移对象 | 不可迁移语义 |
|---|---|---|---|
| [LATS](03_analysis/lats.md) Fig.2 / p5 | 六个无外框操作分镜，树节点和活跃色反复使用 | 同一版本节点语法、只展开代表操作 | backpropagation是树值回传，不是Git Agent参数梯度 |
| [ToT](03_analysis/tree_of_thoughts.md) Fig.2 / p5；辅Fig.1 / p2 | 左真实树，右生成/评价；取景框和引线有具体起点 | v4→candidate边级透视 | thought节点不是恢复checkpoint；红绿可行性不能永久标记历史版本好坏 |
| [A-Mem](03_analysis/amem.md) Fig.2 / p4 | 相同note母题在集合、链接、演化和检索中保持形状 | Q/W节点跨尺度身份一致 | 旧memory可被更新；GitHarness历史不可原地改 |
| [AWM](03_analysis/awm.md) Fig.2 / p3；辅Fig.3 / p3 | 同一个Memory/Agent收束闭环；具体轨迹与抽象workflow对照 | 共享对象、从例子到规则的展开 | workflow归纳不是参数RL；Memory不是历史DAG |
| [ACE](03_analysis/ace.md) Fig.4 / p5 | 三角色横线与产物间隔，底部长回线回Playbook | 少量对象、短标签、准确回路落点 | Playbook更新不是commit图；无权重训练 |
| [ExpeL](03_analysis/expel.md) Fig.1 / p3 | 左主图、右A/B解释，索引对应；双路进入评估 | 单一历史图+有身份的机制放大 | training阶段不是参数训练，经验池不是版本图 |
| [Reflexion](03_analysis/reflexion.md) Fig.2 / p4 | Actor/环境交互与评估/反思回到同一Actor | 唯一策略对象与明确反馈终点 | 语言反思不是GRPO；图偏工程，不宜当整体模板 |
| [Voyager](03_analysis/voyager.md) Fig.2 / p2 | 三域围绕中央代码对象，任务和技能双输入，成功写回 | 候选工作居中、选择和执行分工 | skill复用不是W4恢复；失败程序修正不是丢弃candidate |
| [DS-Agent](03_analysis/ds_agent.md) Fig.3 / p4 | 案例重排前后+同一Case3被复用；共享案例库连两阶段 | 选中v4的身份连续性 | 相似度排名不等于完整需求兼容性；不借数据库/多图标流程 |
| [Agent Lightning](03_analysis/agent_lightning.md) Fig.2 / p6；辅Fig.1/3/4 | 状态槽位固定、有效值逐次改变；记录转换连接训练 | W4/W_t^0/W̃_t对齐；决策与训练数据对应 | gray未赋值不是stale；通用多agent训练不是只训Git Agent |
| [LoongReflect](03_analysis/loongreflect.md) Fig.2 / p4 | 推理树与训练两带、失活枝保留、训练快慢通道 | 推理主对象+支持性训练层；保留历史 | 不照搬teacher/双通道；恢复前缀不等于隔离fork |
| [AgenticRag-R1](03_analysis/agenticrag_r1.md) Fig.2 / p4 | 顶部主线+三处淡色楔形展开；动作色跨栈/序列复用 | 主图与局部机制的父子关系 | LIFO pop、attention mask、轨迹拒绝均非GitHarness机制 |

## 4. 五类需求的覆盖与发现

### A. Tree Search / Branching Agent

LATS、ToT、LoongReflect都让拓扑负担真实科学信息。ToT最直接：即使遮住方法名，树的展开和选择仍可区分其推理组织。GitHarness也应达到这个标准——遮掉标题后，仍能看出v4而非v6产生v7。不能只画任意分叉后用“Selected Base”文字补救。[ToT原文](https://proceedings.neurips.cc/paper_files/paper/2023/file/271db9922b8d1f4dd7aaef84ed5ac703-Paper-Conference.pdf)

### B. Agent Memory / Experience Reuse

AWM、ACE、ExpeL、Voyager各自围绕一个被反复使用的对象组织流程：Memory、Playbook、Experience/Insights、Skill/Code。它们整体感强的地方，是箭头持续回到同一对象。A-Mem则说明内容很相关并不保证布局整体性：四列内部的细节多，读者仍要追踪多个方向。GitHarness需要共享**真实历史图**，不能借一个云状Memory替代。[AWM原文](https://proceedings.mlr.press/v267/wang25bx.html)；[ACE原文](https://arxiv.org/abs/2510.04618)

### C. Incremental State Evolution

Agent Lightning Fig.2用稳定槽位显示变量变更；ACE把增量项放在回线中；A-Mem用同形note表达更新前后；AgenticRag-R1用相邻栈和mask说明删除的影响。这些图都把“状态发生什么变化”画出来，而不是仅写Update。GitHarness可使用四行工作成分的同位对齐，但变换必须发生在fork后候选上，不可把ACE/A-Mem的原地更新语义带进历史。[Agent Lightning原文](https://arxiv.org/abs/2508.03680)；[A-Mem原文](https://proceedings.neurips.cc/paper_files/paper/2025/hash/19909c36f51abc4856b4560aff3d36d6-Abstract-Conference.html)

### D. Agent Training + Inference

Agent Lightning和两篇2026预印本确实提供参数优化结构；多数memory论文的“学习”只是上下文或程序变化。这是本轮最重要的语义防线：不能把ExpeL的Training、AWM的归纳、Reflexion的反馈都拿来充当Harness RL。GitHarness的版本写入和参数训练要用两个不同终点：前者进入版本图，后者返回Git Agent。[LoongReflect原文](https://arxiv.org/abs/2608.11967)；[AgenticRag-R1原文](https://arxiv.org/abs/2608.29622)

### E. Dense Scientific Framework Figures

ExpeL的A/B对应与AgenticRag-R1的楔形展开，把“多区”组织成“主对象+解释”，因此比简单并排模块更完整。Voyager用中央代码同时接住左右两路输入，验证后的成功/失败又以不同路径返回。这些是结构组织，而非配色或插画风。LoongReflect的宏观上下层清楚，但密集的小字提醒我们：有框架感不代表所有细节在纸面都合格。[ExpeL原文](https://ojs.aaai.org/index.php/AAAI/article/view/29936)；[Voyager原文](https://arxiv.org/abs/2305.16291)

## 5. 可以迁移的六条构图原则

**1. 让贡献变成一个可见的空间事实。** v7在v4的新枝上、W4在候选边界外，比“历史保持不变”说明句更强。对象、祖先边与边界优先于模块标题。

**2. 局部细节要有地址。** 每一处机制放大都能回答“它解释主图中的哪一节点、哪一条边、哪一种操作”。ToT取景框、ExpeL A/B、AgenticRag楔形展开是三种不同的地址标记。无地址的小面板应合并或删除。

**3. 同一对象跨区域保持身份。** v4→W4→W_t^0不是同名方框随意出现。用连续连线、同形节点、固定行槽或取景关系明确“所选版本的工作checkpoint被fork”。对象重复可以有用，前提是它在解释不同尺度/时刻。

**4. 颜色必须服务跨区域语法。** 蓝只承载requirement、mint承载work；橙承载选择和更新；绿承载保留/成功；灰承载非活动或排除。灰色在不同作用域需要文字/位置辅助，不能把旧HEAD画成错误失败。紫色只用于参数训练。

**5. 回线终点就是科学定义。** commit回到新版本，INSPECT指向历史，选择到v4，梯度到Git Agent。这些箭头即使走在同一画布，也不能落在大区域边缘后让读者猜。

**6. 先分配注意力，再分配内容。** 主版本图或中央候选对象约占视觉主导；需求解析解释选取的依据；训练支持主故事，约一小条带/小回路即可。没有证据表明某个比例普遍最优，具体比例由下一轮5秒/20秒读图测试决定。

## 6. 对现有GitHarness图的诊断

已检查用户最初提供的参考PNG以及本任务前一轮生成的`figures/githarness/githarness.svg/png`。本轮未取得单独可辨识的v5.2原件，故以下不冒充v5.2逐像素审查。

1. **多个局部起点竞争主命题。** 顶部讲图演化，中左重新讲q_t→Q_t，中右重新讲Router→执行，底部重新讲RL。读者看到四次开场，缺少一次连续解释。
2. **同一身份由标签维系，而非结构维系。** v4/W4在不同位置重复，但未从真实v4节点/边做精确展开；读者必须靠记住名称连接。
3. **重要性与面积不一致。** 当前HEAD不必是base这一贡献只体现在一条小分支；细分模块占据更大面积。减少边框后，这个注意力分配问题仍存在。
4. **局部执行仍偏模块列表。** 画出Core/Evaluation/Legacy/Utilities是进步，但若它们成为两组小卡片与旁边Update Agent，读者看到的是组件inventory；固定槽位、边界和差分才构成状态变换。
5. **训练与状态演化混用循环直觉。** 训练必须返回同一策略；不能只是从图下方拉一根长线。也不能把“结果写入历史”当作“更新模型”。
6. **最小字承载过多关键语义。** immutable、after COMMIT、discard candidate应至少有空间或边界上的冗余支持，不能全部依赖细字。与大标题相比，它们对正确理解更重要。

根本问题是**科学对象与视觉主从关系不够强**，不是缺少漂亮图标、渐变或更像某篇论文的配色。

## 7. 推荐下一轮探索

完整四方案与原始SVG见[设计方向](git_harness_design_directions.md)。优先A与D；B、C是针对特定理解难点的备选。评价时保持同样文字预算和颜色，避免把“更精致”误认为“结构更好”。

最小检查问题：5秒内能否说出v7父版本；20秒内能否区分q_t/Q_t、W4/W_t^0/W̃_t；能否指出被训练模块；能否分别指出Legacy API排除和失败候选丢弃；是否误认为REUSE也过Router。答错应修改空间关系，暂不增加解释句。

## 8. 限制与科学诚信

- 这是一组经过验证的目的性样本，不代表三大会议全部方法图风格。
- 技术/视觉评分是本次设计判断，不是引用量、论文质量或性能排名。
- 680px约等于180mm@96dpi的数字预览；已实际查看，但未进行实体打印。不同会议版芯不同，最终须按真实LaTeX宽度复核。
- 原图只作为内部研究证据，权利归原作者/出版方；不要把原图截片、独特图标或整套设计直接拼入GitHarness最终图。
- 论文的搜索回溯、memory演化、文本反思和参数训练各不相同。所有迁移均以用户定义的GitHarness语义为约束。

## 9. 自检

| 检查 | 结果 |
|---|---|
| 至少8–12篇真实论文，覆盖五类 | 12篇，五类均有原图支撑 |
| 每篇原PDF、图号、PDF页、清晰截图、附近方法核对 | 已完成；见来源JSON与逐篇分析 |
| Unverified不伪装Verified | 特定用户参考图身份未确认；图像本身已核验；三篇preprint不冒称会议录用 |
| 技术相关与视觉价值分开 | 见comparison.md双评分与不迁移列 |
| 原创结构研究而非最终图 | 4份带研究标记的SVG/PNG；未制作PPT或替换现有Figure2 |
| 当前版本比较的证据边界 | 比较实际可见两版；v5.2未取得原件 |
