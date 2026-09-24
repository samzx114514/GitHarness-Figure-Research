# GitHarness Figure 2：三条原创构图方向

这些是**结构研究草图，不是可投稿最终图**。三张图均由[生成脚本](06_original_compositions/make_studies.py)产生 SVG，并附纸宽预览。参照论文只借构图原则：出处到设计的对应见下表；图形和节点均重新绘制。

| 草图 | 矢量/预览 | 第一视觉命题 | 主科学对象 |
|---|---|---|---|
| 1. Ancestry River | [SVG](06_original_compositions/01_ancestry_river.svg) · [PNG](06_original_compositions/01_ancestry_river.png) | 新版本是 v4 的**实际新枝**，非 HEAD v6 的追加 | 单张成对版本历史图及一条橙色分枝 |
| 2. Workbench Cutaway | [SVG](06_original_compositions/02_workbench_cutaway.svg) · [PNG](06_original_compositions/02_workbench_cutaway.png) | 历史工件被复制，候选内部发生选择性变换 | 巨大的 W4 / W_t^0 / W̃_t 对齐工作片；小型插画 Git Agent |
| 3. Requirement Lens | [SVG](06_original_compositions/03_requirement_lens.svg) · [PNG](06_original_compositions/03_requirement_lens.png) | 完整 Q_t 改变同一历史图中的**兼容性视野** | 覆在唯一历史 DAG 上的需求焦点与选中分枝 |

## 1. Ancestry River — 抽象图主导

**空间组织。** 唯一的历史 DAG 横穿画面中央，v2 分成 v3→v5→v6 与 v4→候选→v7。Git Agent 在上游读图并以橙线选 v4；局部工作变换从 v4 的真实边用浅引线放大，训练只占底缘一条细回路。主图与展开共用 v4 和分枝身份，没有三行 Dashboard。

**图形/控制。** Q/W 合为同一双半圆节点；灰虚线 INSPECT；橙色 COMMIT 和 v4 分枝；小号 Router 标注紧贴分枝，Fresh Solve 淡化。放大区的隔离线左侧是原始 W4，右侧才是候选状态。`Q_t,b_t=v4,h_t` 在选中边旁，不变成独立控制面板。成功沿枝落在 v7，失败只使候选无效。紫回线返回顶部同一 Git Agent。

**来源→借法。** [ToT Fig.2](04_visual_analyses/tree_of_thoughts.md)：从真实节点/边展开；[RAP Fig.1](04_visual_analyses/rap.md)：树拓扑承担科学命题；[VAR Fig.2](04_visual_analyses/var.md)：同一对象连续变化。没有复制三论文的节点造型或特色图标。

**风险/与 v5.2、A′ 区别。** 左下局部放大仍可能被误读为又一模块，需用引线、尺度与相同槽位证明它确属 v4 边。A′ 是“上方图 + 下方多个独立功能箱”，此图只保留**一条枝的局部视窗**；训练并非第三个巨型区域。草图把 Exact Reuse/Fresh Solve 仅作淡色文字，最终稿应补准确的旁路终点，但不可放大到抢主线。

## 2. Workbench Cutaway — 克制科学插画

**空间组织。** 上方的历史小图提供来源，画面大部分给“工作副本的剖视台”：左 W4 → 穿过明显边界 → 内部 W_t^0 → Update Agent → W̃_t → v7。v4→v7 的分枝以弧形沿剖视台上方贯穿，说明下面不是另一条独立流程。

**图形/控制。** Git Agent 是唯一有少量面部线索的角色，执行者改用工具状符号；旧工作片与候选工作片用同一四槽位轮廓，Evaluation 由淡色变橙、Legacy API 消失、Core/Utilities 保持绿。Router 只在 COMMIT 后靠近候选入口，训练紫箭头只回到 Git Agent；冻结对象仅一行小注。

**来源→借法。** [Octo Fig.1](04_visual_analyses/octo.md)：一个有身份的科学对象统一关系，少量插画强化识别；[VIMA Fig.1](04_visual_analyses/vima.md)：真实对象对齐而非段落解释；[Voyager Fig.2](04_visual_analyses/voyager.md)：具体工作工件占中心。图标是本项目的原创简化符号，不借章鱼/拼图/机器人形象。

**风险/与 D′ 区别。** 大候选边界可能再次像工程架构框，下一轮应测试无虚线而以淡色底/阴影分隔。D′ 把历史 W4 放到候选内且错写 +Legacy；本图让 W4 明确在外，需求是 `− legacy API`。图中的弧形 ancestry 边应在精修时避免与工作流程构成两个相互竞争的“v4→v7”路径。

## 3. Requirement Lens — 需求视野与历史图同位

**空间组织。** 一片淡蓝焦点区直接罩在**真实历史图**上，不画第二份“检索结果”。大字 `History under resolved Q_t` 与 `Exact match: none / Compatible: v4` 直接解释选择；Git Agent 在焦点外发出橙色判断。v4 向下转入一条候选生成轨道，历史 W4 在边界外、W_t^0/W̃_t 在内部，最终抵达 v7。

**图形/控制。** 图本身既是历史、也是 Q_t 下的选择对象；淡蓝色表示解释视野，**不是把历史节点重写为 Q_t**。INSPECT 灰虚线、COMMIT 橙线，Router 只能在橙色 COMMIT 之后。训练弧绕外部返回同一策略符号。候选中四槽位保留/更新/排除的对应关系仍在，但面积小于前两种研究。

**来源→借法。** [GoT Figs.1–2](04_visual_analyses/graph_of_thoughts.md)：图结构即运算对象；[ToT Fig.2](04_visual_analyses/tree_of_thoughts.md)：局部机制与具体边同位；[ExpeL Fig.1](04_visual_analyses/expel.md)：一条宏观主线由索引关系解释。淡蓝焦点区为 GitHarness 的新隐喻，不借任何论文的具体轮廓。

**风险/与旧稿区别。** “需求透镜”容易暗示选择是几何距离或检索相似度；最终稿须用 `compatible under Q_t` 明确它是 Git Agent 的语义判断。与 A′/D′ 的面板化不同，需求解析不再独立占一块图：`Q_t` 作用于**同一张 G_<t**。小尺度候选槽位可能需要另做 inset 而非扩大整张图。

## 三图共同的科学语义锁

`V_i=(Q_i,W_i)`；实例 `HEAD=v6, base=v4, new=v7`，v7 直接由 v4 的支路产生；`q_t` 是新增反馈（+metrics、−legacy），`Q_t` 才是完整解析需求；此例无 Exact Match，主路 COMMIT + Reuse & Patch。Git Agent 可以 INSPECT/REUSE/COMMIT；Exact Reuse 绕开 Router、Update Agent 与候选。Router 仅在 COMMIT 后，Fresh Solve 从空状态起，Reuse & Patch 复制选中 W4。旧 W4 不可变且始终在隔离候选外；候选由 W_t^0 经 Task-Native Update Agent/Domain Harness 变成 W̃_t。Core/Utilities 保留，Evaluation 更新，Legacy API 排除。成功提交 v7；失败仅丢候选。Final Outcome 与 Query-Tracking（fidelity/base/staleness）经 Harness RL / GRPO **只更新同一 Git Agent**；Router、Update Agent、Harness 冻结。草图的字数/线型简化只用于探索空间构图，不能被解释为删除这些机制。

下一轮应把三张图同时打印在论文版心宽度比较：先遮住全部小标签，让评审口述各自主科学命题，再看他是否能指到 **v4 的真实分枝、隔离线、训练终点**。优先对比图 1 与 2；图 3 检验“需求解析能否成为同一图上的视觉焦点”。
