"""Original, editable SVG design studies. No borrowed paper icons or traced figures."""
from pathlib import Path
from html import escape
import cairosvg

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'06_original_compositions'
ICON=ROOT/'05_iconography_studies'
OUT.mkdir(exist_ok=True); ICON.mkdir(exist_ok=True)
NAVY='#213650'; BLUE='#d9ebf8'; TEAL='#ccebe5'; ORANGE='#ed8742'; GREEN='#3e9b73'; GRAY='#a6adb6'; PURPLE='#7866ae'; PALE='#f7fafb'

def svg_start(w,h):
 return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1 L9 5 L1 9 Z" fill="#213650"/></marker><marker id="arrow-orange" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1 L9 5 L1 9 Z" fill="#ed8742"/></marker><marker id="arrow-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1 L9 5 L1 9 Z" fill="#3e9b73"/></marker><marker id="arrow-purple" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1 L9 5 L1 9 Z" fill="#7866ae"/></marker><marker id="arrow-gray" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1 L9 5 L1 9 Z" fill="#a6adb6"/></marker><style>text{{font-family:Arial,Helvetica,sans-serif;fill:{NAVY}}}.head{{font-weight:700;font-size:28px}}.sub{{font-size:17px;font-weight:700}}.lab{{font-size:14px}}.small{{font-size:11px}}.math{{font-family:Georgia,serif;font-style:italic}}</style></defs><rect width="100%" height="100%" fill="white"/>']
def rect(a,x,y,w,h,fill='white',stroke=NAVY,rx=8,sw=1.5,dash=None):
 a.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
def path(a,d,stroke=NAVY,sw=2,fill='none',arrow=False,dash=None,opacity=1):
 marker={ORANGE:'arrow-orange',GREEN:'arrow-green',PURPLE:'arrow-purple',GRAY:'arrow-gray'}.get(stroke,'arrow')
 a.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}"'+(f' marker-end="url(#{marker})"' if arrow else '')+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
def txt(a,x,y,s,cls='lab',anchor='middle',color=None):
 a.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}"'+(f' fill="{color}" style="fill:{color}"' if color else '')+f'>{escape(str(s))}</text>')
def circle(a,x,y,r,fill='white',stroke=NAVY,sw=1.5):a.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
def pair(a,x,y,n,sel=False,head=False,scale=1):
 # x,y are center; two bound semicircles = one paired scientific node.
 r=27*scale; left=x-r; top=y-r
 path(a,f'M {x} {top} A {r} {r} 0 0 0 {x} {y+r} Z',fill=BLUE,stroke=ORANGE if sel else GREEN if head else NAVY,sw=2.4 if sel or head else 1.4)
 path(a,f'M {x} {top} A {r} {r} 0 0 1 {x} {y+r} Z',fill=TEAL,stroke=ORANGE if sel else GREEN if head else NAVY,sw=2.4 if sel or head else 1.4)
 path(a,f'M {x} {top} L {x} {y+r}',stroke='#86aab2',sw=1)
 txt(a,x-r/2,y+4,'Q', 'small');txt(a,x+r/2,y+4,'W','small')
 txt(a,x,y+r+19,f'v{n}','sub',color=ORANGE if sel else GREEN if head else NAVY)
def agent(a,x,y,illustrated=False):
 # A unique policy character, deliberately compact and original.
 if illustrated:
  path(a,f'M{x-20} {y-2} Q{x-25} {y-31} {x} {y-36} Q{x+25} {y-31} {x+20} {y-2} L{x+17} {y+25} Q{x} {y+36} {x-17} {y+25} Z',fill='#edf1fa',stroke=NAVY,sw=2)
  circle(a,x-8,y-11,3.3,NAVY,NAVY);circle(a,x+8,y-11,3.3,NAVY,NAVY)
  path(a,f'M{x-9} {y+6} Q{x} {y+12} {x+9} {y+6}',sw=1.7)
  path(a,f'M{x} {y-36} V{y-44}',sw=2);circle(a,x,y-47,3,ORANGE,ORANGE)
  path(a,f'M{x-18} {y+21} Q{x-30} {y+34} {x-24} {y+44} M{x+18} {y+21} Q{x+30} {y+34} {x+24} {y+44}',sw=2)
 else:
  circle(a,x,y,27,'#f0eff8',PURPLE,2)
  path(a,f'M{x-11} {y-8} L{x} {y-16} L{x+11} {y-8} V{y+10} L{x} {y+17} L{x-11} {y+10} Z',stroke=PURPLE,sw=1.7)
  circle(a,x-5,y,2.3,ORANGE,ORANGE);circle(a,x+5,y,2.3,ORANGE,ORANGE)
def worker(a,x,y):
 # Domain execution mark, distinct from the policy character.
 circle(a,x,y,27,'#fff5ed',ORANGE,2)
 path(a,f'M{x-10} {y+8} L{x+9} {y-11} M{x-2} {y-12} Q{x+12} {y-21} {x+15} {y-7} L{x+8} {y} M{x-15} {y+9} Q{x-12} {y+20} {x-3} {y+17}',stroke=ORANGE,sw=3)

def work(a,x,y,which='old',scale=1):
 # Four aligned stripes in one work object. Historical & candidate use same identity.
 w=126*scale; h=19*scale; gap=5*scale
 labels=['Core','Evaluation','Legacy API','Utilities']
 for i,label in enumerate(labels):
  yy=y+i*(h+gap)
  if which=='result' and i==2:
   path(a,f'M{x+8*scale} {yy+h/2} H{x+w-8*scale}',stroke=GRAY,sw=2,dash='4 4');txt(a,x+w/2,yy+h/2+4*scale,'excluded','small',color=GRAY);continue
  fill=TEAL if i in (0,3) else '#fff0e5' if which=='result' and i==1 else '#e8edf1' if i==2 else '#e7f4ef'
  stroke=GREEN if i in (0,3) else ORANGE if which=='result' and i==1 else GRAY if i==2 else '#82b8a5'
  rect(a,x,yy,w,h,fill,stroke,rx=4*scale,sw=1)
  txt(a,x+w/2,yy+h*.68, "Evaluation'" if which=='result' and i==1 else label,'small')
def header(a,title,subtitle):txt(a,55,44,title,'head','start');txt(a,56,69,subtitle,'lab','start',color='#607287')
def legend(a,x,y):
 for i,(color,label) in enumerate([(BLUE,'requirement'),(TEAL,'checkpoint'),(ORANGE,'selected / updated'),(GREEN,'preserved / committed'),(GRAY,'excluded / inactive'),(PURPLE,'training')]):
  circle(a,x+i*150,y,5,color,color,1);txt(a,x+10+i*150,y+4,label,'small','start')
def save(a,p):
 a.append('</svg>');p.write_text(''.join(a),encoding='utf-8')
 cairosvg.svg2png(url=str(p),write_to=str(p.with_suffix('.png')),output_width=1200)

def icon_sheet(illustrated=False):
 a=svg_start(1280,510);header(a,'Restrained illustrated symbols' if illustrated else 'Minimal scientific symbols','Original GitHarness icon study · same semantic inventory, two visual styles')
 xs=[115,345,585,825,1060]
 labels=['Git Agent','Paired version','Inspect / select','Fork copy','Work transformation']
 for x,label in zip(xs,labels):txt(a,x,125,label,'sub')
 agent(a,xs[0],220,illustrated);txt(a,xs[0],296,'policy only','lab')
 pair(a,xs[1],215,4,sel=True,scale=1.4);txt(a,xs[1],310,'V_i = (Q_i, W_i)','lab')
 pair(a,xs[2]-35,220,4,scale=.75);circle(a,xs[2]+34,208,17,'white',NAVY,2);path(a,f'M{xs[2]+46} 220 l18 19',sw=3);path(a,f'M{xs[2]-8} 220 H{xs[2]+13}',stroke=ORANGE,sw=2,arrow=True);txt(a,xs[2],310,'read vs choose','lab')
 work(a,xs[3]-55,167,'old',.65);path(a,f'M{xs[3]+20} 210 H{xs[3]+89}',stroke=ORANGE,sw=2.5,arrow=True);work(a,xs[3]+100,167,'old',.65);txt(a,xs[3]+25,310,'W4 → W_t^0','lab')
 work(a,xs[4]-55,167,'result',.83);txt(a,xs[4],310,'selective change','lab')
 path(a,'M60 352 H1220',stroke='#d8e2e9',sw=1)
 txt(a,75,393,'Stroke / fill / role','sub','start')
 txt(a,75,425,'One paired silhouette · blue Q + mint W · orange choice · gray stale work · purple learning','lab','start')
 txt(a,75,455,'Illustrated style adds facial cues only to the policy; all state and work objects stay scientific abstractions.','lab','start')
 save(a,ICON/('illustrated_symbols.svg' if illustrated else 'minimal_symbols.svg'))

def river():
 a=svg_start(1600,860);header(a,'Study 1 · Ancestry river','The historical branch is the figure; local execution grows from the selected edge.')
 txt(a,190,115,'feedback q_t','sub');txt(a,190,141,'+ evaluation metrics · - legacy API','lab');agent(a,330,126)
 txt(a,330,187,'Git Agent','sub');path(a,'M255 130 H294',stroke=BLUE,sw=3,arrow=True)
 path(a,'M355 118 C470 75 580 85 665 130',stroke=GRAY,sw=1.7,arrow=True,dash='5 6');txt(a,530,92,'INSPECT','small')
 path(a,'M370 146 C515 245 647 280 790 347',stroke=ORANGE,sw=3,arrow=True);txt(a,575,259,'COMMIT · Q_t, b_t = v4, h_t','lab',color=ORANGE)
 coords={0:(475,390),1:(605,390),2:(735,390),3:(865,258),5:(1000,258),6:(1135,258),4:(865,390),7:(1348,493)}
 for u,v in [(0,1),(1,2),(2,3),(3,5),(5,6),(2,4)]:
  x,y=coords[u];X,Y=coords[v];path(a,f'M{x+30} {y} C{x+60} {y} {X-60} {Y} {X-30} {Y}',stroke='#60738b',sw=2.5,arrow=True)
 for n,(x,y) in coords.items():
  if n!=7:pair(a,x,y,n,sel=n==4)
 txt(a,1135,205,'Current HEAD','lab');txt(a,865,454,'Selected base','lab',color=ORANGE)
 path(a,'M890 389 C1020 395 1050 490 1125 493',stroke=ORANGE,sw=4,arrow=True)
 txt(a,1010,417,'fork W4','lab',color=ORANGE)
 circle(a,1150,493,31,'#fff6ee',ORANGE,2)
 txt(a,1150,498,'W_t^0','sub');path(a,'M1183 493 H1312',stroke=ORANGE,sw=3,arrow=True);pair(a,1348,493,7,head=True)
 txt(a,1250,464,'Update Agent → W~_t','lab')
 # Local edge magnification, attached by two light rays.
 path(a,'M925 419 L690 550 M1180 523 L1090 550',stroke='#cad8df',sw=1.6)
 rect(a,630,550,610,177,'#fbfdfd','#cad8df',18,1.3)
 txt(a,655,578,'Historical W4','sub','start');work(a,655,595,'old',.83)
 path(a,'M795 636 H865',stroke=ORANGE,sw=2.4,arrow=True);txt(a,830,615,'fork','small')
 path(a,'M866 587 V714',stroke='#70b7aa',sw=1.8,dash='6 5');txt(a,910,578,'Isolated candidate','sub','start')
 work(a,915,595,'result',.83);txt(a,1120,600,'preserve Core / Utilities','small');txt(a,1120,625,"update Evaluation'",'small',color=ORANGE);txt(a,1120,650,'exclude Legacy API','small',color=GRAY)
 txt(a,1080,706,'success → v7   ·   failure → discard candidate only','small')
 path(a,'M555 786 C155 790 83 620 301 126',stroke=PURPLE,sw=2.2,arrow=True);txt(a,766,787,'Outcome + Tracking (fidelity · base · staleness) → GRPO → Git Agent only','lab',color=PURPLE)
 txt(a,426,217,'REUSE → exact version (optional bypass)','small',color=GRAY)
 txt(a,1140,360,'Router after COMMIT: Reuse & Patch','lab',color=ORANGE)
 txt(a,1140,385,'Fresh Solve = empty (inactive)','small',color=GRAY)
 legend(a,95,827);save(a,OUT/'01_ancestry_river.svg')

def cutaway():
 a=svg_start(1600,900);header(a,'Study 2 · Workbench cutaway','An illustrated policy selects a historical specimen; the candidate is a detached, editable copy.')
 agent(a,125,174,True);txt(a,125,241,'Git Agent','sub')
 txt(a,38,276,'q_t  + metrics  - legacy API','lab','start');path(a,'M145 178 C225 115 315 120 395 160',stroke=GRAY,sw=1.5,dash='5 5',arrow=True);txt(a,277,121,'INSPECT G<t','small')
 # A compact historical graph forms a live shelf, not a detached panel.
 pos={0:(390,175),1:(500,175),2:(610,175),3:(720,105),5:(830,105),6:(940,105),4:(720,250)}
 for u,v in [(0,1),(1,2),(2,3),(3,5),(5,6),(2,4)]:
  x,y=pos[u];X,Y=pos[v];path(a,f'M{x+27} {y} C{x+48} {y} {X-47} {Y} {X-28} {Y}',stroke='#788ba2',sw=1.9,arrow=True)
 for n,(x,y) in pos.items():pair(a,x,y,n,sel=n==4,scale=.85)
 txt(a,940,55,'HEAD','lab');path(a,'M160 211 C275 300 495 305 670 250',stroke=ORANGE,sw=2.5,arrow=True)
 txt(a,415,324,'COMMIT  (Q_t, v4, h_t)','sub',color=ORANGE)
 # Massive central paired work object.
 txt(a,92,394,'Historical checkpoint W4','sub','start');work(a,100,417,'old',1.55)
 rect(a,398,395,826,315,'#f8fcfb','#5baea0',35,2,dash='9 6');txt(a,430,427,'ISOLATED CANDIDATE WORKSPACE','sub','start')
 path(a,'M300 478 C340 478 355 478 405 478',stroke=ORANGE,sw=4,arrow=True)
 txt(a,355,461,'fork','lab',color=ORANGE);work(a,450,453,'old',1.23);txt(a,528,592,'W_t^0','sub')
 worker(a,815,496);txt(a,815,549,'Update Agent','lab')
 path(a,'M615 502 H780',stroke=ORANGE,sw=3,arrow=True);path(a,'M850 502 H930',stroke=ORANGE,sw=3,arrow=True)
 work(a,940,453,'result',1.23);txt(a,1018,592,'W~_t','sub')
 txt(a,634,638,'preserve','small',color=GREEN);txt(a,752,638,'update','small',color=ORANGE);txt(a,858,638,'exclude','small',color=GRAY)
 txt(a,100,671,'W4 stays immutable','lab','start');txt(a,468,672,'Router: Reuse & Patch  ·  Fresh Solve inactive','lab','start')
 path(a,'M1085 496 H1308',stroke=GREEN,sw=3,arrow=True);pair(a,1365,495,7,head=True,scale=1.2)
 txt(a,1365,407,'New HEAD','sub');txt(a,1365,575,'success → commit','lab',color=GREEN)
 path(a,'M1130 610 C1200 706 1325 702 1390 660',stroke=GRAY,sw=1.8,arrow=True,dash='5 5');txt(a,1300,737,'failure → discard candidate only','lab',color=GRAY)
 path(a,'M740 275 C1020 289 1270 334 1365 451',stroke=ORANGE,sw=2.5,arrow=True);txt(a,1150,300,'v7 descends from v4','lab',color=ORANGE)
 path(a,'M420 818 C210 821 22 634 94 176',stroke=PURPLE,sw=2.5,arrow=True)
 txt(a,800,819,'Final Outcome + Query Tracking → Harness RL / GRPO → Git Agent only','lab',color=PURPLE)
 txt(a,800,845,'Tracking: requirement fidelity · base optimality · staleness exclusion   |   Frozen: Router, Update Agent, Harness','small')
 legend(a,95,875);save(a,OUT/'02_workbench_cutaway.svg')

def lens():
 a=svg_start(1600,870);header(a,'Study 3 · Requirement lens','A resolved requirement selects one point in a single historical graph; construction occupies the chosen branch.')
 agent(a,195,220);txt(a,195,277,'Git Agent','sub');txt(a,195,105,'q_t  + metrics  - legacy API','lab')
 path(a,'M195 142 V182',stroke=BLUE,sw=3,arrow=True)
 # Q lens is a translucent region overlay on the real history graph.
 a.append(f'<ellipse cx="795" cy="343" rx="398" ry="223" fill="{BLUE}" opacity="0.26" stroke="#78a9d1" stroke-width="2"/>')
 txt(a,794,155,'History under resolved Q_t','sub');txt(a,795,181,'Exact match: none  ·  Compatible: v4','lab')
 pos={0:(495,348),1:(605,348),2:(715,348),3:(825,258),5:(935,258),6:(1045,258),4:(825,442)}
 for u,v in [(0,1),(1,2),(2,3),(3,5),(5,6),(2,4)]:
  x,y=pos[u];X,Y=pos[v];path(a,f'M{x+27} {y} C{x+48} {y} {X-47} {Y} {X-28} {Y}',stroke='#869bb0',sw=2,arrow=True)
 for n,(x,y) in pos.items():pair(a,x,y,n,sel=n==4,scale=.9)
 txt(a,1045,207,'HEAD','lab');path(a,'M222 220 C340 256 491 409 789 442',stroke=ORANGE,sw=3,arrow=True);txt(a,392,345,'COMMIT (Q_t, v4, h_t)','lab',color=ORANGE)
 txt(a,201,350,'INSPECT (read only)','small');path(a,'M210 296 C275 145 384 133 486 198',stroke=GRAY,sw=1.8,dash='5 6',arrow=True)
 # Branch is a single tapered visual corridor, from v4 to v7.
 path(a,'M827 473 C827 555 997 582 1114 582 L1433 582',stroke=ORANGE,sw=5,arrow=True)
 txt(a,824,516,'fork W4','lab',color=ORANGE);txt(a,1040,542,'Router → Reuse & Patch','lab');txt(a,1040,565,'Fresh Solve: empty (inactive)','small',color=GRAY)
 path(a,'M875 540 L875 744 M1390 540 L1390 744',stroke='#67b2a5',sw=1.5,dash='6 6')
 txt(a,1118,630,'isolated candidate','sub');work(a,915,646,'old',.83);txt(a,967,759,'W_t^0','lab')
 path(a,'M1025 690 H1122',stroke=ORANGE,sw=2.5,arrow=True);worker(a,1155,690);txt(a,1155,755,'Update Agent','small')
 path(a,'M1188 690 H1250',stroke=ORANGE,sw=2.5,arrow=True);work(a,1272,646,'result',.83);txt(a,1324,759,'W~_t','lab')
 pair(a,1480,582,7,head=True,scale=1.1);txt(a,1480,508,'New HEAD','lab')
 txt(a,1480,686,'success → commit','small',color=GREEN);txt(a,1480,708,'failure → discard candidate','small',color=GRAY)
 txt(a,593,703,'W4 immutable','lab');work(a,545,581,'old',.83)
 path(a,'M660 640 C727 630 800 624 864 611',stroke=ORANGE,sw=2.3,arrow=True)
 path(a,'M560 806 C260 811 37 652 166 220',stroke=PURPLE,sw=2.3,arrow=True)
 txt(a,870,817,'Outcome + Tracking (fidelity, base, staleness) → GRPO → Git Agent only','lab',color=PURPLE)
 txt(a,871,839,'REUSE: optional exact-version bypass; no Router or Update Agent   |   Frozen: Router, Update Agent, Harness','small')
 save(a,OUT/'03_requirement_lens.svg')

for illustrated in (False,True):icon_sheet(illustrated)
river();cutaway();lens()
print('Created 2 icon style sheets and 3 composition studies, SVG + PNG previews')
