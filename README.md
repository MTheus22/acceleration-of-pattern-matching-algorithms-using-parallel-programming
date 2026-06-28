# Acceleration of Pattern Matching Algorithms Using Parallel Programming

Projeto LaTeX do Trabalho de Conclusão de Curso (TCC) de **Matheus
Antônio de Castro de Barros** — Engenharia de Software, IDP, 2025.
Orientador: **Jeremias Moreira Gomes**.

O trabalho projeta, implementa e avalia uma versão paralela do
algoritmo **Aho–Corasick** para correspondência multi-padrão,
direcionada a **CPUs multi-core em memória compartilhada** usando a
API **POSIX Threads (Pthreads)**. A implementação prática vive em um
repositório separado:
[`parallel-aho-corasick`](../parallel-aho-corasick).

> **Mudança de escopo**: versões anteriores do texto enquadravam o
> trabalho como uma otimização específica do mecanismo Aho–Corasick do
> YARA. O foco atual é genérico — acelerar o Aho–Corasick em si — com
> YARA citado apenas como aplicação representativa. Veja o commit
> `8f79895` para o registro dessa transição.

## Sumário do conteúdo

- **Introdução**: motivação a partir da natureza sequencial do
  Aho–Corasick e da prevalência de arquiteturas multi-core.
- **Fundamentação Teórica**: arquiteturas paralelas (Flynn, MIMD,
  memória compartilhada), métricas (speedup, eficiência, lei de
  Amdahl, lei de Gustafson), Pthreads, tries, problema do
  pattern matching e o algoritmo de Aho–Corasick.
- **Revisão Sistemática**: protocolo SLR (RQs, strings de busca em
  ACM/IEEE/Scopus/WoS, critérios IC/EC) sobre paralelização do
  Aho–Corasick em CPUs multi-core, janela 2015–2025.
- **Proposta**: estratégia de paralelismo de dados com chunking,
  overlap `max_pattern_len - 1` e listas thread-local de matches.

## Estrutura do repositório

```
main.tex                  Documento raiz. Define metadados, carrega a classe
                          e orquestra as seções.
referencias.bib           Bibliografia em BibTeX (estilo IEEE).
Makefile                  Pipeline xelatex → bibtex → xelatex → xelatex.
partes/                   Conteúdo das seções (uma por arquivo .tex).
  introduction.tex        Introdução, motivação, objetivos, estrutura.
  fundamentacao.tex       Fundamentação teórica.
  rsl.tex                 Revisão sistemática.
  proposal.tex            Solução proposta e cronograma.
  results.tex             (em construção) resultados experimentais.
  abstract.tex            Resumo / abstract.
  apendicei.tex           Apêndices.
  anexoi.tex              Anexos.
configs/                  Classe LaTeX customizada do IDP (idp-model.cls)
                          e folha de estilo (idp-style.sty).
pacotes/                  Lista centralizada de pacotes (pacotes.tex).
figuras/                  Figuras (PDFs/PNGs); o graphicspath aponta para cá.
reviews/                  PDFs anotados de revisão + backlog extraído em
                          `*.comments.db` e `*.comments.md`.
.github/                  Instruções para o GitHub Copilot.
tools/article-ai/         Workflow auxiliar de IA para resumir artigos
                          relacionados (mais detalhes no README local).
review_of_studies_inspiration.md   Material de inspiração (não publicado).
```

## Build

A classe `configs/idp-model.cls` depende de `fontspec` com `Arial`, então
o pipeline **exige** XeLaTeX (ou LuaLaTeX) — `pdflatex` não funciona.

| Comando         | O que faz                                       |
|-----------------|-------------------------------------------------|
| `make`          | `xelatex → bibtex → xelatex → xelatex` e depois `make clean` |
| `make clean`    | Remove arquivos auxiliares (`*.aux`, `*.bbl`, …) |
| `make cleanall` | Remove também o `main.pdf` e artefatos extras   |

Pré-requisitos: TeX Live (ou MikTeX) com `xelatex`, `bibtex` e a fonte
**Arial** instalada no sistema.

> O editor recomendado é o VS Code com a extensão *LaTeX Workshop*.
> O `.vscode/settings.json` deste repositório já configura `xelatex`,
> `bibtex` e a receita `make` para build automático ao salvar.

## Convenções da classe `idp-model`

Os comandos padrão do LaTeX para seccionamento foram **substituídos** por
versões customizadas — usar `\section` quebra o sumário. As regras:

- **Seções de topo**: `\secao{Título}{partes/arquivo}` no `main.tex`.
  O comando já faz o `\input` do arquivo; não inclua manualmente.
- **Subseções**: `\subsecao{Título}` dentro do `.tex` da seção.
- **Sub-subseções**: `\subsubsecao{Título}`.
- **Citações**: `\cite{chave}` (estilo numérico IEEE).
- **Metadados** (autor, título, banca, palavras-chave, etc.) ficam no
  preâmbulo de `main.tex`.

## Como adicionar / editar conteúdo

| Tarefa                          | Onde mexer                                                 |
|---------------------------------|------------------------------------------------------------|
| Editar uma seção existente      | `partes/<nome>.tex`                                        |
| Criar uma nova seção            | criar `partes/nova.tex` + `\secao{...}{partes/nova}` no `main.tex` |
| Adicionar uma figura            | `figuras/figura.pdf` (ou `.png`) + `\includegraphics{figura}` |
| Adicionar uma referência        | nova entrada em `referencias.bib` + `\cite{chave}`         |
| Adicionar um pacote LaTeX       | `pacotes/pacotes.tex`                                      |
| Ajustar layout da classe        | `configs/idp-model.cls` (evitar; só se realmente necessário) |

## Review do PDF anotado

O workflow atual de revisão do texto usa:

- `reviews/*.pdf` — PDF anotado pelo revisor
- `reviews/*.comments.db` — base SQLite com um registro por comentário
- `reviews/*.comments.md` — visão legível do backlog
- `../automation/extract_pdf_comments.py` — extração do PDF anotado
- `../automation/review_comments.py` — consulta e atualização do backlog
- `../automation/review_issue_sync.py` — criação/vínculo de uma issue GitHub por comentário

Ao corrigir um comentário no LaTeX, prefira deixar um comentário local
próximo ao trecho alterado, por exemplo:

```latex
% review: issue #101, comment 14
```

## Workflows de IA auxiliar (`tools/`, `.agents/`)

- [`tools/article-ai/`](tools/article-ai/) — pipeline para gerar
  resumos formais de artigos da revisão sistemática usando Claude +
  Gemini em modo headless. Saída em
  [`../tcc_notes/related_work_summaries/`](../tcc_notes/related_work_summaries).
- [`.github/copilot-instructions.md`](.github/copilot-instructions.md)
  — instruções específicas para o GitHub Copilot.
- [`AGENTS.md`](AGENTS.md) — guia rápido para o Claude e agentes
  similares.
- [`../.agents/skills/tcc-review-workflow/SKILL.md`](../.agents/skills/tcc-review-workflow/SKILL.md)
  — workflow do review do TCC baseado em `reviews/*.comments.db`,
  mapeamento para `partes/*.tex` e sincronização com issues GitHub.

## Repositórios relacionados

| Repositório                                                                                   | Conteúdo                                  |
|-----------------------------------------------------------------------------------------------|-------------------------------------------|
| [`../parallel-aho-corasick`](../parallel-aho-corasick)                                       | Implementação em C, benchmarks, datasets  |
| [`../tcc_notes`](../tcc_notes)                                                                | Anotações em Obsidian (revisão sistemática, resumos de artigos relacionados) |
