# Roteiro da Apresentação de Defesa — TCC

> **Documento de orientação, alinhado ao deck real (`slides.md`, 27 slides).**
> Cada bloco descreve um slide com objetivo, conteúdo, números canônicos,
> sugestão visual, nota de oratória e tempo. Reflete o que está montado hoje;
> ao editar os slides, manter este arquivo em sincronia.

---

## 0. Parâmetros gerais (ler antes de mexer em qualquer slide)

| Item | Definição |
|------|-----------|
| **Trabalho** | *Acceleration of Pattern Matching Algorithms Using Parallel Programming* — paralelização do Aho–Corasick em CPUs multi-core de memória compartilhada com POSIX Threads. |
| **Autor / Orientador** | Matheus Antônio de Castro de Barros / Jeremias Moreira Gomes (IDP, Eng. de Software). |
| **Idioma** | **Português** (banca brasileira). O TCC escrito está em inglês; ao falar, traduza, mas **mantenha os termos técnicos** (Aho–Corasick, speedup, memory-bound, cache, DFA, throughput, P-core/E-core). |
| **Duração-alvo** | ~20–22 min de fala. Para 15 min, cortar os slides marcados **[CORTÁVEL]**. |
| **Nº de slides** | **27** (capa + 25 de conteúdo + encerramento). **Sem slides de apêndice** — o conteúdo útil foi integrado ao fluxo principal. |
| **Tom** | Formal e didático. Títulos **neutros e descritivos** — nada de frases de efeito. |
| **Mensagem única (o que a banca deve lembrar)** | O gargalo de escalar o Aho–Corasick em escala de IDS é **microarquitetural (estouro de cache + banda de DRAM)**, não a lógica de casamento. Paralelizar o **texto** + layout de saída *cache-friendly* é a resposta correta; particionar o **dicionário** não é. |

### Princípios de design
- **Um conceito por slide.** Pouco texto; o detalhe vai na fala.
- **Números headline destacados** (cor/negrito): `4,79×`, `4,52×`, `2,79×`/`2,85×`, `−74,0%`, `+13,0%`, `42×`, `4,50×`, `2,76×`.
- Cores do TCC: azul IDP **#005DAA** e ciano **#00B3FF** (de `configs/idp-model.cls`).
- Vírgula decimal em todos os números (`4,79×`, não `4.79×`).
- Figuras em `figuras/`: `trie-1.png` (slide 7), `ac_matching-1.png` (disponível, não usado no fluxo), `speedup_results.svg` (slide 20). **Não** usar `software.png` (diagrama de SDLC, sem relação com o tema).

---

## BLOCO 1 — Abertura

### Slide 1 — Capa
- Título completo; autor; orientador; IDP — Engenharia de Software; "Trabalho de Conclusão de Curso"; data; identidade IDP (fundo azul, título em ciano).
- **Fala (~30s):** cumprimento à banca, nome, título, orientador.
- **Tempo:** 0:30

### Slide 2 — Agenda / Roteiro
- Quatro blocos: (1) Introdução e Problema; (2) Fundamentos e Literatura; (3) Proposta e Metodologia; (4) Resultados e Conclusão.
- **Tempo:** 0:30

---

## BLOCO 2 — Contexto, Problema e Objetivos (~3 min)

### Slide 3 — Contexto: A Transição para Arquiteturas Multi-core
- Estagnação do clock (limites térmicos/físicos, meados de 2000) → **multi-core** vira a arquitetura dominante → ganho de desempenho **exige software paralelo explícito**.
- **Visual:** bullets + dois boxes ("2005"; "Frequência → Núcleos").
- **Tempo:** 1:00

### Slide 4 — O Algoritmo Aho–Corasick: Eficiente, porém Sequencial
- AC = casamento de **múltiplos padrões** em **uma única passada**, tempo linear <em>O</em>(<em>n</em> + <em>z</em>).
- Aplicações: **Snort/Suricata (NIDS), YARA (malware)**, spam, bioinformática.
- **Limitação:** processa o texto estritamente da esquerda para a direita, cada transição depende da anterior → **intrinsecamente sequencial**, usa **1 núcleo**.
- **Visual:** cartão com aplicações + destaque "1 núcleo". (YARA/Snort são **aplicações**, não o objeto.)
- **Tempo:** 1:00

### Slide 5 — Problema e Motivação: O Regime Memory-Bound
- Conjuntos de regras crescem → autômato de **centenas de MB**, muito além da **LLC** → **regime memory-bound**: o gargalo vira **banda de DRAM**, não cálculo.
- Pouco caracterizado em CPUs commodity. **Termina aqui** (sem questões de pesquisa na introdução).
- **Visual:** bullets + cartão "Estouro de Cache" + box "DRAM".
- **Tempo:** 1:00

### Slide 6 — Objetivos do Trabalho
- **Geral:** projetar, implementar e avaliar uma versão paralela do AC para CPUs multi-core de memória compartilhada com **POSIX Threads**.
- **Específicos (3 cartões):** (1) Implementar em C/pthreads; (2) Quantificar ganhos (speedup, throughput, eficiência) vs. baseline; (3) Analisar escalabilidade por workload, padrões e nº de threads.
- **Importante:** **não** há RQs aqui. As Questões de Pesquisa são as da **RSL** e aparecem no Slide 11.
- **Tempo:** 1:00

---

## BLOCO 3 — Fundamentação mínima (~3 min)

> **Corte:** a banca conhece a teoria. Mostre só o necessário para entender os resultados. Não detalhar KMP/Boyer-Moore/naive.

### Slide 7 — Fundamentação: O Aho–Corasick em uma Figura
- **trie** (goto) + **failure links** (retomam sem reler caracteres, herança do KMP) + **output** (padrões que terminam em cada estado).
- Compila para **DFA**: tabela plana <code>δ(estado, byte)</code> → **1 lookup por byte**. Custo: tabela grande (4·|Q|·256 bytes) → **estoura a cache**.
- **Visual:** figura grande da trie (`trie-1.png`, "car/cat/cart/dog"). Ponte para o resultado central (footprint × throughput).
- **Tempo:** 1:15

### Slide 8 — Paralelismo de Memória Compartilhada e Pthreads
- **Threads** compartilham o espaço de endereçamento → ideais para um **autômato grande e read-only** acessado por todos.
- **pthreads:** API portátil, padrão, com controle de afinidade de núcleo.
- Conceito-chave: **autômato read-only ⇒ hot path sem locks**.
- **Visual:** N threads → 1 autômato compartilhado (somente leitura) → listas de matches privadas.
- **Tempo:** 0:45

### Slide 9 — Métricas: Speedup, Amdahl e Eficiência
- **Speedup** <em>S = Ts/Tp</em> (ideal linear <em>S = P</em>); **Amdahl** (fração serial limita o teto); **Eficiência** <em>E = S/P</em>.
- **Visual:** três equações (KaTeX). Mote: "eficiência baixa nos resultados não é bug — é o teto físico aparecendo."
- **Tempo:** 0:45

### Slide 10 — O Fator Decisivo: Hierarquia de Cache e Núcleos Híbridos
- **Slide mais importante da fundamentação.** Hierarquia L1/L2 privadas → **LLC (L3) compartilhada** → DRAM.
- **Compute-bound × memory-bound:** tabela > LLC ⇒ cada transição vira acesso à DRAM ⇒ teto = banda de memória.
- **Híbrido P/E (i5-1235U):** 2 P-cores (HT) + 8 E-cores = **12 threads de HW**; gera um **"joelho"** quando os P-cores saturam (após 4 threads). *O P/E é a plataforma, não o objeto de estudo.*
- **Tempo:** 0:45

---

## BLOCO 4 — Revisão Sistemática (~2,5 min)

> Mostrar **rigor + a lacuna**, não resumir os 10 papers.

### Slide 11 — RSL: Questões de Pesquisa e Funil de Seleção
- **As 2 RQs do trabalho (em destaque):** **RQ1** — quais técnicas de paralelização e desafios estão documentados na literatura para o AC com threads em CPUs multi-core? **RQ2** — quais otimizações do AC são empregadas com grandes conjuntos de padrões, sobretudo em segurança da informação?
- **4 bases** (WoS, Scopus, ACM DL, IEEE Xplore), busca maio/2025, janela 2015–2025.
- **Funil:** 196 → **24** únicos → **10** primários.
- **Tempo:** 1:15

### Slide 12 — RSL: Estado da Arte e Lacunas
- **3 consensos (agrupados):** (1) **particionar texto com overlap** L<sub>max</sub>−1 funciona (Qu et al., Jepsen et al.); (2) **cache é o teto** (head-body de Lee & Yang); (3) caminhos **ortogonais** (SIMD/GPU/construção/benchmarks).
- **Lacuna:** caracterizar a paralelização do AC no **regime memory-bound** (autômato ≫ LLC) em CPUs multi-core commodity com pthreads, validada contra o baseline. *(Não enquadrar a assimetria P/E como objeto.)*
- **Tempo:** 1:15

---

## BLOCO 5 — Proposta (~2 min)

### Slide 13 — Proposta: A Decisão Estrutural Única
- **Fases separadas:** mestre **constrói** o autômato → declarado **read-only** → workers percorrem **sem locks** → **merge** sequencial.
- Framework **modular**: cada otimização pluga e é medida isoladamente.
- **Visual:** diagrama de fases (Construção → Bloqueio read-only → Busca concorrente → Merge).
- **Tempo:** 0:40

### Slide 14 — Particionamento do Texto + Overlap de Borda
- Texto em segmentos contíguos, um por worker; matches em lista privada (sem sincronização).
- **Problema:** padrão cruzando fronteira se perderia. **Solução:** overlap de **L<sub>max</sub> − 1** bytes (warm-up) → cada padrão visto por **exatamente um** worker; correspondência 1:1 com o sequencial.
- **Visual:** dois segmentos com zona de overlap e um padrão cruzando a borda.
- **Tempo:** 0:40

### Slide 15 — As Quatro Estratégias Projetadas e Avaliadas
- (1) **Texto + flat output**; (2) **Balanceamento heterogêneo** (frequency-weighted **ou** dispatch dinâmico bag-of-tasks); (3) **Sharding de dicionário** (por prefixo — *hipótese*); (4) **Composição 2D** (chunking + sharding — *hipótese*).
- **Fala:** sinalizar que (3) e (4) são hipóteses que os resultados vão **julgar — inclusive negar**.
- **Tempo:** 0:40

---

## BLOCO 6 — Metodologia (~2,5 min)

### Slide 16 — Ambiente Experimental e Workloads
- **Plataforma:** i5-1235U (2 P + 8 E = 12 threads HW; **L3 = 12 MiB**; ~31 GiB DDR4 ~25 GB/s). C11, GCC 13.3.0 `-O3 -march=native`, Linux 6.17.
- **Dicionários:** Snort-100 (**1,93 MiB**, cabe na L3) → Snort-1k (11,92 MiB, borda) → Snort full (55,23 MiB, > L3) → **Emerging Threats (506,78 MiB ≈ 42× a L3, memory-bound)**.
- **Corpora:** Enron ~1,32 GiB; SimpleWiki ~1,19 GiB; Enron×8 ~10,6 GiB.
- **Tempo:** 1:00

### Slide 17 — Rigor Experimental e Protocolo de Medição
- **Sweep** formal (`sweep.db`); 2 warm-ups + 5 medições; média **e CV**.
- **Anti-boost:** processador móvel **throttla** → publicam-se os números **sustentados (sob carga)**, conservadores.
- **Correção primeiro:** **MD5** do stream batido até **64 threads**; **ThreadSanitizer** sem data races. *(Cobre o que seria o "apêndice de validação".)*
- **Tempo:** 1:00

### Slide 18 — Estratégias Avaliadas (tabela de variantes) [CORTÁVEL]
- Tabela por **eixo**: Baseline · Paralelismo de texto (4 variantes) · Layout de saída (flat) · Paralelismo de dicionário (sharding) · Composição (2D). Todas compartilham o mesmo autômato e isolam um único eixo.
- *Conteúdo antes no Apêndice D; agora integrado ao fluxo.*
- **Tempo:** 0:40

---

## BLOCO 7 — Resultados (~5 min — o coração da defesa)

> Começar pelo **gargalo** (a causa), depois cada eixo, terminando nos **resultados negativos** (que são contribuição).

### Slide 19 — Resultados: Impacto do Footprint no Throughput
- **1 thread**, corpus fixo, só o dicionário cresce: 483,1 → 337,3 → 240,7 → **125,6 MB/s** ⇒ **−74,0%**.
- **Cross-corpus integrado** (cartão): Enron 241,0 × SimpleWiki 248,4 MB/s → **é o footprint, não o texto**. *(Conteúdo antes no Apêndice C.)*
- **Fala:** "sem mexer em thread nenhuma, caiu 74% só pelo tamanho do autômato. Esse é o problema."
- **Tempo:** 1:15

### Slide 20 — Escalabilidade do Paralelismo de Texto (slide central)
- Curva speedup × threads (corpus ~10,6 GiB), `speedup_results.svg`:
  - **Snort 55 MiB (azul, moderado):** 1,04 → 2,43 → 3,61 → **4,52× (12)**; pico canônico **4,79×** (dispatch dinâmico).
  - **Emerging Threats 507 MiB (vermelho):** 1,14 → 1,98 → 2,64 → **2,79× (12)**; canônico **pico ~2,85× em 6 threads e depois REGRIDE**.
  - **Eficiência (12 threads):** 37,7% (moderado) × 23,3% (memory-bound).
- **Fala:** "a 42× a cache, a DRAM satura antes de usar todos os núcleos — mais thread (E-core) piora. O teto é físico."
- **Tempo:** 1:30

### Slide 21 — Resultados: Otimização Flat Output Layout
- Ganho single-thread cresce com a pressão de memória: +1,0% (≪L3) → +4,7% (>L3) → **+13,0% (≫L3)**. Muda só o layout; preserva o conjunto exato de matches.
- **Tempo:** 0:40

### Slide 22 — Resultados: Balanceamento em CPUs Híbridas
- O efeito está no **CV**, não na média: estático homogêneo **39,9%–52,9%** → frequency-weighted **1,7%**, dispatch dinâmico 3,3%, flat chunking **0,4%**.
- Compra **previsibilidade**, não pico; o teto continua sendo a memória.
- **Tempo:** 0:30

### Slide 23 — Resultados Negativos: Sharding de Dicionário
- **Sharding por prefixo:** só **1,37×** sobre o baseline (ganho é localidade, não paralelismo); **0,34×** do paralelismo de texto.
- **Composição 2D:** **mais lenta** (0,80×–0,93×) — cada shard varre o texto inteiro ⇒ <em>K</em> shards multiplicam o tráfego de DRAM. Encolher abaixo da LLC exigiria **>40 shards** → inviável.
- **Fala:** "reportar o que não funcionou delimita a fronteira além da qual otimizações plausíveis param de pagar."
- **Tempo:** 0:50

### Slide 24 — Avaliação End-to-End e Construção Paralela [CORTÁVEL]
- Pipeline completo (build + busca + merge), ~10,6 GiB: Snort full **4,50×** (45 s → 10 s); ET **2,76×**.
- **Construção paralela** (cartão): só compensa no dicionário grande (**1,55×** em 8 threads); <1% do tempo num scan multi-GB → o melhor resultado memory-bound usa build sequencial.
- **Tempo:** 0:40

---

## BLOCO 8 — Fechamento (~2,5 min)

### Slide 25 — Conclusão
- **Achado central (blockquote):** o obstáculo é **microarquitetural** (cache + DRAM), não a lógica de casamento; a resposta é paralelizar o **texto** com layout amigo da cache.
- **Objetivos atendidos** (cartão): implementação validada; ganhos 4,79× / 4,52× + eficiências 37,7%/23,3%; escalabilidade em 7 threads × 3 corpora × faixa de 42× da cache.
- **Contribuições** (cartão): caracterização do regime memory-bound; flat layout (+13,0%); **resultados negativos** (sharding/2D falsificados).
- *(Não enquadrar como "RQ1/RQ2 respondidas" — as RQs são as da RSL.)*
- **Tempo:** 1:15

### Slide 26 — Ameaças à Validade e Trabalhos Futuros
- **Ameaças:** processador móvel único + throttling (números conservadores, variância documentada); a conclusão **não** depende da cache pequena (507 MiB excede a LLC de quase todo servidor); explicações inferidas do tempo, **sem telemetria direta**.
- **Futuros:** (1) contadores de hardware (PMU); (2) repetir sharding+chunking em **servidores**; (3) sharding por **footprint real**; (4) protocolo térmico com cool-down.
- **Tempo:** 1:00

### Slide 27 — Encerramento
- "**Obrigado**" (fundo IDP, ciano) + autor / orientador / curso. **Sem** frase de efeito e **sem** "Perguntas e Sugestões" — o convite à arguição é verbal.
- **Tempo:** 0:15

---

## Preparação para a arguição (respostas faladas — NÃO há slides de apêndice)

O deck não tem apêndices; o conteúdo útil foi integrado ao fluxo. Itens abaixo são para preparar a **resposta verbal** a perguntas prováveis:

1. **AC detalhado:** goto/failure/output, NFA × DFA, custo `4·|Q|·256` bytes. *(Base no Slide 7.)* — "por que estoura a cache?"
2. **Amdahl aplicado:** eficiência 37,7% ⇒ fração serial ~15% (merge + dispatch + assimetria P/E na barreira). *(Base no Slide 9.)* — "por que não escala linear?"
3. **Cross-corpus:** Enron 241,0 × SimpleWiki 248,4 MB/s. *(Já no Slide 19.)* — "e se o texto fosse outro?"
4. **Variantes experimentais:** *(Já no Slide 18.)*
5. **Validação/sanitização:** MD5 até 64 threads, ThreadSanitizer. *(Já no Slide 17.)*
6. **Por que pthreads (e não OpenMP/MPI/GPU):** afinidade P/E, portabilidade, autômato read-only compartilhado sem cópia.
7. **Posição na literatura:** throughput de ordem comparável ao head-body (Lee & Yang) mantendo o autômato matematicamente intacto; Harry/SIMD é **ortogonal** (intra-thread), não competidor.

---

## Checklist de coerência (validar antes de finalizar)

- [ ] Todo número bate com `results.tex` / `abstract.tex` (fonte: `sweep.db`, 2026-05-29). **Não** reintroduzir números descartados (7,49×, 4,13×, 1,83×).
- [ ] Headlines consistentes: `4,79×`, `4,52×`, `2,79×`/`2,85×`, `−74,0%`, `+13,0%`, `42×`, `4,50×`, `2,76×`.
- [ ] Sujeito é **Aho–Corasick**; YARA/Snort/Suricata são **aplicações**. Assimetria P/E é **plataforma**, não objeto de estudo.
- [ ] RQs (RSL) só no Slide 11; Slide 6 traz apenas Objetivos; Conclusão (25) não fala em "RQ respondidas".
- [ ] Títulos neutros (sem frases de efeito); encerramento sem "Perguntas e Sugestões".
- [ ] Vírgula decimal; cores IDP **#005DAA** / **#00B3FF**.
- [ ] Snort 55 MiB rotulado como **moderado** (excede L3), nunca "residente na cache".
- [ ] Tempo ensaiado ≤ limite (para 15 min, cortar slides 18 e 24).

### Armadilhas do Marp (aprendidas — não repetir)
- **Markdown não renderiza dentro de blocos HTML** (`<div>`, `<li>`, `<td>`…): `**negrito**`, `*itálico*`, `` `código` `` e `$math$` saem literais. Usar `<strong>`, `<em>`, `<code>` e Unicode.
- **Linha em branco dentro de um `<div>` o encerra:** o `<table>`/`<h3>` indentado seguinte vira "código" e renderiza cru. **Nunca** deixar linha vazia entre tags do mesmo bloco HTML.
- **Marp remove `style` e `class` das tags `<img>`:** dimensionar via **CSS no `<style>`** (ex.: `.fig-trie img { height: 400px; width: auto; }` + `<div class="fig-trie">`), nunca por `style=` inline no `<img>`.
- Build: `npx -y @marp-team/marp-cli@latest slides.md -o slides.pdf --allow-local-files --pdf` (idem para `.html`).
