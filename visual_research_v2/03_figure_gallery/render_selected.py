"""Crop verified figures from saved PDFs and make 680px comparison previews."""
from pathlib import Path
import hashlib
import json
import pymupdf
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'03_figure_gallery'
OUT.mkdir(parents=True,exist_ok=True)
SOURCES={x['slug']:x for x in json.loads((ROOT/'01_screening'/'new_candidate_sources.json').read_text(encoding='utf-8'))}
SPECS={
  'graph_of_thoughts':[(1,3,[47,43,564,235]),(2,3,[316,274,566,427])],
  'rap':[(1,2,[98,50,500,276])],
  'octo':[(1,1,[44,202,570,498])],
  'vima':[(1,2,[53,66,548,319])],
  'var':[(2,2,[103,65,510,262])],
  'autogen':[(1,1,[103,291,510,445])],
  'openvla':[(1,1,[98,195,522,416])],
  'diffusion_policy':[(3,3,[39,44,568,205])],
}
records=[]
for slug,figs in SPECS.items():
    pdf_path=ROOT/'02_verified_papers'/f'{slug}.pdf'
    pdf=pymupdf.open(pdf_path)
    source=SOURCES[slug]
    for num,pageno,coords in figs:
        page=pdf[pageno-1]
        rect=pymupdf.Rect(coords)
        if not page.rect.contains(rect):raise ValueError((slug,pageno,coords,page.rect))
        pix=page.get_pixmap(matrix=pymupdf.Matrix(3,3),clip=rect,alpha=False)
        high=OUT/f'{slug}_fig{num}_pdfp{pageno}.png'
        pix.save(high)
        image=Image.open(high).convert('RGB')
        image.thumbnail((680,1500),Image.Resampling.LANCZOS)
        preview=OUT/f'{slug}_fig{num}_680px.png'
        image.save(preview,optimize=True)
        records.append(dict(slug=slug,title=source['title'],venue=source['venue'],primary=slug in {'rap','octo','vima','var'},
                            publication_record=source['publication_record'],pdf_url=source['pdf_url'],
                            local_pdf=f'02_verified_papers/{slug}.pdf',pdf_sha256=hashlib.sha256(pdf_path.read_bytes()).hexdigest(),
                            figure=num,pdf_page_1based=pageno,crop_pdf_points=coords,
                            crop=f'03_figure_gallery/{high.name}',preview=f'03_figure_gallery/{preview.name}'))
    pdf.close()
(ROOT/'03_figure_gallery'/'new_figure_records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print('Rendered',len(records),'figure crops and paper-scale previews')
