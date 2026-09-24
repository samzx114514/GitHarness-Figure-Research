# Tree of Thoughts：拓扑即命题，选定局部再展开

- **论文**：Tree of Thoughts: Deliberate Problem Solving with Large Language Models；NeurIPS 2023。
- **来源**：[正式会议页](https://proceedings.neurips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html)、[原始 PDF](../01_papers/tree_of_thoughts.pdf)。
- **核验**：Verified。Figure 1 在 PDF 第 2 页；Figure 2 在第 5 页。已检查原图、图注及第 2–5 页框架和 Game of 24 方法段落。
- **材料**：[Fig.1](../02_figures/tree_of_thoughts_fig1_pdfp2.png)、[Fig.2](../02_figures/tree_of_thoughts_fig2_pdfp5.png)、[Fig.1 整页](../02_figures/tree_of_thoughts_pdfp2_page.png)、[Fig.2 整页](../02_figures/tree_of_thoughts_pdfp5_page.png)、[Fig.2 180 mm 预览](../02_figures/tree_of_thoughts_fig2_180mm_150dpi.png)。

## A. 第一眼的科学命题

Fig.1 先用拓扑告诉读者：直接输入输出、单链推理、多链投票和树搜索是不同的计算结构。右侧 ToT 分支树是全图唯一具有多层选择、绿色路径和淡红未选节点的区域，无须依赖一长段创新说明。Fig.2 则把具体数字状态放进同一树语法，使抽象树变成可核查的过程。这对 GitHarness 特别关键：v7 的父节点为 v4，本身就应是视觉命题，而不应靠箭头旁的长句解释。

## B. 整体构图

Fig.1 有四个并排结构，但只用一条竖向虚线隔开先前方法与 ToT，没有四个背景面板。输入与输出的水平对齐提供比较基线。Fig.2 改为左侧一棵具体问题树，右侧上下两条机制展开：生成与评价。这两个图各自有明确任务，没有把概念比较、所有实现细节和训练堆在一张图里。

## C. 局部机制展开

Fig.2 的关键手法是两条有明确起点的引出线：灰色虚框圈住第一层展开位置，灰色箭头连向 Propose Prompt；橙色虚框圈住一个具体算式状态，橙色箭头连向 Value Prompt。读者知道右侧机制在处理左侧哪一部分，而不是看到凭空出现的另一个流程。GitHarness 可以在真实 v4—candidate 边上附着执行放大，不再在下方另放一个不知来自何处的 W4。

## D. 图与状态

Fig.1 节点保持极简空方块，强调拓扑。Fig.2 节点换成一步算式，并以小字标出剩余数字；颜色暗示可行性，展开边保留父子关系。右侧评价示例与左侧被框选状态一致，形成跨区域的实例身份连续性。GitHarness 应保留这种连续性，但节点必须是成对版本 (Q_i,W_i)，不可把一步 thought 当作可恢复 checkpoint，也不能把历史 graph 画成默认完整搜索树。

## E. 训练

没有训练区域。论文把该方法作为预训练模型上的推理搜索，正文明确不需要额外训练。右侧两个 LM 是生成与评价角色，并不意味着有两个受训策略。GitHarness 的 RL 应另有细小回路连接唯一 Git Agent，不能根据本图推断所有 LM 框都受训练。

## F. 密度

Fig.1 依赖树的分叉、色深与节点对齐，几乎没有解释句。Fig.2 的右侧提示和结果框明显更文字密集，但每段文字服务一个可核验例子。其优点是实例解释而非模块清单；局限是框内完整推理文字占据较多面积。GitHarness 可沿用局部引出，舍弃完整提示词，改成四条工作组件的保留/更新/排除标记。

## G. 论文尺度

检查了 180 mm 宽、150 dpi 的 Fig.1 与 Fig.2 预览。Fig.1 的主拓扑、颜色路径和 Input / Output 非常清晰；Fig.2 主流程与算式可读，树旁剩余数字和淡灰省略示例较小。GitHarness 的重要语义不能降级为这种小字；特别是 immutable、fork 和 candidate 应具有独立空间关系。这里是屏幕检查，未进行打印。

## H. 迁移与边界

**首选迁移**：一个版本图承担主命题，再用虚线括取一条选定边或一个选定节点，把局部机制作为其展开。v4 的强调色应在选中、fork 和 W4 三处连续出现；v6 保留普通历史色。**不能迁移**：以红/绿判断所有历史节点成败；GitHarness 的兼容性依赖当前 Q_t，不是节点的永久好坏。也不建议照搬四算法并排比较，Figure 2 应专注 GitHarness 内部机制。

**评分（设计判断）**：技术相关性 4/5；视觉借鉴价值 5/5。Fig.2 的“真实对象—具体取景框—机制展开”比它的提示词卡片更值得借鉴。

### 补充：680 px / 180 mm @ 96 dpi 核验

已实际打开[680 px 缩略图](../02_figures/tree_of_thoughts_fig2_180mm_96dpi.png)。左树、两个取景框、橙色引出与两条 LM 行仍然一眼可辨。主算式和框标题可读，剩余数字的小括注与淡灰省略文字开始丢失；右侧完整评价句需要近看。这进一步支持借鉴取景关系而减少框内文本，而不是照搬提示词密度。
