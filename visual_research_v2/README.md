# GitHarness Figure 2：第二轮视觉研究

本目录是**论文方法图的绘画语言研究**，不是 GitHarness Figure 2 定稿，也没有开始 PowerPoint 重建。先打开[并排真实图画廊](03_figure_gallery/index.html)，切换“All / 7 primary”，点击原图看高分辨率。再看[三张原创 SVG 研究草图](git_harness_composition_directions.md)和[两种图标风格](iconography_guide.md)。

| 目录/文件 | 内容 |
|---|---|
| `01_screening/` | 25 篇筛查矩阵、A′/D′ 原图诊断、页面索引与下载/裁图脚本 |
| `02_verified_papers/` | 本轮 13 篇原始 PDF 与版本/权利说明 |
| `03_figure_gallery/` | 11 张深度分析图的高分辨率裁图、约 680 px 预览、HTML 并排画廊及可追溯记录 |
| `04_visual_analyses/` | 11 篇逐篇视觉分析：主画面、构图、图标、机制、纸张可读性和迁移边界 |
| `05_iconography_studies/` | 极简/克制插画同语义矢量符号对照 |
| `06_original_compositions/` | 3 张结构不同的原创 SVG+PNG 结构草图与可重绘脚本 |
| [`visual_survey.md`](visual_survey.md) | 跨图综合与主参考选择 |
| [`reference_comparison.md`](reference_comparison.md) | 技术相关性和视觉价值分开的比较表 |
| [`iconography_guide.md`](iconography_guide.md) | 图形语法建议 |
| [`git_harness_composition_directions.md`](git_harness_composition_directions.md) | 三条候选构图的来源映射、风险与语义锁 |

**复核方式。** 每张正式参考的出版记录、图号、保存 PDF 的物理页码、原图裁图与纸宽预览在画廊中配对；第二轮新增图的坐标及 PDF SHA256 在 `03_figure_gallery/new_figure_records.json`。首轮原资料保留在仓库根目录的 `01_papers/`、`02_figures/`、`03_analysis/`、`04_composition_studies/`，未覆盖。对会议身份与 VAR 奖项的官方记录，参见[筛查矩阵](01_screening/screening_matrix.md)和[比较表](reference_comparison.md)。

生成脚本（可选）：`python 03_figure_gallery/render_selected.py` 重新从保存 PDF 裁图；`python 03_figure_gallery/build_gallery.py` 重建并排画廊；`python 06_original_compositions/make_studies.py` 重绘原创 SVG/PNG。系统需 Python、PyMuPDF、Pillow、CairoSVG。图注/正文核对已在每篇分析中记录。所有 SVG 都是开放文本形式，节点、线、标签可编辑。
