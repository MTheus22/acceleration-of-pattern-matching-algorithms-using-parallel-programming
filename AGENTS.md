# AGENTS.md

Short, factual guide for Codex, Claude, and similar AI agents operating in
this repository. The Portuguese-facing audience for this thesis is
documented in [`README.md`](README.md); this file targets the agent.

## What this repo is

This is the **LaTeX source** of an undergraduate thesis (TCC, IDP,
2025) titled *"Acceleration of Pattern Matching Algorithms Using
Parallel Programming"*. It produces a single `main.pdf` from
sectioned content under `partes/`, a custom IDP class under
`configs/`, a BibTeX file `referencias.bib`, and figures under
`figuras/`.

The companion C implementation lives in a sibling repo at
`../parallel-aho-corasick`. Empirical results in this thesis come
from that codebase.

## Current scope (important)

The current scope is the **parallelization of Aho–Corasick on
shared-memory multi-core CPUs** using POSIX Threads. This is a
**generalization** of an earlier framing that focused specifically on
accelerating YARA's Aho–Corasick engine. Treat YARA as one
representative application, not as the thesis's subject. When editing
text, follow these rules:

- Frame the contribution as parallelizing Aho–Corasick itself, not
  YARA.
- It is fine to mention YARA, Snort/Suricata, NIDS, bioinformatics,
  and spam filtering as **applications** of Aho–Corasick.
- Do not reintroduce phrases like *"YARA's sequential engine"*,
  *"intra-file parallelism in YARA"*, or objectives framed as
  modifying YARA's source.
- See commit `8f79895` ("remove foco em YARA") for the canonical
  rewording examples.

## Build pipeline

```text
xelatex main.tex
bibtex  main.aux
xelatex main.tex
xelatex main.tex
```

Use **`xelatex`** — `pdflatex` will not work because
`configs/idp-model.cls` calls `\setmainfont{Arial}` via `fontspec`.

| Command          | Purpose                                          |
|------------------|--------------------------------------------------|
| `make`           | Full build + clean of aux files (default target) |
| `make clean`     | Remove `.aux`, `.bbl`, `.blg`, `.log`, …         |
| `make cleanall`  | Also remove `main.pdf` and `main.synctex.gz`     |

If citations show up as `[?]`, run `make` again — the full cycle
(xelatex → bibtex → xelatex × 2) needs to complete for cross-refs.

## Layout

```
main.tex                  Document root. Loads the class, sets metadata,
                          calls \secao{...}{partes/...} for each chapter.
referencias.bib           BibTeX entries (IEEE-style numeric citations).
Makefile                  Build pipeline (see above).
partes/                   One .tex file per chapter/section. EDIT HERE.
  introduction.tex
  fundamentacao.tex       Theoretical framework.
  rsl.tex                 Systematic literature review.
  proposal.tex            Proposed solution and schedule.
  results.tex             Reserved for experimental results.
  abstract.tex            Abstract / resumo.
configs/                  Custom IDP class. AVOID editing unless you
                          really intend to change the template.
  idp-model.cls
  idp-style.sty
pacotes/pacotes.tex       Central place to add LaTeX packages.
figuras/                  Figures. graphicspath already includes this.
reviews/                  Annotated review PDFs + extracted `*.comments.db`
                          and `*.comments.md` backlogs.
.github/                  Copilot instructions.
```

## Class conventions (DO NOT use plain \section)

The IDP class **replaces** the standard sectioning commands. Using
`\section`, `\subsection`, or `\subsubsection` will produce broken
output (missing entries in the table of contents, wrong numbering).

| Use                                    | Not                  |
|----------------------------------------|----------------------|
| `\secao{Title}{partes/file}` in `main.tex` (auto-inputs the file) | `\section` + `\input` |
| `\subsecao{Title}` inside section files | `\subsection`        |
| `\subsubsecao{Title}` inside section files | `\subsubsection`  |

Other custom commands relevant for editing:

- `\cite{key}` — numeric IEEE citations.
- `\textbf`, `\textit`, `\texttt`, standard `itemize`/`enumerate` —
  unchanged.
- Metadata commands live in `main.tex` preamble: `\autor{}`,
  `\titulo{}`, `\orientador{}`/`\orientadora{}`, `\membrobancai{}{}`,
  `\keywords{}`, `\palavraschave{}`, `\dataaprovacao{}`.
- Course selector: `\engenhariadesoftware` (currently active) or
  `\cienciadacomputacao`.

## Writing rules

- Body language: **English** (the abstract and front matter exist in
  both English and Portuguese; check existing files before adding
  new text).
- Tone: formal, third-person, no first-person pronouns ("we", "I",
  "our").
- Citations: introduce a study by author + bracketed citation, e.g.,
  *"Smith et al. [12] propose…"*. Multiple citations must be written
  as **separate** commands — `\cite{a}, \cite{b}` (renders `[1], [2]`)
  — NOT merged into `\cite{a,b}` (which renders `[1, 2]`). This is the
  author's required style; do not "tidy" adjacent `\cite`s into one.
- New references must have a corresponding entry in
  `referencias.bib`. Do not invent citation keys without adding them.
- Do not commit `main.pdf` changes that you produced just to "see how
  it looks" — only commit when the content changes warrant it. The
  PDF is regeneratable.

## Common editing tasks

| Task                              | Where / how                                          |
|-----------------------------------|------------------------------------------------------|
| Add or edit a paragraph           | `partes/<chapter>.tex`                               |
| Inspect review backlog            | `reviews/*.comments.db` via `../automation/review_comments.py` |
| Sync comments to GitHub issues    | `../automation/review_issue_sync.py`                 |
| Consolidate section evidence first| `../tcc_notes/sections/notes/<section>.md`           |
| Draft a section before LaTeX      | `../tcc_notes/sections/text/<section>.md`            |
| Add a new top-level section       | create `partes/new.tex`, then add `\secao{Title}{partes/new}` to `main.tex` |
| Add a figure                      | put PDF/PNG in `figuras/`, then `\includegraphics{name}` |
| Add a bibliography entry          | append to `referencias.bib`, cite with `\cite{key}`  |
| Add a LaTeX package               | add `\usepackage{...}` in `pacotes/pacotes.tex`      |
| Generate a clean PDF              | `make`                                               |

## Review workflow

When addressing advisor/reviewer comments from an annotated PDF:

- Treat `reviews/*.comments.db` as the source of truth for extracted
  comments and statuses.
- One GitHub issue may exist per extracted comment; issue metadata is
  stored back in the same DB.
- Prefer the workspace skill `tcc-review-workflow` plus the helper
  scripts in `../automation/`.
- For substantive LaTeX changes tied to a review issue, add a nearby
  comment such as `% review: issue #101, comment 14` to make later
  audit/review easier.

## Presentation (`apresentacao/`)

The defense slides live in `apresentacao/`, authored in **Marp**
(Markdown → HTML/PDF). Source of truth: `apresentacao/slides.md`.
`slides.html` and `slides.pdf` are **generated** — never edit them by
hand; regenerate after editing `slides.md`.

Marp is **not** on `PATH`; it runs via `npx` and the package is
`@marp-team/marp-cli` (v4.4.0), *not* `marp`. PDF export needs Chrome.

```bash
cd apresentacao
python3 gerar_grafico_svg.py                                   # if data changed → figuras/speedup_results.svg
npx @marp-team/marp-cli@4.4.0 slides.md -o slides.html --allow-local-files
CHROME_PATH=/usr/bin/google-chrome \
  npx @marp-team/marp-cli@4.4.0 slides.md -o slides.pdf --allow-local-files
```

`--allow-local-files` is required because slides reference images in
`figuras/`. Per-slide citations use the Marp directive
`<!-- _footer: "Author (year); ..." -->`. Any number in the slides must
match the thesis (and thus `sweep.db`). See `apresentacao/README.md`.

## Helpers in this repo

- [`.github/copilot-instructions.md`](.github/copilot-instructions.md)
  — GitHub Copilot rules, mirroring this file in shorter form.

For AI-driven automations that span sub-repos (e.g., scheduled cron
workflows calling Claude or Antigravity to write into
`../tcc_notes/`), see the workspace-level `agent-cron` skill and the `automation/` directory at the workspace root. Those tools are intentionally kept **outside**
this versioned LaTeX source.

## Things to leave alone unless asked

- `configs/idp-model.cls` — institutional template; changes risk
  visual/layout regressions.
- The build pipeline order (`xelatex → bibtex → xelatex × 2`).
- File names in `partes/` referenced from `main.tex` (`abstract.tex`,
  `apendicei.tex`, `introduction.tex`, `fundamentacao.tex`,
  `rsl.tex`, `proposal.tex`, `results.tex`, `conclusion.tex`,
  `methodology.tex`).
- Top-level metadata commands (`\autor`, `\titulo`, etc.) unless the
  user explicitly requests an update.

## Sibling repositories

- `../parallel-aho-corasick` — C implementation, datasets, benchmarks.
  Its own `AGENTS.md` is the source of truth for the empirical side.
  **The canonical machine is the Ryzen 9 9950X workstation** (homogeneous
  16C/32T); the canonical collection is `runs/workstation_2026-06-30/`
  (analysis in its `RESULTS.md`; champion `pthread_dynamic_flat`, snort 22.91× /
  et_32 18.96× @ T=32). The **thesis body already cites these workstation
  numbers** (migration completed 2026-07-02 via epic-03); the **i5-1235U sweep**
  (`runs/i5/sweep.db`, 2026-05-29) is used **only** in the P/E (hybrid-core)
  section. Any headline number must match the canonical `sweep.db`; interim runs
  were removed (see `runs/MANIFEST.md`).
- `../tcc_notes` — Obsidian vault with the systematic-review notes
  and related-work summaries. Use `sections/notes/` for consolidated
  raw material and `sections/text/` for prose drafts before touching
  `partes/*.tex`.
