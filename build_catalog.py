"""Unify paper records, validate source evidence, and build an offline gallery."""
from pathlib import Path
from html import escape
import hashlib, json, re, xml.etree.ElementTree as ET
import pymupdf

ROOT = Path(__file__).parent
checks, catalog = [], []
def check(ok, msg): checks.append({'passed': bool(ok), 'message': msg})
def first(d, *keys):
    return next((d[k] for k in keys if d.get(k) is not None), None)

for src in sorted((ROOT/'01_papers').glob('*_source.json')):
    d=json.loads(src.read_text(encoding='utf-8'))
    slug=src.name.removesuffix('_source.json')
    pdf_path=ROOT/'01_papers'/f'{slug}.pdf'
    check(pdf_path.is_file(), f'{slug}: PDF exists')
    if not pdf_path.is_file(): continue
    data=pdf_path.read_bytes()
    check(data.startswith(b'%PDF'), f'{slug}: PDF header')
    digest=hashlib.sha256(data).hexdigest()
    check(not d.get('sha256') or d['sha256']==digest, f'{slug}: source SHA256')
    try: pdf=pymupdf.open(pdf_path)
    except Exception as exc:
        check(False,f'{slug}: PDF parse: {exc}');continue
    raw=(d['figures'] if isinstance(d.get('figures'),list) else [d]+d.get('additional_figures',[]))
    figs=[]
    for f in raw:
        n=first(f,'figure','figure_number')
        page=f.get('pdf_page_1based')
        crop=first(f,'crop_pdf_points','crop_coordinates_pdf_points')
        image=first(f,'screenshot','figure_path','image')
        preview=first(f,'paper_scale_screenshot','paper_scale_path','paper_scale_preview_96dpi','paper_scale_preview')
        if not preview and image:
            candidate=Path(image).with_name(Path(image).stem+'_180mm.png').as_posix()
            if (ROOT/candidate).is_file(): preview=candidate
        whole=first(f,'full_page_screenshot','full_page_path','original_page')
        if not whole and isinstance(page,int):
            choices=[f'02_figures/{slug}_pdfp{page}_full.png',f'02_figures/{slug}_pdfp{page}_page.png',f'02_figures/{slug}_page_{page:02}.png']
            whole=next((x for x in choices if (ROOT/x).is_file()),None)
        check(isinstance(page,int) and 1<=page<=len(pdf),f'{slug} Fig.{n}: PDF page in range')
        check(isinstance(n,int) and n>0,f'{slug}: figure number')
        if not isinstance(page,int) or not 1<=page<=len(pdf): continue
        rect=pymupdf.Rect(crop) if crop else pymupdf.Rect()
        check(bool(crop) and not rect.is_empty and pdf[page-1].rect.contains(rect),f'{slug} Fig.{n}: crop bounds')
        for tag,p in [('crop',image),('preview',preview),('whole page',whole)]:
            check(bool(p) and (ROOT/p).is_file(),f'{slug} Fig.{n}: {tag} screenshot')
        text=pdf[page-1].get_text()
        check(bool(re.search(rf'(?:Figure|Fig\.)\s*{n}\b',text,re.I)),f'{slug} Fig.{n}: caption marker')
        figs.append({'number':n,'pdf_page_1based':page,'crop_pdf_points':crop,'screenshot':image,'preview':preview,'whole_page':whole})
    analysis=f'03_analysis/{slug}.md'
    check((ROOT/analysis).is_file(),f'{slug}: A-H analysis exists')
    if (ROOT/analysis).is_file():
        t=(ROOT/analysis).read_text(encoding='utf-8')
        check(all(re.search(rf'^##\s*{x}[.。\s]',t,re.M) for x in 'ABCDEFGH'),f'{slug}: A-H sections')
    check(bool(d.get('source_url') and d.get('pdf_url')),f'{slug}: source URLs')
    catalog.append({'slug':slug,'title':d['title'],'venue':d['venue'],'source_url':d['source_url'],'pdf_url':d['pdf_url'],
                    'local_pdf':f'01_papers/{slug}.pdf','pdf_sha256':digest,'analysis':analysis,'figures':figs,
                    'technical_relevance_1to5':first(d,'technical_relevance','technical_score','technical_relevance_1to5'),
                    'visual_transfer_1to5':first(d,'visual_transfer','visual_score','visual_value','visual_transfer_value_1to5'),
                    'status':d.get('verification_status','Verified: original PDF and figure inspected')})
    pdf.close()

for stem in ('A_graph_scaffold','B_paired_lanes','C_shared_policy','D_central_transformation'):
    svg=ROOT/'04_composition_studies'/f'{stem}.svg'
    png=svg.with_suffix('.png')
    check(svg.is_file() and png.is_file(),f'{stem}: SVG/PNG')
    if svg.is_file():
        try: ET.parse(svg);check(True,f'{stem}: valid SVG')
        except ET.ParseError: check(False,f'{stem}: valid SVG')

check(len(catalog)==12,'12 papers')
check(sum(map(lambda x:len(x['figures']),catalog))>=12,'at least 12 numbered figures')

(ROOT/'manifest.json').write_text(json.dumps({'date':'2026-09-24','papers':catalog},ensure_ascii=False,indent=2),encoding='utf-8')

cards=[]
primary_figures={'agent_lightning':2,'lats':2,'tree_of_thoughts':2}
for p in catalog:
    f=next((x for x in p['figures'] if x['number']==primary_figures.get(p['slug'])),p['figures'][0]);e=escape
    aux=''.join(f'<a href="{e(x["screenshot"])}">Aux Fig. {x["number"]} · PDF p.{x["pdf_page_1based"]}</a>' for x in p['figures'] if x is not f)
    cards.append(f'''<article><div class="figure"><img src="{e(f['preview'] or f['screenshot'])}" data-full="{e(f['screenshot'])}" data-preview="{e(f['preview'] or f['screenshot'])}" alt="Figure {f['number']} from {e(p['title'])}" loading="lazy"></div><div class="detail"><div class="tag">{e(p['venue'])} · Fig. {f['number']} · PDF p.{f['pdf_page_1based']}</div><h2>{e(p['title'])}</h2><p>Technical {p['technical_relevance_1to5']}/5 · Visual {p['visual_transfer_1to5']}/5</p><nav><a href="{e(p['analysis'])}">Visual analysis</a><a href="{e(p['local_pdf'])}">Saved PDF</a><a href="{e(f['screenshot'])}">Clear crop</a><a href="{e(p['source_url'])}">Source ↗</a>{aux}</nav></div></article>''')
template=(ROOT/'gallery_template.html').read_text(encoding='utf-8')
(ROOT/'gallery.html').write_text(template.replace('<!-- CARDS -->','\n'.join(cards)),encoding='utf-8')

for md in ROOT.rglob('*.md'):
    for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',md.read_text(encoding='utf-8')):
        if link.startswith(('http://','https://','#','mailto:')):continue
        target=(md.parent/link.split('#',1)[0]).resolve()
        check(target.exists(),f'{md.relative_to(ROOT)}: link {link}')

(ROOT/'validation.json').write_text(json.dumps({'passed':all(x['passed'] for x in checks),'paper_count':len(catalog),
                                        'figure_count':sum(len(x['figures']) for x in catalog),'checks':checks},ensure_ascii=False,indent=2),encoding='utf-8')

failed=[x['message'] for x in checks if not x['passed']]
print(json.dumps({'papers':len(catalog),'figures':sum(len(x['figures']) for x in catalog),'checks':len(checks),'failed':failed},ensure_ascii=False,indent=2))
if failed: raise SystemExit(1)
