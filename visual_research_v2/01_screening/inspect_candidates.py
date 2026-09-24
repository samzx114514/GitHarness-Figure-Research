"""Index figure captions and render early-page contact sheets for visual triage."""
from pathlib import Path
import json
import re
import pymupdf
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PDFS = ROOT / "02_verified_papers"
OUT = ROOT / "01_screening" / "page_contacts"
OUT.mkdir(parents=True, exist_ok=True)
all_records = []
for pdf_path in sorted(PDFS.glob("*.pdf")):
    pdf = pymupdf.open(pdf_path)
    caps=[]
    for index in range(min(12,len(pdf))):
        page=pdf[index]
        lines=page.get_text().splitlines()
        for i,line in enumerate(lines):
            if re.match(r"\s*(?:Figure|Fig\.)\s*\d+\s*[:.]",line,re.I):
                caps.append({"page":index+1,"line":" ".join(lines[i:i+3])[:350]})
    count=min(6,len(pdf))
    thumb_w=620
    thumb_h=800
    sheet=Image.new("RGB",(thumb_w*2,thumb_h*3),(240,244,248))
    draw=ImageDraw.Draw(sheet)
    for i in range(count):
        pix=pdf[i].get_pixmap(matrix=pymupdf.Matrix(0.95,0.95),alpha=False)
        im=Image.frombytes("RGB",(pix.width,pix.height),pix.samples)
        im.thumbnail((thumb_w-16,thumb_h-38))
        x=(i%2)*thumb_w+(thumb_w-im.width)//2
        y=(i//2)*thumb_h+30
        sheet.paste(im,(x,y))
        draw.text(((i%2)*thumb_w+12,(i//2)*thumb_h+7),f"{pdf_path.stem} / PDF p{i+1}",fill=(28,45,66))
    out=OUT/f"{pdf_path.stem}_p1-6.jpg"
    sheet.save(out,quality=88)
    all_records.append({"slug":pdf_path.stem,"pages":len(pdf),"caption_lines":caps,"contact_sheet":out.relative_to(ROOT).as_posix()})
    print(pdf_path.stem, "pages",len(pdf),"captions",[(c['page'],c['line'][:100]) for c in caps[:8]])
    pdf.close()
(ROOT / "01_screening" / "pdf_figure_index.json").write_text(json.dumps(all_records,indent=2,ensure_ascii=False),encoding="utf-8")
