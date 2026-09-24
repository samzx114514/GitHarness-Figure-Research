# GitHarness Figure 2 · 开放式视觉探索 v1

**打开方式：** 先看[六张并排画廊](gallery.html)，切换两列/三列；点图看 3000 px PNG，点下方链接看可编辑 SVG、[设计理由](candidate_01/design_rationale.md)与技术审查。六张都是完整方法图候选，用于用户和师兄选方向；**没有提前确定最终方案或制作 PPT**。

## 文件

每个 `candidate_01/` 至 `candidate_06/` 都有：

| 文件 | 用途 |
|---|---|
| `figure.svg` | 原生、可编辑的矢量图形与文字 |
| `figure.png` | 3000 px 宽的高清渲染 |
| `paper_width_preview.png` | 1063 px 宽，约等于 180 mm/150 dpi 的屏幕尺度预览 |
| `design_rationale.md` | 视觉命题、1–3 张已核验论文图的来源→画法映射、取舍 |
| `technical_audit.md` | 历史血缘、控制路由、隔离状态、选择性更新、训练目标逐项核对 |

[comparison.md](comparison.md)横向比较六种构图；[qa_log.md](qa_log.md)记录实际查看预览后的修复。`build_figures.py` 以 SVG 原语绘图并渲染两个 PNG 尺度；`write_notes.py` 生成每个候选的文字记录。

## 依据与制作

先重新阅读了 [第二轮视觉调查](../visual_research_v2/visual_survey.md)、[跨论文比较](../visual_research_v2/reference_comparison.md)、[图标研究](../visual_research_v2/iconography_guide.md)、[构图研究](../visual_research_v2/git_harness_composition_directions.md)，并直接查看 RAP、Octo、VIMA、VAR、ExpeL、ToT、Voyager、AgenticRAG-R1 的本地原图裁图。源图只提供**科学视觉原则**；六张候选中的图标、人物、工作片与线条均为本轮原创。

当前环境中有 `drawio-diagram-builder`、`research-paper-writing` 等相关技能。本轮实际采用了前者关于“一个图形元素对应一个科学语义”、来源角色区分、渲染审查和纸宽可读性的规则，以及后者关于“图先讲清主要科学命题”的原则。用户指定 SVG 作为交付，所以未生成 `.drawio` 或 PPT。用 Python 3 + CairoSVG 渲染，另以 SVG XML 解析和可见预览做核验。

**科学语义锁：** `V_i=(Q_i,W_i)`，`q_t` 改变活动需求并由 Git Agent 解析 `Q_t`；旧 HEAD=v6，选中 base=v4，无 Exact Match，COMMIT + Reuse & Patch，v7 从 v4 分枝。W4 不变且在候选外；fork 出 W_t^0，Task-Native Update/Domain Harness 得 W~_t，Core/Utilities 保留、Evaluation 更新、Legacy API 排除；成功提交 v7，失败只丢候选。REUSE 是直返旧版本的可选旁路；独立 Router 仅在 COMMIT 后选择 Fresh Solve（空）或 Reuse & Patch。Final Outcome 与 Query Tracking 的优势分开处理，经 Harness RL / GRPO **只训练 Git Agent**；Router、Update Agent、Domain Harness 冻结。

复现命令（在仓库根目录）：`python open_exploration_v1/build_figures.py`，随后 `python open_exploration_v1/write_notes.py`。论文尺度预览是屏幕模拟，不代替最终定稿的实体印样。源论文图版权属于原作者；这些设计没有照描其独特插画或完整图形。
