# Voyager — v2 绘画语言复核

**核验。** [TMLR 2024 身份记录](https://rpl.cs.utexas.edu/publications/2024/03/14/wang-tmlr24-voyager/)；arXiv 作者版 [Fig. 2/PDF p2](../../02_figures/voyager_fig2_pdfp2.png)、[680 px 预览](../../02_figures/voyager_fig2_180mm96dpi.png)；完整首轮分析见[原记录](../../03_analysis/voyager.md)。

Fig. 2 最有价值的不是某个图标，而是**中央具体工作产物**：技能代码与环境执行是可观察对象，任务与技能库从不同方向输入。大区域围绕这份工作展开，角色/库/执行不再是同形方框。左、右和反馈的环向空间关系让工作产生与验证关联起来。680 px 下关键方向仍清楚，但若复制较多小字，纸张尺度会受损。GitHarness 可让一件复制出来的 `W_t^0` 成为画面中间真实对象，历史 `W4` 必须在候选边界外，更新后形成 `W̃_t`；选历史与做工作要分别由 Git Agent、Router/Update Agent 执行。Voyager 的“复用技能”不是恢复 checkpoint，也不能借其失败重试语义替代“失败仅丢弃隔离候选”。
