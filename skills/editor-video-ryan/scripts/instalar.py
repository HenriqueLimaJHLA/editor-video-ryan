"""Instalador do Editor de Vídeo Ryan.
Uso: python scripts/instalar.py [--completo | --atualizar]
  (sem opção)   baixa os kits nas versões testadas e ativa a skill
  --completo    idem + instala os programas extras (demora 10-30 min)
  --atualizar   baixa a versão mais nova de cada kit
"""
import os, shutil, subprocess, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
ROOT = Path(__file__).resolve().parent.parent
V, LOCK = Path(os.environ.get("EDITOR_VIDEO_KITS") or Path.home() / ".editor-video-ryan" / "kits"), ROOT / "kits.lock"
PY = sys.executable
modo = sys.argv[1] if len(sys.argv) > 1 else ""

def passo(msg): print(f"\n>> {msg}")
def run(cmd, cwd=None, quiet=True):
    r = subprocess.run(cmd, cwd=cwd, capture_output=quiet, text=True, shell=(os.name == "nt" and cmd[0] == "npm"))
    return r.returncode == 0

def precisa(prog, como):
    if shutil.which(prog): return True
    print(f"   [falta] {prog} não está instalado. {como}")
    return False

passo("Conferindo programas básicos")
win = os.name == "nt"
ok = precisa("git", "Instale: winget install Git.Git" if win else "Instale: brew install git")
precisa("ffmpeg", "Instale: winget install Gyan.FFmpeg" if win else "Instale: brew install ffmpeg")
precisa("node", "Instale: winget install OpenJS.NodeJS.LTS" if win else "Instale: brew install node")
if not ok:
    sys.exit("\nSem o git não dá para baixar os kits. Instale e rode de novo.")

passo("Baixando os 8 kits de edição (na primeira vez demora alguns minutos)")
V.mkdir(parents=True, exist_ok=True)
linhas = [l.split() for l in LOCK.read_text(encoding="utf-8").splitlines() if l.strip()]
novas = []
for nome, repo, sha in linhas:
    d = V / nome
    if not (d / ".git").exists():
        print(f"   baixando {nome}...")
        run(["git", "clone", "-q", f"https://github.com/{repo}.git", str(d)])
    if modo == "--atualizar":
        run(["git", "fetch", "-q", "origin"], d); run(["git", "checkout", "-q", "--detach", "origin/HEAD"], d)
    else:
        if not run(["git", "checkout", "-q", "--detach", sha], d):
            run(["git", "fetch", "-q", "--unshallow"], d); run(["git", "fetch", "-q", "origin", sha], d)
            run(["git", "checkout", "-q", "--detach", sha], d)
    atual = subprocess.run(["git", "rev-parse", "HEAD"], cwd=d, capture_output=True, text=True).stdout.strip()
    print(f"   ok  {nome}")
    novas.append(f"{nome} {repo} {atual}")
if modo == "--atualizar":
    LOCK.write_text("\n".join(novas) + "\n", encoding="utf-8")
    print("   versões novas anotadas em kits.lock")

if modo == "--completo":
    passo("Instalando programas extras (pode demorar bastante, não feche a janela)")
    run([PY, "-m", "pip", "install", "-q", "playwright", "imageio-ffmpeg", "numpy", "pillow", "faster-whisper"], quiet=False)
    run([PY, "-m", "playwright", "install", "chromium"], quiet=False)
    run([PY, "-m", "pip", "install", "-q", "-e", "."], V / "video-use", quiet=False)
    if shutil.which("npm"):
        run(["npm", "ci"], V / "herk-edit-kit", quiet=False)
        run([PY, "-m", "pip", "install", "-q", "-r", "requirements.txt"], V / "OpenMontage", quiet=False)
        run(["npm", "install"], V / "OpenMontage" / "remotion-composer", quiet=False)

passo("Ativando a skill no Claude Code")
subprocess.run([PY, str(ROOT / "scripts" / "catalogo.py")])
via_plugin = "plugins" in ROOT.parts  # instalada pelo /plugin: o Claude Code já registra
dest = Path.home() / ".claude" / "skills" / "editor-video-ryan"
dest.parent.mkdir(parents=True, exist_ok=True)
if via_plugin:
    pass
elif not dest.exists():
    if win: subprocess.run(["cmd", "/c", "mklink", "/J", str(dest), str(ROOT)], capture_output=True)
    else: dest.symlink_to(ROOT)
print("   ok  skill ativa" + ("" if via_plugin else f" em {dest}"))

passo("Diagnóstico final")
subprocess.run([PY, str(ROOT / "scripts" / "doctor.py")])
print("\nPRONTO! Abra o Claude Code e peça, por exemplo:")
print('   "edita esse vídeo num Reels de 60 segundos com legenda"')
