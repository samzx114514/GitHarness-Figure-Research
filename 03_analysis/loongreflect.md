# LoongReflect：推理对象与训练双通道的分层闭环

- **论文**：LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation。
- **来源及版本**：[arXiv:2608.11967v1](https://arxiv.org/abs/2608.11967)，2026-08-12 提交；[PDF](../01_papers/loongreflect.pdf)。仅核验为预印本，未确认会议录用。
- **身份边界**：用户写的是“LongReflect 参考图”，本任务未附该图。LoongReflect 是名称和主题接近的候选，**不能宣称已确认它就是用户所指图片**。
- **图像核验**：Verified。Figure 2，PDF 第 4 页；目视检查高清裁图，阅读图注与第 3–4 页 Method、状态公式、memory control 和 two-channel optimization。
- **材料**：[高清图](../02_figures/loongreflect_fig2_pdfp4.png)、[含图注整页](../02_figures/loongreflect_pdfp4_page.png)、[180 mm 预览](../02_figures/loongreflect_fig2_180mm_150dpi.png)。

## A. 第一眼的科学命题

最明显的是上推理、下训练两大横带，上半带中央是一棵反复回溯再延展的轨迹树，右边橙色反思控制器和紫色恢复过程说明为什么返回。下半带用 FAST、SLOW 和协调三块解释学习。图不是仅说“Agent + memory + RL”，而是强调可逆执行和局部/全局两种学习信号的配合。

## B. 全局构图

两大带以深色轮廓统一，各自内部仍有多个框。上带从左至右是任务/策略动作集、轨迹树、反思控制、恢复；下带三个相邻区域横向展开训练。推理与训练之间有标注 on-policy trajectories 的下行箭头，训练底部有 next iteration 回路，上带恢复底部有回到策略的虚线。分层关系清晰，但训练占接近一半高度，且内框、插图与说明很多；它不是减少 over-boxing 的直接范本。

## C. 机制展开

树、控制器和恢复不是三个平行清单：树右侧箭头接入反思；控制器以可靠性菱形分出继续与回溯；恢复区逐项说明回溯效果。树内部圆节点按动作类型着色，旁边小图例将颜色与动作关联。下方训练重复使用上方策略符号与轨迹对象，形成跨层语义联系。但图中训练更新策略与上方策略的连接仍需沿边缘细虚线追踪，GitHarness 应把返回唯一 Git Agent 的终点画得更直接。

## D. 图与状态

树向下增长，红色弧形虚线回到较早位置，短侧枝保留被放弃的后缀。正文确认 inactive branches 仍保存在轨迹树，但不进入后续 active context，故这些回溯弧不表示删除全部历史。与 GitHarness 的历史保留具有可比性。不过 LoongReflect 的节点是行动/轨迹状态，GitHarness 节点是成对需求与工作 checkpoint；前者的恢复当前前缀不能不加区分地等同后者的独立 candidate fork。

## E. 训练表示

下带左侧为带 EMA teacher、结构提示和局部 token 掩码的蒸馏，中间为完整轨迹奖励、组相对优势与 GRPO，右侧用暂时更新、再评估和方向合并解释协调。各块的输入/输出方向清楚，也以相同策略符号建立身份连续性。GitHarness 只需两个奖励汇入 GRPO 并更新 Git Agent，不应移入 teacher、fast/slow 梯度或 look-ahead 步骤；它们不是 GitHarness 机制。

## F. 密度来源

优点是树拓扑、动作色、双训练通道和更新方向都提供真实机制密度。缺点是数据库、放大镜、剪刀、机器人、奖杯等图标叠加上大量小字，降低了抽象对象的统一性。GitHarness 可借两级布局和回路端点，不能把这种丰富图标风格当作“像论文”的必要条件。

## G. 论文尺度

180 mm、150 dpi 预览中两大标题、轨迹形态、FAST/SLOW/协调区清晰；细粒度 token 标签、公式、四格反思内容和步骤说明明显吃力。通栏印刷不能以高分辨率代替合适字体尺寸。对 GitHarness 应压缩训练带到约五分之一高度、只保留奖励名称和唯一更新目标，放大 v4 分叉及 checkpoint 变换。该结论来自屏幕预览，未做实体打印测试。

## H. 迁移与不能迁移

**迁移**：推理的科学对象在上、训练作为支持闭环在下；保留失活历史但突出唯一活跃路径；回路有明确源和终点。**不能迁移**：把恢复旧前缀画成直接修改历史 checkpoint；把删除 active suffix 与 GitHarness 的失败丢弃 candidate 混为一谈；把训练双通道照搬成两个 Git Agent。GitHarness 应更进一步，以 W4 在隔离区外、fork 箭头跨边界、candidate 在区内来解决可逆状态语义。

**评分（设计判断）**：技术相关性 5/5；视觉借鉴价值 4/5。值得作为推理—训练整体层级参考，同时也是小字过密、图标过多的反例。

### 补充：680 px / 180 mm @ 96 dpi 核验

已实际打开[680 px 缩略图](../02_figures/loongreflect_fig2_180mm_96dpi.png)。上下两带和下方三列、橙色控制区、弧形回溯仍可识别；四格反思内容、训练 token、公式及右下步骤详情明显难读。它的视觉整体感在缩小时保留，但机制细节不应被视为全部合格。GitHarness 下一轮需要主动删减图标和次要操作细节，为 Q/W 配对及 fork 边界留出字级和空间。
