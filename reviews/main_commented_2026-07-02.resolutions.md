# Review resolutions - main_commented_2026-07-02

Source database: `reviews/main_commented_2026-07-02.comments.db`

Validation: `make` completed successfully after the edits. `git diff --check`
also completed without errors. The LaTeX run still reports pre-existing
template/header warnings and a few small overfull boxes outside these review
items, but no unresolved reference was left for the removed end-to-end table.

## Resolved comments

| Comment | Issue | File(s) | What changed |
| --- | --- | --- | --- |
| 2 | #168 | `partes/fundamentacao.tex` | Replaced the visually ambiguous `\operatorname` notation with the local macro `\acfunc{...}` (`\mathtt` inside math mode), so the function names themselves render as formatted identifiers in calls such as `\acfunc{goto}(s,a)`, `\acfunc{fail}(s)`, and `\acfunc{output}(s)`. |
| 3 | #169 | `partes/rsl.tex` | Converted the synthesis block beginning with "Parallelization strategies" into an `itemize` organizer with three labelled bullets: parallelization strategies, memory/automaton optimizations, and applications/benchmarking. |
| 4 | #170 | `partes/proposal.tex`, `partes/methodology.tex` | Simplified the heterogeneous-core load-balancing explanation, removed the long literal `/sys/devices/...` path from prose, and stated that the i5-1235U is only a P/E diagnostic, not the canonical measurement platform. |
| 9 | #175 | `partes/methodology.tex` | Reorganized the Phase A-G protocol description into an `itemize` list with labelled phase markers. |
| 11 | #177 | `partes/methodology.tex` | Reformatted the hypotheses table with fixed-width, wrapping columns using `p{...}` and `\raggedright\arraybackslash`, so it fits within the text width. |
| 12 | #178 | `partes/results.tex` | Made the Results chapter state the expected section order explicitly: introduction, figure/table, objective description, interpretation, and local conclusion. |
| 13 | #179 | `partes/results.tex` | Reworked "The Flattened Output Layout" around automaton footprint/working-set size, removed architecture-dependent L3 labels from the table, and kept cache discussion as workstation-specific supporting evidence. |
| 15 | #181 | `partes/results.tex`, `partes/apendicei.tex` | Removed "End-to-End Consistency Check" as a separate subsection/table, converted it into a short consistency paragraph, and updated the appendix so it no longer references the deleted `tab:e2e` label. |

## Human decisions left open

None. The only judgement-heavy item was comment 15; it was applied by reducing
the section instead of keeping a separate experiment/table.
