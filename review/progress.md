# Review — Correction Progress

Tracks the **minor, safe** corrections applied automatically after the
multi-agent review (see `review.md`). Substantive/structural items and the RSL
are intentionally left to the author.

## ✅ Done (applied, safe factual/mechanical only)

- [x] **m1** — Fixed malformed citation `\cite{AhoCorasick1975},{Gusfield1997}`
  → `\cite{AhoCorasick1975, Gusfield1997}` (`fundamentacao.tex:261`). Would
  otherwise render as literal text in the PDF.
- [x] **m2** — Fixed Amdahl contradiction: "even a small sequential fraction
  (`s` large)" → "(small `s`)" (`fundamentacao.tex:70`).
- [x] **m3** — `S_{\text{escalado}}` → `S_{\text{scaled}}` (Portuguese label in
  English body) (`fundamentacao.tex:82`).
- [x] **m4** — Removed leftover `% TODO adicionar coesão` (`fundamentacao.tex:100`).
- [x] **m5** — Typos: "efficientily" → "efficiently"; "highly
  multi-pattern-matching" → "highly efficient multi-pattern-matching"
  (`introduction.tex:5`).
- [x] **m6** — SimpleWiki corpus size "~1.2 GiB" → "~1.19 GiB"
  (`methodology.tex:83`). Verified against `sweep.db`: 1,275,540,181 B = 1.188
  GiB; aligns precision with sibling rows (~1.32, ~10.59).

## ✅ Done — RSL consistency fixes (2nd round, author-directed: consistency only)

- [x] **C1a** — Replaced the placeholder funnel text (commented `Y`/`Z`, stale
  "30") with real counts: 196 records retained → 24 unique after de-duplication →
  10 primary studies included (`rsl.tex`). Meaning locked with the author: 24 =
  deduplicated pool read by abstract/conclusion (matches `articles/` + workspace
  canonical "24"); 10 = most-related studies summarized in detail.
- [x] **C1b** — Resolved the GPU protocol-vs-corpus contradiction with one
  sentence: the `Title excl.: GPU` filter is a coarse identification-stage noise
  reducer, while EC2 governs the platform decision (non-CPU studies retained when
  insights transfer to CPU). No papers removed.
- [x] **C1c** — Reworded "studies most directly pertinent" → "the ten selected
  primary studies" so the prose no longer implies a larger included set.
- [x] **C1d** — Renumbered IC/EC contiguously (IC1–IC7, EC1–EC7); the skipped
  IC5/EC3 are gone. EC2 reference preserved.
- [x] Full clean rebuild (`make cleanall && make`): PDF regenerated, 0 `[?]`,
  0 undefined citations/refs in final pass.

## ⏳ Left to author (substantive / content / data-dependent)

- [ ] **C1 (quality, not consistency)** — RSL still lacks an aggregate RQ1/RQ2
  synthesis and a threats-to-validity subsection; the two search strings have
  unbalanced parentheses (String 1) and smart quotes (String 2). Intentionally
  **not** touched — author requested consistency-only, no quality improvements.
- [ ] **C2** — Intro/Abstract scope mismatch; add NIDS motivation + research gap
  + explicit RQs.
- [ ] **C3** — Conclusion: add the 2.85× peak-and-regress; disambiguate
  4.79× (canonical) vs 4.52× (at-scale).
- [ ] **M1** — Framework: DFA/NFA distinction, memory-bound vs compute-bound,
  cache coherence/false sharing/NUMA, P/E heterogeneity, boundary-overlap.
- [ ] **M2** — Methodology: per-phase repetition table, dispersion/CV on
  headline numbers, source the 25 GB/s, pin GCC/kernel/flags, affinity policy +
  P/E core-fill order, state performance thread grid.
- [ ] **M3** — Report parallel efficiency or drop it from Objective 2.
- [ ] **M4** — Objective-by-objective closure in Conclusion; document the E2E
  benchmark in the appendix; state where `sweep.db` lives.
- [ ] **m7–m14** — see table in `review.md` (figure caption, Amdahl-ceiling
  sentence, abstract 2.85×/2.79× wording, baseline footnote, Moore's Law
  phrasing, bib hygiene, cosmetic rounding, anexo cleanup).

## Autonomous round
- [x] **T02** — Framework: DFA vs NFA distinction. Added \subsubsecao{NFA versus DFA Representations} in fundamentacao.tex between Time/Space Complexity and Applications, naming the NFA vs DFA trade-off, the LLC-overflow → DRAM-bound mechanism, and confirming the implementation uses the DFA flat table. Build: 77 pages, 0 [?], OK.

- [x] **T01** — Introduction: NIDS motivation + research gap + explicit RQs.
  Added Snort/Suricata NIDS mention to paragraph 3 (citing LeeYang2017FHBM).
  Replaced the two motivation paragraphs that undercut the contribution with a
  three-paragraph block stating the memory-bound/hybrid-CPU gap and naming large
  NIDS automata as the context (citing Aldwairi2018Characterizing). Added RQ1/RQ2
  itemize block at end of Motivation subsection, aligned with abstract claims.
  Build: 76 pages, 0 [?], OK.
- [x] **T05** — Conclusion: 2.85× peak-and-regress. Added one sentence after
  "collapses accordingly" (conclusion.tex ~line 17): states the 2.85× peak near
  six threads on the canonical corpus and the subsequent regression due to DRAM
  saturation. Verified against sweep.db (pthread_chunked_v3_flat/enron_corpus/T=6
  = 2.853×). Build: 76 pages, 0 [?], OK.
- [x] **T06** — Conclusion: disambiguate 4.79× vs 4.52×. Fixed conclusion.tex
  lines 11-12: replaced vague "4.79× for a moderate dictionary / 4.52× at
  multi-gigabyte scale" with "4.52× on the multi-gigabyte corpus / 4.79×
  canonical-corpus peak via dynamic dispatch." Verified against sweep.db (see
  TASKS.md notes). Build: 76 pages, 0 [?], OK.

- [x] **T03** — Framework: cache architecture and memory-bound parallelism. Added \subsubsecao{Cache Architecture and Memory-Bound Parallelism} at the end of the Fundamentals of Parallelism block in fundamentacao.tex. Covers L1/L2/LLC hierarchy, compute-bound vs memory-bandwidth-bound, cache coherence (MESI), false sharing, and NUMA (noting UMA topology on i5-1235U). Cites Grama2003 and Pacheco2011. Build: 78 pages, 0 [?], OK.

- [x] **T04** — Framework: P/E-core heterogeneity. Added \subsubsecao{Hybrid P/E-Core Architectures} at end of Fundamentals of Parallelism block in fundamentacao.tex. Covers Intel Alder Lake hybrid design (2 P-cores + HT = 4 HW threads; 8 E-cores = 8 HW threads; 12 total), P vs E per-thread throughput difference, and the resulting ~4-thread knee in scaling curves. % REVIEW-TODO(cite) left for Intel i5-1235U datasheet. Build: 78 pages, 0 [?], OK.

- [x] **T07** — Parallel efficiency reported. Added paragraph in results.tex (Scalability section) stating E=37.7% (moderate dict, T=12) and E=23.3% (memory-bound, T=12), referencing eq:efficiency. Added one-sentence reflection in conclusion.tex. Satisfies Objective 2's claim without removing content. Build: 80 pages, 0 [?], OK.
- [x] **T08** — Conclusion: objective-by-objective closure. Added a three-sentence paragraph in conclusion.tex before \subsecao{Threats to Validity}: maps Objective 1 (design+implement pthreads searcher), Objective 2 (speedup/throughput/efficiency quantified: 4.79×/4.52×, 37.7%/23.3%), Objective 3 (scalability sweep: 7 thread counts, 3 corpora, 42× automaton range, saturation identified). Build: 80 pages, 0 [?], OK.
- [x] **T09** — Methodology: per-phase repetition table. Replaced the vague "at least one warm-up...three or more timed" opening in methodology.tex Measurement Protocol with precise per-phase prose and Table~\ref{tab:protocol} (A-C: 2/5; D: 1/3; E: 0/1). Values verified against sweep.db. Build: 80 pages, 0 [?], OK.
- [x] **T10** — Report dispersion (CV) on headline numbers. Added parenthetical CV to the four headline speedups in results.tex (Scalability section): 4.52× (CV~10%), 4.79× (CV~2%), 2.79× (CV~8%), 2.85× (CV~16%); all values queried from sweep.db (phase A_speedup_curves). Build: 80 pages, 0 [?], OK.
- [x] **T11** — Methodology: affinity policy, thread grid, toolchain pinning, bandwidth source. (1) GCC 13.3.0 pinned (from env/start.txt). (2) Kernel 6.17.0 pinned (from env/start.txt uname). (3) Affinity corrected: only v3/v3_flat use pthread_setaffinity_np; others rely on OS scheduling. (4) 25 GB/s relabeled (removed "measured" — tool not documented); added % REVIEW-TODO(cite). (5) Thread grid T ∈ {1,2,4,6,8,10,12} / {1,4,8,12} stated and verified in sweep.db. Build: 80 pages, 0 [?], OK.
- [x] **T19** — Appendix: E2E benchmark provenance + sweep.db location. Revised opening paragraph in apendicei.tex: (1) pointed "documented separately" to the synthesis report (docs/tcc-synthesis.html §3.9), confirmed as the source for the F3 sweep (2026-05-22) with exact 4.48×/3.04× numbers; (2) noted raw script/log not archived, added % REVIEW-TODO; (3) stated sweep.db full path as parallel-aho-corasick/runs/overnight/sweep.db. Build: 80 pages, 0 [?], OK.
- [x] **T13** — Results: Amdahl/serial-fraction sentence for the moderate-dict ceiling. Inserted one sentence in results.tex Scalability section after "The physical limit is memory bandwidth, not the number of cores.": frames the 4.52× ceiling via Amdahl's law (Grama2003), noting 37.7% efficiency implies ~15% serial fraction from merge coordination and work dispatch, compounded by P/E asymmetry (4 P-core HW threads vs 8 E-cores). Build: 80 pages, 0 [?], OK.
- [x] **T12** — Results: figure caption searcher names + corpus. Added searcher identifiers to the speedup figure caption in results.tex: Snort curve identified as pthread_chunked_v3_flat, ET curve as pthread_chunked_flat (both verified against sweep.db at T={1,4,8,12} on enron_x8). Corpus made explicit as enron_x8 in the caption. Build: 80 pages, 0 [?], OK.
- [x] **T14** — Abstract: reconcile "saturates near 2.85×" vs Figure's 2.79× at T=12. Changed "saturates near $2.85\times$" → "peaks near $2.85\times$ at six threads on the canonical corpus before regressing, reaching $2.79\times$ at twelve threads on the multi-gigabyte corpus" in abstract.tex. "Saturates" implied a stable plateau; the behavior is a peak (T=6, canonical) that regresses, with 2.79× at T=12 on enron_x8 (consistent with the figure). Build: 80 pages, 0 [?], OK.
- [x] **T15** — Introduction: Moore's Law transistor-vs-performance phrasing. Fixed introduction.tex line 1: replaced "the performance of single-core processors followed the trend predicted by Moore's Law, which forecast the doubling of transistors on a chip every eighteen months" with "the number of transistors on a chip doubled roughly every eighteen months, following the observation formalized as Moore's Law; rising clock speeds translated these denser circuits into proportional single-core performance gains." Correctly separates transistor count (Moore) from single-core performance (Dennard scaling / clock speed). Build: 80 pages, 0 [?], OK.

- [x] **T16** — RSL: repaired malformed search strings. String 1 (rsl.tex line 34): removed trailing unbalanced `)` (`NOT "distributed systems")}` → `...systems"}`). String 2 (rsl.tex line 37): removed trailing unbalanced `)` and replaced three Unicode curly-quote pairs (U+201C/U+201D) around "application", "implementation", "use case" with straight ASCII `"` (U+0022). Semantics unchanged. Build: 80 pages, 0 [?], OK.
- [x] **T20** — anexoi.tex boilerplate: decided to leave in place. File contains IDP template placeholder text (Portuguese description of Annexes) and is already excluded from the PDF via `%\anexo{...}` in main.tex. Deletion optional — kept as harmless dead file. No .tex edit. Build: 80 pages, 0 [?], OK.

## Build note

Run `make` (xelatex → bibtex → xelatex ×2) to regenerate `main.pdf` and confirm
the corrected `\cite` resolves (no `[?]`).
