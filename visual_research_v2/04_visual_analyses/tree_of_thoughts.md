# Tree of Thoughts — v2 绘画语言复核

**核验。** [NeurIPS 2023 正式记录](https://proceedings.neurips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html)；[Fig. 2/PDF p5](../../02_figures/tree_of_thoughts_fig2_pdfp5.png)、[680 px 预览](../../02_figures/tree_of_thoughts_fig2_180mm_96dpi.png)；辅助 [Fig. 1/p2](../../02_figures/tree_of_thoughts_fig1_pdfp2.png)。完整首轮逐图分析见[原记录](../../03_analysis/tree_of_thoughts.md)。

本轮重点观察 Fig. 2 的**边级放大**：左侧树保留被选择的真实节点/边，右侧把该边对应的生成与评估展开。读者不会误以为局部过程是另一个图。圆节点是 thought state，选中路径/候选分枝通过空间拓扑与颜色成为主角；没有角色插画。图中很小的文字在 680 px 预览中减弱，因此可迁移的是几何父子关系，而非全部局部字。GitHarness 应从历史图的**真实 v4 分枝**引出 W4 复制、工作更新和提交，再回到同一分枝上的 v7；不能把 thought 节点直接等同可恢复 paired version，也不能把树的评价色当作历史版本的永久优劣。
