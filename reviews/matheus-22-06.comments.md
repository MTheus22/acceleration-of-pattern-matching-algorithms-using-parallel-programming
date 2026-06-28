# Comentarios de revisao

- Total: 63
- Abertos: 63
- Concluidos: 0
- Invalidos: 0
- Rejeitados: 0

## Pagina 2

### Comentario 001

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T09:08:53-03:00`

**Comentario**

Undergraduate Thesis submitted in partial fulfillment of the requirements for the degree
of Bachelor of Computer Science at the Brazilian Institute of Education, Development
and Research (IDP).

**Trecho associado**

> Qualification Exam document submitted as a partial requirement for the Bachelor’s
> Degree in Software Engineering at the Instituto Brasileiro de Ensino,
> Desenvolvimento e Pesquisa (IDP).

## Pagina 3

### Comentario 002

- Status: `open`
- Metodo: `highlight_only`
- Tipos: `Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T09:09:07-03:00`

**Comentario**

[Sem comentario textual]

**Trecho associado**

> Qualification Exam document submitted as a partial requirement for the Bachelor’s De-
> gree in Software Engineering at the Instituto Brasileiro de Ensino, Desenvolvimento e
> Pesquisa (IDP).

## Pagina 12

### Comentario 003

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T09:13:11-03:00`

**Comentario**

Aqui você fala o nome Aho-Corasick, mas o leitor ainda não tem um entendimento duqe ele faz. Então precisa de uma frase sumarizando isso para contextualizar o leitor. Algo como:
These applications rely on highly efficient multi-pattern-matching algorithms, and the Aho-Corasick algorithm stands out because it can search for multiple patterns simultaneously while scanning the input only once, achieving linear-time complexity with respect to the input text.

**Trecho associado**

> possibilities for performance enhancement; however, to take advantage of multi-core
> processors, programs must be intentionally written or adapted to execute tasks in par-
> These applications rely on highly efficient multi-pattern-matching algorithms, and the

## Pagina 13

### Comentario 004

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T09:17:48-03:00`

**Comentario**

Aqui você pode terminar falando sobre a revisão sistemática feita no capítulo XX.
This observation is supported by the systematic literature review presented in Chapter 3.

**Trecho associado**

> comparatively little attention.

### Comentario 005

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T09:21:04-03:00`

**Comentario**

Essa afirmação precisa de citação.

**Trecho associado**

> the primary performance
> bottleneck shifts from computation to memory bandwidth.

### Comentario 006

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T09:22:32-03:00`

**Comentario**

Faltou o objetivo de fazer uma Revisão Sistemática da Literatura.

**Trecho associado**

> architectures, using the POSIX Threads programming model, in order to accelerate
> 1. To design and implement a parallel version of the Aho-Corasick algorithm in C,
> using the pthreads API, exploiting intra-input parallelism on shared-memory multi-

## Pagina 16

### Comentario 007

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T09:29:39-03:00`

**Comentario**

This distinction is fundamental to the present work, which exploits true hardware parallelism through multiple CPU cores.

**Trecho associado**

> tion of different tasks, simulating parallelism through preemption. True parallelism, on
> 2.1.1 Parallel Computing Architectures
> Parallel computer architectures are classified according to various criteria. A promi-

## Pagina 19

### Comentario 008

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T10:30:56-03:00`

**Comentario**

As vezes, falta no texto uma relação do porque o tópico está sendo apresentado. aqui no 2.2 mesmo, daria pra falar que vai ser utilizado nos experimentos.
The evaluation of parallel algorithms requires objective metrics that quantify both performance gains and resource utilization. Accordingly, the metrics presented in this section provide the basis for evaluating the implementation proposed in this work and for interpreting the experimental results presented in Chapters 5 and 6.

**Trecho associado**

> solution, whose purpose is to keep the heterogeneous cores from idling at the synchro-
> Performance evaluation is fundamental to metrics
> allel program. The following metrics compare this

## Pagina 22

### Comentario 009

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T10:37:51-03:00`

**Comentario**

O \caption de figuras é depois do \include. Ele tem que aparecer abaixo da figura e não acima. Somente tabela é que normalmente fica acima.
Se as próvimas figuras estiverem assim, não vou anotar o comentário, mas precisa corrigir em todas.

**Trecho associado**

> Figure 2: Example trie storing {“car”, “cat”, “cart”, “dog”}. Nodes marking the end of a
> c
> d

### Comentario 010

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T10:36:09-03:00`

**Comentario**

Acho que a gente já conversou sobre isso. Você cita quando é adaptado de alguém, e não quando você mesmo fez.

**Trecho associado**

> Source: Prepared by the author.

## Pagina 24

### Comentario 011

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T11:33:00-03:00`

**Comentario**

Acho que pode deixar aqui, mas esse texto faz mais sentido no início do 2.3 pro leitor ter uma noção da relação do conteúdo com o todo. Aí no final, um parágrafo (ao invés de uma subseção) só reforçando o que já foi apresentado.

**Trecho associado**

> lead to considerable memory consumption due to numerous unused (null) links [14],
> The trie data structure is a cornerstone for numerous
> work [4]. A thorough grasp of trie principles is thus essential for developing and an-

## Pagina 25

### Comentario 012

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T12:31:53-03:00`

**Comentario**

Dá pra botar o algoritmo aqui.

**Trecho associado**

> text T at every possible starting position i (from 0 to N − M ). For each alignment, P is
> compared character by character, from left to right, against Dá
> simplicity, Knuth, Morris, and Pratt (1977) state that this method can be highly ineffi-

## Pagina 27

### Comentario 013

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T12:36:19-03:00`

**Comentario**

Acrescentar que ele via ser explorado na próxima seção.

**Trecho associado**

> pattern-matching machine, typically based on a trie structure augmented with special-
> ized failure transitions [4]. This automaton-based paradigm
> for efficiently solving multi-pattern matching problems.

## Pagina 28

### Comentario 014

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T14:31:07-03:00`

**Comentario**

os nomes das funções não estão em notação matemática

**Trecho associado**

> (f):
> f(s)
> output(s),
> output(s)
> output(s) ∪ output(f(s)).

### Comentario 015

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T14:33:02-03:00`

**Comentario**

Aqui eu acho que você pode explicar em mais detalhes como o autômato (da figura) funciona em um exemplo.

**Trecho associado**

> chain.
> The complete automaton, combining the goto transitions, failure links, and output
> match sets, is illustrated in Figure 3 for the pattern set K = {”he”, ”she”, ”hers”}.

## Pagina 29

### Comentario 016

- Status: `open`
- Metodo: `highlight_only`
- Tipos: `Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T14:32:40-03:00`

**Comentario**

[Sem comentario textual]

**Trecho associado**

> goto

### Comentario 017

- Status: `open`
- Metodo: `highlight_only`
- Tipos: `Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T14:32:51-03:00`

**Comentario**

[Sem comentario textual]

**Trecho associado**

> Source: Prepared by the author.

## Pagina 34

### Comentario 018

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T16:38:14-03:00`

**Comentario**

Um parágrafo depois das RQs:
These research questions were formulated based on the objectives of this work and aim to identify both parallelization strategies and optimization techniques applicable to the proposed implementation.

**Trecho associado**

> 2. RQ2: What specific optimizations for the Aho-Corasick algorithm are employed in
> application scenarios involving extensive pattern sets, particularly within domains
> sion and exclusion criteria.

## Pagina 40

### Comentario 019

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T18:48:14-03:00`

**Comentario**

Sempre que um título ficar na última linha assim, você dá um \newline antes dele, para jogar o conteúdo para a próxima página.

**Trecho associado**

> grained parallelism as the GPU counterpart of the coarse-grained, chunked Pthreads
> strategy adopted in this thesis.
> 30

## Pagina 51

### Comentario 020

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T21:08:37-03:00`

**Comentario**

Começar o 3.4 com:
The systematic review answered both research questions by identifying the predominant parallelization strategies for Aho–Corasick on multi-core CPUs and the optimization techniques most frequently employed in practical applications.

**Trecho associado**

> thesis adopts; conversion from microseconds plus payload size in bytes is therefore re-
> quired when quoting the Aldwairi figures as competitors. The paper should be cited for
> SYNTHESIS AND IDENTIFIED GAP

### Comentario 021

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T21:09:24-03:00`

**Comentario**

Eu acho que tá muito misturada essa síntese. Acho que daria pra categorizar entre paralelização, otimização de memória e aplicações.

**Trecho associado**

> not native shared-memory threading (MPI in Qu et al. [19], Erlang OTP processes over
> a non-Aho–Corasick
> Aldwairi et al. [6] contributes benchmark methodology rather than a parallel technique.

## Pagina 52

### Comentario 022

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T21:10:45-03:00`

**Comentario**

Trocar por:
Based on these findings, the next chapter presents the design and implementation of the proposed shared-memory parallel version of the Aho–Corasick algorithm.

**Trecho associado**

> No reviewed study delivers this combination, which
> motivates the design and the experimental questions of the chapters that follow.

## Pagina 54

### Comentario 023

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T21:13:08-03:00`

**Comentario**

Onde tá destacado, tem que comentar que é inspirado no que foi coletado da revisão:
The design choices presented in this chapter are directly motivated by the findings of the systematic literature review discussed in Chapter 3.

**Trecho associado**

> The design is guided by a single structural decision from which every other
> property follows.

### Comentario 024

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T21:15:25-03:00`

**Comentario**

Por que tem um gap de texto aqui? Se for por causa da figura naõ caber, a próxima seção poderia apareer aqui. Não tem necessidade de new page assim.

**Trecho associado**

> benefits both the sequential and the parallel cases. The remainder of this chapter de-
> scribes each component. The overall phased execution flow of the proposed parallel
> framework is illustrated in Figure 5.

## Pagina 55

### Comentario 025

- Status: `open`
- Metodo: `highlight_only`
- Tipos: `Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T21:16:09-03:00`

**Comentario**

[Sem comentario textual]

**Trecho associado**

> Source: Prepared by the author.

## Pagina 56

### Comentario 026

- Status: `open`
- Metodo: `highlight_only`
- Tipos: `Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T21:19:06-03:00`

**Comentario**

[Sem comentario textual]

**Trecho associado**

> Source: Prepared by the author.

### Comentario 027

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T21:23:36-03:00`

**Comentario**

Tem zero explicação de como foi feito aqui.

**Trecho associado**

> processor, where Performance and Efficiency cores run at different clock frequencies,
> equal-sized segments cause the threads
> and scales each segment in proportion to the relative speed of the core processing it.

## Pagina 57

### Comentario 028

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T23:37:09-03:00`

**Comentario**

espaço sobrando que não faz sentido

**Trecho associado**

> from the inner loop. This optimization is purely a memory-layout change: it preserves
> the exact set of reported matches and is inherited by every scanning variant, whether
> sequential or parallel. Figure 7 contrasts this contiguous layout with the canonical linked

## Pagina 58

### Comentario 029

- Status: `open`
- Metodo: `highlight_only`
- Tipos: `Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-26T23:36:42-03:00`

**Comentario**

[Sem comentario textual]

**Trecho associado**

> Source: Prepared by the author.

### Comentario 030

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T10:29:12-03:00`

**Comentario**

aqui também falta uma explicação mais clara, não dá pra entender se essa partição é livre de custos por exemplo, e dá até pra fazer uma figura pra seção não parecer só um texto jogado aqui com um ou dois parágrafos

**Trecho associado**

> then scanned over the
> working set, which might
> single monolithic automaton. The framework also supports a two-dimensional compo-

## Pagina 61

### Comentario 031

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T10:48:20-03:00`

**Comentario**

muito marketing e pouco técnico esse primeiro parágrafo.. as vezes é melhor ser um pouco mais direto
This chapter describes the experimental methodology adopted to evaluate the proposed parallel implementation of the Aho–Corasick algorithm. The evaluation focuses on assessing its performance, scalability, and correctness under a shared-memory multi-core environment, using representative pattern dictionaries and text corpora. The experimental design aims to quantify the impact of the optimization strategies introduced in Chapter 4 and to provide a consistent basis for analyzing their effectiveness.

**Trecho associado**

> The central
> object of study is not a particular processor, but a computational regime: the behaviour
> of multi-pattern matching when the automaton footprint greatly exceeds the last-level
> cache (LLC), which is the operating point of signature-based intrusion detection over
> large rule sets.
> The reference machine is therefore treated as a measurement plat-
> form rather than as the subject of the investigation, and the conclusions are framed in
> terms of relative scalability behaviour (speedup, throughput, and efficiency) instead of
> absolute production capacity.

### Comentario 032

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T11:03:24-03:00`

**Comentario**

mesma coisa aqui, o principal é alimentar o leitor com a estrutura do que ele vai ler nas subseções, isso de princípios me parece bem estranho aqui, como se o leitor não soubesse o que é uma metodologia

**Trecho associado**

> The methodology is organized around four principles: (i) every parallel variant is
> validated for
> claim
> is made; (ii)
> be
> attributed the
> experiments are intended to falsify, not merely to confirm; and (iv) measurement noise
> inherent to the hardware is reported explicitly rather than hidden.

### Comentario 033

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T11:04:54-03:00`

**Comentario**

Isso daqui tem que ser atualizado né.

**Trecho associado**

> All measurements were performed on a single Intel Core i5-1235U processor, a
> hybrid (heterogeneous)
> by the frequency-weighted partitioning strategy. The memory hierarchy comprises a

## Pagina 62

### Comentario 034

- Status: `open`
- Metodo: `ink_bbox`
- Tipos: `FreeText,Ink`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T11:13:04-03:00`

**Comentario**

Essa coluna faz sentido estar aqui? Você já está ecoando um resultado de arquitetura independente de teste ou organização de hardware aqui.
Quando você tem uma relação de dados, você precisa de um parâmetro que se relacione. Exemplo: Cabe em cache
Do jeito que tá, me parece extreamente dependente da arquitetura onde o teste foi executado, o que vai totalmente contra a premissa da metodologia.

**Trecho associado**

> Cache regime
> Well within L3 (cache-resident)
> Near the L3 boundary
> Exceeds L3 (moderate)
> 42× the L3 (memory-bound)
> Threats rule sets.

### Comentario 035

- Status: `open`
- Metodo: `highlight_only`
- Tipos: `Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T11:20:39-03:00`

**Comentario**

[Sem comentario textual]

**Trecho associado**

> Source: Prepared by the author from

## Pagina 63

### Comentario 036

- Status: `open`
- Metodo: `highlight_only`
- Tipos: `Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T11:19:52-03:00`

**Comentario**

[Sem comentario textual]

**Trecho associado**

> Source: Prepared by the author.

### Comentario 037

- Status: `open`
- Metodo: `highlight_only`
- Tipos: `Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T11:20:43-03:00`

**Comentario**

[Sem comentario textual]

**Trecho associado**

> Source: Prepared by the author.

### Comentario 038

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T11:40:25-03:00`

**Comentario**

(BFS)

**Trecho associado**

> their automata fit in or near the cache and expose the cross-over point at which mem-
> ory pressure begins to dominate.

## Pagina 64

### Comentario 039

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T11:43:57-03:00`

**Comentario**

Lá atrás você não explicou como isso daqui foi calculado, e agora eu leio e ainda não faz sentido pra mim. Uma coisa é você dividir em tarefas pequenas que cada thread vai pegando. Outra coisa é falar que é topology-aware, o que eu ainda não visualizei. Ambos são uma coisa só, ou deveriam ser dois axis diferentes?

**Trecho associado**

> Topology-aware chunking that weights segment
> sizes by core frequency.
> Source: Prepared by the author.

### Comentario 040

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T12:47:55-03:00`

**Comentario**

Olhando essa tabela, acho que faz sentido essa seção informar quais estratégias podem ser combinadas com qual.

**Trecho associado**

> and text chunking.
> The text-parallelism axis partitions the
> allel variant. Because the automaton produced by the parallel construction is bit-for-

## Pagina 65

### Comentario 041

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T15:12:10-03:00`

**Comentario**

Aqui você tem que falar separadamente o que é métrica e o que é "ferramenta de apoio". O que tou chamando de ferramenta de apoio: o que não mede performance (não achei um nome melhor). Coeficiente de variação, per-thread timing, isso tá mais relacionado com diagnóstico do que desempenho. Separa em dois parágrafos isso.

**Trecho associado**

> strategy is valid, which cleanly isolates the contribution of each axis. An exploratory
> software-prefetch variant of the
> The primary metrics follow the standard definitions introduced in the theoretical

### Comentario 042

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T15:18:47-03:00`

**Comentario**

Eu acho que fica melhor se explicar cada uma em um parágrafo diferente. Pra ficar mais legível e claro na mente de quem tá lendo pela primeira vez.
E explica o que é o warmup em um parágrafo separado no início, aí não precisa ficar repetindo.

**Trecho associado**

> Table 5: Per-phase repetition protocol of the formal sweep (2026-05-29), verified
> Phase A (speedup curves) sweeps thread counts T ∈ {1, 2, 4, 6, 8, 10, 12} for the
> canonical Enron corpus and T ∈ {1, 4, 8, 12} for the eight-fold replica, as recorded in

## Pagina 66

### Comentario 043

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T15:17:55-03:00`

**Comentario**

Isso daqui tem que sair, por isso quero os experimento em uma máquina desktop. Eu acho que esse parágrafo sai todo. Ele no máximo tem que ser mencionado em um capítulo de conclusão, a partir da observação do resultado dos experimentos.

**Trecho associado**

> The refer-
> ence machine is a thermally constrained mobile processor.

### Comentario 044

- Status: `open`
- Metodo: `highlight_only`
- Tipos: `Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T15:20:35-03:00`

**Comentario**

[Sem comentario textual]

**Trecho associado**

> A caveat specific to the measurement platform must be stated explicitly. The refer-
> ence machine is a thermally constrained mobile processor. Under sustained all-core
> load lasting hours, the package throttles its frequency, and the measured multi-threaded
> throughput settles roughly 15 to 35% below what isolated bursts on a cold processor
> report. The values published in this work are deliberately the sustained, under-load fig-
> ures, which are conservative and reproducible; cold-burst peaks are treated as the non-
> sustainable upper bound and are not used as headline results. This thermal sensitivity
> is itself a finding consistent with the central thesis: at the scale of interest, performance
> is governed by physical resource limits rather than by the number of threads.

### Comentario 045

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T15:34:48-03:00`

**Comentario**

Essa seção tem que ser quebrada em parágrafos.
O primeiro parágrafo você introduz e lista as estratégiras. Para só depois você explicar cada uma separadamente em um parágrafo.
Na introdução você deixa claro a importância da corretude, que não adianta ser mais rápido, se o resultaod não é o mesmo da execução serial. Então, busca-se reduzir o tempo de execução, mas preservar a corretude do algoritmo.

**Trecho associado**

> 5.7
> CORRECTNESS VALIDATION
> parallel construction produces an automaton bit-for-bit identical to the sequentially built

## Pagina 67

### Comentario 046

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T15:44:10-03:00`

**Comentario**

Aqui tem que estruturar melhor. As hipóteses dão a impressão que não tem relação com o objetivo principal do trabalho (porque apareceu só aqui). Você precisa relacionar cada experimento com uma hipótse diferente, se quer escrever assim. Ou seja, cada experimento vai responder uma pergunta diferente. Exemplos:
- 1 - avaliar o speedup
- 2 - avaliar a eficiência
- 3 - avaliar a escalabilidade
- 4 - comparar
E no final, você fala que o próximo capítulo vai vão ter o resultados desse planejamento experimental.

**Trecho associado**

> flattened output layout reduces emission cost in both the sequential and parallel cases;
> that a level-synchronous parallel construction reduces build time for large dictionar-
> ies; that prefix-based dictionary sharding can recover throughput in the memory-bound

## Pagina 69

### Comentario 047

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T15:54:26-03:00`

**Comentario**

Você já tá concluindo coisas aqui, ao mesmo tempo que não dá passando para o leito a organização da seção.
This chapter presents the experimental evaluation of the proposed parallel Aho–Corasick implementation. Following the methodology established in Chapter 5, the results are analyzed to assess the effectiveness of the proposed optimization strategies and to evaluate the research hypotheses defined for this work.
Section 6.1 examines the relationship between automaton footprint and search performance, establishing the experimental context for the subsequent analyses. Sections 6.2 through 6.7 evaluate the individual optimization strategies introduced in Chapter 4, including text partitioning, output-layout optimization, topology-aware scheduling, dictionary partitioning, and their combinations. Section 6.8 analyzes the construction phase of the automaton, while Section 6.9 summarizes the experimental findings and discusses their implications for the proposed implementation.

**Trecho associado**

> contribution of each optimization axis; and it finally reports the cumulative behaviour at
> scale, including the strategies that did not pay off. Throughout, speedup is measured
> against the single-threaded
> tained, under-load figures,

### Comentario 048

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T16:42:08-03:00`

**Comentario**

Agora eu entendi a tabela lá dá página 52, e continua não fazendo sentido ela. Qualquer coisa relacionada com L3 é totalmente dependente de arquitetura. A maioria dos processadores nem tem L3. Por isso te falei em alguma reunião que throughput era irrelevante por que a gente queria fazer, mas você manteve mesmo assim.

**Trecho associado**

> Source: Prepared by the author.

### Comentario 049

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T16:47:01-03:00`

**Comentario**

Pra manter essa seção, ela tem que estar escrita com o pensamento de mensurar o impacto do tamanhyo do autômato em relação ao throughput. Qualquer coisa relacionada com L3, seria necessário medir cache miss, latência e até banda.
Aqui tem que ser reescrito para mostrar a degradação do throughput em função do aumento do autômato e discutir (na conclusão) a hierarquia de memória como uma possível explicação para o comportamento observado, reservando referências explícitas à LLC para a análise dos resultados. Isso não pode ser a base para o experimento.
Essa seção tem que ter como objetivo ou começar com:
Before evaluating the proposed optimizations, this experiment characterizes how the execution platform responds to increasing automaton footprints.

**Trecho associado**

> THROUGHPUT
> (MB/s)
> Snort-100

## Pagina 70

### Comentario 050

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T16:59:00-03:00`

**Comentario**

Falta um texto inicial pra relembrar o que é o experimento e o que vai avaliar.

**Trecho associado**

> to minimize scheduler and ther-
> mal noise.

## Pagina 71

### Comentario 051

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T16:56:07-03:00`

**Comentario**

Por que parou em 12, se parece que o speedup vai continuar subindo se aumentar o número de threads? Normalmente você executa até achar uma estabilidade ou degradação, pra saber qual o máximo.

**Trecho associado**

> grow.
> 5
> 1

### Comentario 052

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T17:00:25-03:00`

**Comentario**

Primeiro você descreve os resultados, depois você tece qualquer observação. Misturar os dois fica confuso. E lembrando agora, você elencou as hipóteses, mas em momento nenhum você citou elas aqui. Tem que reescrever bastante aqui.

**Trecho associado**

> Source: Prepared by the author.
> CV 2%), the highest search speedup observed on the intrusion-detection-scale dic-
> tionaries. With the memory-bound dictionary, the curve flattens far earlier: the best

## Pagina 72

### Comentario 053

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T17:03:25-03:00`

**Comentario**

Isso daqui não foi medido. Você pod efalar que tel relação com comportamento da memória, mas afirmar dessa forma como tá, sem medir banda, cache hit, cache miss tá concluindo mais do que deveria.

**Trecho associado**

> DRAM saturation rather than threading overhead,

### Comentario 054

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T17:05:12-03:00`

**Comentario**

De novo: a ordem dessas seções tem que ser:
introdução -> gráfico -> descrição do resultado -> interpretação -> conclusão
Quando for trocar os testes, fazer com base nisso daqui.

**Trecho associado**

> two corpora is nearly identical (241.0 MB/s versus 248.4 MB/s), and the twelve-thread
> regardless of match density, the footprint of the automaton dominates the behaviour far
> more than the characteristics of the corpus.

## Pagina 74

### Comentario 055

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T17:14:40-03:00`

**Comentario**

Ainda não sei se essa seção fica, com os testes sendo executados no outro computador, mas partindo da premissa que eles ficam. Esse figura das partições deveria estar na proposta. Além disso, ela é bem estranha, porque os retângulos parecem demonstrar tempo, ao invés de tamanho da tarefa. Daria pra representar melhor, se o retângulo fosse proporcional ao tamanhod a tarefa, e ele estivesse esticado no tempo.

**Trecho associado**

> topology-aware, frequency-weighted chunking sizes each segment to its core’s speed;
> (c) dynamic dispatch hands out small tasks on demand. Both (b) and (c) equalize fin-
> ishing times.

## Pagina 75

### Comentario 056

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T18:08:34-03:00`

**Comentario**

De novo, você tá explicando e mostrando figura de algo que é pra estar na proposta de solução.

**Trecho associado**

> first traversal that computes the failure links depends only on shallower levels and can
> therefore be processed
> next level begins.

## Pagina 76

### Comentario 057

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T18:10:20-03:00`

**Comentario**

Não faz sentido mostrar só o pico para cada, a coluna perde o sentido, mostre múltiplas colinas onde cada coluna é uma quantidade de threads.

**Trecho associado**

> Source: Prepared by the author.

## Pagina 77

### Comentario 058

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T18:13:29-03:00`

**Comentario**

Se você tá comentando um dado, ele deveria estar na tabela.

**Trecho associado**

> Source: Prepared by the author.
> 1.35× at two shards,

### Comentario 059

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T18:23:55-03:00`

**Comentario**

Mudar nome da seção pra ficar de forma mais descritiva, algo como (exemplo)
Combined Strategy Evaluation

**Trecho associado**

> 6.7 COMPOSING
> POTHESIS

## Pagina 78

### Comentario 060

- Status: `open`
- Metodo: `highlight`
- Tipos: `FreeText,Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T18:20:31-03:00`

**Comentario**

mais teoria que o leitor não aprendeu na proposta.. você tem que explicar na proposta, e aqui só relembrar, essas imagens de explicaçaõd e como funcionam tem que estar tudo lá

**Trecho associado**

> Prepared by the author.

## Pagina 79

### Comentario 061

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T18:27:27-03:00`

**Comentario**

não sei se entendi essa seção, ela é algum experimento que não tá descrito? Avaliar tudo junto não necessariamente é algo útil, e lendo aqui nada parece agregar para o que já foi mostrado. No máximo merece um parágrafo na conclusão e não uma seção separada.

**Trecho associado**

> Finally, the complete pipeline—automaton
> of the corpus (with the parallel strategies junto
> reported as end-to-end wall-clock time on mostrado.

## Pagina 80

### Comentario 062

- Status: `open`
- Metodo: `nearby_lines`
- Tipos: `FreeText`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T18:30:00-03:00`

**Comentario**

Aqui não andianta ler com esses testes, nem o capítulo da conclusão.

**Trecho associado**

> Overall, the results point to a single clear conclusion. The dominant obstacle to
> shifts from thread scheduling to DRAM bandwidth — the situation in which a cache-
> friendly emission path helps the most.

## Pagina 84

### Comentario 063

- Status: `open`
- Metodo: `highlight_only`
- Tipos: `Highlight`
- Autor: `j3r3mias _`
- Criado em: `2026-06-27T18:30:33-03:00`

**Comentario**

[Sem comentario textual]

**Trecho associado**

> 7.2
> FUTURE WORK

