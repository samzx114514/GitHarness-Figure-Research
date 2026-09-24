"""Original low-fidelity composition studies; deliberately not a final Figure 2."""
from pathlib import Path
from html import escape
P=Path(__file__).parent
N='#23364C';O='#CE6C32';G='#388365';X='#778391';R='#84689D';B='#E8F1FA';M='#E1F1E9'
class Canvas:
 def __init__(self,title,subtitle):
  self.s=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720"><defs>']
  for i,c in [('n',N),('o',O),('g',G),('x',X),('r',R)]: self.s.append(f'<marker id="{i}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L8 4 L0 8Z" fill="{c}"/></marker>')
  self.s.append('</defs><rect width="1200" height="720" fill="white"/>')
  self.t(30,35,title,25,bold=True);self.t(30,63,subtitle,16,X)
 def t(self,x,y,s,size=19,c=N,bold=False,anchor='start'):
  self.s.append(f'<text x="{x}" y="{y}" font-family="Arial,Helvetica,sans-serif" font-size="{size}" fill="{c}" font-weight="{700 if bold else 400}" text-anchor="{anchor}">{escape(s)}</text>')
 def rect(self,x,y,w,h,fill='white',stroke='none',dash=False,rx=5):
  self.s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"'+(' stroke-dasharray="6 5"' if dash else '')+'/>')
 def edge(self,d,c=N,dash=False,arrow=True,w=2):
  k={N:'n',O:'o',G:'g',X:'x',R:'r'}[c]
  self.s.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'+(' stroke-dasharray="5 5"' if dash else '')+(f' marker-end="url(#{k})"' if arrow else '')+'/>')
 def pair(self,x,y,n,c=N,label=None,side=False):
  self.rect(x,y,42,32,B,rx=0);self.rect(x+42,y,42,32,M,rx=0);self.rect(x,y,84,32,'none',c,rx=4)
  self.t(x+21,y+22,'Q'+str(n),17,anchor='middle');self.t(x+63,y+22,'W'+str(n),17,anchor='middle')
  self.t(x-8 if side else x+42,y+22 if side else y+53,label or 'v'+str(n),17,c,True,'end' if side else 'middle')
 def agent(self,x,y):
  self.rect(x,y,145,54,'#F4F0F8',R);self.t(x+72,y+33,'Git Agent',22,N,True,'middle')
 def footer(self):
  self.t(30,687,'COMPOSITION STUDY ONLY',14,X,True)
  self.t(300,687,'All historical nodes: Vᵢ = (Qᵢ, Wᵢ)  ·  Solid edges: ancestry / execution; orange: active choice',14,X)
  self.t(30,709,'Details omitted for layout comparison; no new algorithmic components are proposed.',14,X)
 def save(self,name):
  self.footer();self.s.append('</svg>');(P/(name+'.svg')).write_text('\n'.join(self.s),encoding='utf-8')

# A: the graph is the continuous scaffold; one edge is enlarged rather than a second execution pipeline.
c=Canvas('A  Graph as the scaffold','One historical graph; requirement selection is an overlay; execution is an edge-level lens.')
c.t(50,118,'qₜ  + metrics / − legacy API',19);c.edge('M307 111 H348',O);c.agent(360,86)
c.t(540,109,'Qₜ · full requirement',20);c.edge('M505 113 H529',N)
for d in ['M164 224 H210','M294 224 H350','M434 224 C470 224 478 164 520 164','M604 164 H690','M774 164 H875','M434 224 C470 224 478 314 520 314'] :c.edge(d)
for x,y,n in [(80,208,0),(210,208,1),(350,208,2),(520,148,3),(690,148,5),(875,148,6)]:c.pair(x,y,n)
c.t(917,136,'Current HEAD',17,N,True,'middle')
c.rect(489,272,152,108,'#FFF5ED',O,True);c.edge('M434 224 C470 224 478 314 518 314');c.pair(520,298,4,O);c.t(490,401,'Compatible under Qₜ',18,O)
c.edge('M432 140 C430 262 472 278 528 296',O);c.t(283,293,'select',17,O)
c.t(47,339,'INSPECT · read-only',17,X);c.t(47,367,'Exact match: ∅',17,X)
c.edge('M604 314 H753',O);c.rect(765,292,158,48,'#F6FAF8',X,True);c.t(844,322,'(Qₜ, W̃ₜ)',23,anchor='middle')
c.edge('M923 314 H1020',G);c.pair(1032,298,7,G,'v7 · New HEAD')
c.t(658,299,'fork',17,O);c.t(955,299,'commit',17,G)
c.rect(650,273,290,80,'none',X,True)
c.edge('M700 355 V430 H620 V443',X,True,False);c.edge('M935 355 L1084 443',X,True,False)
c.rect(579,447,546,154,'#FAFCFB','#B2C5BD',True)
c.t(600,475,'Edge lens · isolated candidate',20,N,True)
c.t(330,504,'W4 · immutable',18);c.edge('M480 498 H601',O);c.t(518,486,'fork',16,O)
c.t(603,508,'Wₜ⁰',24);c.edge('M656 499 H700',O);c.t(710,507,'Update Agent',19);c.edge('M842 499 H886',O);c.t(899,508,'W̃ₜ',24)
c.t(603,541,'Core / Utilities preserved',18,G);c.t(603,568,'Evaluation′ updated',18,O);c.t(865,568,'Legacy API excluded',17,X)
c.t(325,540,'COMMIT record',17,O);c.t(325,565,'(Qₜ, v4, hₜ) → Router',18,O)
c.t(590,625,'Success → v7     Failure → discard candidate only',18)
c.t(48,590,'Outcome + Query rewards',17,R);c.t(48,618,'Harness RL / GRPO',19,R,True)
c.edge('M215 629 H20 V77 H430 V84',R,True)
c.save('A_graph_scaffold')

# B: correspondence between requirement and work is the global organizing principle.
c=Canvas('B  Paired-state correspondence','Requirement and work occupy aligned lanes; Qₜ constrains each stage of candidate construction.')
c.t(35,116,'Recoverable history',21,N,True)
for d in ['M90 157 V183','M90 216 V242','M90 274 L222 201','M264 166 V143','M306 126 H347','M90 274 V328']:c.edge(d)
for x,y,n in [(48,125,0),(48,184,1),(48,243,2),(222,168,3),(222,110,5),(348,110,6),(48,328,4)]:c.pair(x,y,n,O if n==4 else N,side=x<100 or (x==222 and y==110))
c.t(353,99,'HEAD',16);c.t(42,406,'bₜ = v4',18,O,True)
c.t(478,117,'qₜ + historical Q',20);c.edge('M678 110 H725',O);c.agent(740,85)
c.rect(472,170,647,71,B);c.t(492,199,'REQUIREMENT',15,N,True);c.t(492,226,'Qₜ: evaluation metrics; no legacy API',21)
c.edge('M812 140 V166',O)
c.t(472,289,'COMMIT (Qₜ, v4, hₜ) → Router → Reuse & Patch',20,O)
c.rect(400,320,721,245,'#FCFDFB','#B2C5BD',True);c.t(423,348,'WORK · isolated candidate workspace',20,N,True)
c.edge('M132 344 H280 V420 H441',O);c.t(233,408,'fork W4',18,O)
c.t(451,396,'Wₜ⁰',26);c.t(891,396,'W̃ₜ',26)
for j,(a,b,col) in enumerate([('Core Logic','Core Logic',G),('Evaluation','Evaluation′',O),('Legacy API','— excluded',X),('Utilities','Utilities',G)]):
 y=426+32*j;c.t(451,y,a,19);c.t(866,y,b,19,col)
c.edge('M611 446 H660',N);c.t(673,452,'Update Agent',20);c.edge('M812 446 H854',N)
c.edge('M1015 241 V366',N);c.t(1031,303,'Qₜ, hₜ',18)
c.edge('M1119 458 H1153 V595 H1024',G);c.pair(925,580,7,G,'v7 · New HEAD')
c.t(605,609,'Success commits paired state',18,G);c.t(413,551,'Failure: discard candidate only',16,X)
c.t(30,465,'Exact match: ∅',17,X);c.t(30,495,'Fresh Solve: ∅ → Wₜ⁰',17,X)
c.t(30,602,'Outcome + Query rewards → Harness RL / GRPO',17,R)
c.edge('M450 653 H1168 V77 H812 V83',R,True)
c.save('B_paired_lanes')

# C: one policy is the shared junction of the decision, execution, and learning loops.
c=Canvas('C  Shared-policy orbit','History surrounds one policy; selection and training return to different objects.')
c.t(380,250,'qₜ → Qₜ',21);c.edge('M469 264 V285',O)
for d in ['M150 175 H205','M289 175 H345','M429 175 H485','M569 175 H635','M719 175 H782','M429 175 C454 255 263 272 255 350']:c.edge(d)
for x,y,n in [(66,159,0),(205,159,1),(345,159,2),(485,159,3),(635,159,5),(782,159,6)]:c.pair(x,y,n)
c.t(824,145,'Current HEAD',16,N,True,'middle')
c.rect(180,329,161,111,'#FFF5ED',O,True);c.edge('M429 175 C454 255 263 272 255 350');c.pair(214,354,4,O)
c.t(180,464,'Compatible under Qₜ',17,O)
c.agent(430,290);c.edge('M430 316 C369 312 355 366 305 370',O);c.t(334,339,'select',17,O)
c.edge('M495 289 V218',X,True);c.t(515,236,'INSPECT',16,X)
c.edge('M575 317 H706',O);c.t(715,313,'COMMIT record',19,O,True);c.t(715,341,'(Qₜ, v4, hₜ)',22)
c.edge('M807 352 V382',O);c.t(777,408,'Router',20,N,True)
c.t(886,405,'Fresh: ∅',17,X);c.t(751,439,'Reuse & Patch',18,O)
c.rect(525,480,487,125,'#FAFCFB','#B2C5BD',True);c.t(546,507,'Isolated candidate workspace',20,N,True)
c.edge('M298 373 H375 V547 H539',O);c.t(379,536,'fork W4',17,O)
c.t(549,551,'Wₜ⁰',25);c.edge('M603 542 H652',N);c.t(664,550,'Update Agent',19);c.edge('M796 542 H845',N);c.t(859,550,'W̃ₜ',25)
c.edge('M813 445 V476',O)
c.t(549,585,'preserve / update / exclude',18)
c.edge('M1012 543 H1050',G);c.pair(1063,526,7,G,'v7 · New HEAD')
c.t(729,633,'Failure → discard candidate only',17,X)
c.t(68,529,'REUSE → return Vₖ',17,X);c.t(68,556,'Exact match: ∅',17,X)
c.t(953,139,'Rewards',20,R,True);c.t(953,169,'Outcome + Query',17,R);c.t(953,202,'Harness RL / GRPO',18,R)
c.edge('M1045 217 V270 H548 V287',R,True)
c.save('C_shared_policy')

# D: a large central work transformation, with history as an input source and the new branch as output.
c=Canvas('D  Work transformation at the center','A small history supplies W4; the main visual event is the candidate state change.')
c.t(31,114,'Historical graph',21,N,True)
for d in ['M93 151 V184','M93 216 V249','M135 265 H196 V176 H222','M306 160 V127 H331','M415 111 H448','M93 281 V345']:c.edge(d)
for x,y,n in [(51,119,0),(51,184,1),(51,249,2),(222,144,3),(332,95,5),(448,95,6),(51,346,4)]:c.pair(x,y,n,O if n==4 else N,side=x<100 or (x==222 and y==110))
c.t(490,85,'HEAD',16);c.t(32,426,'W4 immutable',18,O)
c.t(591,110,'qₜ: + metrics / − legacy API',20);c.agent(667,134)
c.edge('M740 113 V132',O);c.edge('M667 157 H577 V361 H141',O);c.t(329,350,'select bₜ = v4',18,O)
c.t(617,223,'COMMIT (Qₜ, v4, hₜ)',22,O);c.edge('M740 188 V201',O)
c.t(666,262,'Router · Reuse & Patch',19,O);c.edge('M740 229 V244',O)
c.rect(315,387,650,217,'#FAFCFB','#A6C2B5',True);c.t(335,416,'Isolated candidate',21,N,True)
c.edge('M135 363 H238 V469 H332',O);c.t(241,453,'fork',17,O)
c.t(340,454,'Wₜ⁰',25);c.t(790,454,'W̃ₜ under Qₜ',25)
for j,(a,b,col) in enumerate([('Core Logic','Core Logic',G),('Evaluation','Evaluation′',O),('Legacy API','— excluded',X),('Utilities','Utilities',G)]):
 y=484+31*j;c.t(340,y,a,19);c.t(790,y,b,19,col)
c.rect(529,459,214,72,'#F0F5F2',N);c.t(636,486,'Task-Native',19,N,False,'middle');c.t(636,516,'Update Agent',20,N,True,'middle')
c.edge('M484 495 H524',N);c.edge('M743 495 H779',N)
c.edge('M739 275 V370 H636 V455',O);c.t(752,321,'Qₜ, hₜ',18)
c.edge('M965 496 H1026',G);c.pair(1040,479,7,G,'v7 · New HEAD');c.t(1005,462,'commit',17,G)
c.t(549,633,'Failure → discard candidate only',17,X)
c.t(32,497,'Exact match: ∅',17,X);c.t(32,526,'REUSE bypass',17,X);c.t(32,573,'Fresh: ∅ → Wₜ⁰',17,X)
c.t(970,122,'Outcome + Query',18,R);c.t(970,154,'rewards',18,R);c.t(970,194,'Harness RL / GRPO',18,R)
c.edge('M1072 208 V247 H899 V161 H816',R,True)
c.save('D_central_transformation')
print('Four original SVG composition studies written.')
