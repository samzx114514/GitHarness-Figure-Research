# Agent Workflow Memory — Fig. 2 / Fig. 3 视觉核验

- **论文**：Agent Workflow Memory；最终发表 **ICML 2025**，PMLR 267:63897–63911。检索可遇到 ICLR 2025 匿名投稿旧版，不能以它标注最终会议。
- **原文**：[PMLR 会议页](https://proceedings.mlr.press/v267/wang25bx.html) · [会议页所链接 PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bx/wang25bx.pdf)。
- **核验对象**：Figure 2 与 Figure 3 均在 PDF 第 3 页（正文页码 3）；读图注及 §2.3。状态 **Verified**。
- **材料**：[Fig. 2](../02_figures/awm_fig2_pdfp3.png) · [Fig. 3](../02_figures/awm_fig3_pdfp3.png) · [含图注整页](../02_figures/awm_pdfp3_full.png) · [Fig. 2 通栏等效](../02_figures/awm_fig2_pdfp3_180mm.png) · [Fig. 3 通栏等效](../02_figures/awm_fig3_pdfp3_180mm.png)。
- **主观评分**：技术相关性 4/5；视觉借鉴价值 4/5。

## A. Main visual thesis

Fig. 2 第一眼看到蓝色椭圆中的环境与 Agent，以及被特别放大的粉色 Memory 云。它把“经验回到记忆后帮助下一次行动”作为中心对象关系。Fig. 3 则在左右对照中把“先归纳后应用”和“持续归纳再应用”的不同节奏可视化；两图各自的中心都是可复用 workflow。

## B. Global composition

Fig. 2 不是等宽横向方框链：上半部是共享 Agent/Environment 场域，下方是行动轨迹，右下是成功筛选，右上是归纳出的 workflow，再向左回到原 Memory。空间绕行形成一圈，重复访问同一对象使闭环完整。Fig. 3 通过左侧两叠样本和右侧流式条目构成两种时间组织；中间均为工作流记忆。薄弱点是流程还依赖 Step 1/2/3 标题和大块文本，不应原样照搬到 GitHarness。

## C. Mechanism expansion

Fig. 2 将一次具体查询“Who ordered order #0130?”接到环境，把具体轨迹放在下方，再把归纳结果放到右侧。两个文本区域不是任意模块，而是一对“具体轨迹→抽象工作流”的实例展开：例如实例订单号变为占位符。局部机制围绕共享 Agent，而没有再画第二套抽象框架。可迁移的是主对象周围的解释环绕，而不是其代码密集例子。

## D. Graph and state representation

此图没有历史版本 DAG。箭头表示动作、观察、评估、归纳和写入，粉色 Memory 是经验集合；Fig. 3 右边变大的记忆云和多条重复箭头表示积累。拓扑的科学含义是反馈循环和时间重复，不是父版本和后继版本。因此 GitHarness 可以学“回到同一对象”的闭环，但必须用真正的版本节点、祖先边和 v4→v7 分支来表达可恢复历史，不能画一个不断膨胀的 Memory 云替代版本图。

## E. Training representation

Fig. 3 左侧把 Training 加引号，附近方法说明是离线诱导 workflow 后在推理中调用，并非参数更新。Fig. 2 的 YES/NO 也在控制是否保存经验。它可启发训练/推理之间不重复画 Agent，却不能提供 GRPO 梯度语义。GitHarness 的 RL 支路应专门标明只更新 Git Agent，不能将执行成功后写版本和策略训练混为一个回路。

## F. Visual density

Fig. 2 信息主要来自例子的具体/抽象对照、成功门和回写线，但具体代码占据大约半图，标题色条加上云、椭圆和粗浅色箭头造成多种视觉语言并存。Fig. 3 更依赖空间节奏：左侧批量样本、右侧逐条样本，箭头次数直接表达离线/在线区别。后者是适合迁移的无长句密度。

## G. Paper-scale readability

实际查看了 680 px 宽的两图。Fig. 2 放至通栏时主标签和轨迹大多可读，原论文却为单栏使用，整页图显示细代码负担明显；不能把放大后的清晰误称为原印刷尺寸清晰。Fig. 3 在 680 px 下结构与关键动词可读，灰色细标题较弱，图标比文字更显眼。GitHarness 通栏图应保留这样的宏观节奏，避免依赖小字号代码或图标含义。

## H. Transfer to GitHarness

**迁移**：将 Git Agent 作为全图唯一策略实体；历史选择、执行结果和训练反馈都有精确落点。W4 的局部展开围绕主版本图安排，通过细引线说明它属于哪一节点。让提交门作为一个明确判定位置，主成功箭头继续到 v7。

**不迁移**：不断增长的记忆云、将所有成功经验无差别加入上下文、参数无关归纳被命名为训练。GitHarness 还须区分两种灰色语义：局部排除 Legacy API 是候选构造，失败丢弃是候选生命周期终止，不能像原图 NO/pass 那样用一个出口含混代表两者。

**一句构图启发**：回路必须回到同一个、占视觉中心的科学对象；循环形状本身不保证技术语义一致。
