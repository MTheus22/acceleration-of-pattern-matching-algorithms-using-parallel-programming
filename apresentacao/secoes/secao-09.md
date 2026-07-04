### Secao 9 - Conclusao, limitacoes e futuro

**Intuito:** fechar com contribuicoes claras, sem prometer alem dos dados.

**Precisa conter:**

- Achado central: o limite dominante e microarquitetural/memoria, nao a logica
  de casamento.
- Contribuicoes:
  - implementacao paralela correta em C/POSIX Threads;
  - caracterizacao do regime memory-bound no Ryzen;
  - estrategia vencedora: texto + automato read-only + saida plana + despacho
    dinamico;
  - resultados negativos sobre sharding e composicao 2D;
  - diagnosticos de balanceamento.
- Limitacoes:
  - plataforma canonica unica;
  - sweep canonico sem replicas independentes;
  - cache/DRAM inferidos por tempo e footprint, sem PMU;
  - skew diagnosticado no i5, nao repetido na workstation.
- Trabalhos futuros:
  - contadores de hardware;
  - replicas independentes com mediana/IQR;
  - repetir skew na workstation;
  - ampliar para outras CPUs/NUMA.

**Ideias de slide:**

- Slide de sintese com quatro achados.
- Slide de limitacoes e proximos passos, sem tom defensivo.
- Slide final "Obrigado".

**Nao falar:**

- Nao usar Perguntas? no slide.
- Nao encerrar com frase de efeito.