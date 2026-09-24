# 第二轮视觉筛查：25 篇

筛查标准是**实际方法图的构图价值**，不是论文影响力。页码为本地保存 PDF 的物理页码（从 1 开始）。前 12 篇继承并重新核对首轮保存的 PDF、裁图与分析；后 13 篇本轮重新下载、读图注并渲染整页。P = 主视觉参考，D = 深度分析但不列入主参考，S = 仅筛查。所有 P 均有原图与 680 px 预览。

| 论文 | 来源身份 | 实际检查的图 | 决定 | 视觉判断 |
|---|---|---|---|---|
| Tree of Thoughts | NeurIPS 2023 | Fig. 1/p2, Fig. 2/p5 | **P** | 真实树和节点局部展开之间有身份联系；缩小后小字变弱，但几何仍清楚 |
| ExpeL | AAAI 2024，作者保存 PDF | Fig. 1/p3 | **P** | 主过程与索引化的局部机制联系明确，适合跨尺度讲述 |
| Voyager | TMLR 2024，arXiv PDF | Fig. 2/p2 | **P** | 具体代码工件成为多来源输入汇合处，科学对象身份鲜明 |
| RAP | EMNLP 2023 | Fig. 1/p2 | **P** | 机器人、世界模型和树的图形类别清楚，搜索拓扑承担论点 |
| Octo | RSS 2024 | Fig. 1/p1 | **P** | 中央可识别科学对象把不同任务输入/动作输出统一起来；图标服务于方法 |
| VIMA | ICML 2023 | Fig. 1/p2 | **P** | 图像序列直接表达状态变化，文字负担较轻 |
| VAR | NeurIPS 2024，官方 Best Paper | Fig. 2/p2 | **P** | 相同视觉对象在尺度上递进，状态演化可一眼读出 |
| Graph of Thoughts | AAAI 2024，arXiv PDF | Figs. 1–2/p3 | D | 运算与图结构直接结合；原图细节密度高，主参考优先 ToT |
| Agent Lightning | 2025 arXiv 预印本 | Figs. 1–4/p2,6,8,9 | D | 对齐状态槽位及训练痕迹有价值；不借泛化多 Agent 训练语义 |
| AutoGen | COLM 2024，arXiv PDF | Fig. 1/p1 | D | 重复的微型角色图标有辨识力，但整体拼贴与小字不适合主模板 |
| OpenVLA | CoRL 2024，arXiv PDF | Fig. 1/p1 | D | 真实任务照片与策略对象的区分值得学习，图标风格混用需警惕 |
| A-Mem | NeurIPS 2025 | Fig. 2/p4 | S | 同一 note 母题贯穿存储/演化；此前已有详细分析，第二轮视觉增益较低 |
| Agent Workflow Memory | ICML 2025 | Figs. 2–3/p3 | S | 轨迹到 workflow 的抽象可借鉴，但仍较像模块流程图 |
| ACE | ICLR 2026 | Fig. 4/p5 | S | 回线明确返回被更新的 playbook；GitHarness 的训练回线可参照 |
| Reflexion | NeurIPS 2023 | Fig. 2/p4 | S | 反馈回同一 Actor；整体盒式工程感较强 |
| LATS | ICML 2024 | Fig. 2/p5 | S | 同一树节点的操作分镜清楚；非一张统一主对象图 |
| DS-Agent | ICML 2024 | Fig. 3/p4 | S | 同一案例的选择/复用身份清楚；检索排序图不等于需求兼容 |
| LoongReflect | 2026 arXiv 预印本 | Fig. 2/p4 | S | 推理树与学习部分分层，视觉较密；不能借教师/恢复前缀语义 |
| AgenticRag-R1 | 2026 arXiv 预印本 | Fig. 2/p4 | S | 多处局部放大连到主线，但纸张尺度小字过多 |
| SWE-agent | NeurIPS 2024 | Fig. 1/p1 | S | 界面截图/文字占主导，科学对象的形态不突出 |
| Generative Agents | UIST 2023，作者 PDF | Fig. 5/p8 | S | 记忆流机制重要，方法图本身是黑白方框图 |
| Self-Refine | NeurIPS 2023 | Fig. 1/p2 | S | 清楚但只有简单三步回路，不足以解决 GitHarness 的复杂构图 |
| Diffusion Policy | RSS 2023 | Fig. 3/p3 | S | 观测、动作和模型内部结合；小字号和层级密度偏工程架构 |
| SayCan | CoRL 2022 | Fig. 2/p4 | S | 动作打分很具体，但论文宽度下微字/图标读不清 |
| RT-2 | CoRL 2023 | Fig. 1/p2 | S | 真实任务和 token/模型的拼接有信息，但不是本轮需要的原创组织方式 |

**质量门槛。** 11 篇进入第二轮深度分析，7 篇成为主参考；未用弱图凑数。VAR 的奖项仅依据 [NeurIPS 官方奖项公告](https://blog.neurips.cc/2024/12/10/announcing-the-neurips-2024-best-paper-awards/)；其他论文不做奖项声明。完整来源、版本回退和 SHA256 见 `new_candidate_sources.json` 与首轮 `../..` 下的 `01_papers/*_source.json`。
