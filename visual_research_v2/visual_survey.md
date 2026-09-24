# 让 GitHarness 方法图成为一张科学图，而不是四块工程流程

**研究结果。** 25 篇真实论文筛查后，11 篇进入原图深度分析，7 篇列为[主视觉参考](03_figure_gallery/index.html)。这不是相关工作综述：选择依据是**图如何让科学对象、变化和局部机制可视**。本轮保留首轮所有 PDF/截图/分析，新增 [A′/D′ 图像诊断](01_screening/candidate_diagnosis.md)、[逐图分析](04_visual_analyses/)、[可并排看的真实图画廊](03_figure_gallery/index.html)、[图标试验](iconography_guide.md)和[三张原创结构草图](git_harness_composition_directions.md)。没有生成最终 Figure 2。

## 发现：一个主对象比“模块齐全”更重要

RAP 的读者先看到搜索树与带世界模型的语言模型；Octo 的读者先看到能连接输入/动作的中央策略形象；VAR 的读者先看到同一鹦鹉由粗到细；VIMA 的读者先看到四排具体状态变化。它们的技术主题并不都像 GitHarness，但画法有同一强点：**读者先识别科学对象，再读局部文字**。A′/D′ 的四种功能（历史、需求、执行、训练）虽齐全，缺少一个持续占据视觉中心的对象，故易被看成工程拼接。

GitHarness 的对象应是**单一、可恢复、可分枝的成对版本图**，尤其是 `v4 → (forked candidate) → v7` 这条新枝。图上的 v6 保持旧枝 HEAD，选中的 v4 不由当前 HEAD 决定。放大的工作片段仍必须认得出来自 v4，而非另起独立软件流水线。这个诊断来自 A′/D′ 原图，不意味着必须选“图最大”的布局：第二草图让工作副本占面积、历史分枝只在上方保证血缘，但二者仍共享同一个 v4。

## 七张主参考分别值得借什么

1. **[ToT Fig.2](04_visual_analyses/tree_of_thoughts.md)**：用具体历史节点/边锚定局部放大。GitHarness 的 fork/patch 解释必须接在真实 v4 分枝上。
2. **[ExpeL Fig.1](04_visual_analyses/expel.md)**：宏观主线与 A/B 解释有可追踪索引。GitHarness 只保留一张历史图，把需求判断与候选细节挂在选中位置。
3. **[Voyager Fig.2](04_visual_analyses/voyager.md)**：中央是实际工作产物，多个控制/信息来源向其汇聚。GitHarness 的候选 `W_t^0 / W̃_t` 可成为真正可见的变换对象。
4. **[RAP Fig.1](04_visual_analyses/rap.md)**：小角色剪影、world-model 图形与搜索树各用不同形态，树结构本身陈述贡献。Git Agent 的身份和 v4 分枝可以用形态而非重复标题表达。
5. **[Octo Fig.1](04_visual_analyses/octo.md)**：一个略带插画感的中央科学对象凝聚输入/输出；插画有角色识别功能。GitHarness 可试克制的小 Git Agent，但不能借章鱼、拼图边或机器人图。
6. **[VIMA Fig.1](04_visual_analyses/vima.md)**：状态变化由对齐的可见对象承担，文字只确认。四条工作内容应在 W4、W_t^0、W̃_t 的同一槽位中持续出现。
7. **[VAR Fig.2](04_visual_analyses/var.md)**：重复同一视觉对象，通过变化本身解释方法。GitHarness 应让 Evaluation 更新和 Legacy API 消失一眼可见；绝不能暗示版本进化单调提高。

[比较表](reference_comparison.md)把技术相近度和视觉价值分开。VAR 是与算法最不相似、对“同一对象发生可见变化”最有用的参考；RAP 是图结构/角色区别较兼顾的参考。GoT、Agent Lightning、AutoGen、OpenVLA 进入深分析但不占 7 个主槽：它们各有单点启发，不过整体图在纸宽或统一性上较弱。

## 5 类视觉问题的跨论文答案

| 视觉问题 | 原图观察 | 对 GitHarness 的可操作规则 |
|---|---|---|
| 图与分枝 | ToT 的树局部展开、RAP 的真实规划树、GoT 的操作图 | 历史 `G_<t` 只画一次；橙选中线抵达真实 v4；v7 从 v4 分枝，不得与 v6 串联 |
| Agent/工具/环境 | RAP 的机器人/世界模型/树；Octo 的任务/策略/动作；AutoGen 的重复角色 | Git Agent、Router、Update Agent 和工作状态有不同形态；只有 Git Agent 被紫色训练回线命中 |
| 局部状态变化 | VIMA 的同一对象多帧、VAR 的同一图像多尺度、Agent Lightning 的对齐槽位 | W4（外部）复制成 W_t^0（内部），四个工作内容对齐；保留/更新/排除可一眼辨识 |
| 宏观+微观联系 | ToT/ExpeL 的具体边或索引关系；Voyager 的中央工作对象 | 局部变换只应附着到 v4→v7 枝，不再平行讲述一条第二主流程 |
| 训练与推理 | Agent Lightning 的执行数据/训练联系；首轮 ACE/Reflexion 的回到同一对象 | Final Outcome 和 Tracking 奖励经 GRPO 汇合，紫回线落到唯一 Git Agent；冻结组件只需小注 |

## 插画到底能帮多少

[两张原创建模图](iconography_guide.md)检验了同一语义的极简与克制插画版本。小角色可使“谁在决策、谁被训练”更快被找到，特别是紫色回线能落到同一个标记。但 `V_i=(Q_i,W_i)`、工作 checkpoint、候选边界应坚持几何科学对象，不宜角色化。Octo 的章鱼给中央对象命名，RAP 的机器人给模型定位；两者都没有把所有流程角色漫画化。AutoGen 的微型角色过多使 680 px 图难读，是明确的负例。我们建议只给 Git Agent 使用低细节人格化线索，并让 Task-Native Update Agent 用不同的工具/执行标记。

## 纸宽可读性的实际观察

画廊里每张都可切换原图与 680 px 预览，约模拟 180 mm/96 dpi；图号、物理页码对应**保存的 PDF 版本**。RAP 的角色/树、Octo 的中心对象、VIMA 的状态列、VAR 的尺度层在预览仍清楚；ToT/ExpeL 的微字和 VAR 的底座小字须放大才读得全。结论不是“所有文字再缩一点”，而是让初读只依赖大形状、路径与少数短标签。未做实体打印，因此最终定稿前仍须实际版心校样。

## 来源与学术完整性

所有主参考有正式出版/会议记录、可访问的原始 PDF、明确图号和本地 PDF 页码、裁图、缩放预览；[目录](02_verified_papers/README.md)说明三份作者/arXiv 回退版本。**只有 VAR 的 Best Paper 身份据 [NeurIPS 官方公告](https://blog.neurips.cc/2024/12/10/announcing-the-neurips-2024-best-paper-awards/)声明**。论文图版权仍归原作者/出版方；草图只复用抽象构图原则和科学视觉隐喻，不照描整图、独特图标或拼贴作品。技术语义始终以用户给定 GitHarness 论文定义为准，三草图的共同约束见[设计方向文末](git_harness_composition_directions.md)。
