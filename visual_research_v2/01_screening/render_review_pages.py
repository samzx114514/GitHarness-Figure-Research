"""Render targeted original-PDF pages before choosing the deep visual set."""
from pathlib import Path
import pymupdf
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
PDFS=ROOT/'02_verified_papers'
OUT=ROOT/'01_screening'/'review_pages'
OUT.mkdir(parents=True,exist_ok=True)
PAGES={
    'graph_of_thoughts':[3,5],
    'swe_agent':[1],
    'vima':[2,4],
    'var':[2,5],
    'generative_agents':[8],
    'autogen':[1,4],
    'self_refine':[2],
    'openvla':[1,4],
    'rap':[2,5],
    'octo':[1,3],
    'diffusion_policy':[3],
    'saycan':[4],
    'rt2':[1,2,3],
}
for slug,pages in PAGES.items():
    pdf=pymupdf.open(PDFS/f'{slug}.pdf')
    for page_no in pages:
        page=pdf[page_no-1]
        pix=page.get_pixmap(matrix=pymupdf.Matrix(1.7,1.7),alpha=False)
        image=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
        image.save(OUT/f'{slug}_pdfp{page_no}.png',optimize=True)
    pdf.close()
print('Rendered',sum(map(len,PAGES.values())),'full PDF pages')
