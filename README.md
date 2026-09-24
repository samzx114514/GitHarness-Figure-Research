# GitHarness Figure 2 · 方法图视觉调研

**成果：12篇真实论文、18张编号方法/概念图、12份A–H视觉分析、4种原创SVG构图草图。** 原始PDF、整页证据、清晰裁图及来源记录均已保存。没有生成最终Figure2，没有制作PowerPoint，也没有修改上一轮GitHarness图。

## 建议阅读路径

1. 先读[调研报告](survey.md)，了解跨图结论及当前图的根本问题。
2. 用[跨论文比较](comparison.md)区分技术相关与视觉借鉴价值。
3. 打开[原图浏览页](gallery.html)，点击原图放大；页内可切换统一680px预览尺度。来源链接与PDF页码在每张图旁。
4. 阅读[四种原创设计方向](git_harness_design_directions.md)，重点比较A与D；四份SVG均可独立打开/编辑。
5. 对重点来源，核对`03_analysis/`中的分析和`02_figures/`整页截图，必要时回到PDF。

## 目录

```text
figure_research/
├── 01_papers/                 原PDF、全文辅助提取、逐篇source.json
├── 02_figures/                高清裁图、含图注整页、180mm屏幕预览
├── 03_analysis/               12篇中文A–H分析及Skill发现记录
├── 04_composition_studies/    4份SVG、PNG、研究草图生成/渲染文件
├── README.md
├── survey.md
├── comparison.md
├── git_harness_design_directions.md
├── gallery.html              离线原图浏览入口
├── manifest.json             统一来源与图页索引
└── validation.json           文件、页码、图号、链接与草图检查记录
```

## 文件命名与核验含义

`<paper>_figN_pdfpP.png`表示原论文Figure N，保存PDF的第P页（从1开始）。`full/page`是完整页；`180mm/96dpi`是纸面阅读代理；部分来源另有150dpi预览。裁图可能包含图注，完整页始终保留以核对上下文。

**Verified**表示：原论文可取得；图像已渲染并实际查看；图号/页码、图注和邻近方法已核对。它不代表期刊会议录用，也不代表图的每一细节都值得借鉴。LoongReflect、AgenticRag-R1与Agent Lightning按预印本记录；其他venue有对应主源。用户所称LongReflect/AgenticRAG-R1参考附件未出现在本轮附件中，具体图片身份仍未确认。

统一680px宽约对应180mm@96dpi，仅用于屏幕横向比较，不能代替最终论文版芯和实际打印测试。部分原图原本是单栏，本报告不会把放大到通栏后的效果当成其原印刷效果。

## 原创草图

- [A：版本图作为主体](04_composition_studies/A_graph_scaffold.svg)
- [B：Q/W双层对应](04_composition_studies/B_paired_lanes.svg)
- [C：唯一策略闭环](04_composition_studies/C_shared_policy.svg)
- [D：中央工作变换](04_composition_studies/D_central_transformation.svg)

草图只验证空间组织与阅读顺序，有意简化可选路径与训练细项；完整语义约束及必须补回的内容在设计方向文件中。PNG供快速比较，SVG为可渲染矢量源。不是可直接提交论文的最终排版。

## 来源与使用边界

原图版权归论文作者/出版方；保存在此供研究核验。公开论文最终图应使用GitHarness原创绘制，不应拼贴这些原图、独特图标或完整视觉设计。逐篇source.json和manifest.json保留官方/作者来源链接、实际PDF URL、SHA256和裁框。

本报告是有目的的视觉样本调研，不是穷尽性文献综述。评分是设计判断，不是算法能力、论文质量或会议等级排名。详细适用Skill与用户优先约束见[Skill记录](03_analysis/00_skills_and_scope.md)。
