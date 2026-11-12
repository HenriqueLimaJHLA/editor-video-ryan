#!/usr/bin/env bash
# Uso:
#   bash install.sh            clona os kits nas versões fixadas em kits.lock e registra a skill
#   bash install.sh --deps     idem + dependências Python/Node
#   bash install.sh --update   puxa a versão mais nova de cada kit e atualiza kits.lock
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
PY="$(command -v python || command -v python3)"
mkdir -p "$ROOT/vendor"
while read -r dir repo sha; do
  [ -z "$dir" ] && continue
  D="$ROOT/vendor/$dir"
  if [ ! -d "$D/.git" ]; then git clone -q "https://github.com/$repo.git" "$D"; fi
  if [ "$1" = "--update" ]; then
    git -C "$D" fetch -q origin && git -C "$D" checkout -q --detach origin/HEAD
  else
    git -C "$D" fetch -q origin "$sha" 2>/dev/null || git -C "$D" fetch -q --unshallow 2>/dev/null || true
    git -C "$D" checkout -q --detach "$sha"
  fi
  echo "$dir @ $(git -C "$D" rev-parse --short HEAD)"
done < "$ROOT/kits.lock"

if [ "$1" = "--update" ]; then
  tmp="$(mktemp)"; while read -r dir repo sha; do echo "$dir $repo $(git -C "$ROOT/vendor/$dir" rev-parse HEAD)"; done < "$ROOT/kits.lock" > "$tmp"; mv "$tmp" "$ROOT/kits.lock"
  echo "kits.lock atualizado — revise o diff antes de commitar"
fi

if [ "$1" = "--deps" ]; then
  echo "==> dependências"
  "$PY" -m pip install -q playwright imageio-ffmpeg numpy pillow faster-whisper && "$PY" -m playwright install chromium || true
  (cd "$ROOT/vendor/video-use" && "$PY" -m pip install -q -e .) || true
  (cd "$ROOT/vendor/herk-edit-kit" && npm ci) || true
  (cd "$ROOT/vendor/OpenMontage" && "$PY" -m pip install -q -r requirements.txt && cd remotion-composer && npm install) || true
fi

"$PY" "$ROOT/scripts/catalogo.py"

DEST="$HOME/.claude/skills/editor-video-ryan"
mkdir -p "$HOME/.claude/skills"
if [ ! -e "$DEST" ]; then
  if command -v cmd.exe >/dev/null; then cmd.exe //c mklink //J "$(cygpath -w "$DEST")" "$(cygpath -w "$ROOT")" >/dev/null
  else ln -s "$ROOT" "$DEST"; fi
fi
echo "Pronto: skill registrada em $DEST"
"$PY" "$ROOT/scripts/doctor.py"
