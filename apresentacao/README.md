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
| `slides.html` | Deck HTML atual da defesa. |

## Subpastas

| Pasta | Uso |
|---|---|
| `figuras/` | Figuras finais ou candidatas a entrar nos slides. |
| `scripts/` | Scripts de extracao e geracao de graficos. |

## Fluxo recomendado

1. Revisar `base-apresentacao.md` para entender premissas, numeros e storyboard.
2. Ajustar `slides.html` quando for necessario mexer no deck atual.
3. Usar `figuras/` e `scripts/` para apoiar o deck e eventual reuso do material.
4. Se um novo deck precisar ser recriado, derive-o do TCC final e deste
   material-base, em vez de depender de uma estrutura de build antiga.

Nao ha mais uma pasta `build/` rastreada neste repositorio. Se for necessario
exportar um novo PDF a partir de `slides.html`, trate isso como artefato
derivado e gere fora do estado versionado ou reintroduza o fluxo de forma
explícita.
