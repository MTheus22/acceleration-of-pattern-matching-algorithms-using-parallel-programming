### Secao 5 - Estrategia adotada

**Intuito:** explicar a solucao de forma que os resultados facam sentido.

**Precisa conter:**

- Tres fases: construir automato, buscar em paralelo, mesclar resultados.
- Automato fica compartilhado e somente leitura.
- Cada thread varre um segmento do texto e escreve matches em lista privada.
- Sem locks no caminho quente da busca.
- Overlap de `Lmax - 1` bytes para nao perder padroes na fronteira.
- Layout de saida plana para reduzir ponteiros.
- Despacho dinamico como forma de robustez contra desequilibrio.
- Particionamento do dicionario avaliado como contraste, nao como solucao final.

**Ideias de slide:**

- "Uma decisao estrutural: automato imutavel".
- "Dividir o texto sem perder matches na borda".
- "Remover ponteiros da emissao de matches".
- "Estrategias avaliadas como eixos".

**Ideias visuais:**

- Pipeline horizontal: construcao -> busca concorrente -> merge.
- Dois segmentos com uma palavra atravessando a fronteira.
- Antes/depois do layout de saida: lista encadeada versus bloco contiguo.
- Comparacao de trafego: texto lido uma vez versus texto relido por shard.

**Roteiro de fala:**

- Destacar que a solucao preserva equivalencia com o sequencial.
- Explicar que o overlap e pequeno e determinado pelo maior padrao.
- Dizer que a decisao de nao mexer no automato facilita validar corretude.

**Nao falar:**

- Nao entrar em detalhes de `pthread_setaffinity_np` salvo em pergunta.
- Nao listar todas as variantes pelo nome interno.
- Nao vender despacho dinamico como sempre mais rapido; ele foi escolhido por
  throughput canonico e robustez.