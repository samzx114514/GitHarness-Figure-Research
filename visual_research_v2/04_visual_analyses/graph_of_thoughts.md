# Graph of Thoughts — graph grammar as operations

**核验。** [AAAI 2024 正式记录](https://ojs.aaai.org/index.php/AAAI/article/view/29720)；可获取的 [arXiv 原文](https://arxiv.org/pdf/2308.09687)，[Fig. 1/PDF p3](../03_figure_gallery/graph_of_thoughts_fig1_pdfp3.png) 与 [Fig. 2/PDF p3](../03_figure_gallery/graph_of_thoughts_fig2_pdfp3.png)，[Fig. 2 680 px 预览](../03_figure_gallery/graph_of_thoughts_fig2_680px.png)。图注附近将 thought graph 的生成、聚合、评价和反馈定义为操作；本地版本页码不套用到会议版。

画面主对象是 thought 节点及其边，线性链、树与图的比较使“结构更自由”直接可见。Fig. 2 把生成/聚合操作画进节点拓扑，圈、箭头和线型承担含义；没有 agent 角色。整体由多个小子图对照，680 px 时操作小字很难读，所以不升为主参考。对 GitHarness 最直接的启发是让真实 `G_{<t}` 本身承担 read-only 历史、分叉、选中基底的叙事；不再配一个“existing graph”替身。不可借聚合边：GitHarness 的 v7 只有选中的 v4 为 base，而不是从 v4 与 v6 合并。
