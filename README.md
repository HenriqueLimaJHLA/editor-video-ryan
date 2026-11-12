# Editor de Vídeo Ryan

Faz o Claude Code editar vídeos por você: você descreve o que quer em português e ele corta, legenda, converte, anima e entrega o arquivo pronto.

## Como instalar

### Jeito mais fácil: dentro do Claude Code

Cole esta linha no Claude Code e aperte Enter:

```
/plugin install editor-video-ryan --marketplace DONO/editor-video-ryan
```

Pronto. Na primeira vez que você pedir um vídeo, o Claude baixa sozinho os kits de edição (leva alguns minutos). As atualizações chegam automaticamente.

### Alternativa: duplo clique (Windows)

1. Baixe esta pasta para o seu computador.
2. Dê **duplo clique** em **`1 - Instalar.bat`**.
3. Espere aparecer **PRONTO!** e feche a janela.

Se o Python não estiver instalado, a janela instala sozinha e pede para você clicar de novo. No Mac, use **`Instalar (Mac).command`**.

| Arquivo | Quando usar |
|---|---|
| `1 - Instalar.bat` | Primeira vez. Rápido, deixa tudo pronto para o básico. |
| `2 - Instalar tudo (completo).bat` | Para liberar animações, GIFs de SVG e legendas grátis. Demora 10 a 30 min. |
| `3 - Verificar.bat` | Mostra o que está instalado e o que falta. |
| `4 - Atualizar kits.bat` | Baixa a versão mais nova dos kits. |

## Como usar

Abra o Claude Code na pasta onde estão seus vídeos e peça, por exemplo:

- *"Edita esse vídeo num Reels de 60 segundos com legenda"*
- *"Corta do segundo 10 ao 40, deixa em pé e comprime"*
- *"Transforma esse vídeo num GIF leve"*
- *"Faz um vídeo animado de 20 segundos apresentando minha loja"*

**Não precisa digitar nenhum comando:** o Claude percebe que é um pedido de vídeo e ativa a skill sozinho. Se quiser garantir que ele use esta skill (por exemplo, num pedido vago ou se você tiver outras skills de vídeo), comece a mensagem com `/editor-video-ryan`:

- `/editor-video-ryan corta do segundo 10 ao 40 e deixa em pé`

Ele mostra o plano antes de cortar e **nunca mexe no vídeo original**. Os arquivos prontos vão para a pasta `saida/`.

## Dicas

- Comece com um vídeo curto (1 a 2 minutos).
- Algumas funções pedem uma **chave de serviço pago** (ElevenLabs para transcrever, Google para gerar com IA). Sem chave, ele usa as alternativas grátis e te avisa.

## O que vem dentro

8 kits de código aberto, baixados dos links oficiais:

| Kit | Para quê |
|---|---|
| [video-use](https://github.com/browser-use/video-use) | corta pausas, legenda, cor (vídeo falado) |
| [ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | cortar, comprimir, converter, exportar por rede |
| [Herk Edit Kit](https://github.com/nateherkai/herk-edit-kit) | Reels e Shorts |
| [Claude GIF](https://github.com/AgriciDaniel/claude-gif) | GIFs |
| [Claude Motion Design](https://github.com/howseen-ai/claude-motion-design) | vídeo animado com código |
| [Remotion Skills](https://github.com/remotion-dev/skills) | vídeo em código, em série |
| [Video Editor Skills](https://github.com/appariciojunior/video-editor-skills) | primeiro corte no DaVinci Resolve Studio (pago) |
| [OpenMontage](https://github.com/calesthio/OpenMontage) | do roteiro ao vídeo final |

<details><summary>Para quem é técnico</summary>

- Plugin do Claude Code: manifesto em `.claude-plugin/plugin.json`; o próprio repositório é o marketplace (`.claude-plugin/marketplace.json`).
- A skill fica em `skills/editor-video-ryan/`: instalador `scripts/instalar.py` (`--completo`, `--atualizar`), diagnóstico `scripts/doctor.py`.
- Os kits são baixados em `~/.editor-video-ryan/kits/` (ou na pasta da variável `EDITOR_VIDEO_KITS`), fora do plugin, para sobreviverem às atualizações. As versões ficam fixadas em `kits.lock`.
- `references/catalogo.md` lista as 142 sub-skills (gerado por `scripts/catalogo.py`).
- Para publicar uma versão nova: suba o número em `plugin.json` e rode `claude plugin validate .`.
</details>
