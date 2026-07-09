# DESIGN.md - Guia visual da defesa

Este guia orienta a criacao dos slides. A apresentacao deve parecer academica,
tecnica e didatica, nao comercial.

## Paleta

Inspirada no template do TCC:

| Papel | Cor |
|---|---|
| Azul IDP principal | `#005DAA` |
| Ciano de titulo/destaque | `#00B3FF` |
| Azul escuro para capas | `#003A6B` |
| Texto principal | `#0F172A` |
| Texto secundario | `#475569` |
| Linhas e divisores | `#CBD5E1` |
| Fundo claro | `#FFFFFF` / `#F8FAFC` |
| Sucesso/resultado positivo | `#168A4A` |
| Alerta/inferencia/limite | `#B7791F` |
| Resultado negativo ou queda | `#C62828` |

Use azul e ciano como identidade, mas nao transforme todos os elementos em
variacoes de azul. Resultados negativos e limites fisicos podem usar vermelho ou
ambar com moderacao.

## Tipografia e legibilidade

- Formato 16:9.
- Titulo de slide: 32-40 px.
- Texto principal: 24-30 px.
- Rotulos de grafico: 18-22 px no minimo.
- Evitar paragrafo corrido. Preferir tres a cinco blocos curtos.
- Nenhum texto importante deve depender de rodape pequeno.
- Numeros headline devem ser grandes e acompanhados de unidade.
- Usar virgula decimal em portugues: `22,91x`, `7.542 MB/s`.

## Layout

- Um conceito por slide.
- Priorizar diagramas, fluxos, comparacoes lado a lado e graficos simples.
- Evitar cards decorativos em excesso. Cards so quando agruparem informacao
  repetida ou comparavel.
- Nao usar landing page, hero de marketing, slogans ou frases de impacto.
- Capa simples: titulo, subtitulo explicativo, autor, orientador, instituicao.
- Encerramento simples: "Obrigado", autor e orientador. O convite a arguição e
  verbal.

## Figuras

Figuras devem ser refeitas ou simplificadas quando o original do TCC for denso.
Cada figura precisa responder a uma funcao clara:

- explicar um conceito;
- preparar a leitura de um resultado;
- destacar uma comparacao;
- reduzir texto no slide.

Figuras candidatas do TCC:

| Figura do TCC | Uso provavel nos slides | Cuidado |
|---|---|---|
| `pipeline.pdf` | Mostrar fases: construir, buscar, mesclar | Simplificar rotulos. |
| `boundary_overlap.pdf` | Explicar overlap de borda | Fazer progressivo, se possivel. |
| `flattened_output.pdf` | Explicar remocao de ponteiros | Deixar antes/depois bem grande. |
| `memory_traffic.pdf` | Explicar por que sharding perde | Bom para resultado negativo. |
| `cache_hierarchy.pdf` | Introduzir cache/DRAM | Evitar texto pequeno. |
| `load_balancing.pdf` | Explicar diagnostico de balanceamento | Nao centralizar o i5 na narrativa. |
| `parallel_bfs.pdf` | Construção paralela | Provavelmente cortavel. |
| `trie.pdf` / `ac_automaton.pdf` | Conceito do Aho-Corasick | Recriar como sequencia didatica. |

## Graficos

- Preferir SVG.
- Cada grafico deve ter titulo contextual no slide, eixo com unidade e uma
  anotacao visual no dado principal.
- Evitar tabelas grandes nos slides. Se a tabela do TCC for necessaria,
  transformar em grafico ou em comparacao de poucos numeros.
- Grafico de speedup deve mostrar a linha ideal apenas como referencia discreta.
- Grafico de footprint deve destacar a queda com crescimento do automato.
- Nao usar 3D, sombra pesada, degradê decorativo ou cores sem significado.

## Sequencias progressivas

Um deck baseado em HTML ou Markdown pode duplicar slides para criar revelacoes
por avancos. Sequencias uteis:

- Aho-Corasick: inserir padroes na trie, ler caracteres, seguir transicoes,
  ativar failure link, emitir match.
- Overlap: dividir texto, mostrar padrao cruzando fronteira, adicionar margem,
  suprimir duplicata, preservar equivalencia com sequencial.
- Cache: mostrar automato pequeno na L3, automato Snort cruzando um CCD,
  Emerging Threats muito maior que L3, setas para DRAM.
- Resultado principal: primeiro eixo, depois curva Snort, depois curva Emerging
  Threats, por fim destacar `22,91x` e `18,96x`.

Use sequencias progressivas quando elas reduzirem explicacao verbal, nao para
decorar o deck.

## Coisas a evitar

- Perguntas no slide.
- Frases como "solucao revolucionaria", "mudanca de paradigma", "performance
  extrema" ou equivalentes.
- Blocos com codigo C, SQL ou nomes internos de variante.
- Prints do terminal, prints do banco ou logs de benchmark.
- Figuras complexas do TCC sem redesenho para projetor.
- Dar a entender que cache misses ou banda DRAM foram medidos diretamente.
