# OpenVLA — real-task evidence versus policy abstraction

**核验。** [CoRL 2024 正式目录](https://mlanthology.org/corl/2024/kim2024corl-openvla/)；OpenReview PDF 端点拒绝访问，改用[arXiv 作者 PDF](https://arxiv.org/pdf/2406.09246)；本地版 [Fig. 1/PDF p1](../03_figure_gallery/openvla_fig1_pdfp1.png)、[680 px 预览](../03_figure_gallery/openvla_fig1_680px.png)。图注把可训练视觉语言动作模型与机器人部署图像放在同一方法背景中。

真实机器人照片先说明任务实体，视觉输入/语言/动作 token 再对应模型抽象；颜色和图像纹理区分“环境证据”和“模型对象”。它的弱处是图标与照片、模型模块混用，主体并不十分统一，纸宽预览中小模型字难读。GitHarness 无需机器人照片，但可借两级对象的区分：历史 checkpoint 用稳定的抽象“工作片”，候选执行展示可观察的局部变换。不能用照片式拼贴填补方法图留白，也不能把 Git Agent 当作具象机器人执行工具任务。
