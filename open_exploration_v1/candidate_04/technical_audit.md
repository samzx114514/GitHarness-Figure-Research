# Technical audit — Field-notebook scene

审查对象：[SVG](figure.svg) / [高分辨率图](figure.png) / [180 mm 预览](paper_width_preview.png)。这是视觉探索候选，技术内容遵循用户提供的**论文定义**。

| 科学约束 | 本图的可见证据 |
|---|---|
| 每个提交版本为 `V_i=(Q_i,W_i)`，历史可恢复、可分枝 | 所有 v0–v6 节点均在同一图中绑定蓝 Q 与薄荷 W；v2 分叉，一枝保留 v6（Previous HEAD），另一枝通向 v4。 |
| `q_t` 与 `Q_t` 有别 | 反馈明确写“+ evaluation metrics / − legacy API”；Git Agent 结合只读历史解析完整 `Q_t`，COMMIT 记录含 `Q_t`。 |
| INSPECT / REUSE / COMMIT | 细灰 INSPECT 是只读；淡灰 REUSE 是未触发的精确匹配旁路（本例无匹配）；橙色 COMMIT 是唯一激活主路。REUSE 若触发直接返回旧版本，不经过 Router、Update Agent 或新提交。 |
| COMMIT 决策记录 | 图上标记 `(Q_t,b_t=v4,h_t)` 或等价短写；`h_t` 是语义提示，**并非**预定的文件改动清单。 |
| Router 独立且只在 COMMIT 后 | Git Agent 到 v4 是 COMMIT；Router 独立在候选外；Fresh 仅淡化备选。 |
| 路由与候选执行 | Active 是 Reuse & Patch（从 W4 fork）；Fresh Solve 从空状态初始化但本例未选；Task-Native Update/Domain Harness 完成实际工作。 |
| 历史不可变，候选隔离 | 折角历史 W4 完整地在椭圆外；椭圆内只有复制出的工作与更新。 |
| 工作状态改变 | Core Logic、Utilities 保留；Evaluation→Evaluation' 更新；Legacy API 仅在更新后的候选中排除。图内的灰色“excluded”与失败丢整个候选是不同标记。 |
| 提交与失败 | v4 的橙线向下抵达候选边界外 Router；结果绿色提交 v7，v6 仍保持旧枝 HEAD。 灰虚线从候选结果片段向边界外散去，和内部 Legacy API 排除不是同一路。 |
| 训练对象与信号 | Final Outcome 与 Query Tracking（Requirement Fidelity、Base Optimality、Staleness Exclusion）各自产生归一化 advantage，经 interface-level Harness RL / GRPO 只回到**同一 Git Agent**；Router、Update Agent、Domain Harness 冻结。提交 v7 的绿色路径与紫色策略学习路径分开。 |

**本候选仍需观察的视觉风险：** 插画稍大时可能喧宾夺主；需要与师兄讨论小角色是帮助快速定位训练对象，还是削弱版本拓扑的严肃感。
