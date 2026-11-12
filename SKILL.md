---
name: editor-video-ryan
description: Estúdio de edição de vídeo que reúne 8 kits de skills (video-use, ffmpeg-skill, Herk Edit Kit, Claude GIF, Claude Motion Design, Remotion, Video Editor Skills/DaVinci, OpenMontage). Use sempre que a pessoa pedir para editar, cortar, legendar, comprimir, converter, exportar (Reels/TikTok/Shorts/YouTube), fazer GIF, motion design, vídeo animado em código, vídeo explicativo, primeiro corte no DaVinci Resolve, ou qualquer tarefa com arquivos de vídeo/áudio — mesmo sem dizer "skill".
---

# Editor de Vídeo Ryan — roteador

Esta skill não edita sozinha: ela escolhe o kit certo, carrega o SKILL.md dele e segue as instruções dele à risca.

`$ROOT` = a pasta desta skill (onde está este arquivo). Os kits ficam em `$ROOT/vendor/`.
Se `vendor/` estiver vazio ou faltando um kit, rode `bash $ROOT/install.sh`.

## Passo 1 — escolher o kit

| Pedido | Kit | Carregue |
|---|---|---|
| Vídeo falado (talking head): tirar pausas, "é…", falsos começos, cor, legenda | **video-use** | `vendor/video-use/SKILL.md` (precisa `ELEVENLABS_API_KEY`) |
| Cortar trecho, juntar, comprimir, mudar formato (9:16, 1:1), limpar/nivelar áudio, logo, exportar por rede — local, sem chave | **ffmpeg-skill** | `vendor/ffmpeg-skill/SKILL.md` |
| Reels/Shorts semanais: gancho, B-roll, música, cards animados (HyperFrames) | **Herk Edit Kit** | trabalhe DENTRO de `vendor/herk-edit-kit/` seguindo o `CLAUDE.md` dele; skills em `vendor/herk-edit-kit/.claude/skills/<nome>/SKILL.md` (comece por `short-form-edit` ou `edit-video`) |
| GIF (de vídeo, imagens, SVG, IA), otimizar para Discord etc. | **Claude GIF** | `vendor/claude-gif/skills/claude-gif/SKILL.md` (sub-skills: `-convert`, `-create`, `-edit`, `-generate`, `-optimize`) |
| Motion design em código, vídeo de lançamento no ritmo da música, refazer vídeo de referência | **Claude Motion Design** | `vendor/claude-motion-design/skill/motion-design/SKILL.md` |
| Vídeo em código React/Remotion, vídeos em série com dados (um por cliente/produto), mapas | **Remotion** | `vendor/remotion-skills/skills/remotion-create/SKILL.md` (+ `remotion-studio`, `remotion-render`, `remotion-captions`, `remotion-best-practices`…) |
| Primeiro corte de vlog/aula no DaVinci Resolve Studio | **Video Editor Skills** | `vendor/video-editor-skills/skills/video-editor-setup/SKILL.md` na 1ª vez, depois `edit-video/SKILL.md` |
| Vídeo do zero (roteiro, narração, imagens, música, legenda): explicativo, documentário | **OpenMontage** | trabalhe DENTRO de `vendor/OpenMontage/` seguindo o `CLAUDE.md`/`AGENT_GUIDE.md` dele |

Regras de escolha:
- Só cortar/legendar vídeo falado → video-use; sem chave ElevenLabs → ffmpeg-skill (+ faster-whisper para legenda).
- Sem gravação nenhuma → Motion Design (rápido, grátis), Remotion (reutilizável) ou OpenMontage (produção completa).
- Ambíguo? Faça UMA pergunta curta oferecendo 2-3 kits, com o motivo de cada.
- Pode encadear kits (ex.: video-use para o corte → ffmpeg-skill para exportar Reels → Claude GIF para um teaser).

## Passo 2 — executar
1. Leia o SKILL.md escolhido inteiro (e os arquivos que ele mandar ler). Caminhos relativos dentro dele são relativos à pasta DELE.
2. Confira dependências (`ffmpeg`, `python`, `node`, chaves). Faltou algo → explique e ofereça instalar.
3. Nunca altere o vídeo original: trabalhe em cópia/pasta de saída.
4. Teste primeiro com trecho curto (1-2 min) quando o material for longo.
5. Responda sempre em português.

## Custos / licenças (avise antes de usar)
- video-use, Herk: ElevenLabs (pago). Claude GIF com IA: chave Google (Veo US$0,60–4/clipe).
- Video Editor Skills: DaVinci Resolve **Studio** (pago); licença CC BY-NC (proibido uso comercial das skills).
- Remotion: grátis p/ pessoa física e empresas ≤3 funcionários; acima disso, licença paga.
- OpenMontage: AGPL-3.0.
