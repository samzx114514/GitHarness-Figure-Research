# LATS：同一棵树的操作分镜

- **论文**：Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models；ICML 2024。
- **来源**：[正式论文页](https://proceedings.mlr.press/v235/zhou24r.html)、[PDF](../01_papers/lats.pdf)。正式会议页已核验。
- **核验**：Verified。主看 Figure 2，PDF 第 5 页；辅助 Figure 1，第 1 页。已渲染目视检查原图，阅读图注及第 5 页 Selection / Expansion / Evaluation / Simulation / Backpropagation / Reflection 原文。
- **图像**：[Fig.2 高清裁图](../02_figures/lats_fig2_pdfp5.png)、[含图注整页](../02_figures/lats_pdfp5_page.png)、[Fig.1](../02_figures/lats_fig1_pdfp1.png)、[180 mm 阅读预览](../02_figures/lats_fig2_180mm_150dpi.png)。

## A. 第一眼的科学命题

Fig.2 的主角是逐渐长大的搜索树，而不是一个占据中央的 Agent 图标。横向六个操作以序号和空白间距组织；Selection、Expansion、Simulation、Backpropagation 中反复出现同一种 Input 椭圆、状态方块、Output 椭圆。这使读者认出它们是同一科学对象在不同操作下的状态，而不是六套独立系统。粉红活跃节点与灰色备选分支的对照，比配套文字更快地表达选择性探索。

## B. 整体构图

Fig.2 是一条六格分镜，没有六个外框，也没有横向串起全部模块的总管线。各格靠一致的顶部标题、节点尺度和 Input 高度形成整体；第四、第五格的树更深，自然产生视觉重心。它适合讲算法操作顺序，但缺少贯穿六格的唯一可追踪节点，读者仍须认出重复结构。Fig.1 则用小型循环连接环境、Agent、Context、Memory 和 Tree Search，适合作为系统摘要，却不是 GitHarness 应照搬的主要构图。

## C. 机制如何展开

Evaluation 将树中一个状态 S 单独拿出来，展示 S → LM → Value；Reflection 则展开 Output → LM → Reflection，再与状态相加。两者与树分镜交替，避免把树的每个节点都画成复杂模块。值得迁移的是“复杂过程只展开一个代表节点”，而不是把所有机制平均摊开。GitHarness 可只对 v4 → candidate 的边做工作状态放大。

## D. 图与状态

节点的形状承担类型区分，颜色承担活跃性，边承担搜索拓扑。第五格在原有向下树边旁增加细红色向上箭头，表达值向祖先回传；这不是参数梯度训练。图注和正文明确其 backpropagation 更新树节点价值。GitHarness 必须避免复制这一箭头并称作 RL：历史版本的祖先关系、只读 INSPECT、选中 base 和参数更新应有不同线型和终点。

## E. 训练表示

图中没有模型参数训练带。正文说明 LATS 不依赖训练，并通过 LM 评分、环境反馈及反思推进搜索。因此本图只能提供推理状态叙事参考，不能作为 GitHarness 的训练布局依据。其 Evaluation / Reflection 方块也不能直接替换成奖励训练模块。

## F. 密度来源

Fig.2 的密度主要来自树深度、活跃路径和箭头方向；节点只含 S 的下标，文字负担低。颜色不是随模块任意分配，而是反复出现的状态语法。不过六格存在重复 Input 和相似树，占用了一部分空间；GitHarness 只有一次历史 base 选择，没必要重复六次版本图。

## G. 论文尺度

已将裁图按 180 mm 宽、150 dpi 导出并目视检查。六个操作标题、Input / Output 和状态编号都可分辨，细箭头和小 Value 字样较弱。它的可读性来源于少量大节点，不能直接推导加入 Q/W 双槽及四项工作内容后仍可使用同样六格密度。该预览是屏幕尺度检查，未进行纸张打印。

## H. 迁移与边界

**适合**：用灰色保持 v6 及未选历史的存在，用单一强调色追踪 v4 选择及其新枝；只放大新枝；以开放留白替代每步边框。**不适合**：六阶段复制整棵版本树，会再次造成碎片化；粉红/灰的成败搜索树含义也不能直接对应历史版本质量。GitHarness 的 v6 不是失败节点，v4 被选也不意味着其余历史无效。建议采用“一个真实历史图 + 一个边级放大”，而非直接照搬分镜。

**评分（设计判断）**：技术相关性 4/5；视觉借鉴价值 4/5。最值得研究的是 Fig.2 的状态语法一致性及无外框操作分镜。

### 补充：680 px / 180 mm @ 96 dpi 核验

已实际打开[680 px 缩略图](../02_figures/lats_fig2_180mm_96dpi.png)。六格次序、粉色活跃树枝和灰色旁枝仍清楚，Input/Output 与 S 标签可读；操作标题需要仔细看，Value 和下标更弱，反向传播的细红箭头容易忽略。因此可借整体拓扑和重复节点语法，但不能把关键 fork 语义寄托在同样细小的反向箭头上。
