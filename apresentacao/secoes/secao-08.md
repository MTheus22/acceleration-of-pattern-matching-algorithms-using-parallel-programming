### Secao 8 - Diagnosticos de balanceamento

**Intuito:** explicar por que despacho dinamico e topologia aparecem no trabalho,
sem desviar a apresentacao da campanha principal.

**Precisa conter:**

- Ryzen homogeneo: nucleos iguais, pouco desequilibrio estrutural.
- i5 hibrido usado apenas como diagnostico P/E.
- Em i5, particionamento estatico teve CV `39,9%` a `52,9%`; politicas de
  balanceamento reduziram para `1,7%` a `3,3%`.
- Em conteudo com matches concentrados, estrategias estaticas perderam
  `16%` a `30%`, enquanto dinamicas ganharam `16%` a `31%`.
- A politica topologica NAO corrige skew de conteudo: no corpus concentrado o
  spread dos workers dela sobe de `5,9%` para `173,4%`, igual ao estatico.
  Nenhum modelo de hardware antecipa onde os matches estao. Esse contraste e o
  que separa as duas familias de balanceamento.
- Conclusao: topologia corrige hardware heterogeneo; so o despacho dinamico
  corrige tambem o desequilibrio de conteudo. E a unica politica avaliada que
  fica balanceada sob as duas fontes de desequilibrio.

**Ideias de slide:**

- Um slide "Onde o balanceamento realmente importa".
- Dois pequenos paineis: hardware heterogeneo e conteudo concentrado.

**Roteiro de fala:**

- Dizer explicitamente que estes diagnosticos nao substituem a plataforma
  principal.
- Usar para justificar robustez, nao para acrescentar novos headlines.

**Nao falar:**

- Nao reabrir a narrativa antiga centrada no i5.
- Nao gastar tempo em afinidade de CPU salvo pergunta da banca.
- Nao dizer que o dinamico "venceu" no i5 em geral: no corpus uniforme desse
  processador as estaticas planas lideram (`473,1` contra `390,6 MB/s`). O que
  o contraste estabelece e robustez sob skew, nao dominancia --- o proprio TCC
  usa essa formulacao.
- Nao apresentar os throughputs do i5 como comparaveis aos da workstation; a
  maquina e outra e o par sintetico tem densidade de matches maior que o Enron.
