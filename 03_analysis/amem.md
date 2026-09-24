# A-Mem — Fig. 2 视觉核验

- **论文**：A-Mem: Agentic Memory for LLM Agents；NeurIPS 2025。
- **原文**：[官方 PDF](https://papers.neurips.cc/paper_files/paper/2025/file/19909c36f51abc4856b4560aff3d36d6-Paper-Conference.pdf)；[会议记录](https://proceedings.neurips.cc/paper_files/paper/2025/hash/19909c36f51abc4856b4560aff3d36d6-Abstract-Conference.html)。
- **核验对象**：Figure 2，PDF 第 4 页（正文页码 4），读图注、§3.2、§3.3 及第 5 页延续部分。状态 **Verified**。
- **材料**：[裁图](../02_figures/amem_fig2_pdfp4.png) · [含图注整页](../02_figures/amem_pdfp4_full.png) · [180 mm 屏幕等效图](../02_figures/amem_fig2_pdfp4_180mm.png)。
- **主观评分**：技术相关性 4/5；视觉借鉴价值 3/5。后者评价对 GitHarness 的可迁移性，不是论文质量。

## A. Main visual thesis

第一眼是从左到右的四个浅底色竖区，以及贯穿其中的蓝色小笔记母题。最突出的科学对象不是单个 LLM，而是反复被构造、连接、演化和取出的 note。笔记图形在左侧起源、中部簇和右侧检索结果中保持一致，帮助读者确认这些步骤处理的是同一种对象。

## B. Global composition

四区分别为 Note Construction、Link Generation、Memory Evolution、Memory Retrieval。前三区对应写入机制，右区处理查询。中上部共享 Memory 区域将中间两列合并为更大的对象；左下新笔记沿折线送入中区，右侧查询从反方向读取它。标题形成横向阅读顺序，但各列内部主要向下，构成多次转向；四列淡色带仍有明显拼接感。因此它不是解决 GitHarness 碎片化的最佳整体模板。

## C. Mechanism expansion

连接生成从上方小簇下取 Top-k，在中部展开为中心笔记及相关笔记，再压回下方分组。此处不是独立文字解释框，而是同一对象由集合尺度变成局部关系尺度。左下属性列把抽象 note 展开为时间、内容、上下文等字段，右侧则让一个高亮笔记与邻居一起被取出。适合学习“对象反复出现但尺度改变”的解释方法。

## D. Graph and state representation

节点为同形蓝色笔记，簇用矩形容器和 Box 编号标识；小连接承担关联关系，而非版本祖先关系。顶部和底部重复簇表达存储状态变化，但缺少清晰旧/新时间轴。原图注明确允许一个记忆同时属于多个盒子，故不能把这些盒子当 Git 分支。§3.3 第 5 页明确新记忆会替代旧记忆，技术上是可变记忆演化，不是不可变历史 checkpoint。

## E. Training representation

图内没有奖励、优势、优化器或参数梯度路径。Memory Evolution 下方的 action/evolve 是记忆内容操作。不能把其向下更新箭头直接解释为 Git Agent 的 RL 更新；GitHarness 必须另设从奖励到同一策略的反馈，并限定训练边界。

## F. Visual density

密度主要来自小笔记重复、集合压缩及局部展开；大量机器人、地球、属性图标贡献辨识但也占空间。两段具体会话提供变化动机，却是最小最难读的文字。黑细箭头与蓝粗箭头区分一定层级，但这套差异并不自动等于控制流/数据流。迁移时应自己定义语义，不能假借原图外观。

## G. Paper-scale readability

已查看裁图及 680 px 宽版本（约 180 mm@96 dpi；只是屏幕检查代理，不等于打印 proof）。四列标题、Top-k、LLM 和蓝笔记仍可识别，具体会话与 Box 索引明显过小。科学对象可追踪，但核心机制若依赖会话全文就会失效。GitHarness 应把实例压缩为“+ Metrics / − Legacy API”，让细节由状态变化承担。

## H. Transfer to GitHarness

**迁移**：蓝/薄荷配对版本在历史图、所选 v4 和新 v7 中保持同一形状；从 v4 引出局部放大，展开 W4 的四个工作项；把颜色与形状同时用于对象连续性，而不重复解释句子。

**不迁移**：四个平行竖栏、服务器式存储组织、装饰图标和旧节点原地演化。GitHarness 的历史节点必须不变，选中 W4 后应跨越隔离边界生成 Wt⁰；只有候选内部呈现更新，最终新增 v7。不能将关系记忆图当成祖先图，也不能将 Top-k 相似度检索等同于 requirement-compatible base selection。

**一句构图启发**：让同一状态对象跨尺度保持可识别，而不要复制四列流程架构。
