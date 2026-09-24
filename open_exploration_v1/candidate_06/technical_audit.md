# Technical audit — Paired-version loom

审查对象：[SVG](figure.svg) / [高分辨率图](figure.png) / [180 mm 预览](paper_width_preview.png)。这是视觉探索候选，技术内容遵循用户提供的**论文定义**。

| 科学约束 | 本图的可见证据 |
|---|---|
| 每个提交版本为 `V_i=(Q_i,W_i)`，历史可恢复、可分枝 | 所有 v0–v6 节点均在同一图中绑定蓝 Q 与薄荷 W；v2 分叉，一枝保留 v6（Previous HEAD），另一枝通向 v4。 |
| `q_t` 与 `Q_t` 有别 | 反馈明确写“+ evaluation metrics / − legacy API”；Git Agent 结合只读历史解析完整 `Q_t`，COMMIT 记录含 `Q_t`。 |
| INSPECT / REUSE / COMMIT | 细灰 INSPECT 是只读；淡灰 REUSE 是未触发的精确匹配旁路（本例无匹配）；橙色 COMMIT 是唯一激活主路。REUSE 若触发直接返回旧版本，不经过 Router、Update Agent 或新提交。 |
| COMMIT 决策记录 | 图上标记 `(Q_t,b_t=v4,h_t)` 或等价短写；`h_t` 是语义提示，**并非**预定的文件改动清单。 |
| Router 独立且只在 COMMIT 后 | 橙色 COMMIT 从 Git Agent 抵达 v4；Router 在其后，Fresh 未激活。 |
| 路由与候选执行 | Active 是 Reuse & Patch（从 W4 fork）；Fresh Solve 从空状态初始化但本例未选；Task-Native Update/Domain Harness 完成实际工作。 |
| 历史不可变，候选隔离 | 虚线边界同时覆盖主图中的 candidate 标记与下方执行细节；旧 W4 在边界左侧，v7 在右侧外。 |
| 工作状态改变 | Core Logic、Utilities 保留；Evaluation→Evaluation' 更新；Legacy API 仅在更新后的候选中排除。图内的灰色“excluded”与失败丢整个候选是不同标记。 |
| 提交与失败 | v2 分为左下 v3→v5→v6 与右侧 v4；v4→独立 Router→边界内候选→边界外 v7。 候选宏观节点发出灰虚线 discard 分支，未以 v7 为失败起点。 |
| 训练对象与信号 | Final Outcome 与 Query Tracking（Requirement Fidelity、Base Optimality、Staleness Exclusion）各自产生归一化 advantage，经 interface-level Harness RL / GRPO 只回到**同一 Git Agent**；Router、Update Agent、Domain Harness 冻结。提交 v7 的绿色路径与紫色策略学习路径分开。 |

**本候选仍需观察的视觉风险：** 竖向旧枝与右向新枝让 v6 看起来在画面下方，评审可能误以为时间位置决定 HEAD；HEAD 标签和 v4 选中标记必须保留。
