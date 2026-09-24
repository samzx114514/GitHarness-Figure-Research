"""Six original, editable SVG method-figure candidates for GitHarness.

Run: python open_exploration_v1/build_figures.py
The SVG is primary; PNG and 180-mm previews are rendered evidence.
"""
from html import escape
from pathlib import Path
import cairosvg

ROOT = Path(__file__).resolve().parent
NAVY='#1f334e'; BLUE='#dcecf8'; TEAL='#d3ebe7'; ORANGE='#e97732'
GREEN='#35936e'; GRAY='#9ca6af'; PURPLE='#745baa'; LIGHT='#f7fafb'
INK='#52667d'; LINE='#bdcbd4'

class Fig:
    def __init__(self,w=1500,h=850):
        self.w,self.h=w,h
        self.a=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
                '<defs><style>text{font-family:Arial,Helvetica,sans-serif;fill:#1f334e}.title{font-size:30px;font-weight:700}.section{font-size:24px;font-weight:700}.label{font-size:21px}.small{font-size:18px}.tiny{font-size:16px}.math{font-family:Georgia,serif;font-style:italic}</style>'
                '<marker id="m-navy" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M1 1 L9 5 L1 9 Z" fill="#1f334e"/></marker>'
                '<marker id="m-orange" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M1 1 L9 5 L1 9 Z" fill="#e97732"/></marker>'
                '<marker id="m-green" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M1 1 L9 5 L1 9 Z" fill="#35936e"/></marker>'
                '<marker id="m-gray" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M1 1 L9 5 L1 9 Z" fill="#9ca6af"/></marker>'
                '<marker id="m-purple" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M1 1 L9 5 L1 9 Z" fill="#745baa"/></marker>'
                '</defs><rect width="100%" height="100%" fill="white"/>']
    def raw(self,x): self.a.append(x)
    def text(self,x,y,t,size='label',anchor='middle',color=None,weight=None,rotate=None):
        st=f'fill:{color or NAVY};'+(f'font-weight:{weight};' if weight else '')
        rt=f' transform="rotate({rotate} {x} {y})"' if rotate else ''
        self.a.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{size}" style="{st}"{rt}>{escape(str(t))}</text>')
    def rect(self,x,y,w,h,fill='white',stroke=LINE,r=8,sw=1.5,dash=None,opacity=1):
        self.a.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
    def ellipse(self,x,y,rx,ry,fill='none',stroke=LINE,sw=1.5,opacity=1,dash=None):
        self.a.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
    def path(self,d,color=NAVY,sw=2.2,arrow=False,dash=None,fill='none',opacity=1):
        mark={ORANGE:'orange',GREEN:'green',GRAY:'gray',PURPLE:'purple'}.get(color,'navy')
        self.a.append(f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}"'+(f' stroke-dasharray="{dash}"' if dash else '')+(f' marker-end="url(#m-{mark})"' if arrow else '')+'/>')
    def circle(self,x,y,r,fill='white',stroke=NAVY,sw=1.5):self.ellipse(x,y,r,r,fill,stroke,sw)
    def end(self):self.a.append('</svg>');return ''.join(self.a)

def header(s,name,thesis):
    s.text(45,49,name,'title','start')
    s.text(46,77,thesis,'small','start',INK)

def pair(s,x,y,n,selected=False,head=False,scale=1):
    # One indivisible paired-version silhouette; internal Q/W partition.
    w,h=70*scale,48*scale; l=x-w/2; t=y-h/2
    edge=ORANGE if selected else GREEN if head else NAVY
    s.rect(l,t,w,h,'white',edge,13*scale,2.7 if selected or head else 1.7)
    s.raw(f'<path d="M{l+12*scale} {t+2*scale} H{x} V{t+h-2*scale} H{l+12*scale} Q{l+2*scale} {t+h-2*scale} {l+2*scale} {t+h-12*scale} V{t+12*scale} Q{l+2*scale} {t+2*scale} {l+12*scale} {t+2*scale}" fill="{BLUE}" stroke="none"/>')
    s.raw(f'<path d="M{x} {t+2*scale} H{l+w-12*scale} Q{l+w-2*scale} {t+2*scale} {l+w-2*scale} {t+12*scale} V{t+h-12*scale} Q{l+w-2*scale} {t+h-2*scale} {l+w-12*scale} {t+h-2*scale} H{x} Z" fill="{TEAL}" stroke="none"/>')
    s.path(f'M{x} {t+3*scale} V{t+h-3*scale}',LINE,1)
    s.text(x-17*scale,y+5*scale,f'Q{n}', 'tiny')
    s.text(x+17*scale,y+5*scale,f'W{n}', 'tiny')
    s.text(x,y+h/2+22*scale,f'v{n}','label',color=edge if selected or head else NAVY,weight=700)

def agent(s,x,y,character=False,scale=1):
    r=30*scale
    if character:
        s.path(f'M{x-20*scale} {y-18*scale} Q{x-18*scale} {y-43*scale} {x} {y-44*scale} Q{x+18*scale} {y-43*scale} {x+20*scale} {y-18*scale} L{x+23*scale} {y+17*scale} Q{x} {y+41*scale} {x-23*scale} {y+17*scale} Z',NAVY,2.5,fill='#f0f2fa')
        s.path(f'M{x} {y-44*scale} V{y-53*scale}',NAVY,2)
        s.circle(x,y-56*scale,3.5*scale,ORANGE,ORANGE)
        s.circle(x-8*scale,y-12*scale,3*scale,NAVY,NAVY)
        s.circle(x+8*scale,y-12*scale,3*scale,NAVY,NAVY)
        s.path(f'M{x-8*scale} {y+5*scale} Q{x} {y+11*scale} {x+8*scale} {y+5*scale}',NAVY,1.6)
        s.path(f'M{x-20*scale} {y+16*scale} Q{x-38*scale} {y+26*scale} {x-33*scale} {y+38*scale} M{x+20*scale} {y+16*scale} Q{x+38*scale} {y+26*scale} {x+33*scale} {y+38*scale}',NAVY,2)
    else:
        s.circle(x,y,r,'#f1eff8',PURPLE,2.2)
        s.path(f'M{x-12*scale} {y-8*scale} L{x} {y-17*scale} L{x+12*scale} {y-8*scale} L{x+12*scale} {y+11*scale} L{x} {y+19*scale} L{x-12*scale} {y+11*scale} Z',PURPLE,1.7)
        s.circle(x-5*scale,y,2.5*scale,ORANGE,ORANGE)
        s.circle(x+5*scale,y,2.5*scale,ORANGE,ORANGE)
    s.text(x,y+65*scale,'Git Agent','small',weight=700)

def router(s,x,y):
    s.path(f'M{x} {y-27} L{x+27} {y} L{x} {y+27} L{x-27} {y} Z',NAVY,1.7,fill='#f0f4f7')
    s.text(x,y+6,'R','label',weight=700)
    s.text(x,y+51,'Router','small')

def updater(s,x,y):
    s.circle(x,y,29,'#fff5ec',ORANGE,1.8)
    s.path(f'M{x-12} {y+11} L{x+9} {y-11} M{x-2} {y-13} Q{x+15} {y-18} {x+17} {y-3} L{x+10} {y+3}',ORANGE,3)

def work(s,x,y,kind='old',scale=1,short=False):
    # x,y top-left; three states share exact row registration.
    w=144*scale; rh=27*scale; gap=6*scale
    names=['Core Logic','Evaluation','Legacy API','Utilities']
    if short:names=['Core','Eval','Legacy','Utilities']
    for i,label in enumerate(names):
        yy=y+i*(rh+gap)
        if kind=='result' and i==2:
            s.path(f'M{x+8*scale} {yy+rh/2} H{x+w-8*scale}',GRAY,2,dash='5 4')
            s.text(x+w/2,yy+rh*.72,'excluded','tiny',color=GRAY);continue
        fill=TEAL if kind!='result' else '#d9eee3' if i in (0,3) else '#fff0e4'
        edge='#86b6ad' if kind!='result' else GREEN if i in (0,3) else ORANGE
        s.rect(x,yy,w,rh,fill,edge,5*scale,1.4)
        s.text(x+w/2,yy+rh*.71,"Evaluation'" if kind=='result' and i==1 and not short else "Eval'" if kind=='result' and i==1 else label,'tiny')
    return w,4*rh+3*gap

def reward(s,x,y,vertical=False):
    # Outcome and tracking advantages kept distinct until the GRPO step.
    if vertical:
        s.text(x,y,'Final Outcome','small')
        s.text(x,y+25,'norm A_out','tiny',color=PURPLE)
        s.text(x,y+64,'Tracking','small')
        s.text(x,y+88,'Fidelity · Base · Staleness','tiny')
        s.text(x,y+111,'norm A_track','tiny',color=PURPLE)
        s.path(f'M{x} {y+123} V{y+142}',PURPLE,2,arrow=True)
        s.rect(x-75,y+143,150,37,'#f0edf7',PURPLE,18,1.3)
        s.text(x,y+167,'Harness RL / GRPO','tiny',color=PURPLE,weight=700)
    else:
        s.text(x,y,'Final Outcome  →  norm A_out','small',color=PURPLE)
        s.text(x,y+26,'Tracking (Fidelity · Base · Staleness)  →  norm A_track','small',color=PURPLE)
        s.path(f'M{x+435} {y+3} H{x+448} M{x+435} {y+27} H{x+448}',PURPLE,1.6)
        s.rect(x+450,y-15,155,55,'#f0edf7',PURPLE,20,1.3)
        s.text(x+527,y+18,'Harness RL / GRPO','tiny',color=PURPLE,weight=700)

def footer(s,x,y):s.text(x,y,'Frozen: Router · Update Agent · Domain Harness','tiny','start',GRAY)
def small_reuse(s,x,y):
    s.path(f'M{x} {y} H{x+72}',GRAY,1.7,arrow=True,dash='5 5')
    s.text(x+88,y+5,'REUSE → exact V_i (none here)','tiny','start',GRAY)

def lineage(s,pos,edges,selected=4,head=7,scale=1):
    for u,v in edges:
        x,y=pos[u]; X,Y=pos[v]
        col=ORANGE if u==4 or v==7 else INK
        s.path(f'M{x+38*scale} {y} C{x+58*scale} {y} {X-58*scale} {Y} {X-39*scale} {Y}',col,2.3 if col==ORANGE else 1.8,arrow=True)
    for n,(x,y) in pos.items():pair(s,x,y,n,selected=n==selected,head=n==head,scale=scale)

def save(s,num):
    d=ROOT/f'candidate_{num:02d}';d.mkdir(parents=True,exist_ok=True)
    svg=d/'figure.svg';svg.write_text(s.end(),encoding='utf-8')
    cairosvg.svg2png(url=str(svg),write_to=str(d/'figure.png'),output_width=3000)
    cairosvg.svg2png(url=str(svg),write_to=str(d/'paper_width_preview.png'),output_width=1063)

def candidate_01():
    s=Fig();header(s,'01  Branch canopy','One recoverable graph; the active v4 branch carries construction and commit.')
    s.rect(52,114,183,77,BLUE,'#9dbdd6',13,1.3)
    s.text(144,143,'feedback  q_t','label')
    s.text(144,170,'+ metrics   - legacy API','small')
    agent(s,287,151)
    s.path('M237 153 H253',INK,2,arrow=True)
    s.path('M316 152 C344 183 335 222 298 249',GRAY,1.2,dash='4 5')
    s.path('M317 141 C405 93 570 99 653 203',GRAY,1.6,arrow=True,dash='5 5')
    s.text(492,112,'INSPECT G_<t  (read only)','small',color=GRAY)
    small_reuse(s,298,249)
    pos={0:(415,331),1:(535,331),2:(655,331),3:(790,232),5:(915,232),6:(1040,232),4:(790,389)}
    lineage(s,pos,[(0,1),(1,2),(2,3),(3,5),(5,6),(2,4)])
    s.text(742,144,'V_i = (Q_i, W_i)','small')
    s.text(1040,163,'Previous HEAD','small')
    s.path('M318 168 C300 446 558 499 750 389',ORANGE,3.2,arrow=True)
    s.text(470,418,'COMMIT','label',color=ORANGE,weight=700)
    s.text(455,469,'(Q_t, b_t = v4, h_t)','small',color=ORANGE)
    s.text(790,453,'Selected base','small',color=ORANGE)
    s.path('M829 389 C874 392 894 416 907 424',ORANGE,3.2,arrow=True)
    router(s,937,438)
    s.text(928,502,'Reuse & Patch','small',color=ORANGE)
    s.text(928,525,'Fresh Solve: empty','tiny',color=GRAY)
    s.path('M966 438 H1001',ORANGE,3,arrow=True)
    pair(s,1460,438,7,head=True)
    s.text(1478,358,'Success: commit','small','end',color=GREEN)
    s.text(1478,381,'New HEAD','small','end',color=GREEN)
    s.path('M1390 681 C1431 714 1452 737 1461 769',GRAY,1.8,arrow=True,dash='5 5')
    s.text(1315,755,'Failure: discard candidate only','tiny',color=GRAY)
    s.path('M791 423 C796 477 785 517 754 548',ORANGE,1.8,arrow=True)
    s.text(758,536,'Historical W4','small')
    work(s,680,565,scale=.9)
    s.text(745,722,'immutable','tiny',color=INK)
    s.rect(1003,405,412,317,'none','#75b7aa',20,1.8,dash='7 6')
    s.text(1025,573,'isolated candidate','small','start')
    s.path('M818 633 H1031',ORANGE,2.5,arrow=True)
    s.text(909,619,'fork W4','small',color=ORANGE)
    work(s,1048,583,scale=.78)
    s.text(1104,714,'W_t^0','small')
    updater(s,1205,635)
    s.text(1205,537,'Task-Native Update','tiny')
    s.path('M1159 633 H1171 M1236 633 H1260',ORANGE,2.3,arrow=True)
    work(s,1280,583,'result',.78)
    s.text(1337,714,'W~_t','small')
    s.path('M1392 582 C1441 545 1460 499 1460 475',GREEN,2.1,arrow=True)
    reward(s,330,753)
    s.path('M842 787 C825 847 38 846 48 590 C55 360 205 295 258 171',PURPLE,2.2,arrow=True)
    footer(s,1020,825)
    save(s,1)

def candidate_02():
    s=Fig();header(s,'02  State metamorphosis','The work artifact stays recognizable while the active requirement changes its contents.')
    s.text(90,130,'q_t  + evaluation metrics  - legacy API','label','start')
    agent(s,421,155)
    s.path('M342 129 H385',INK,2,arrow=True)
    s.path('M396 170 C309 207 208 245 70 282',GRAY,1.2,dash='4 5')
    s.text(421,249,'resolve Q_t','small')
    # A compact ancestry strip above the specimen: only v4 has an active descendant.
    pos={0:(635,154),1:(748,154),2:(861,154),3:(970,111),5:(1083,111),6:(1196,111),4:(970,244)}
    lineage(s,pos,[(0,1),(1,2),(2,3),(3,5),(5,6),(2,4)],scale=.78)
    s.text(843,67,'V_i = (Q_i, W_i)','tiny')
    s.text(1196,70,'Previous HEAD','tiny')
    s.path('M451 168 C608 202 745 244 934 244',ORANGE,2.7,arrow=True)
    s.text(662,225,'COMMIT (Q_t, v4, h_t)','small',color=ORANGE)
    s.path('M451 145 C535 83 681 82 826 111',GRAY,1.4,arrow=True,dash='4 5')
    s.text(622,91,'INSPECT','tiny',color=GRAY)
    small_reuse(s,70,282)
    s.text(230,375,'Historical W4','section')
    work(s,110,403,scale=1.55)
    s.text(225,614,'recoverable · immutable','small')
    s.path('M335 521 H448',ORANGE,3.5,arrow=True)
    s.text(397,496,'fork','label',color=ORANGE)
    pair(s,1365,282,7,head=True,scale=1.05)
    s.text(1365,221,'New HEAD','small',color=GREEN)
    s.text(1245,246,'v7 descends from v4','tiny',color=ORANGE)
    s.path('M970 278 C855 327 531 322 225 325 V389',LINE,1.3)
    s.rect(464,344,947,337,'#f8fcfb','#78b9af',33,2,dash='9 7')
    s.text(489,378,'isolated candidate','section','start')
    s.path('M968 278 C795 287 645 280 523 294',ORANGE,1.8,arrow=True)
    router(s,492,295)
    s.text(617,315,'Reuse & Patch active','small',color=ORANGE)
    s.text(824,315,'Fresh: empty (inactive)','tiny',color=GRAY)
    s.path('M478 324 C429 351 401 421 397 472',ORANGE,1.6,arrow=True,dash='5 5')
    work(s,530,420,scale=1.45)
    s.text(635,638,'W_t^0','section')
    s.path('M748 513 H813',ORANGE,3,arrow=True)
    updater(s,860,516)
    s.text(860,601,'Task-Native Update','small')
    s.path('M892 513 H968',ORANGE,3,arrow=True)
    work(s,1005,420,'result',1.45)
    s.text(1110,638,'W~_t','section')
    s.text(1110,663,'preserve  ·  update  ·  exclude','tiny',color=INK)
    s.path('M1215 467 C1281 422 1349 370 1365 320',GREEN,2.5,arrow=True)
    s.path('M1241 594 C1328 669 1392 659 1445 637',GRAY,1.8,arrow=True,dash='5 5')
    s.text(1326,704,'Failure: discard candidate only','tiny',color=GRAY)
    reward(s,400,743)
    s.path('M912 779 C800 849 36 838 43 557 C53 292 246 153 389 155',PURPLE,2.1,arrow=True)
    footer(s,1000,818)
    save(s,2)

def candidate_03():
    s=Fig();header(s,'03  Requirement field','The same history is reinterpreted under Q_t; compatibility is a policy judgment.')
    s.rect(70,136,305,93,BLUE,'#8fb7d6',26,1.5)
    s.text(223,173,'dynamic feedback  q_t','label')
    s.text(223,202,'+ evaluation metrics   - legacy API','small')
    agent(s,254,316)
    s.path('M254 231 V282',INK,2,arrow=True)
    s.path('M224 336 C170 365 130 414 89 452',GRAY,1.2,dash='4 5')
    s.path('M285 300 C379 189 495 167 578 214',GRAY,1.7,arrow=True,dash='6 5')
    s.text(435,213,'INSPECT G_<t','small',color=GRAY)
    # Transparent requirement field covers the actual graph, not a duplicate summary.
    s.ellipse(833,355,427,251,BLUE,'#8bb9d7',2,.38)
    s.text(805,148,'History under resolved Q_t','section')
    s.text(830,178,'No exact match     ·     v4 compatible','label')
    s.text(830,211,'V_i = (Q_i, W_i)','small')
    pos={0:(512,344),1:(615,344),2:(718,344),3:(827,261),5:(936,261),6:(1045,261),4:(827,439)}
    lineage(s,pos,[(0,1),(1,2),(2,3),(3,5),(5,6),(2,4)],scale=.82)
    s.text(1045,208,'Previous HEAD','small')
    s.path('M287 327 C436 385 619 438 790 439',ORANGE,3.2,arrow=True)
    s.text(487,445,'COMMIT','label',color=ORANGE,weight=700)
    s.text(522,475,'(Q_t, b_t = v4, h_t)','small',color=ORANGE)
    small_reuse(s,89,452)
    s.path('M829 470 C852 511 907 530 934 531',ORANGE,3,arrow=True)
    s.path('M811 470 C804 514 783 551 783 595',LINE,1.4)
    router(s,964,535)
    s.text(973,608,'Reuse & Patch','small',color=ORANGE)
    s.text(973,630,'Fresh Solve: empty','tiny',color=GRAY)
    s.rect(1060,546,377,219,'#f8fcfb','#79b7ac',26,1.9,dash='8 6')
    s.text(1080,575,'isolated candidate','small','start')
    s.path('M990 535 H1071',ORANGE,3,arrow=True)
    work(s,1091,610,scale=.76)
    s.text(1146,748,'W_t^0','small')
    updater(s,1228,652)
    s.text(1228,593,'Task-Native','tiny')
    s.text(1228,613,'Update','tiny')
    s.path('M1204 661 H1198 M1259 661 H1280',ORANGE,2,arrow=True)
    work(s,1294,610,'result',.76)
    s.text(1349,748,'W~_t','small')
    s.text(783,583,'Historical W4','small')
    work(s,728,605,scale=.76)
    s.text(783,748,'immutable','tiny',color=INK)
    s.path('M840 662 H1075',ORANGE,2.3,arrow=True)
    s.text(948,683,'fork','tiny',color=ORANGE)
    pair(s,1369,427,7,head=True,scale=1.04)
    s.text(1369,350,'Success → commit','small',color=GREEN)
    s.path('M1388 610 C1439 562 1432 490 1397 459',GREEN,2.1,arrow=True)
    s.path('M1397 692 C1455 712 1467 752 1467 782',GRAY,1.5,arrow=True,dash='4 5')
    s.text(1320,801,'Failure: discard candidate only','tiny',color=GRAY)
    reward(s,149,568,vertical=True)
    s.path('M149 753 C35 772 42 537 222 316',PURPLE,2,arrow=True)
    footer(s,465,817)
    save(s,3)

def candidate_04():
    s=Fig();header(s,'04  Field-notebook scene','A restrained illustrated policy handles one historical specimen and one isolated copy.')
    # A manuscript-like illustrated field, without software cards or Git icons.
    s.path('M74 139 C212 95 366 128 457 207',LINE,2)
    s.path('M427 206 C583 156 757 152 925 218',LINE,2)
    s.text(103,126,'q_t','section')
    s.text(117,160,'+ metrics','small')
    s.text(117,184,'- legacy API','small')
    s.path('M192 164 C273 175 319 222 352 276',BLUE,10,opacity=.8)
    s.path('M321 240 L352 276',INK,1.5,arrow=True)
    agent(s,388,298,character=True,scale=1.45)
    s.path('M347 317 C258 348 168 414 82 479',GRAY,1.2,dash='4 5')
    s.text(386,408,'resolves Q_t','small')
    s.text(386,434,'INSPECT · REUSE · COMMIT','tiny',color=INK)
    s.path('M424 282 C525 170 629 160 738 220',GRAY,1.7,arrow=True,dash='5 6')
    s.text(581,176,'read-only history','small',color=GRAY)
    pos={0:(572,304),1:(674,304),2:(776,304),3:(881,231),5:(986,231),6:(1091,231),4:(881,371)}
    lineage(s,pos,[(0,1),(1,2),(2,3),(3,5),(5,6),(2,4)],scale=.76)
    s.text(860,133,'V_i = (Q_i, W_i)','tiny')
    s.text(1091,179,'Previous HEAD','small')
    s.path('M431 311 C566 377 722 394 847 371',ORANGE,3.1,arrow=True)
    s.text(612,397,'COMMIT: Q_t, v4, h_t','small',color=ORANGE)
    small_reuse(s,82,479)
    # A recoverable specimen sheet left of a translucent candidate membrane.
    s.path('M538 486 Q550 467 574 469 H728 Q754 471 754 491 V703 Q754 724 728 724 H574 Q548 723 538 703 Z',LINE,1.7,fill='#fcfdfd')
    s.path('M720 469 L754 502 H720 Z',LINE,1.1,fill='#edf3f5')
    s.text(645,503,'historical W4','small')
    work(s,574,534,scale=1)
    s.text(646,692,'immutable','tiny',color=INK)
    s.ellipse(1190,574,280,200,'#f1faf8','#77b8ab',2,.84)
    s.text(1190,414,'isolated candidate','section')
    s.path('M757 605 H910',ORANGE,3,arrow=True)
    s.text(795,637,'fork','small',color=ORANGE)
    router(s,847,478)
    s.text(847,551,'Reuse & Patch','tiny',color=ORANGE)
    s.text(847,573,'Fresh Solve: empty','tiny',color=GRAY)
    work(s,947,515,scale=.83)
    s.text(1006,663,'W_t^0','small')
    updater(s,1119,583)
    s.text(1119,502,'Task-Native Update','tiny')
    s.path('M1069 588 H1085 M1150 588 H1183',ORANGE,2.4,arrow=True)
    work(s,1225,515,'result',.83)
    s.text(1284,663,'W~_t','small')
    s.path('M882 401 C869 425 847 437 847 449',ORANGE,2.3,arrow=True)
    s.path('M861 389 C782 432 726 452 646 470',LINE,1.4)
    pair(s,1361,335,7,head=True,scale=1.1)
    s.text(1361,248,'New HEAD','small',color=GREEN)
    s.path('M1341 515 C1392 463 1397 400 1375 370',GREEN,2.1,arrow=True)
    s.path('M1344 643 C1420 686 1441 726 1460 780',GRAY,1.7,arrow=True,dash='5 5')
    s.text(1292,802,'failure → discard candidate only','tiny',color=GRAY)
    s.text(1267,697,'success → commit','tiny',color=GREEN)
    reward(s,175,574,vertical=True)
    s.path('M175 758 C22 770 37 466 345 300',PURPLE,2.2,arrow=True)
    footer(s,579,804)
    save(s,4)

def candidate_05():
    s=Fig();header(s,'05  Policy orbit','Decisions orbit one Git Agent; a single history branch is promoted to candidate work.')
    # Actual graph to the left, policy at the center, construction to the right.
    s.ellipse(770,355,88,172,'#fbfafc','#dcd5ee',1.7,.85)
    pos={0:(115,315),1:(218,315),2:(321,315),3:(432,221),5:(541,221),6:(650,221),4:(432,435)}
    lineage(s,pos,[(0,1),(1,2),(2,3),(3,5),(5,6),(2,4)],scale=.78)
    s.text(228,168,'V_i = (Q_i, W_i)','small')
    s.text(650,170,'Previous HEAD','tiny')
    s.text(900,159,'q_t  + metrics  - legacy API','small')
    s.path('M790 170 C759 179 735 197 735 217 V288',BLUE,4,arrow=True)
    agent(s,735,350,scale=1.32)
    s.path('M713 384 C670 423 640 480 628 524',GRAY,1.2,dash='4 5')
    s.text(735,462,'resolve Q_t · choose under history','small')
    s.path('M691 335 C607 298 532 298 483 317',GRAY,1.9,arrow=True,dash='5 6')
    s.text(559,298,'INSPECT','tiny',color=GRAY)
    s.path('M695 383 C629 441 541 453 469 435',ORANGE,3.2,arrow=True)
    s.text(595,485,'COMMIT: (Q_t, v4, h_t)','small',color=ORANGE)
    s.path('M785 352 H893',ORANGE,3,arrow=True)
    router(s,927,352)
    s.text(927,436,'Reuse & Patch','small',color=ORANGE)
    s.text(927,458,'Fresh Solve: empty','tiny',color=GRAY)
    small_reuse(s,628,524)
    # The candidate is a crescent around the right of the central policy.
    s.path('M432 467 C451 518 508 543 571 574',LINE,1.5)
    s.text(560,561,'Historical W4','small')
    work(s,509,579,scale=.85)
    s.text(571,728,'immutable','tiny',color=INK)
    s.ellipse(1193,578,275,210,'#f7fcfa','#76b9ad',2,.9)
    s.text(1190,399,'isolated candidate','section')
    s.path('M633 634 C779 704 878 669 985 633',ORANGE,2.7,arrow=True)
    s.text(823,689,'fork W4','small',color=ORANGE)
    work(s,1000,540,scale=.83)
    s.text(1060,687,'W_t^0','small')
    updater(s,1177,601)
    s.text(1177,519,'Task-Native Update','tiny')
    s.path('M1121 602 H1145 M1208 602 H1243',ORANGE,2.3,arrow=True)
    work(s,1260,540,'result',.83)
    s.text(1320,687,'W~_t','small')
    s.path('M955 352 C1014 397 1047 471 1018 540',ORANGE,2.4,arrow=True)
    pair(s,1374,291,7,head=True,scale=1.12)
    s.text(1374,218,'New HEAD','small',color=GREEN)
    s.path('M1369 541 C1423 469 1434 381 1394 326',GREEN,2.4,arrow=True)
    s.path('M1375 651 C1430 691 1461 739 1461 779',GRAY,1.6,arrow=True,dash='5 5')
    s.text(1314,804,'failure: discard candidate only','tiny',color=GRAY)
    s.text(1320,724,'success: commit','tiny',color=GREEN)
    # Training follows a broad outer return arc to the same central policy.
    reward(s,210,550,vertical=True)
    s.path('M210 734 C45 762 49 554 372 323 C494 240 621 269 704 330',PURPLE,2.3,arrow=True)
    footer(s,72,817)
    save(s,5)

def bound_version(s,x,y,n,selected=False,head=False,scale=1):
    # A large bound Q/W specimen: two distinct layers locked inside one version.
    w,h=67*scale,88*scale; l=x-w/2;t=y-h/2
    edge=ORANGE if selected else GREEN if head else NAVY
    s.rect(l,t,w,h,'#fbfdfd',edge,20*scale,2.3 if selected or head else 1.5)
    s.rect(l+7*scale,t+7*scale,w-14*scale,30*scale,BLUE,'#9abbd2',10*scale,1)
    s.rect(l+7*scale,t+51*scale,w-14*scale,30*scale,TEAL,'#8cbab1',10*scale,1)
    s.path(f'M{x} {t+38*scale} V{t+50*scale}',edge,2.3)
    s.circle(x,t+44*scale,3*scale,edge,edge)
    s.text(x,t+29*scale,f'Q{n}','small')
    s.text(x,t+73*scale,f'W{n}','small')
    s.text(x+w/2+12*scale,y+6*scale,f'v{n}','small','start',color=edge if selected or head else NAVY,weight=700)

def candidate_06():
    s=Fig();header(s,'06  Paired-version loom','Each committed version visibly binds a requirement state to a recoverable checkpoint.')
    s.text(65,139,'feedback q_t','section','start')
    s.text(66,169,'+ evaluation metrics','small','start')
    s.text(66,196,'- legacy API','small','start')
    agent(s,251,291)
    s.path('M190 211 C220 232 231 245 239 260',BLUE,3,arrow=True)
    s.path('M221 309 C170 348 116 404 72 446',GRAY,1.2,dash='4 5')
    s.text(251,397,'Q_t from q_t + history','small')
    s.path('M280 262 C354 143 449 91 550 118',GRAY,1.6,arrow=True,dash='5 6')
    s.text(434,126,'INSPECT G_<t','small',color=GRAY)
    pos={0:(582,153),1:(582,261),2:(582,369),3:(406,489),5:(406,616),6:(406,744),4:(758,489)}
    s.text(735,146,'V_i = (Q_i, W_i)','small')
    for u,v in [(0,1),(1,2),(2,3),(3,5),(5,6),(2,4)]:
        x,y=pos[u];X,Y=pos[v]
        s.path(f'M{x} {y+46} C{x} {y+76} {X} {Y-78} {X} {Y-48}',INK,2,arrow=True)
    for n,(x,y) in pos.items():bound_version(s,x,y,n,selected=n==4,scale=.8)
    s.text(406,819,'Previous HEAD v6','tiny')
    s.path('M284 321 C404 426 591 476 719 489',ORANGE,3,arrow=True)
    s.text(544,463,'COMMIT (Q_t, b_t=v4, h_t)','small',color=ORANGE)
    small_reuse(s,72,446)
    s.path('M795 489 H878',ORANGE,3.2,arrow=True)
    router(s,911,489)
    s.text(911,550,'Reuse & Patch','small',color=ORANGE)
    s.text(911,571,'Fresh Solve: empty','tiny',color=GRAY)
    s.path('M939 489 H975',ORANGE,3,arrow=True)
    bound_version(s,1425,489,7,head=True,scale=1.03)
    s.text(1425,392,'New HEAD','small',color=GREEN)
    s.text(1340,440,'success → commit','tiny',color=GREEN)
    s.text(786,618,'Historical W4','small')
    s.path('M758 532 C754 570 782 602 786 630',LINE,1.4)
    work(s,722,642,scale=.82)
    s.text(786,779,'immutable','tiny',color=INK)
    s.rect(977,455,400,322,'none','#72b6aa',21,1.8,dash='7 5')
    s.text(993,645,'isolated candidate','small','start')
    s.path('M842 694 H1000',ORANGE,2.2,arrow=True)
    s.text(910,679,'fork','tiny',color=ORANGE)
    work(s,1014,659,scale=.68)
    s.text(1063,768,'W_t^0','tiny')
    updater(s,1176,705)
    s.text(1176,614,'Task-Native Update','tiny')
    s.path('M1113 707 H1142 M1206 707 H1223',ORANGE,2,arrow=True)
    work(s,1247,659,'result',.68)
    s.text(1296,768,'W~_t','tiny')
    s.path('M1345 659 C1407 628 1424 576 1425 535',GREEN,2.2,arrow=True)
    s.path('M1338 750 C1388 769 1420 792 1442 813',GRAY,1.5,arrow=True,dash='5 5')
    s.text(1335,796,'failure: discard candidate','tiny',color=GRAY)
    reward(s,174,598,vertical=True)
    s.path('M174 782 C5 736 23 523 222 291',PURPLE,2.2,arrow=True)
    footer(s,880,820)
    save(s,6)

if __name__=='__main__':
    for fn in (candidate_01,candidate_02,candidate_03,candidate_04,candidate_05,candidate_06):fn()
    print('Rendered six SVG figures, high-resolution PNGs, and 180-mm previews')
