# Apresentacao da defesa

Pasta de trabalho para preparar a defesa do TCC. A apresentacao sera feita em
portugues, com foco didatico e visual, derivada do texto final do trabalho.

## Fonte de verdade

Para esta fase, o texto do TCC e a fonte de verdade:

- `../partes/introduction.tex`
- `../partes/fundamentacao.tex`
- `../partes/rsl.tex`
- `../partes/proposal.tex`
- `../partes/methodology.tex`
- `../partes/results.tex`
- `../partes/conclusion.tex`
- `../partes/abstract.tex`

Use `../../parallel-aho-corasick/` apenas para gerar ou conferir graficos quando
for necessario. Se houver conflito entre banco de resultados, notas antigas e o
texto do TCC, o texto do TCC vence.

## Arquivos principais

| Arquivo | Papel |
|---|---|
| `AGENTS.md` | Instrucoes para agentes de IA que trabalharem nesta pasta. |
| `DESIGN.md` | Diretrizes visuais, paleta, tipografia e regras de legibilidade. |
| `base-apresentacao.md` | Indice narrativo global: premissas, numeros, storyboard e orientacoes transversais. |

## Subpastas

| Pasta | Uso |
|---|---|
| `secoes/` | Briefs focados por secao da apresentacao; use para dividir trabalho entre agentes. |
| `figuras/` | Figuras finais ou candidatas a entrar nos slides. |
| `graficos/` | Graficos gerados para a apresentacao, preferencialmente em SVG. |
| `dados/` | CSV/JSON intermediarios extraidos do TCC ou do `sweep.db`. |
| `scripts/` | Scripts de extracao e geracao de graficos. |
| `roteiro/` | Roteiros de fala derivados dos slides aprovados. |
| `build/` | Saidas geradas, como HTML/PDF. Nao editar manualmente. |

## Fluxo recomendado

1. Revisar `base-apresentacao.md` para entender premissas, numeros e storyboard.
2. Trabalhar a secao relevante em `secoes/secao-*.md`.
3. Criar `slides.md` em Marp ou um deck HTML a partir da base e das secoes.
4. Criar o roteiro em `roteiro/` slide a slide, depois que o deck estabilizar.
5. Gerar figuras/graficos sob demanda, sempre com legenda e fonte rastreavel.
6. Exportar HTML/PDF para `build/`.

Comandos esperados para a fase de slides:

```bash
cd apresentacao
npx @marp-team/marp-cli@4.4.0 slides.md -o build/slides.html --allow-local-files
CHROME_PATH=/usr/bin/google-chrome npx @marp-team/marp-cli@4.4.0 slides.md -o build/slides.pdf --allow-local-files
```

`build/slides.html` e `build/slides.pdf` sao artefatos gerados. O conteudo
editavel deve ficar em Markdown, scripts e fontes de figura.
