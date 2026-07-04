### Secao 3 - Conceito minimo de Aho-Corasick

**Intuito:** dar repertorio suficiente para a banca entender overlap, automato,
saida de matches e custo de memoria.

**Precisa conter:**

- Trie de padroes.
- Transicoes `goto`.
- Links de falha como retomada sem reler texto.
- Saidas/matches associados a estados.
- Compilacao para tabela de transicao: um lookup por byte, mas tabela grande.

**Ideias de slide:**

- "O automato guarda todos os padroes".
- "Cada byte move o estado".
- "A tabela acelera a busca, mas aumenta o footprint".

**Sequencia criativa recomendada:**

Criar uma sequencia progressiva de 8 a 10 avancos com o mesmo layout:

1. Mostrar padroes pequenos, por exemplo `he`, `her`, `hers`, `she`.
2. Inserir os padroes em uma trie.
3. Destacar o estado inicial.
4. Ler o primeiro byte de uma palavra de exemplo.
5. Avancar uma transicao.
6. Emitir um match quando um estado final e atingido.
7. Mostrar uma falha e o link de retomada.
8. Continuar sem voltar no texto.
9. Mostrar que a execucao e uma cadeia de dependencias.
10. Transformar a figura na tabela `estado x byte`.

**Roteiro de fala:**

- A sequencia deve substituir explicacao longa.
- O ponto final da sequencia e: "essa tabela e otima para um nucleo, mas cresce
  com o numero de estados".

**Nao falar:**

- Nao comparar em detalhe com KMP, Boyer-Moore ou Wu-Manber.
- Nao usar formalismo pesado de automatos se a imagem ja transmitiu a ideia.