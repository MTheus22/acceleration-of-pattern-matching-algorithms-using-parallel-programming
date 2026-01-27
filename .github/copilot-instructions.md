# Copilot Instructions for IDP Capstone LaTeX Project

## Project Overview
This is a custom LaTeX template for IDP Capstone (TCC) projects. It uses `XeLaTeX` and a custom class `idp-model.cls`.

## Architecture & File Structure
- **Root**: `main.tex` is the entry point. It defines metadata, loads the class, and orchestrates content.
- **Class Implementation**: `configs/idp-model.cls` defines the document layout, custom commands, and styling. **Avoid modifying this file** unless specifically changing the template design.
- **Content**: All content text resides in `partes/*.tex`.
- **Packages**: Add new LaTeX packages to `pacotes/pacotes.tex`.
- **Figures**: Store images in `figuras/`. The path is auto-configured.
- **Bibliography**: `referencias.bib` contains BibTeX entries (IEEE standard).

## Build & Workflow
- **Build System**: Use `make` (or `make all`) to build the PDF.
  - The process is: `xelatex -> bibtex -> xelatex -> xelatex`.
  - **Do NOT** use `pdflatex` or standard latex commands directly; the font specs require `xelatex`.
- **Cleaning**: `make clean` removes aux files; `make cleanall` removes the PDF as well.

## Project Conventions

### Custom Sectioning Commands
The standard `\section`, `\subsection`, etc., are **REPLACED** by custom commands in `idp-model.cls`.
- **Top-Level Sections**: Use `\secao{Title}{path/to/file}`.
  - Example: `\secao{Introduction}{partes/introduction}`
  - Note: This command **automatically inputs** the file. Do not use `\input` inside `main.tex` for main sections.
- **Subsections**: Use `\subsecao{Title}` inside the content files.
- **Sub-subsections**: Use `\subsubsecao{Title}`.

### Metadata
- Set metadata in `main.tex` preamble: `\autor{}`, `\titulo{}`, `\orientador{}`, `\membrobancai{}{}`, `\keywords{}`.
- Course selection: Use `\cienciadacomputacao` or `\engenhariadesoftware`.

### Bibliography
- Use `\cite{key}` for numeric citations (IEEE style).
- Ensure `referencias.bib` is up to date.

### Content Editing
- **Abstract/Resumo**: Edit `partes/resumo.tex` and `partes/abstract.tex`. Do not rename these files.
- **New Chapters**:
  1. Create `partes/new-chapter.tex`.
  2. Add `\secao{Chapter Title}{partes/new-chapter}` to `main.tex`.

## Common Issues
- **Missing Fonts**: If compilation fails on fonts, ensure `Arial` is installed on the system, as `idp-model.cls` relies on `\setmainfont{Arial}` via `fontspec`.
- **BibTeX Errors**: If citations appear as `[?]`, run `make` again to ensure the full build cycle runs.
