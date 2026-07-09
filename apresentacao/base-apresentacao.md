# Base da apresentacao de defesa

> Revisao 2026-07-04: todos os numeros deste documento foram conferidos contra
> `../partes/{results,methodology,conclusion,abstract,rsl}.tex`. O implementador
> dos slides pode usa-los sem re-auditar, mas deve respeitar as notas de
> contexto (baseline sequencial, empate tecnico, nuances do i5) marcadas abaixo.

Versao inicial para orientar duas frentes posteriores:

1. Criacao dos slides.
2. Criacao do roteiro de fala para treino.

O documento esta em portugues porque a defesa sera em portugues. Ele nao e o
deck; e o mapa narrativo que deve impedir que os slides virem uma copia densa do
TCC.

Este arquivo permaneceu como a referencia consolidada da defesa depois da
simplificacao da pasta `apresentacao/`. Use-o como storyboard unico.

## Premissas globais

- Publico: banca academica, estudantes e comunidade tecnica geral. Nem todos
  terao familiaridade com arquitetura de computadores, IDS ou Aho-Corasick.
- Tom: tecnico, sobrio e didatico. Sem linguagem de marketing.
- Estilo visual: inspirado no template do TCC, com azul IDP `#005DAA` e ciano
  `#00B3FF`, fundo claro, alto contraste e pouco texto.
- Regra de ouro: cada slide deve ensinar uma coisa que prepara a proxima.
- Slides nao devem conter perguntas. A RSL pode ser explicada como lacuna e
  metodologia, sem colocar RQs em forma de pergunta.
- Evitar jargoes nao explicados. Quando necessario, usar o termo tecnico e a
  traducao funcional: `throughput` como vazao, `speedup` como aceleracao,
  `memory-bound` como limitado pela memoria.
- Nao usar termos internos do laboratorio nos slides: nomes de searchers,
  `sweep.db`, fases A/B/C, ideias, specs, scripts ou identificadores C.
- Texto do TCC atual e fonte de verdade. Numeros historicos do i5 ou de decks
  antigos nao devem ser reintroduzidos.

## Mensagem central

O Aho-Corasick ja e eficiente em uma passada, mas foi concebido como uma
travessia sequencial de automato. Ao levar esse algoritmo para CPUs multi-core
com dicionarios de seguranca grandes, o limite principal deixa de ser a logica
de casamento de padroes e passa a ser a memoria: muitos nucleos tentam percorrer
o mesmo automato grande, e a hierarquia de cache/DRAM define o teto. A estrategia
mais efetiva foi dividir o texto entre threads, manter o automato compartilhado
e somente leitura, e reduzir custo de emissao de matches com layout contiguo.

Versao curta para repetir na fala:

> O ganho vem de paralelizar o texto, nao de dividir o dicionario. O limite que
> aparece nos resultados e principalmente de memoria.

## Numeros que podem virar destaque

Usar com parcimonia. Nem todos precisam aparecer no deck.

| Tema | Numero | Uso sugerido |
|---|---:|---|
| Plataforma canonica | Ryzen 9 9950X, 16 cores / 32 threads | Metodologia. |
| Cache da plataforma | L3 total 64 MiB, em 2 slices de 32 MiB | Explicar footprint. |
| Snort full | 4.188 padroes, automato 55,23 MiB | Workload moderado/principal. |
| Emerging Threats | 44.678 padroes, automato 506,78 MiB | Workload memory-bound. |
| Throughput sequencial Snort-100 | 629,0 MB/s | Inicio da queda por footprint. |
| Throughput sequencial Emerging Threats | 210,2 MB/s | Fim da queda por footprint. |
| Queda sequencial por footprint | -66,6% | Mostrar que tamanho do automato domina. |
| Melhor Snort | 22,91x e 7.542 MB/s em 32 threads | Resultado principal. |
| Melhor Emerging Threats | 18,96x e 3.979 MB/s em 32 threads | Resultado memory-bound. |
| Eficiencia em 16 threads | 86,9% Snort; 79,5% ET | Mostrar escalabilidade boa antes de SMT. |
| Eficiencia em 32 threads | 71,6% Snort; 59,3% ET | Mostrar sublinearidade e limite fisico. |
| Cross-corpus Snort | 7.976 MB/s SimpleWiki; 7.595 MB/s Enron | Texto importa menos que automato. |
| Tarefa dinamica grossa | 7.804 MB/s | Granularidade reduz overhead. |
| Layout de saida plana | +3,0%, +4,2%, +6,9% | Otimizacao pequena, consistente. |
| Sharding de dicionario | pico 1,89x; 620,9 MB/s | Resultado negativo qualificado. |
| Texto paralelo contra sharding | 22,91x; 7.542,3 MB/s | Eixo correto e texto, nao dicionario. |
| Composicao 2D | 0,73x a 0,81x do texto paralelo | Resultado negativo. |
| End-to-end Enron 8x | 22,23x Snort; 17,71x ET | Pipeline completo ainda dominado pela busca. |
| Build paralelo ET | pico 1,59x | Beneficio operacional, nao central. |
| Colapso paralelo por footprint | 16.230 -> 4.046 MB/s em T=32 | Mesma queda do footprint, amplificada em paralelo; par visual do resultado 1. |
| Ganho do SMT (16 -> 32 threads) | 1,65x Snort; 1,49x ET | Explicar por que throughput sobe enquanto eficiencia cai. |
| Sharding declina apos o pico | 1,89x em 8 shards -> 1,78x em 32 | Pico antes do limite de threads indica localidade, nao paralelismo. |
| Tamanho dos corpora | Enron 1,32 GiB; Enron 8x 10,59 GiB; SimpleWiki 1,19 GiB | Sustentar a alegacao de "gigabytes" na motivacao/metodologia. |
| Diagnostico i5 | CV 39,9%-52,9% cai para 1,7%-3,3% | Usar so para explicar heterogeneidade. |
| Skew de conteudo | estaticas perdem 16%-30%; dinamicas ganham 16%-31% | Robustez do despacho dinamico. |
| Empate tecnico no ET 8x | estatico plano 19,83x vs dinamico plano 19,79x | Nao e headline; preparar para arguicao sobre "dinamico sempre vence". |

Nota sobre o baseline sequencial do Snort full: o TCC reporta tres medicoes
proximas, de fases diferentes da campanha --- `328,9 MB/s` na tabela de
footprint, `329,2 MB/s` na nota da tabela de sharding e `329,4 MB/s` no
experimento cross-corpus. Em um slide, use o valor da mesma fase do numero que
ele acompanha e nao misture os tres; se precisar de um unico valor solto,
prefira `328,9 MB/s` (tabela de footprint).

## Termos para usar no slide

| Evitar no slide | Preferir |
|---|---|
| `searcher` | estrategia de busca |
| `pthread_dynamic_flat` | estrategia dinamica com saida plana |
| `pthread_chunked_flat` | particionamento estatico com saida plana |
| `sweep.db` | campanha experimental |
| fase A/B/C/G | experimento de escalabilidade, footprint, corpus etc. |
| output list | emissao de matches |
| bag-of-tasks | despacho dinamico de tarefas |
| sharding | particionamento do dicionario, depois introduzir "sharding" se preciso |

## Estrutura sugerida

Alvo inicial: 20 a 22 slides para uma fala de 18 a 22 minutos. Se o tempo
oficial for menor, cortar diagnosticos e detalhes de build antes de cortar o
conceito do algoritmo ou o resultado central.

## Storyboard inicial de slides

Esta e uma primeira sequencia candidata. Deve ser ajustada antes de virar um
novo deck, se ele precisar ser recriado.

| # | Titulo sugerido | Funcao |
|---:|---|---|
| 1 | Acceleration of Pattern Matching Algorithms Using Parallel Programming | Capa. |
| 2 | Caminho da defesa | Orientar a banca. |
| 3 | Processadores ficaram paralelos | Motivacao de hardware. |
| 4 | Muitos padroes em uma unica passada | Introduzir Aho-Corasick. |
| 5 | O Aho-Corasick em uma sequencia visual | Conceito do automato (trie, falha, tabela). |
| 6 | A dependencia sequencial concentra o trabalho | Explicar por que 1 nucleo limita. |
| 7 | O automato cresce alem da cache | Introduzir regime memory-bound. |
| 8 | A literatura aponta o eixo e a lacuna | RSL em funil + sintese. |
| 9 | Texto dividido, automato compartilhado | Estrategia principal. |
| 10 | Overlap preserva matches de fronteira | Corretude do particionamento. |
| 11 | Saida plana reduz ponteiros | Otimizacao de layout. |
| 12 | Workloads cobrem de 1,93 a 506,78 MiB | Metodologia e dados. |
| 13 | A medicao compara contra o sequencial | Rigor e corretude. |
| 14 | Footprint derruba throughput mesmo com uma thread | Resultado 1. |
| 15 | O paralelismo de texto escala ate 32 threads | Resultado 2. |
| 16 | O conteudo do corpus pesa menos que o automato | Resultado 3, cortavel. |
| 17 | Layout ajuda, mas nao muda o teto | Resultado 4. |
| 18 | Dividir o dicionario multiplica trafego | Resultado negativo. |
| 19 | O pipeline completo continua dominado pela busca | End-to-end, cortavel. |
| 20 | Balanceamento importa em hardware ou conteudo irregular | Diagnosticos. |
| 21 | Achados e limites | Conclusao + ameacas + futuro. |
| 22 | Obrigado | Encerramento. |

A ordem acima preserva um fluxo didatico: a sequencia visual do automato
(slide 5) vem antes dos slides de dependencia sequencial e de cache
(6 e 7), porque ambos dependem do conceito de tabela de transicao que a
sequencia constroi; a RSL (slide 8) fecha o bloco conceitual e justifica a
estrategia que comeca no slide 9.

Para uma defesa de 15 minutos, cortar ou comprimir os slides 16, 19 e 20. Para
uma defesa de 20 minutos, manter todos se o ritmo estiver bom.

Importante: para valorizar a didática, é possível expandir os slides com figuras ou digramas para vários slides,
por exmplo, mostrando sequencias e transições, onde cada slida dá um efeito de "passo a passo" ou "animação" do conceito.

## Materiais visuais a produzir

Prioridade alta:

- Sequencia didatica do Aho-Corasick.
- Diagrama de cache/footprint com 32 MiB, 64 MiB e 506,78 MiB.
- Diagrama de particionamento com overlap.
- Grafico de speedup Snort versus Emerging Threats.
- Grafico de throughput por footprint com as duas curvas (T=1 e T=32); e o
  visual mais direto do argumento central e o TCC ja o traz como figura
  (`cache_cliff`). Dados no apendice.
- Figura de trafego explicando por que sharding perde.

Prioridade media:

- Antes/depois do layout de saida.
- Grafico end-to-end.
- Painel de diagnostico de balanceamento.

Prioridade baixa:

- Construção paralela BFS, salvo se a banca pedir detalhes.
- Tabela completa de estrategias.

## Pontos para roteiro de fala

O roteiro deve enfatizar transicoes:

- "Agora que a motivacao de hardware esta clara, falta entender o algoritmo."
- "Com o algoritmo entendido, aparece o problema de memoria."
- "A RSL mostra que o eixo natural e dividir o texto, mas faltava medir esse
  regime em POSIX Threads."
- "A estrategia so funciona se ela mantiver a mesma resposta do sequencial."
- "Antes de mostrar speedup, primeiro mostro que o tamanho do automato sozinho
  derruba throughput."
- "O resultado negativo e importante porque separa uma ideia plausivel de uma
  estrategia realmente competitiva."
- "Os diagnosticos explicam robustez, mas nao mudam a plataforma principal."

## Perguntas provaveis da banca para preparar no roteiro

Estas perguntas nao devem virar titulos de slides, mas o roteiro deve preparar
respostas curtas. Cada item traz o nucleo da resposta e onde ela vive no TCC.

- Por que POSIX Threads e nao OpenMP, MPI ou GPU?
  Controle explicito de afinidade, particionamento e emissao por thread; a RSL
  mostra GPU/SIMD como eixos complementares, nao concorrentes (rsl e discussao
  de posicionamento em results).
- Como o overlap garante que nenhum match de fronteira se perde?
  Overlap de `Lmax - 1` bytes e o minimo que garante que um padrao cruzando a
  fronteira e detectado por exatamente um worker; a posse do match e decidida
  pela posicao final (proposal).
- O que muda se a cache de outro processador for maior?
  A fronteira entre regimes se move, mas o fenomeno permanece: automato maior
  cria working set maior. O TCC formula isso explicitamente na discussao do
  layout plano (results).
- Por que 32 threads nao chegam a 32x?
  Escala sublinear: contencao pelo barramento de memoria compartilhado no
  regime memory-bound e SMT que esconde latencia sem dobrar computo. Eficiencia
  medida de `71,6%`/`59,3%` em 32T; formulado como inferencia (results).
- O resultado depende de Snort/Suricata ou vale para outros dicionarios?
  O eixo dominante e o footprint do automato, nao o conteudo do dicionario ou
  do corpus; a varredura de 1,93 a 506,78 MiB cobre o espectro (results).
- Por que dividir o dicionario nao funcionou?
  Cada shard revarre o texto inteiro: K shards multiplicam o trafego de
  memoria por K; o pico em 8 shards seguido de declinio mostra que o ganho era
  localidade, nao paralelismo (results, tabela de sharding).
- Como garantir que as variantes paralelas produzem os mesmos matches?
  Tres niveis: match set exato na suite automatizada, digest MD5 do fluxo
  canonicalizado ate T=64 e ThreadSanitizer sem data races (methodology,
  correctness).
- O que faltou medir para afirmar cache misses diretamente?
  Contadores de PMU (misses, banda, stalls); e a primeira linha de trabalhos
  futuros. Toda atribuicao a cache/DRAM no TCC e inferencia consistente com os
  dados (threats to validity).
- O i5 ainda importa depois da migracao para a workstation?
  Sim, mas so como diagnostico: e o unico processador hibrido disponivel, entao
  e onde o desbalanceamento estrutural de nucleos existe para ser medido. Zero
  numeros headline vem dele (results, secao heterogenea).
- O despacho dinamico e sempre a melhor escolha?
  Nao: no corpus uniforme do i5 as estaticas lideram, e no ET 8x ha empate
  tecnico com o estatico plano. A recomendacao se apoia em throughput lider nos
  cenarios canonicos MAIS robustez sob as duas fontes de desequilibrio
  (discussao final de results).
- Por que nao ha barras de erro / replicas?
  Campanha canonica e sweep unico com CV intra-run baixo (< ~2%); replicas
  independentes com mediana/IQR sao trabalho futuro. O diagnostico de skew ja
  segue o protocolo mais estrito, com mediana de cinco invocacoes
  (methodology, protocolo de medicao).

## Apendice - Dados prontos para os graficos

Coordenadas extraidas de `../partes/results.tex` (que por sua vez vem do
`sweep.db` canonico). Suficientes para gerar os graficos principais sem
consultar o banco. Nos rotulos dos eixos, usar virgula decimal.

### Curva de speedup por threads (grafico principal)

Estrategia dinamica com saida plana, corpus Enron canonico.

| T | Snort (55 MiB) | Emerging Threats (507 MiB) |
|---:|---:|---:|
| 1 | 1,04 | 1,07 |
| 4 | 3,97 | 3,83 |
| 8 | 7,60 | 7,05 |
| 12 | 10,79 | 10,13 |
| 16 | 13,90 | 12,72 |
| 20 | 15,32 | 13,86 |
| 24 | 17,93 | 15,80 |
| 28 | 20,32 | 17,47 |
| 32 | 22,91 | 18,96 |

Linha ideal `y = x` apenas como referencia discreta. Destacar T=16 (fim dos
nucleos fisicos) e T=32 (SMT completo).

### Throughput por footprint (queda por tamanho do automato)

Corpus fixo (Enron). Duas curvas: sequencial (T=1) e dinamica plana (T=32).

| Dicionario | Footprint | T=1 (MB/s) | T=32 (MB/s) |
|---|---:|---:|---:|
| Snort-100 | 1,93 MiB | 629,0 | 16.230 |
| Snort-1k | 11,92 MiB | 452,3 | 10.074 |
| Snort full | 55,23 MiB | 328,9 | 7.594 |
| Emerging Threats | 506,78 MiB | 210,2 | 4.046 |

Marcar a linha da LLC agregada (64 MiB); eixos em escala log como na figura
`cache_cliff` do TCC.

### Ganho do layout de saida plana (single-thread)

| Dicionario | Baseline (MB/s) | Plano (MB/s) | Ganho |
|---|---:|---:|---:|
| Snort-100 | 629,0 | 647,8 | +3,0% |
| Snort full | 328,9 | 342,6 | +4,2% |
| Emerging Threats | 210,2 | 224,6 | +6,9% |

### Sharding versus texto paralelo (resultado negativo)

Baseline sequencial desta tabela: `329,2 MB/s`.

| Configuracao | MB/s | vs. sequencial |
|---|---:|---:|
| Sharding, 2 shards | 481,1 | 1,46x |
| Sharding, 4 shards | 570,1 | 1,73x |
| Sharding, 8 shards (pico) | 620,9 | 1,89x |
| Sharding, 16 shards | 605,0 | 1,84x |
| Sharding, 32 shards | 586,0 | 1,78x |
| Texto paralelo (32 threads) | 7.542,3 | 22,91x |

### Skew de conteudo (i5, 12 threads, medianas de 5 invocacoes)

Snort, MB/s, uniforme -> concentrado:

| Estrategia | Uniforme | Concentrado | Variacao |
|---|---:|---:|---:|
| Estatica (cache-padded) | 446,4 | 317,0 | -29,0% |
| Estatica plana | 473,1 | 333,2 | -29,6% |
| Topologica | 394,9 | 316,7 | -19,8% |
| Dinamica | 371,6 | 430,8 | +15,9% |
| Dinamica plana | 390,6 | 456,8 | +16,9% |

Nao comparar estes valores absolutos com os da workstation.

## Lista de checagem para a proxima etapa

- [ ] Confirmar tempo oficial da defesa.
- [ ] Escolher quais slides serao cortaveis.
- [ ] Gerar os graficos principais em SVG.
- [ ] Redesenhar as figuras conceituais para 16:9.
- [ ] Criar um novo deck com pouco texto, se necessario.
- [ ] Exportar PDF e revisar legibilidade em tela cheia, se o deck for recriado.
- [ ] Criar roteiro depois que a ordem dos slides estabilizar, se houver nova iteracao.
