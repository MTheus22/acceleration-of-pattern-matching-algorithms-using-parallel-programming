# Scripts

Pasta para scripts de apoio da apresentacao.

- `export-pdf.sh` — exporta um `../slides.html` local, caso ele exista, para
  um PDF via `npx decktape@3 reveal` + Chrome headless.
  Uso: `./export-pdf.sh [caminho-de-saida.pdf]`.

Uso esperado:

- extrair poucos numeros canonicos para CSV;
- gerar SVGs de graficos;
- converter ou otimizar figuras.

Regras:

- Scripts devem ser pequenos e reproduziveis.
- Nao embutir numeros sem comentario de origem.
- Saidas devem ir para um caminho explicitamente escolhido pelo operador.
- Se ler `sweep.db`, o script deve apontar claramente para a coleta canonica da
  workstation e permitir conferir contra o TCC.
