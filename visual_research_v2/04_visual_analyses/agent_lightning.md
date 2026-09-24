# Agent Lightning — aligned state and training connection

**核验。** [2025 arXiv 记录](https://arxiv.org/abs/2508.03680)，[Fig. 2/PDF p6](../../02_figures/agent_lightning_fig2_pdfp6.png)、[180 mm 预览](../../02_figures/agent_lightning_fig2_pdfp6_180mm.png)；首轮还检查 Figs. 1/3/4，见[完整分析](../../03_analysis/agent_lightning.md)。**这是预印本，不标作已被某会议录用。**

Fig. 2 不是强主画面，但相同位置的结构槽位通过多个步骤保持，变化项很明确。图标少，形状基本是对齐记录/状态槽；适合学习严谨的前后对应，不适合学习整体构图。图中的训练轨迹转换显示如何从 agent 执行取得可训练信息，控制对象和学习数据有联系。680 px 时槽位间的形状关系可见，细字难读。GitHarness 可让 Core Logic、Evaluation、Legacy API、Utilities 在 W4、复制后的 W_t^0、W̃_t 三处严格对位，并把两种奖励反馈只指向**同一个 Git Agent**。不可把图中多 agent 通用训练搬来；Router/Update Agent/Harness 在本文冻结。
