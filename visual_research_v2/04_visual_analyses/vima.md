# VIMA — Robot Manipulation with Multimodal Prompts

**核验。** [ICML 2023 正式记录](https://proceedings.mlr.press/v202/jiang23b.html)；[正式 PDF](https://proceedings.mlr.press/v202/jiang23b/jiang23b.pdf)；[Fig. 1，PDF p2 原图](../03_figure_gallery/vima_fig1_pdfp2.png) / [680 px 预览](../03_figure_gallery/vima_fig1_680px.png)。邻近正文说明四类 multimodal prompts；右侧是这些任务的视觉执行示例。图中的 token 小格确实是 text/object/padding token，不是装饰。

- **第一眼与构图：** 左侧四种不同颜色的提示类型经中央 VIMA 汇入右侧四排机器人动作图。右侧真实状态序列面积最大，贡献是“同一策略处理不同视觉目标”，并非四个软件模块。中央小模型节点起到汇合点作用。
- **图标：** 左侧照片表示视觉 goal，抽象方块/token 表示提示序列，小物体贴图表示对象概念；右侧三帧一行真实展现状态变化。物体的轮廓与颜色在提示和动作例子之间持续出现，读者可追踪“同一个东西”。箭头以四种淡色对应四类提示，颜色是实例索引，不是任意装饰。
- **局部机制：** 每行左边微型输入与右边结果在水平线上对应，中央策略只画一次。图像序列替代长段“动作使物体由 A 到 B”的解释。680 px 下任务名称尚可读，细小 token 标签较弱；但图像动作关系仍清楚。
- **GitHarness 应用：** 选择 `v4` 之后，在 `W4 / W_t^0 / W̃_t` 使用**同一组对齐槽位**，让 Core Logic、Evaluation、Legacy API、Utilities 的身份持续；用颜色和轮廓标识保留、更新、排除。重要差异是 GitHarness 的 `W` 是可恢复工作 checkpoint，不是照片帧；应画抽象工作片段而非复制 VIMA 的机器人截图。也不应画“token 小方格”去装饰需求，除非真实 token 序列本身是论文贡献。
