# 跨论文构图比较

评分是针对GitHarness的设计判断，1低、5高。**技术相关性≠视觉借鉴价值**；“5”不是整图可照搬。A树/分支；B记忆/复用；C增量状态；D训练与推理；E高密度框架。页码指保存PDF的物理页。所有列出的图均Verified，会议身份与特定用户参考图身份另列边界。

| 论文／发表 | 覆盖 | 主图／PDF页 | 技术 | 视觉 | 最值得迁移的组织方式 | 最需避免的误迁移 |
|---|---|---|---:|---:|---|---|
| [LATS](03_analysis/lats.md) · ICML24 | A,E | 2 / 5；辅1 / 1 | 4 | 4 | 同一节点语法、开放式操作分镜 | 六次复制整图；把树值回传当参数训练 |
| [ToT](03_analysis/tree_of_thoughts.md) · NeurIPS23 | A,E | 2 / 5；辅1 / 2 | 4 | 5 | 真实树上的取景框→局部机制 | thought代替(Q,W)；历史节点永久红绿好坏 |
| [A-Mem](03_analysis/amem.md) · NeurIPS25 | B,C | 2 / 4 | 4 | 3 | 同一note跨集合/局部保持形态 | 四列碎片化；原地修改历史 |
| [AWM](03_analysis/awm.md) · ICML25 | B,C,E | 2、3 / 3 | 4 | 4 | 唯一共享对象与具体→抽象对应 | Memory云代替DAG；归纳当RL |
| [ACE](03_analysis/ace.md) · ICLR26 | B,C | 4 / 5 | 4 | 5 | 短主线、产物节点、精确回路终点 | Playbook原地更新；三个Agent等权 |
| [ExpeL](03_analysis/expel.md) · AAAI24 | B,E | 1 / 3，作者38页版 | 4 | 5 | 主图+A/B展开，有地址的机制解释 | Training阶段当权重训练；经验池替代历史 |
| [Reflexion](03_analysis/reflexion.md) · NeurIPS23 | B | 2 / 4 | 3 | 3 | 反馈返回同一Actor | verbal RL当参数GRPO；整套工程框架 |
| [Voyager](03_analysis/voyager.md) · TMLR24 | B,C,E | 2 / 2 | 4 | 5 | 中央工作对象+两路输入+成功写回 | 技能库当checkpoint；大段代码细字 |
| [DS-Agent](03_analysis/ds_agent.md) · ICML24 | B,C,E | 3 / 4 | 4 | 3 | 同一Case3经历重排、选取、使用 | 排名相似性当需求兼容；数据库/工具图标堆叠 |
| [Agent Lightning](03_analysis/agent_lightning.md) · 2025预印本 | C,D | 2 / 6；辅1/2、3/8、4/9 | 4 | 4 | 固定状态槽位与训练数据对应 | 空槽/无值当排除；让全系统被训练 |
| [LoongReflect](03_analysis/loongreflect.md) · 2026预印本 | A,C,D,E | 2 / 4 | 5 | 4 | 失活枝保留、推理与训练分层 | teacher/快慢通道照搬；恢复前缀代替fork |
| [AgenticRag-R1](03_analysis/agenticrag_r1.md) · 2026预印本 | C,D,E | 2 / 4 | 4 | 5 | 主线节点对应局部展开、状态色贯穿 | 栈pop当删历史；mask与拒绝机制照搬 |

## 构图维度横向对照

| 论文 | 主视觉对象 | 主要空间关系 | 局部展开方式 | 训练占比/性质 | 680px缩小表现 |
|---|---|---|---|---|---|
| LATS | 搜索树 | 六格横向操作分镜 | 一状态抽出评分/反思 | 无参数训练 | 树清楚，细回传箭头弱 |
| ToT | 真实问题树 | 左树右机制 | 两个取景框+引线 | 无参数训练 | 宏观极清楚，完整提示句偏小 |
| A-Mem | Note/记忆集合 | 四竖区，多方向流 | 集合到局部note | 无RL带 | 主标题清楚，细链/属性负担大 |
| AWM | Memory与轨迹 | 绕同一Agent/Memory | 具体轨迹对抽象workflow | 无参数训练 | 原图单栏；放通栏仍有代码负担 |
| ACE | Playbook/增量项 | 一条主线+长回线 | 小型局部迭代环 | 上下文适应 | 关键对象/回路清楚 |
| ExpeL | Experience→Insight | 左主图，右上下A/B | 字母索引对应 | 经验“training”，非参数 | 宏微主从清楚，B细动作小 |
| Reflexion | Actor与两类记忆 | 左流程右伪代码 | 旁置算法说明 | 语言反馈，非参数 | 标签可读，伪代码抢注意力 |
| Voyager | 中央代码/新技能 | 无大外框三域 | 代码中技能引用 | 程序学习，非参数 | 三域清楚，代码需放大 |
| DS-Agent | Case重排与计划 | 大Development+小Deployment | 排序前后、内部执行环 | 任务模型训练，非Git Agent RL | 大阶段清楚，小图标文字拥挤 |
| Agent Lightning | 状态槽/调用记录 | 左时间向下，右数据向右 | 槽位变化与括号汇聚 | Fig2右侧训练数据；另图RL | 固定槽位清楚，元组较小 |
| LoongReflect | 可逆轨迹树/策略 | 上推理下训练 | 双通道+控制器 | 训练接近一半高度 | 宏观清楚，训练细节难读 |
| AgenticRag-R1 | 动作/栈/轨迹 | 上主线，下/右三展开 | 淡色楔形、重复状态色 | 全图训练方法 | 区域强，示例句/公式过密 |

训练面积是对已核验截图的近似视觉判断，不是像素精确统计。完整纸面讨论和语义核对见逐篇报告。

## 优先级建议

**第一组，直接研究组织原则：** ToT Fig2、ExpeL Fig1、Voyager Fig2、ACE Fig4。

**第二组，解决具体机制表达：** Agent Lightning Fig2（状态差分）、AgenticRag-R1 Fig2（主线→展开）、LoongReflect Fig2（推理/训练及失活历史）。

**第三组，局部借鉴和反例：** A-Mem、Reflexion、DS-Agent。它们技术相关，但整图风格容易重新引入多模块、装饰图标与小字。LATS和AWM适合研究一致对象语法及共享闭环，无需复制全部布局。

## 图号与版本风险

- [来源JSON](01_papers/)是复核入口，每张图保留原始PDF和整页证据。
- LoongReflect与AgenticRag-R1原论文图已验证，但与用户提到的具体参考附件的同一性未确认。
- 同论文不同版本图号/页码可能变动。本报告只对本地保存版本的对应关系负责。
- 未取得独立v5.2文件；不把当前Codex版本的缺陷无依据推广到那一版。
