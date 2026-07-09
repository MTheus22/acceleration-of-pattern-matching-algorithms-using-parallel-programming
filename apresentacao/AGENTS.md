# AGENTS.md - Apresentacao da defesa

Instrucoes para agentes de IA trabalhando em `apresentacao/`.

## Objetivo da pasta

Preservar o material-base da defesa:

1. `base-apresentacao.md` como narrativa consolidada.
2. `DESIGN.md` como guia visual.
3. `slides.html` como deck atual rastreado.
4. `figuras/` e `scripts/` como apoio para eventual reuso futuro.

O texto final do TCC continua sendo a fonte de verdade. O deck HTML existe como
artefato derivado e pode ser ajustado, mas nao deve contradizer o TCC.

## Leitura obrigatoria

Antes de editar slides, roteiro, graficos ou figuras:

1. Leia este arquivo.
2. Leia `DESIGN.md`.
3. Leia `base-apresentacao.md`.
4. Leia o `../AGENTS.md` do repositorio LaTeX.
5. Leia as partes relevantes do TCC em `../partes/*.tex`.

O texto final do TCC e a fonte de verdade. Notas antigas, decks antigos e
resultados historicos so podem ser usados como contexto, nunca como autoridade.

## Fonte de verdade numerica

Use os numeros que aparecem no TCC atual, especialmente em:

- `../partes/abstract.tex`
- `../partes/methodology.tex`
- `../partes/results.tex`
- `../partes/conclusion.tex`

Principais constantes atuais:

- Plataforma principal: AMD Ryzen 9 9950X, 16 cores, 32 threads, L3 total de
  64 MiB em dois CCDs de 32 MiB.
- Workload principal: Aho-Corasick com dicionarios Snort e Emerging Threats.
- Melhor estrategia nos cenarios canonicos: particionamento de texto com
  despacho dinamico e saida plana.
- Headline Snort: `22,91x`, `7.542 MB/s`, `T=32`.
- Headline Emerging Threats: `18,96x`, `3.979 MB/s`, `T=32`.
- End-to-end no Enron 8x: `22,23x` em Snort e `17,71x` em Emerging Threats.

O i5-1235U aparece apenas como diagnostico de nucleos heterogeneos e de
conteudo desbalanceado. Nao use o i5 como plataforma principal da defesa.

## Linguagem e narrativa

- A apresentacao e em portugues.
- O TCC escrito esta em ingles; traduza a narrativa, mas mantenha termos
  essenciais quando forem convencionais: Aho-Corasick, POSIX Threads, speedup,
  throughput, cache, memory-bound.
- Explique cada termo tecnico na primeira aparicao.
- O sujeito do trabalho e o algoritmo Aho-Corasick. YARA, Snort e Suricata sao
  aplicacoes ou fontes de workloads, nao o objeto do TCC.
- Evite termos internos de desenvolvimento: `searcher`, `ideia 3`, `spec`,
  nomes de fases do sweep, nomes de scripts e nomes de funcoes.
- Se um nome interno for inevitavel na engenharia do deck, traduza no slide:
  "estrategia dinamica com saida plana", nao o identificador C.

## Regras para slides

- Nao colocar perguntas nos slides, nem como titulo nem como corpo principal.
  A RSL pode ser apresentada como lacuna e criterio de selecao, sem listar RQs
  em forma de pergunta.
- Evitar frases de efeito e linguagem de marketing.
- Um conceito por slide.
- Pouco texto. O detalhe fica no roteiro de fala.
- Texto grande, contraste alto, graficos com poucos elementos e destaques
  claros.
- Toda figura reaproveitada do TCC deve ser reavaliada para legibilidade no
  projetor. Nao copiar figura automaticamente se os rotulos ficarem pequenos.
- Toda afirmacao causal sobre cache/DRAM deve ser formulada como inferencia
  consistente com os dados, pois o TCC nao mediu PMU/counters diretamente.
- Nao prometer replicacao estatistica entre execucoes independentes para a
  campanha canonica; ela foi um sweep unico com iteracoes temporizadas.

## Deck atual e futuras recriacoes

O deck atual rastreado e `slides.html`. Se for necessario reconstruir ou
substituir esse deck no futuro, trate isso como uma derivacao nova a partir de
`base-apresentacao.md` e do TCC final. Nao assuma a existencia de `slides.md`,
`build/` ou `roteiro/` neste repositorio.

## Checklist antes de finalizar novo deck ou roteiro

- [ ] Todo numero confere com o TCC atual.
- [ ] Nenhum headline usa os numeros antigos do i5.
- [ ] O deck explica o Aho-Corasick antes de discutir cache e paralelismo.
- [ ] A motivacao esta clara para ouvintes nao especialistas.
- [ ] Resultados negativos aparecem como contribuicao tecnica, sem tom defensivo.
- [ ] Limitações aparecem com honestidade: plataforma unica, sweep canonico sem
      replicas independentes, inferencia microarquitetural sem PMU.
- [ ] O encerramento nao usa "Perguntas?" como slide.
