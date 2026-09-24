# VAR — Visual Autoregressive Modeling

**核验。** [NeurIPS 2024 论文记录](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9a24e284b187f662681440ba15c416fb-Abstract-Conference.html)；[官方 Best Paper 公告](https://blog.neurips.cc/2024/12/10/announcing-the-neurips-2024-best-paper-awards/)；[Fig. 2，PDF p2 原图](../03_figure_gallery/var_fig2_pdfp2.png) / [680 px 预览](../03_figure_gallery/var_fig2_680px.png)。图注逐一对照文本 next-token、图像 next-image-token 与作者的 next-scale prediction；本图不是训练总览。

- **第一眼与形状：** 左边两个较小的序列示意作为对照，右边逐渐放大的同一鹦鹉画面压倒性地主导视线。对象身份连续、分辨率阶梯可见，即使读者不读公式也会看到“由粗到细”的科学变化。
- **画法：** 左侧离散 token 与网格真的对应研究对象；右侧堆叠的透明尺度面沿空间深度排列，每层仍是同一图像。变化由**同一形状重复 + 尺度/清晰度变化**承担，而不是每一步独立矩形卡。通用 Transformer 底座作为视觉支持，未与主对象争夺视觉重心。
- **展开与密度：** 对照 A/B 与主方法 C 在同一画面中共享“生成的对象”这一语法。右侧大物体让密集细节集中在科学对象本身；680 px 下大鸟与层级仍清楚，细小底座说明需放大，图注可在正文阅读。
- **GitHarness 应用：** `W4→W_t^0→W̃_t` 可沿同一工件轮廓重复，且在第二/第三位置让 Evaluation 变形、Legacy API 消失；这比三个异形清单更直观。历史图中的 v4 和 v7 也必须保持相同成对节点形态，显示身份与分枝。不可借“逐渐清晰”暗示 GitHarness 是单调优化：v7 可能改需求且不必比 v6 更完整；也不能把 v6 排成 v7 的祖先。
