"""Download primary-source PDFs for visual screening; never overwrite originals."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import hashlib
import json
import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "02_verified_papers"
OUT.mkdir(parents=True, exist_ok=True)

CANDIDATES = [
    ("graph_of_thoughts", "Graph of Thoughts: Solving Elaborate Problems with Large Language Models", "AAAI 2024", "https://ojs.aaai.org/index.php/AAAI/article/view/29720", "https://ojs.aaai.org/index.php/AAAI/article/download/29720/31236"),
    ("swe_agent", "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", "NeurIPS 2024", "https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html", "https://proceedings.neurips.cc/paper_files/paper/2024/file/5a7c947568c1b1328ccc5230172e1e7c-Paper-Conference.pdf"),
    ("vima", "VIMA: Robot Manipulation with Multimodal Prompts", "ICML 2023", "https://proceedings.mlr.press/v202/jiang23b.html", "https://proceedings.mlr.press/v202/jiang23b/jiang23b.pdf"),
    ("var", "Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction", "NeurIPS 2024 Best Paper", "https://proceedings.neurips.cc/paper_files/paper/2024/hash/9a24e284b187f662681440ba15c416fb-Abstract-Conference.html", "https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf"),
    ("generative_agents", "Generative Agents: Interactive Simulacra of Human Behavior", "UIST 2023", "https://doi.org/10.1145/3586183.3606763", "https://3dvar.com/Park2023Generative.pdf"),
    ("autogen", "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation", "COLM 2024", "https://openreview.net/forum?id=BAakY1hNKS", "https://openreview.net/attachment?id=BAakY1hNKS&name=pdf"),
    ("self_refine", "Self-Refine: Iterative Refinement with Self-Feedback", "NeurIPS 2023", "https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html", "https://proceedings.neurips.cc/paper_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf"),
    ("openvla", "OpenVLA: An Open-Source Vision-Language-Action Model", "CoRL 2024", "https://mlanthology.org/corl/2024/kim2024corl-openvla/", "https://openreview.net/pdf/abf32802eb323064805ffb39688f56254876b4be.pdf"),
    ("rap", "Reasoning with Language Model is Planning with World Model", "EMNLP 2023", "https://aclanthology.org/2023.emnlp-main.507/", "https://aclanthology.org/2023.emnlp-main.507.pdf"),
    ("octo", "Octo: An Open-Source Generalist Robot Policy", "RSS 2024", "https://www.roboticsproceedings.org/rss20/p090.html", "https://www.roboticsproceedings.org/rss20/p090.pdf"),
    ("diffusion_policy", "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion", "RSS 2023", "https://www.roboticsproceedings.org/rss19/p026.html", "https://www.roboticsproceedings.org/rss19/p026.pdf"),
    ("saycan", "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances", "CoRL 2022", "https://proceedings.mlr.press/v205/ichter23a.html", "https://proceedings.mlr.press/v205/ichter23a/ichter23a.pdf"),
    ("rt2", "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control", "CoRL 2023", "https://mlanthology.org/corl/2023/zitkovich2023corl-rt2/", "https://robotics-transformer2.github.io/assets/rt2.pdf"),
]

def get(item):
    slug, title, venue, record, url = item
    path = OUT / f"{slug}.pdf"
    try:
        if not path.exists():
            r = requests.get(url, timeout=90, headers={"User-Agent": "GitHarness visual research (academic figure study)"})
            r.raise_for_status()
            if not r.content.startswith(b"%PDF"):
                raise ValueError(f"response is not PDF: {r.headers.get('content-type')}")
            path.write_bytes(r.content)
        data = path.read_bytes()
        return dict(slug=slug, title=title, venue=venue, publication_record=record, pdf_url=url,
                    local_pdf=f"02_verified_papers/{slug}.pdf", bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), download="ok")
    except Exception as exc:
        return dict(slug=slug, title=title, venue=venue, publication_record=record, pdf_url=url,
                    local_pdf=None, download=f"failed: {exc}")

with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(get, CANDIDATES))
(ROOT / "01_screening" / "new_candidate_sources.json").write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps([{"slug": x["slug"], "download": x["download"], "bytes": x.get("bytes")} for x in results], indent=2))
