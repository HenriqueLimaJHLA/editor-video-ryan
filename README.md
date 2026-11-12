# editor-video-ryan

Uma skill do Claude Code que reúne 8 kits de edição de vídeo e escolhe o certo para cada pedido.

| Kit | Para quê |
|---|---|
| [video-use](https://github.com/browser-use/video-use) | corta pausas, legenda, cor (vídeo falado) |
| [ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | cortar, comprimir, converter, exportar por rede (local) |
| [Herk Edit Kit](https://github.com/nateherkai/herk-edit-kit) | 15 skills para Reels/Shorts |
| [Claude GIF](https://github.com/AgriciDaniel/claude-gif) | GIFs |
| [Claude Motion Design](https://github.com/howseen-ai/claude-motion-design) | motion design em código |
| [Remotion Skills](https://github.com/remotion-dev/skills) | vídeo em código (React) |
| [Video Editor Skills](https://github.com/appariciojunior/video-editor-skills) | primeiro corte no DaVinci Resolve Studio |
| [OpenMontage](https://github.com/calesthio/OpenMontage) | estúdio completo, do roteiro ao vídeo |

## Instalar
```bash
bash install.sh          # clona os kits em vendor/ e registra a skill
bash install.sh --deps   # idem + instala dependências Python/Node (demorado)
```
Requisitos: git, ffmpeg, Python 3.10+, Node 22+. Os kits não são versionados aqui (`vendor/` é ignorado); `install.sh` também os atualiza.

## Usar
No Claude Code, peça normalmente: *"edita esse vídeo num Reels de 60s com legenda"* ou `/editor-video-ryan`.
