# GitHarness 图形词汇实验

同一套语义分别以[极简科学符号 SVG](05_iconography_studies/minimal_symbols.svg) / [预览](05_iconography_studies/minimal_symbols.png)和[克制插画符号 SVG](05_iconography_studies/illustrated_symbols.svg) / [预览](05_iconography_studies/illustrated_symbols.png)绘出。图形都是本轮原创的可编辑矢量几何；不临摹 RAP 的机器人、Octo 的章鱼/拼图或 AutoGen 的角色。所用对象和配色遵从已阅读的 `drawio-diagram-builder` 关于“每一形状必须有方法语义、同一图标保持线宽/尺度”的规则。

| 科学对象 | 极简形式 | 克制插画形式 | 选择理由与风险 |
|---|---|---|---|
| Git Agent | 紫色外环内的抽象策略面孔 | 低细节、单色描边的小角色，只有眼/嘴/一点橙色信号 | 角色仅标识**被训练的策略**；若漫画表情过强，会把研究图带向 mascot 风格。训练箭头只能回到这一个标记 |
| Paired Version | 一个圆轮廓，左淡蓝 Q，右薄荷 W，接缝清楚 | **保持同一极简形式** | 版本是不可拆的 `V_i=(Q_i,W_i)`；不应为了插画趣味把 Q/W 画成两件漂浮物 |
| INSPECT / select | 轻灰读线 + 小放大镜；橙色选中边 | 同左 | 放大镜只代表可选读操作，不替代 Git Agent 的推理；橙色必须指向真实 v4 |
| Fork | 旧工作片穿过隔离边界，形成对齐的副本 | 同左，可略增纸片层叠轮廓 | 旧 W4 位于边界外，`W_t^0` 在边界内；单一分叉箭头不能充分说明复制与隔离 |
| Work artifact | 四条对齐的可恢复工作片段 | 同左 | Core/Evaluation/Legacy API/Utilities 各占稳定槽位；绿色保留、橙色更新、灰色排除 |
| Router / Update Agent | Router 用短决策标记；Update Agent 用工具状标记 | 仍不画成 Git Agent 的同款角色 | 职责不同且二者冻结，不能让相同小机器人暗示共同训练 |
| Training | 较细紫色回线 + reward/GRPO 短标签 | 同左 | 训练是次级信息，但终点必须明确落在**同一个 Git Agent** |

**推荐。** 版本、工作、边界、训练都保持抽象科学符号；只给 Git Agent 试用小型克制插画。这样有辨识度，也不让插画掩盖真实的 v4→v7 拓扑。RAP Fig.1 证明重复角色剪影能建立身份；Octo Fig.1 证明小插画可帮助中心对象被快速识别；AutoGen Fig.1 同时说明重复过多小角色会在纸宽下模糊。[逐图证据](03_figure_gallery/index.html)与[研究分析](04_visual_analyses/)分开保存。

**尺度门槛。** SVG 草图整体按 1200 px 预览；原论文图按 680 px 预览（约 180 mm、96 dpi）核对。最终论文图应以实际版心和字体大小再次印样，不能仅凭屏幕看图。图标至少让轮廓/对象类别在缩小后成立，小字只有二次阅读时才需要。
