# Copilot Instructions

These instructions tell GitHub Copilot how to behave in this LaTeX
repository. Full project context lives in [`../README.md`](../README.md);
detailed agent guidance lives in [`../CLAUDE.md`](../CLAUDE.md). Keep
this file lean — anything that grows belongs in `CLAUDE.md`.

## Project at a glance

LaTeX source of an undergraduate thesis (TCC, IDP, 2025) about
**parallelizing the Aho–Corasick algorithm on shared-memory multi-core
CPUs** using POSIX Threads. The companion C implementation lives at
`../parallel-aho-corasick`.

**Scope note:** earlier drafts framed the work as accelerating YARA's
Aho–Corasick engine specifically. The current scope is the algorithm
itself; YARA is one representative application. Do not reintroduce
YARA-centric objectives.

## Build

- Engine: **XeLaTeX** (not pdflatex — the class uses `fontspec` with
  Arial).
- Pipeline: `xelatex → bibtex → xelatex → xelatex`, driven by
  `Makefile`.
- Targets: `make` (build + clean aux), `make clean`, `make cleanall`.

## File map

- `main.tex` — document root, metadata, chapter wiring.
- `partes/*.tex` — chapter content. **Edit here.**
- `referencias.bib` — BibTeX (IEEE numeric style).
- `configs/idp-model.cls` — institutional class. **Do not edit.**
- `pacotes/pacotes.tex` — add `\usepackage{...}` here.
- `figuras/` — figures (PDF/PNG); `graphicspath` already points here.

## Conventions Copilot must follow

- Sectioning uses **custom** commands:
  - `\secao{Title}{partes/file}` in `main.tex` (auto-inputs).
  - `\subsecao{Title}` and `\subsubsecao{Title}` inside content files.
  - Never suggest `\section`, `\subsection`, `\subsubsection`.
- Citations: `\cite{key}` (numeric IEEE). Every new key must exist in
  `referencias.bib`.
- Tone: formal, third-person English. No "we", "I", "our".
- Comments and identifiers in English; supporting markdown
  (`README.md`, `CLAUDE.md`, `tools/*/README.md`) in Portuguese.
- Abstract/Resumo files: `partes/abstract.tex`. Do not rename.
- Add new chapters by creating `partes/new.tex` and registering them
  in `main.tex` via `\secao{...}{partes/new}`.

## Common pitfalls

- **`[?]` citations**: run `make` again — the full xelatex/bibtex
  cycle has not completed.
- **Missing fonts**: ensure `Arial` is installed; `fontspec` needs it.
- **Broken TOC**: someone used `\section`/`\subsection` — replace
  with `\secao`/`\subsecao`/`\subsubsecao`.

## Out of scope for autocompletion

- Editing `configs/idp-model.cls` (institutional template).
- Touching front-matter metadata (`\autor`, `\titulo`, `\orientador`,
  `\membrobancai`, `\keywords`, `\dataaprovacao`) unless explicitly
  asked.
- Committing `main.pdf` regenerations without an accompanying source
  change.
