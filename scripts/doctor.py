"""Diagnóstico do estúdio: ferramentas, chaves e kits. Uso: python scripts/doctor.py"""
import os, shutil, subprocess, sys
from pathlib import Path
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
V = ROOT / "vendor"
ok = lambda b: "OK " if b else "-- "

def ver(cmd):
    exe = shutil.which(cmd[0])
    if not exe:
        return None
    try:
        out = subprocess.run([exe, *cmd[1:]], capture_output=True, text=True, timeout=20)
        return (out.stdout or out.stderr).strip().splitlines()[0]
    except Exception:
        return "?"

print("== Ferramentas")
for name, cmd in [("ffmpeg", ["ffmpeg", "-version"]), ("ffprobe", ["ffprobe", "-version"]),
                  ("python", [sys.executable, "--version"]), ("node", ["node", "--version"]),
                  ("git", ["git", "--version"]), ("faster-whisper", ["faster-whisper", "--help"])]:
    v = ver(cmd) if name != "python" else sys.version.split()[0]
    print(f"  {ok(v)}{name:15} {v or 'não encontrado'}")
try:
    import playwright  # noqa
    print(f"  {ok(True)}playwright      instalado")
except ImportError:
    print(f"  {ok(False)}playwright      não instalado (Motion Design / Claude GIF SVG)")

print("== Chaves (variáveis de ambiente)")
for k, uso in [("ELEVENLABS_API_KEY", "video-use, Herk"), ("GOOGLE_API_KEY", "Claude GIF com IA"),
               ("GEMINI_API_KEY", "Claude GIF com IA"), ("PEXELS_API_KEY", "Motion Design / OpenMontage")]:
    print(f"  {ok(os.environ.get(k))}{k:20} {uso}")

print("== Kits")
kits = {"video-use": "SKILL.md", "ffmpeg-skill": "SKILL.md", "herk-edit-kit": "CLAUDE.md",
        "claude-gif": "skills/claude-gif/SKILL.md", "claude-motion-design": "skill/motion-design/SKILL.md",
        "remotion-skills": "skills/remotion-create/SKILL.md",
        "video-editor-skills": "skills/edit-video/SKILL.md", "OpenMontage": "CLAUDE.md"}
extra = {"herk-edit-kit": "node_modules", "OpenMontage": "remotion-composer/node_modules"}
missing = 0
for k, f in kits.items():
    present = (V / k / f).exists()
    missing += not present
    note = ""
    if present and k in extra and not (V / k / extra[k]).exists():
        note = "  (dependências Node não instaladas: install.sh --deps)"
    print(f"  {ok(present)}{k}{note}")
if missing:
    print("\nFaltam kits: rode  bash install.sh")
