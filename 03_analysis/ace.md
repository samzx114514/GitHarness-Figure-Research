# ACE — Fig. 4 视觉核验

- **论文**：Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models；**ICLR 2026**。
- **会议核实**：[ICLR 官方展示页](https://iclr.cc/virtual/2026/poster/10008343)。使用[作者 arXiv PDF](https://arxiv.org/pdf/2510.04618)，页眉为 Published as a conference paper at ICLR 2026；本地保存实际下载版本，未把作者博客单独作为录用证明。
- **核验对象**：Figure 4，PDF 第 5 页（正文页码 5）；读图注、第 4 页 §3 与第 5 页 §3.1–3.2。状态 **Verified**。
- **材料**：[裁图](../02_figures/ace_fig4_pdfp5.png) · [含图注整页](../02_figures/ace_pdfp5_full.png) · [180 mm 屏幕等效](../02_figures/ace_fig4_pdfp5_180mm.png)。
- **主观评分**：技术相关性 4/5；视觉借鉴价值 5/5。

## A. Main visual thesis

最先可见的是三个圆形角色沿一条水平主线排列，底下一条长回线返回左侧 Context Playbook。核心视觉命题是“执行产生材料，反思提炼材料，整理后改进供下次执行使用的上下文”。纸张堆与角色圆形明显区分对象与处理者，几乎不需要解释句即可读懂数据从哪里来、回到哪里。

## B. Global composition

整体可以读成一个宽扁闭环：上方前进主线、下方状态回写。没有三个大边框把角色割开，也没有单独画“输入区/输出区/反馈区”。左侧 Query 与 Playbook 从不同高度进入 Generator；Trajectory 和 Insights 各处于角色间隙；Curator 的回线终点准确到 Playbook。Reflector 上方一个短虚线回环表现局部迭代，在尺度上从属于全局长回环，主次很清楚。

## C. Mechanism expansion

局部展开被限制为 Reflector 上方的小回环，没有抢占整片区域。Delta Context Items 放在底部长线上，说明回写的是增量对象，而不是整套生成轨迹。主线角色和中间产物采用两类简单形状，机制细节依靠“什么对象在什么边上流动”展开。附近正文补充增量项的合并由轻量确定性逻辑完成；图不单独展开这层实现，保持了概念尺度一致。

## D. Graph and state representation

图中没有历史树，也没有旧状态/新状态并排对照。一个 Playbook 被持续回写，虚线还把它连到 Curator，表达多角色共同使用同一上下文。纸张叠影暗示多项内容，但不等于可恢复版本或祖先关系。因此本图的最大启发是“唯一共享状态对象”，不是其线性时间结构。GitHarness 应让真实版本图占据共享对象的位置，并在 v4 上发生选取和分支，不能缩成单份 Playbook。

## E. Training representation

没有奖励、梯度或权重训练；Iterative Refinement 是反思文本迭代，底层长回路是上下文适应。不能把同形回箭头直接重新命名为 GRPO 而保留落点到历史图。GitHarness 的训练支路必须以紫色独立编码，明确终止于同一个 Git Agent；工作状态的新版本提交则终止于版本图。这两个回路共享构图语言但不能共享终点。

## F. Visual density

高密度来自水平排列、角色/产物形状对照和长短两级回线，而不是文字或容器数量。标签均很短，黑白近单色使箭头与节点关系成为主信息。脑图标和叠影有些装饰性，GitHarness 可去掉；值得保留的是底部回路并不附带一排同等重量的模块框。代价是算法内部选择规则几乎未画出；GitHarness 仍需保留兼容 base selection 的解释，不能只做极简角色串联。

## G. Paper-scale readability

已实际查看 680 px 宽版本。三个角色、Trajectory、Insights、Delta Context Items 与回线终点都清楚；小号 Generator/Reflector/Curator 仍可辨识。Playbook 的两行字稍小，但对象不依赖读全小字也能追踪。图的宽扁比例适合通栏，上下空白维持了回线与主线的分离。这种少量稳定对象优于 GitHarness 当前“所有内容等权铺开”的问题。

## H. Transfer to GitHarness

**迁移**：使用一条读者第一眼就能跟随的主路径，角色间放控制记录或状态，而不另建一排 UI 卡片；把训练做成从奖励汇合至唯一 Git Agent 的次级长回线；将候选内的更新作为比全局提交更小的局部机制。

**不迁移**：三个等权 Agent 圆形会歪曲 GitHarness 的策略/冻结执行差异；Playbook 是上下文知识而非工作 checkpoint，且 §3.2 允许原地更新条目；GitHarness 则必须保留 W4 并 fork Wt⁰。也不能用整图回路替代 v7 从 v4 而不是 v6 产生的拓扑。主图仍应以版本演化为主，闭环只组织辅助学习。

**一句构图启发**：把主线上的产物和回线的落点画准确，整体感往往无需更多外框。
