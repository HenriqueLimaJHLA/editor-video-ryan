"""Gera references/catalogo.md com todas as sub-skills dos kits. Uso: python scripts/catalogo.py"""
import re
import os
from pathlib import Path
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
V = Path(os.environ.get("EDITOR_VIDEO_KITS") or Path.home() / ".editor-video-ryan" / "kits")
GLOBS = {"video-use": ["SKILL.md", "skills/*/SKILL.md"], "ffmpeg-skill": ["SKILL.md"],
         "herk-edit-kit": [".claude/skills/*/SKILL.md"], "claude-gif": ["skills/*/SKILL.md"],
         "claude-motion-design": ["skill/*/SKILL.md"], "remotion-skills": ["skills/*/SKILL.md"],
         "video-editor-skills": ["skills/*/SKILL.md"], "OpenMontage": [".agents/skills/*/SKILL.md"]}

def meta(p):
    t = p.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"---\s*\n(.*?)\n---", t, re.S)
    fm = m.group(1) if m else ""
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    d = re.search(r"^description:\s*(.*?)(?=^\w[\w-]*:|\Z)", fm, re.M | re.S)
    desc = re.sub(r"\s+", " ", d.group(1)).strip(" >|'\"") if d else ""
    return (name.group(1).strip() if name else p.parent.name), desc[:220]

out = ["# Catálogo de sub-skills\n", "Gerado por `scripts/catalogo.py`. Caminhos relativos à pasta dos kits (`~/.editor-video-ryan/kits/`).\n"]
for kit, globs in GLOBS.items():
    files = sorted({f for g in globs for f in (V / kit).glob(g)})
    out.append(f"\n## {kit} ({len(files)})\n")
    for f in files:
        n, d = meta(f)
        out.append(f"- **{n}** — `{f.relative_to(V).as_posix()}` — {d}")
(ROOT / "references" / "catalogo.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("catálogo:", sum(1 for l in out if l.startswith("- ")), "skills")
