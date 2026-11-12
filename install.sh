#!/usr/bin/env bash
# Instala/atualiza os 8 kits em vendor/ e registra a skill em ~/.claude/skills/editor-video-ryan
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$ROOT/vendor"
repos="video-use:browser-use/video-use ffmpeg-skill:kajisho5/ffmpeg-skill herk-edit-kit:nateherkai/herk-edit-kit claude-gif:AgriciDaniel/claude-gif claude-motion-design:howseen-ai/claude-motion-design remotion-skills:remotion-dev/skills video-editor-skills:appariciojunior/video-editor-skills OpenMontage:calesthio/OpenMontage"
for item in $repos; do
  dir="${item%%:*}"; repo="${item#*:}"
  if [ -d "$ROOT/vendor/$dir/.git" ]; then git -C "$ROOT/vendor/$dir" pull -q --ff-only && echo "atualizado $dir"
  else git clone -q --depth 1 "https://github.com/$repo.git" "$ROOT/vendor/$dir" && echo "clonado $dir"; fi
done

if [ "$1" = "--deps" ]; then
  echo "==> dependências"
  pip install -q playwright imageio-ffmpeg numpy pillow && python -m playwright install chromium || true
  (cd "$ROOT/vendor/video-use" && pip install -q -e .) || true
  (cd "$ROOT/vendor/herk-edit-kit" && npm ci) || true
  (cd "$ROOT/vendor/OpenMontage" && pip install -q -r requirements.txt && cd remotion-composer && npm install) || true
fi

# registra a skill (junction no Windows, symlink no resto)
DEST="$HOME/.claude/skills/editor-video-ryan"
mkdir -p "$HOME/.claude/skills"
if [ ! -e "$DEST" ]; then
  if command -v cmd.exe >/dev/null; then cmd.exe //c mklink //J "$(cygpath -w "$DEST")" "$(cygpath -w "$ROOT")" >/dev/null
  else ln -s "$ROOT" "$DEST"; fi
fi
echo "Pronto: skill registrada em $DEST"
