"""Write candidate-specific source mappings and scientific audits."""
from pathlib import Path

R=Path(__file__).resolve().parent
DATA={
1:dict(name='Branch canopy',thesis='历史图本身是主角：读者先看到 v2 分叉、旧枝 v6 和被选中的 v4，然后沿 v4 的橙色支路追到候选与 v7。',space='真实 DAG 占上半画面；W4 复制与选择性更新紧靠选中边下方。细紫线沿外缘回到同一个 Git Agent。',transfer='[ToT Fig.2](../../02_figures/tree_of_thoughts_fig2_pdfp5.png) 的“从真实树边展开机制”；[RAP Fig.1](../../visual_research_v2/03_figure_gallery/rap_fig1_pdfp2.png) 的拓扑承载论点；[ExpeL Fig.1](../../02_figures/expel_fig1_pdfp3.png) 的宏观对象与局部解释对应。',icons='双半圆蓝/薄荷节点始终表示一对 Q/W；橙色是 v4 选择与候选更新；工作四槽位而非软件卡片。',risk='图与下方工作放大仍有上下两层的痕迹；如果 reviewer 在小图下只看见“上图下表”，应继续加深 v4 边与局部的连贯性。',omission='没有在主路细画域内搜索/代码操作；h_t 只作为语义更新提示，未假装是文件清单。',edge='v4 经 Router 后进入虚线候选边界；候选标记和 W_t^0 在内，v7 独立置于边界右侧。',boundary='旧 W4 四槽位在虚线边界左侧，候选初态及更新态在边界内。',control='橙色 COMMIT 由 Git Agent 到 v4；独立菱形 Router 位于 COMMIT 之后，淡灰 Fresh Solve 只作为未选路由。',failure='灰虚线从临时候选构造段离开，未从 v7 发出。'),
2:dict(name='State metamorphosis',thesis='第一眼看到同一工作产物如何改变：W4 被复制，Evaluation 变为 Evaluation\'，Legacy API 从结果中消失。',space='上沿小型历史图确认祖先关系；中央巨大的工作片三态对齐形成实际科学主对象。Router 在候选边界上方，训练沿画面外缘返回 Git Agent。',transfer='[VIMA Fig.1](../../visual_research_v2/03_figure_gallery/vima_fig1_pdfp2.png) 的同一物体跨状态对齐；[VAR Fig.2](../../visual_research_v2/03_figure_gallery/var_fig2_pdfp2.png) 的重复对象可见变化；[Voyager Fig.2](../../02_figures/voyager_fig2_pdfp2.png) 的中央真实工作产物。',icons='W 状态用四条稳定槽位，不把每个动作做成相同方框。橙色更新和灰色删除与绿色保留空间对位。',risk='历史图缩小后技术重点可能变成“如何改工作”而弱化“为何 v4 最优”；正式版需确认 v4/HEAD 的差异仍能第一眼被看到。',omission='没有展开 INSPECT 每次读取内容的完整轨迹；只有必要的只读线与当前 COMMIT 记录。',edge='v4 经橙色控制线回到独立 Router，再由所选 Reuse & Patch 使 W4 发生 fork；绿色结果箭头提交 v7。',boundary='W4 在候选边界外且保留完整 Legacy API；W_t^0 和 W~_t 在内。',control='Router 是 Git Agent 输出 COMMIT 后的单独菱形；Fresh 是淡灰空状态替代路由。',failure='灰虚线从更新后的候选片段离开，表达仅丢弃候选。'),
3:dict(name='Requirement field',thesis='已解析的 Q_t 像一个可视焦点作用于唯一历史图：在没有完全匹配的条件下，v4 被判为兼容基点。',space='淡蓝需求场与真实 DAG 同位；Git Agent 在左侧，v4 下方接 Router，候选局部在右下，紫色学习信号留在左下。',transfer='[ExpeL Fig.1](../../02_figures/expel_fig1_pdfp3.png) 的主图/局部解释关联；[ToT Fig.2](../../02_figures/tree_of_thoughts_fig2_pdfp5.png) 的真实树位置锚定；[GoT Fig.2](../../visual_research_v2/03_figure_gallery/graph_of_thoughts_fig2_pdfp3.png) 的图就是运算对象。',icons='蓝色椭圆仅指“在 Q_t 下解释历史”的可视范围，不代表把任何历史节点原地写成 Q_t。',risk='需求场容易被误读成几何相似度检索。图中“compatible”须保持清楚；不能让椭圆区域暗示历史 checkpoint 可改。',omission='省略对其他历史版本逐一打分的表格，因为论文语义是 Git Agent 判断兼容性，而不是固定相似度矩阵。',edge='唯一 DAG 内有旧枝 v6 和选中的 v4；v4→Router→候选的橙路，结果绿色进入边界外 v7。',boundary='历史 W4 位于候选边界左侧；内部仅 W_t^0、Task-Native Update、W~_t。',control='蓝场说明 Q_t；Git Agent 橙色 COMMIT 选 v4；独立 Router 在历史图之后、候选之前。',failure='灰虚线从 W~_t 区域而非 v7 离开。'),
4:dict(name='Field-notebook scene',thesis='一个有身份的 Git Agent 角色读取历史“标本”，再让隔离的候选副本在工作场中改变。',space='克制插画角色在左中；唯一历史分枝沿其右上方铺开；可恢复 W4 像单张折角标本，右侧淡色椭圆是候选实验区。',transfer='[Octo Fig.1](../../visual_research_v2/03_figure_gallery/octo_fig1_pdfp1.png) 的中心对象与轻插画识别；[RAP Fig.1](../../visual_research_v2/03_figure_gallery/rap_fig1_pdfp2.png) 的角色/状态/行动不同形态；[Voyager Fig.2](../../02_figures/voyager_fig2_pdfp2.png) 的具体工作对象。',icons='角色外形、折角 W4 标本和椭圆候选均为原创。角色只赋予 Git Agent；Router 仍是菱形，执行者是工具圆符号，版本仍为科学节点。',risk='插画稍大时可能喧宾夺主；需要与师兄讨论小角色是帮助快速定位训练对象，还是削弱版本拓扑的严肃感。',omission='纸张/标本只是工作状态的视觉隐喻，不声称实际存储在纸张或 notebook。',edge='v4 的橙线向下抵达候选边界外 Router；结果绿色提交 v7，v6 仍保持旧枝 HEAD。',boundary='折角历史 W4 完整地在椭圆外；椭圆内只有复制出的工作与更新。',control='Git Agent 到 v4 是 COMMIT；Router 独立在候选外；Fresh 仅淡化备选。',failure='灰虚线从候选结果片段向边界外散去，和内部 Legacy API 排除不是同一路。'),
5:dict(name='Policy orbit',thesis='同一个 Git Agent 是需求解释、历史选择和唯一参数训练目标，所有主要对象围绕它定位。',space='中央淡紫策略轨道连接上方反馈、左侧历史、右侧 Router/候选，下部优势奖励回到同一策略。没有三层横排面板。',transfer='[RAP Fig.1](../../visual_research_v2/03_figure_gallery/rap_fig1_pdfp2.png) 的角色与真实树类别分离；[AgenticRAG-R1 Fig.2](../../02_figures/agenticrag_r1_fig2_pdfp4.png) 的主过程附着多处局部机制；[ACE Fig.4](../../02_figures/ace_fig4_pdfp5.png) 的反馈确切落在原对象。',icons='紫圆环只表达训练影响同一策略，不暗示每轮执行都会再次训练；左侧成对版本图仍真实可分枝。',risk='中心策略太大可能让版本恢复创新退到配角；紫轨道也容易被看作在线 self-reflection，需靠 Harness RL / GRPO 文案区分参数训练。',omission='没把 reward 求值器画成可训练模型；只有归一化的 outcome/tracking 优势进入 GRPO。',edge='v4→历史 W4 fork→右侧候选→绿色结果提交 v7；v6 仍在左侧上枝。',boundary='W4 在右侧淡绿椭圆外，W_t^0/W~_t 在内。',control='Git Agent 橙选 v4；Router 另置于右；其输出只初始化候选。',failure='灰虚线从右侧候选结果离开，不从 v7 离开。'),
6:dict(name='Paired-version loom',thesis='版本的 Q/W 成对绑定成为第一视觉对象：纵向历史织出旧枝 v6 和从 v4 开始的新枝 v7。',space='大型竖直版图占左中，节点用上蓝 Q / 下薄荷 W 与中间扣点锁成一件；从 v4 水平引出候选构造。',transfer='[ToT Fig.2](../../02_figures/tree_of_thoughts_fig2_pdfp5.png) 的真实分枝；[A-Mem Fig.2](../../02_figures/amem_fig2_pdfp4.png) 的状态母题跨位置保持身份；[VAR Fig.2](../../visual_research_v2/03_figure_gallery/var_fig2_pdfp2.png) 的同一对象重复变形。',icons='竖直 Q/W 双层节点始终有共同外轮廓；它不是两个可独立提交的版本图。临时候选只用单个 work 状态，不画新的 Q~。',risk='竖向旧枝与右向新枝让 v6 看起来在画面下方，评审可能误以为时间位置决定 HEAD；HEAD 标签和 v4 选中标记必须保留。',omission='主图上只用一个候选圆标记表示宏观分枝，详细 W_t^0 / W~_t 在同一虚线边界中展开。',edge='v2 分为左下 v3→v5→v6 与右侧 v4；v4→独立 Router→边界内候选→边界外 v7。',boundary='虚线边界同时覆盖主图中的 candidate 标记与下方执行细节；旧 W4 在边界左侧，v7 在右侧外。',control='橙色 COMMIT 从 Git Agent 抵达 v4；Router 在其后，Fresh 未激活。',failure='候选宏观节点发出灰虚线 discard 分支，未以 v7 为失败起点。')
}

AUDIT_HEAD='''# Technical audit — {name}

审查对象：[SVG](figure.svg) / [高分辨率图](figure.png) / [180 mm 预览](paper_width_preview.png)。这是视觉探索候选，技术内容遵循用户提供的**论文定义**。

| 科学约束 | 本图的可见证据 |
|---|---|
| 每个提交版本为 `V_i=(Q_i,W_i)`，历史可恢复、可分枝 | 所有 v0–v6 节点均在同一图中绑定蓝 Q 与薄荷 W；v2 分叉，一枝保留 v6（Previous HEAD），另一枝通向 v4。 |
| `q_t` 与 `Q_t` 有别 | 反馈明确写“+ evaluation metrics / − legacy API”；Git Agent 结合只读历史解析完整 `Q_t`，COMMIT 记录含 `Q_t`。 |
| INSPECT / REUSE / COMMIT | 细灰 INSPECT 是只读；淡灰 REUSE 是未触发的精确匹配旁路（本例无匹配）；橙色 COMMIT 是唯一激活主路。REUSE 若触发直接返回旧版本，不经过 Router、Update Agent 或新提交。 |
| COMMIT 决策记录 | 图上标记 `(Q_t,b_t=v4,h_t)` 或等价短写；`h_t` 是语义提示，**并非**预定的文件改动清单。 |
| Router 独立且只在 COMMIT 后 | {control} |
| 路由与候选执行 | Active 是 Reuse & Patch（从 W4 fork）；Fresh Solve 从空状态初始化但本例未选；Task-Native Update/Domain Harness 完成实际工作。 |
| 历史不可变，候选隔离 | {boundary} |
| 工作状态改变 | Core Logic、Utilities 保留；Evaluation→Evaluation' 更新；Legacy API 仅在更新后的候选中排除。图内的灰色“excluded”与失败丢整个候选是不同标记。 |
| 提交与失败 | {edge} {failure} |
| 训练对象与信号 | Final Outcome 与 Query Tracking（Requirement Fidelity、Base Optimality、Staleness Exclusion）各自产生归一化 advantage，经 interface-level Harness RL / GRPO 只回到**同一 Git Agent**；Router、Update Agent、Domain Harness 冻结。提交 v7 的绿色路径与紫色策略学习路径分开。 |

**本候选仍需观察的视觉风险：** {risk}
'''

for n,d in DATA.items():
    folder=R/f'candidate_{n:02d}'
    rationale=f'''# {n:02d} · {d['name']}

**科学视觉命题。** {d['thesis']}

**空间组织。** {d['space']}

**已核验论文图的迁移。** {d['transfer']} 这里只借主对象比例、状态对齐、边级展开或角色区分的原则；不照描源图的角色、配色组合与完整结构。

**图形语言。** {d['icons']}

**技术连线。** {d['edge']} {d['boundary']} {d['control']}

**纸宽检验与取舍。** [1063 px 预览](paper_width_preview.png)对应约 180 mm/150 dpi 的屏幕模拟；主要拓扑与工作变化可在缩小后看到，微型字段需要二次阅读。{d['risk']} {d['omission']}
'''
    folder.joinpath('design_rationale.md').write_text(rationale,encoding='utf-8')
    folder.joinpath('technical_audit.md').write_text(AUDIT_HEAD.format(**d),encoding='utf-8')
print('Wrote rationale and audit for six figures')
