# Apresentação (defesa do TCC)

Slides da defesa, escritos em **Marp** (Markdown → HTML/PDF). A fonte de verdade
é [`slides.md`](slides.md); `slides.html` e `slides.pdf` são **gerados** — não os
edite à mão.

## Ferramenta

[Marp CLI](https://github.com/marp-team/marp-cli) **v4.4.0**, executado via `npx`
(o pacote já está no cache do npx desta máquina). O nome do pacote é
`@marp-team/marp-cli` (não `marp`). Export para PDF usa o Google Chrome
(`/usr/bin/google-chrome`).

## Build

```bash
cd apresentacao

# 1) (se os dados mudaram) regenerar o gráfico de speedup a partir dos números do TCC
python3 gerar_grafico_svg.py            # escreve figuras/speedup_results.svg

# 2) HTML
npx @marp-team/marp-cli@4.4.0 slides.md -o slides.html --allow-local-files

# 3) PDF (precisa do Chrome)
CHROME_PATH=/usr/bin/google-chrome \
  npx @marp-team/marp-cli@4.4.0 slides.md -o slides.pdf --allow-local-files
```

`--allow-local-files` é necessário porque os slides referenciam imagens locais
em `figuras/`. Para uma janela de pré-visualização ao vivo: `... -s slides.md`
(modo server/watch).

## Imagens (`figuras/`)

| Arquivo | Origem |
|---|---|
| `speedup_results.svg` | **Gerado** por `gerar_grafico_svg.py` (dados do sweep canônico). |
| `cache_hierarchy.svg`, `load_balancing.svg`, `parallel_bfs.svg` | Diagramas autorais (espelham as figuras TikZ do TCC). |
| `trie-1.png`, `ac_matching-1.png` | Ilustrações do autômato Aho–Corasick. |

> Coerência: qualquer número nos slides deve bater com o TCC, cuja fonte de
> verdade é `../../parallel-aho-corasick/runs/i5/sweep.db` (sweep
> 2026-05-29). E2E = `build_ms + mean_ms` (ver apêndice do TCC).

## Citações

Trabalhos nomeados em um slide recebem citação curta no rodapé via diretiva
Marp por slide: `<!-- _footer: "Autor (ano); ..." -->`. Referências completas
ficam no TCC.
