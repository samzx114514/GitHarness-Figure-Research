"""Build a local, side-by-side gallery from figures actually cropped from saved PDFs."""
from pathlib import Path
import html, json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '03_figure_gallery'
new = json.loads((OUT / 'new_figure_records.json').read_text(encoding='utf-8'))
by_key = {(x['slug'], x['figure']): x for x in new}

items = [
    dict(slug='tree_of_thoughts', title='Tree of Thoughts: Deliberate Problem Solving with Large Language Models', venue='NeurIPS 2023', fig=2, page=5, primary=True, image='../../02_figures/tree_of_thoughts_fig2_pdfp5.png', preview='../../02_figures/tree_of_thoughts_fig2_180mm_96dpi.png', record='https://proceedings.neurips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html', pdf='https://proceedings.neurips.cc/paper_files/paper/2023/file/271db9922b8d1f4dd7aaef84ed5ac703-Paper-Conference.pdf', lesson='A real tree node anchors a local operation enlargement.'),
    dict(slug='expel', title='ExpeL: LLM Agents Are Experiential Learners', venue='AAAI 2024', fig=1, page=3, primary=True, image='../../02_figures/expel_fig1_pdfp3.png', preview='../../02_figures/expel_fig1_180mm96dpi.png', record='https://ojs.aaai.org/index.php/AAAI/article/view/29936', pdf='https://yongjinliu.github.io/files/2024-ExpeL_LLM_Agents_Are_Experiential_Learners.pdf', lesson='One macroscopic flow is explained by indexed local details.'),
    dict(slug='voyager', title='Voyager: An Open-Ended Embodied Agent with Large Language Models', venue='TMLR 2024', fig=2, page=2, primary=True, image='../../02_figures/voyager_fig2_pdfp2.png', preview='../../02_figures/voyager_fig2_180mm96dpi.png', record='https://rpl.cs.utexas.edu/publications/2024/03/14/wang-tmlr24-voyager/', pdf='https://arxiv.org/pdf/2305.16291', lesson='A concrete work artifact receives distinct sources of guidance.'),
    dict(slug='rap', fig=1, page=2, primary=True, lesson='One compact agent/world-model pair is linked to an actual search tree.'),
    dict(slug='octo', fig=1, page=1, primary=True, lesson='A single illustrated scientific object binds inputs and outputs.'),
    dict(slug='vima', fig=1, page=2, primary=True, lesson='Real state images carry the transition; labels stay secondary.'),
    dict(slug='var', fig=2, page=2, primary=True, lesson='Repeated state silhouettes make incremental change visible.'),
    dict(slug='graph_of_thoughts', fig=2, page=3, primary=False, lesson='The graph itself encodes operations, with no duplicate abstract graph.'),
    dict(slug='agent_lightning', title='Agent Lightning: Train ANY AI Agents with Reinforcement Learning', venue='arXiv 2025 preprint', fig=2, page=6, primary=False, image='../../02_figures/agent_lightning_fig2_pdfp6.png', preview='../../02_figures/agent_lightning_fig2_pdfp6_180mm.png', record='https://arxiv.org/abs/2508.03680', pdf='https://arxiv.org/pdf/2508.03680v1', lesson='Stable aligned state slots show what changes during a rollout.'),
    dict(slug='autogen', fig=1, page=1, primary=False, lesson='Repeated small agent silhouettes distinguish actor identity, but dense mini-panels fail paper scale.'),
    dict(slug='openvla', fig=1, page=1, primary=False, lesson='Photographs separate real tasks from the internal policy; mixed icon styles are a caution.'),
]
for x in items:
    if 'image' not in x:
        y = by_key[(x['slug'], x['fig'])]
        x.update(title=y['title'],venue=y['venue'],image=y['crop'].split('/')[-1],preview=y['preview'].split('/')[-1],record=y['publication_record'],pdf=y['pdf_url'])

(OUT / 'gallery_records.json').write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')
cards=[]
for x in items:
    esc=lambda s:html.escape(str(s),quote=True)
    cards.append(f'''<article class="card" data-tier="{'primary' if x['primary'] else 'secondary'}">
      <div class="meta"><span class="tier">{'PRIMARY' if x['primary'] else 'SECONDARY'}</span><span>{esc(x['venue'])} · Fig. {x['fig']} · PDF p{x['page']}</span></div>
      <a href="{esc(x['image'])}" target="_blank"><img src="{esc(x['preview'])}" alt="Actual Figure {x['fig']} from {esc(x['title'])}" loading="lazy"></a>
      <h2>{esc(x['title'])}</h2><p>{esc(x['lesson'])}</p>
      <div class="links"><a href="{esc(x['record'])}">Publication record</a> · <a href="{esc(x['pdf'])}">Source PDF</a> · <a href="{esc(x['image'])}">Full-resolution crop</a></div>
    </article>''')
doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>GitHarness visual reference gallery</title>
<style>body{{font:15px/1.45 system-ui,sans-serif;color:#14233e;background:#f7f9fb;margin:0 auto;max-width:1600px;padding:28px}}h1{{font-size:29px;margin:0}}header p{{max-width:950px;color:#526178}}button{{margin:12px 8px 16px 0;padding:8px 13px;border:1px solid #9aaac1;border-radius:20px;background:white;cursor:pointer}}button.active{{background:#18355a;color:#fff}}.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}}.card{{background:white;border:1px solid #d9e1e8;border-radius:10px;padding:15px;min-width:0}}.card img{{width:100%;height:285px;object-fit:contain;background:white;border:1px solid #edf0f3}}.meta{{display:flex;justify-content:space-between;gap:10px;font-size:12px;color:#566783}}.tier{{font-weight:700;color:#bd6330}}h2{{font-size:16px;margin:12px 0 4px}}p{{margin:5px 0 10px}}.links{{font-size:12px}}a{{color:#194b87}}@media(max-width:850px){{.grid{{grid-template-columns:1fr}}}}body.primary-only .card[data-tier=secondary]{{display:none}}</style></head>
<body><header><h1>Actual method figures · visual reference gallery</h1><p>Images are crops from saved original paper PDFs, not generated lookalikes. PDF page means the physical 1-based page of the saved version. Click a picture for its full-resolution crop. At 680 px preview width, fine labels that disappear should not be borrowed at paper scale.</p><button id="all" class="active">All 11 figures</button><button id="primary">7 primary references</button></header><main class="grid">{''.join(cards)}</main><script>const a=document.getElementById('all'),b=document.getElementById('primary');a.onclick=()=>{{document.body.classList.remove('primary-only');a.classList.add('active');b.classList.remove('active')}};b.onclick=()=>{{document.body.classList.add('primary-only');b.classList.add('active');a.classList.remove('active')}};</script></body></html>'''
(OUT / 'index.html').write_text(doc,encoding='utf-8')
print(f'Gallery: {len(items)} figures, {sum(x["primary"] for x in items)} primary')
