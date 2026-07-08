### Secao 2 - Motivacao e problema

**Intuito:** fazer a banca entender por que existe problema apesar de o algoritmo
ser classico e eficiente.

**Precisa conter:**

- CPUs passaram a ganhar desempenho por mais nucleos, nao apenas por clock.
- Aho-Corasick faz casamento de multiplos padroes em uma unica passada.
- Usos representativos: Snort, Suricata, YARA, bioinformatica, filtros.
- Em uma entrada grande, a travessia do automato e sequencial: cada estado
  depende do anterior.
- Com dicionarios grandes, o automato passa de dezenas/centenas de MiB e pressiona
  cache/DRAM.

**Ideias de slide:**

- Slide "Processadores ficaram paralelos".
- Slide "Aho-Corasick resolve muitos padroes em uma passada".
- Slide "O problema muda quando o automato cresce".

**Ideias visuais:**

- Linha simples "clock -> nucleos".
- Um fluxo de bytes entrando em um automato e saindo matches.
- Escala visual de tamanhos: L3 64 MiB versus Emerging Threats 506,78 MiB.

**Roteiro de fala:**

- Comecar pelo cotidiano de volume de dados, nao por teoria.
- Explicar que o algoritmo e bom, mas usa um caminho dependente: estado atual +
  byte atual -> proximo estado.
- Conectar isso com hardware: ha muitos nucleos disponiveis, mas a versao
  sequencial concentra o trabalho em um so.
- Introduzir `memory-bound` como "quando a CPU espera dados da memoria".

**Nao falar:**

- Nao apresentar YARA como sujeito do TCC.
- Nao dizer que "o algoritmo e ruim"; o ponto e que ele e sequencial e
  sensivel a memoria em escala.
- Nao chamar o gargalo de DRAM de medida direta; no TCC ele e uma inferencia a
  partir de footprint, throughput e curvas.