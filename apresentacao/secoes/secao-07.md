### Secao 7 - Resultados principais

**Intuito:** entregar o coracao da defesa: o que foi medido e o que isso mostra.

#### Resultado 1 - Footprint domina throughput

**Precisa conter:**

- Com uma thread e corpus fixo, throughput cai de `629,0 MB/s` para
  `210,2 MB/s` conforme o automato cresce de `1,93 MiB` para `506,78 MiB`.
- Queda de `66,6%`.
- Interpretacao: corpus fixo elimina conteudo como causa principal; footprint
  do automato domina.

**Visual recomendado:**

- Grafico simples de linha ou barras em escala logica de footprint.
- Marcar L3 total 64 MiB e, se visualmente claro, slices de 32 MiB.

**Nao falar:**

- Nao afirmar "medimos cache miss"; dizer "a leitura e consistente com pressao
  de cache e memoria".

#### Resultado 2 - Escalabilidade ate 32 threads

**Precisa conter:**

- Snort full: `22,91x`, `7.542 MB/s`, 32 threads.
- Emerging Threats: `18,96x`, `3.979 MB/s`, 32 threads.
- Ambas escalam de forma sublinear.
- Eficiencia em 32 threads: `71,6%` Snort e `59,3%` Emerging Threats.
- A diferenca entre curvas mostra o custo de automato muito maior.

**Visual recomendado:**

- Curva de speedup por threads com linha ideal discreta.
- Destacar T=16 e T=32 para separar cores fisicos e SMT.

**Roteiro de fala:**

- Primeiro descrever a curva, depois interpretar.
- Dizer que 32 e o limite natural da plataforma, nao um ponto arbitrario.
- Ao explicar a queda de eficiencia entre 16 e 32 threads, citar que o SMT
  ainda soma `1,65x` (Snort) e `1,49x` (ET) de throughput: eficiencia cai, mas
  throughput continua subindo ate o ultimo ponto medido.

**Nao falar:**

- Nao afirmar que o despacho dinamico vence em todos os cenarios: no Enron 8x
  com Emerging Threats ha empate tecnico com o particionamento estatico plano
  (`19,83x` contra `19,79x`), e o TCC registra explicitamente que nenhuma
  conclusao depende dessa ordenacao. Ter isso pronto para a arguicao.

#### Resultado 3 - Conteudo do texto e secundario

**Precisa conter:**

- Com Snort e estrategia fixa: `7.976 MB/s` em SimpleWiki e `7.595 MB/s` em
  Enron.
- Aho-Corasick faz uma transicao por byte; se o automato e o mesmo, conteudo
  muda menos que footprint.

**Visual recomendado:**

- Dois numeros lado a lado, nao tabela.

**Cortavel:** sim, se o tempo for curto. Pode entrar como nota no roteiro do
resultado de footprint.

#### Resultado 4 - Layout de saida plana ajuda de forma consistente

**Precisa conter:**

- Ganhos single-thread: `+3,0%`, `+4,2%`, `+6,9%`.
- Ganho cresce com footprint.
- Nao e a principal fonte de speedup, mas reduz custo em um caminho sensivel a
  memoria.

**Visual recomendado:**

- Antes/depois do ponteiro versus array contiguo.
- Pequena barra com os tres ganhos.

#### Resultado 5 - Particionar dicionario e resultado negativo

**Precisa conter:**

- Sharding por prefixo chega a `1,89x` e `620,9 MB/s` --- e o pico ocorre em
  apenas 8 shards, caindo para `1,78x` em 32. Pico antes do limite de threads
  indica que o ganho vem de localidade de cache dentro de sub-automatos
  menores, nao de paralelismo real.
- Texto paralelo chega a `22,91x` e `7.542,3 MB/s`.
- Composicao 2D fica entre `0,73x` e `0,81x` do particionamento de texto.
- Motivo: cada shard precisa varrer o texto; trafego de memoria se multiplica.

**Visual recomendado:**

- Comparacao de trafego: texto lido uma vez versus lido K vezes.
- Barra "1,89x" pequena contra "22,91x" grande.

**Roteiro de fala:**

- Apresentar como contribuicao: uma hipotese plausivel foi testada e delimitada.

**Nao falar:**

- Nao tratar como fracasso do trabalho.
- Nao dizer que sharding nunca serve; dizer "neste desenho e nesta classe de
  workload, nao acompanhou o eixo correto".

#### Resultado 6 - Pipeline completo

**Precisa conter:**

- End-to-end no Enron 8x: `22,23x` Snort e `17,71x` Emerging Threats.
- Build paralelo tem pico de `1,59x` no maior dicionario (324 ms -> ~203 ms em
  16 threads), mas busca domina o tempo total.
- Nuance de honestidade: o build paralelo so compensa no dicionario grande. No
  Snort full o pico e `1,17x` em 4 threads e regride a `0,57x` em 32 threads;
  no menor dicionario e sempre mais lento que o sequencial. Enquadrar como
  beneficio operacional de recarga de regras, nao como throughput.

**Visual recomendado:**

- Dois medidores ou barras de speedup end-to-end.
- Pequena anotacao: "construcao e overhead limitado".

**Cortavel:** sim, mas e util para mostrar que o resultado nao e artificialmente
separado da construcao.