### Secao 6 - Metodologia experimental

**Intuito:** dar confianca nos resultados sem transformar a apresentacao em uma
auditoria de benchmark.

**Precisa conter:**

- Plataforma principal: AMD Ryzen 9 9950X, 16 cores, 32 threads, L3 64 MiB,
  DDR5, Linux, C11/GCC, POSIX Threads.
- Dicionarios: Snort-100, Snort-1k, Snort full, Emerging Threats.
- Corpora: SimpleWiki, Enron, Enron 8x, skew pair como diagnostico.
- Metricas: throughput, speedup, eficiencia, tempo de build, end-to-end.
- Desenho experimental dirigido por hipoteses: cada hipotese e falseavel,
  isola um unico eixo de projeto e mapeia para um experimento e uma secao de
  resultados. Vale um slide ou meia fala; mostra que os resultados negativos
  eram hipoteses testadas, nao acidentes.
- Corretude em tres niveis: match set exato contra o baseline sequencial,
  digest MD5 do fluxo canonicalizado ate T=64 (2x oversubscription) e
  ThreadSanitizer sem data races. No slide basta "equivalencia exata +
  sanitizers"; os niveis ficam no roteiro para arguicao.
- Limitacao metodologica: campanha canonica e sweep unico com iteracoes
  temporizadas, sem replicas independentes para mediana/IQR. Excecao que
  fortalece: o diagnostico de skew usou mediana de cinco invocacoes
  independentes por configuracao.

**Ideias de slide:**

- Tabela visual compacta de plataforma + workloads.
- Slide "Como os numeros foram protegidos" com tres selos: baseline, repeticoes
  temporizadas, corretude.

**Ideias visuais:**

- Barras de tamanho dos automatos.
- Mini diagrama da plataforma com 16 cores/32 threads.
- Checkpoints de validade.

**Roteiro de fala:**

- Explicar por que Ryzen e a plataforma principal.
- Separar claramente o i5: diagnostico, nao headline.
- Enfatizar que todos os resultados principais usam a mesma campanha.

**Nao falar:**

- Nao dizer que ha validacao estatistica completa entre execucoes independentes.
- Nao sobrecarregar com comandos de coleta.