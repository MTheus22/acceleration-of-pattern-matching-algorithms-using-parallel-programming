# Autonomous Correction Queue

Work queue for the scheduled `tcc-review-correction` agent. One task per run.
Findings come from [`review.md`](review.md); decisions taken interactively are
recorded in [`progress.md`](progress.md). The agent picks the **top task whose
`status: pending` and `eligibility: auto`**, JUDGES it (verifies the finding is
real against the actual files + canonical data), then either fixes it
(`status: done`) or records why it is invalid (`status: rejected`). Tasks marked
`author-reserved` are never auto-edited.

**No-fabrication rule:** numbers only from `../../parallel-aho-corasick/runs/overnight/sweep.db`,
`../../parallel-aho-corasick/docs/tcc-synthesis.html`, or `../../tcc_notes/sections/notes/*.md`;
citations only with keys already in `referencias.bib` — if a new citation is
needed, write the prose and leave a `% REVIEW-TODO(cite): …` marker instead of
inventing a BibTeX entry. Methodology facts (affinity, compiler, flags) only if
documented in `../../parallel-aho-corasick`; otherwise leave a `% REVIEW-TODO`.

Priority order: Critical → Major → Minor. Within a priority, top-down.

---

## Critical

### T01 — Introduction: NIDS motivation + research gap + explicit RQs
- finding: review.md C2
- files: partes/introduction.tex
- eligibility: auto
- grounding: rsl.tex RQ1/RQ2; tcc_notes/sections/notes/*.md. Snort/Suricata
  citations: check referencias.bib; if absent, write framing + `% REVIEW-TODO(cite)`.
- acceptance: intro names the NIDS application, states a research gap before the
  objectives, and poses explicit RQs aligned with the abstract's claims; no first
  person; compiles.
- status: done
- notes: (1) introduction.tex paragraph 3 — added Snort/Suricata as NIDS
  application alongside YARA, citing LeeYang2017FHBM (already in bib).
  (2) Motivation section — replaced the two-paragraph block that undercut the
  contribution with three paragraphs: (a) acknowledges prior work on specialized
  platforms while stating the memory-bound/hybrid-CPU gap, (b) names Snort/Suricata
  large automata as the NIDS context, citing Aldwairi2018Characterizing (already
  in bib), (c) states the research gap explicitly. Added explicit RQ1/RQ2 as an
  itemize block at the end of the Motivation subsection, aligned with the
  abstract's claims (text-level parallelism dominance; automaton-to-LLC ratio
  ceiling). No first person. Build: make cleanall && make — 76 pages, 0 [?]. Build OK.

### T05 — Conclusion: add the 2.85× peak-and-regress finding
- finding: review.md C3
- files: partes/conclusion.tex
- eligibility: auto
- grounding: results.tex (memory-bound peak ~2.85× near 6 threads, regresses
  after); sweep.db view v_speedup.
- acceptance: conclusion states the 2.85× peak and the post-6-thread regression
  as the key memory-bound scaling result; compiles.
- status: done
- notes: conclusion.tex lines 16-20 — inserted one sentence after "collapses
  accordingly": states the 2.85× peak near six threads (canonical corpus,
  confirmed from sweep.db: pthread_chunked_v3_flat/enron_corpus/T=6 = 2.853×)
  and the subsequent regression due to DRAM bus saturation. Build: 76 pages,
  0 [?], OK.

### T06 — Conclusion: disambiguate 4.79× (canonical) vs 4.52× (at-scale)
- finding: review.md C3
- files: partes/conclusion.tex
- eligibility: auto
- grounding: results.tex lines ~104–108.
- acceptance: the two figures are no longer conflated; the at-scale headline is
  4.52× and 4.79× is labeled as the canonical-corpus peak; compiles.
- status: done
- notes: conclusion.tex lines 11-12 — replaced "reaching up to 4.79× on twelve
  threads for a moderate dictionary and 4.52× at the multi-gigabyte scale" with
  "reaching 4.52× at twelve threads on the multi-gigabyte corpus and a
  canonical-corpus peak of 4.79× via dynamic dispatch." Verified against sweep.db:
  4.524× = patterns_snort/enron_x8/pthread_chunked_v3_flat/T=12,
  4.792× = patterns_snort/enron_corpus/pthread_dynamic/T=12. Build: 76 pages, 0 [?], OK.

## Major

### T02 — Framework: DFA vs NFA distinction + which variant is benchmarked
- finding: review.md M1
- files: partes/fundamentacao.tex
- eligibility: auto
- grounding: parallel-aho-corasick src (flat goto table / DFA); cite
  AhoCorasick1975 / Gusfield1997 (already in bib).
- acceptance: a passage distinguishes the NFA (goto/failure/output) from the
  fully-expanded DFA transition table, states the memory/throughput trade-off,
  and says which variant the implementation uses; compiles.
- status: done
- notes: fundamentacao.tex — inserted new \subsubsecao{NFA versus DFA
  Representations} between the Time/Space Complexity and Applications
  subsections of the Aho-Corasick section. The paragraph (a) names the
  existing goto/failure/output description as the NFA, (b) introduces the
  DFA flat table as |Q|×|Σ| precomputed transitions, (c) states the
  memory/throughput trade-off and the LLC-overflow → memory-bandwidth-bound
  shift, (d) confirms the implementation uses the DFA exclusively. Cites
  AhoCorasick1975 and Gusfield1997 (both already in bib). Build: 77 pages,
  0 [?], OK.

### T03 — Framework: memory-bound vs compute-bound, cache coherence, false sharing, NUMA
- finding: review.md M1
- files: partes/fundamentacao.tex
- eligibility: auto
- grounding: tcc_notes/sections/notes/methodology.md; cite Grama2003 / Pacheco2011
  (in bib) where applicable, else `% REVIEW-TODO(cite)`.
- acceptance: a subsubsection defines the cache hierarchy/LLC, cache coherence,
  false sharing, NUMA, and the bandwidth-bound vs compute-bound dichotomy that
  the results chapter relies on; compiles.
- status: done
- notes: fundamentacao.tex — added \subsubsecao{Cache Architecture and
  Memory-Bound Parallelism} at the end of the Fundamentals of Parallelism block
  (after POSIX Thread Model). Covers: L1/L2 private + LLC shared hierarchy;
  compute-bound vs memory-bandwidth-bound definition with the automaton/LLC
  overflow mechanism; cache coherence (MESI) and false sharing with mitigation;
  NUMA concept with note that this work uses UMA (i5-1235U single socket).
  Cites Grama2003 and Pacheco2011 (both in bib). Build: 78 pages, 0 [?], OK.

### T04 — Framework: P-core/E-core heterogeneity of the target CPU
- finding: review.md M1
- files: partes/fundamentacao.tex
- eligibility: auto
- grounding: methodology.tex hardware section (i5-1235U: 2 P + 8 E = 12 threads).
- acceptance: the framework introduces hybrid P/E-core asymmetry so the ~4-thread
  knee in results has conceptual support; compiles.
- status: done
- notes: fundamentacao.tex — added \subsubsecao{Hybrid P/E-Core Architectures} at
  the end of the Fundamentals of Parallelism block (after Cache Architecture).
  Explains Intel Alder Lake hybrid design: 2 P-cores × HT = 4 HW threads + 8
  E-cores = 12 total; P-core vs E-core per-thread throughput difference; the
  resulting ~4-thread knee in scaling curves. A % REVIEW-TODO(cite) marker placed
  for an Intel i5-1235U datasheet citation (no matching bib entry exists). Build:
  78 pages, 0 [?], OK.

### T07 — Report parallel efficiency (or drop it from Objective 2)
- finding: review.md M3
- files: partes/results.tex, partes/conclusion.tex (or partes/introduction.tex)
- eligibility: auto
- grounding: efficiency = speedup / threads (e.g. 4.52/12 ≈ 0.38); eq:efficiency
  already defined in fundamentacao.tex.
- acceptance: either an efficiency figure is reported and reflected in the
  conclusion, or Objective 2 no longer claims "parallel efficiency"; compiles.
- status: done
- notes: results.tex — added paragraph after "The physical limit is memory
  bandwidth, not the number of cores." reporting E=37.7% (moderate dict,
  4.52×/12) and E=23.3% (memory-bound, 2.79×/12) with reference to eq:efficiency.
  conclusion.tex — added one sentence after the regression clause reporting the
  same two efficiency figures. Both numbers derived from speedups already
  in the text. Build: 80 pages, 0 [?], OK.

### T08 — Conclusion: objective-by-objective closure
- finding: review.md M4
- files: partes/conclusion.tex
- eligibility: auto
- grounding: introduction.tex objectives 1–3.
- acceptance: the conclusion explicitly states how each of the three specific
  objectives was met; compiles.
- status: done
- notes: conclusion.tex — inserted a three-sentence paragraph before
  \subsecao{Threats to Validity} (after the E2E pipeline sentence). The paragraph
  closes each objective explicitly: (1) design+implement pthreads searcher →
  family of text-partitioning strategies, correctness validated; (2) quantify
  speedup/throughput/efficiency → 4.79×/4.52× speedups, 37.7%/23.3% efficiency
  already reported in the chapter; (3) scalability analysis → seven thread counts,
  three corpora, 42× automaton range, saturation ceiling identified. All numbers
  sourced from existing verified text. Build: 80 pages, 0 [?], OK.

### T09 — Methodology: per-phase repetition table (warmup/iters)
- finding: review.md M2
- files: partes/methodology.tex
- eligibility: auto
- grounding: sweep.db (warmup/iters per phase: A–C = 2/5, D = 1/3, build = 0/1) —
  VERIFY against the DB before writing.
- acceptance: the vague "three or more" is replaced by the exact per-phase
  protocol; compiles.
- status: done
- notes: methodology.tex Measurement Protocol section — replaced the opening
  vague sentence ("at least one warm-up…three or more timed") with a precise
  per-phase prose summary and added Table~\ref{tab:protocol} (phases A–C: 2/5;
  D: 1/3; E: 0/1). All values verified against sweep.db
  (SELECT phase, warmup, iters FROM runs GROUP BY phase, warmup, iters). Phase D
  warmup=1 and phase E warmup=0 were previously unstated; now explicit. Build:
  80 pages, 0 [?], OK.

### T10 — Report dispersion (CV) on headline numbers
- finding: review.md M1 (Results), M2 (Methodology)
- files: partes/results.tex and/or partes/methodology.tex
- eligibility: auto
- grounding: sweep.db cv_pct (verify the actual CVs; do not invent).
- acceptance: headline speedups carry a dispersion statement (CV or min–max);
  compiles.
- status: done
- notes: results.tex Scalability section — added parenthetical CV to each of
  the four headline speedups: 4.52× (CV~10%, from pthread_chunked_v3_flat/
  patterns_snort/enron_x8/T=12, cv_pct=10.2); 4.79× (CV~2%, from
  pthread_dynamic/patterns_snort/enron_corpus/T=12, cv_pct=2.2); 2.79×
  (CV~8%, from pthread_chunked_flat/patterns_et_32/enron_x8/T=12, cv_pct=8.4);
  2.85× (CV~16%, from pthread_chunked_v3_flat/patterns_et_32/enron_corpus/T=6,
  cv_pct=16.0). All values queried from sweep.db runs table (phase
  A_speedup_curves). Build: 80 pages, 0 [?], OK.

### T11 — Methodology: affinity policy, thread grid, toolchain pinning, bandwidth source
- finding: review.md M2
- files: partes/methodology.tex
- eligibility: auto
- grounding: parallel-aho-corasick (affinity impl, GCC version, flags, env
  snapshots); performance thread grid {1,2,4,6,8,10,12} is in sweep.db. Anything
  not documented in the lab repo → `% REVIEW-TODO`, do NOT invent.
- acceptance: thread grid stated; affinity/compiler/kernel pinned where
  documented, TODO-flagged where not; the 25 GB/s figure sourced or relabeled;
  compiles.
- status: done
- notes: methodology.tex Experimental Environment section — (1) GCC version
  pinned: "GCC using" → "GCC~13.3.0 using" (from gcc --version on the sweep
  machine, consistent with env/start.txt commit e3dc7d4). (2) Kernel version
  pinned: "kernel~6.x" → "kernel~6.17.0" (from env/start.txt uname -a). (3)
  Affinity policy corrected: removed "worker threads were pinned to dedicated
  logical cores" (overstated for most searchers); replaced with accurate
  description: only pthread_chunked_v3 and pthread_chunked_v3_flat use
  pthread_setaffinity_np; other searchers rely on OS scheduling (verified in
  src/searchers/). (4) 25 GB/s relabeled: removed "measured" (tool not
  documented in lab files) → "with a peak bandwidth of approximately 25 GB/s";
  added % REVIEW-TODO(cite) comment for author to supply measurement source.
  (5) Thread grid stated: added one sentence in Measurement Protocol — Phase A
  sweeps T ∈ {1,2,4,6,8,10,12} for canonical Enron corpus and T ∈ {1,4,8,12}
  for eight-fold replica (both verified against sweep.db). Build: 80 pages,
  0 [?], OK.

### T19 — Appendix: document the E2E benchmark provenance + sweep.db location
- finding: review.md M4
- files: partes/apendicei.tex
- eligibility: auto
- grounding: parallel-aho-corasick (locate the E2E/pipeline benchmark). If not
  locatable, leave a `% REVIEW-TODO` and state the sweep.db path only.
- acceptance: the E2E times are traceable, or explicitly flagged; the sweep.db
  location is stated; compiles.
- status: done
- notes: apendicei.tex — revised opening paragraph: (1) replaced "documented
  separately" with a pointer to the synthesis report
  (parallel-aho-corasick/docs/tcc-synthesis.html §3.9), which records the F3
  sweep (2026-05-22) with the exact 4.48×/3.04× numbers and configurations
  (verified in synthesis HTML); (2) noted that the raw script/log are not
  currently archived and added % REVIEW-TODO for the author; (3) stated
  sweep.db full path as parallel-aho-corasick/runs/overnight/sweep.db.
  Build: 80 pages, 0 [?], OK.

## Minor

### T13 — Results: add an Amdahl/serial-fraction sentence for the moderate-dict ceiling
- finding: review.md m8
- files: partes/results.tex
- eligibility: auto
- grounding: 12 hw threads = 2 P + 8 E; serial merge + I/O fraction.
- acceptance: one sentence frames the ~4.5× ceiling against Amdahl + P/E
  asymmetry; compiles.
- status: done
- notes: results.tex Scalability section — inserted one sentence between "The
  physical limit is memory bandwidth, not the number of cores." and the
  efficiency paragraph. The sentence states that the 4.52× ceiling is consistent
  with Amdahl's law (citing Grama2003, already in bib): 37.7% efficiency implies
  ~15% serial fraction (derived from 4.52/12 via the Amdahl formula), compounded
  by the P/E asymmetry of the thread pool (4 P-core HW threads vs 8 E-cores).
  Build: 80 pages, 0 [?], OK.

### T12 — Results: name searchers in the speedup figure caption / disclose corpus switch
- finding: review.md m7 (M2)
- files: partes/results.tex
- eligibility: auto
- grounding: results.tex figure vs prose (flat/enron_x8 vs dynamic/canonical).
- acceptance: the figure caption names the searcher + corpus; compiles.
- status: done
- notes: results.tex figure caption (lines 64-68) — added searcher names and
  explicit corpus identifier. Snort curve identified as pthread_chunked_v3_flat
  (verified: T={1,4,8,12} speedups 1.048/2.441/3.621/4.537 match figure
  coordinates 1.04/2.43/3.61/4.52 vs enron_x8/patterns_snort baseline 240.3
  MB/s). ET curve identified as pthread_chunked_flat (verified: normalized vs
  enron_x8/patterns_et_32 baseline 125.4 MB/s gives 1.14/1.99/2.64/2.79
  matching 1.14/1.98/2.64/2.79). Caption now reads "(Snort, 55 MiB;
  pthread_chunked_v3_flat) … (Emerging Threats, 507 MiB; pthread_chunked_flat),
  on the ~10.6 GiB corpus (enron_x8)." Build: 80 pages, 0 [?], OK.

### T14 — Abstract: reconcile "saturates near 2.85×" vs Figure's 2.79× at T=12
- finding: review.md m9
- files: partes/abstract.tex
- eligibility: auto
- grounding: results.tex 2.85× (canonical, ~6T) vs 2.79× (12T, 10.6 GiB).
- acceptance: wording no longer contradicts the figure; compiles.
- status: done
- notes: abstract.tex lines 19-21 — replaced "saturates near $2.85\times$, exposing
  memory bandwidth as the physical ceiling" with "peaks near $2.85\times$ at six
  threads on the canonical corpus before regressing, reaching $2.79\times$ at twelve
  threads on the multi-gigabyte corpus, exposing memory bandwidth as the physical
  ceiling." The word "saturates" implied a stable plateau; the actual behavior is a
  peak at T=6 (2.85×, canonical corpus) that then regresses, and 2.79× at T=12 on
  enron_x8 (what the figure shows). Both numbers are grounded in results.tex (lines
  111-113) and sweep.db. Build: 80 pages, 0 [?], OK.

### T15 — Introduction: fix Moore's-Law transistor-vs-performance phrasing
- finding: review.md m11
- files: partes/introduction.tex
- eligibility: auto
- grounding: Moore's law = transistor count, not single-core performance.
- acceptance: the conflation is corrected; compiles.
- status: done
- notes: introduction.tex line 1 — replaced "the performance of single-core
  processors followed the trend predicted by Moore's Law, which forecast the
  doubling of transistors on a chip every eighteen months" with "the number of
  transistors on a chip doubled roughly every eighteen months, following the
  observation formalized as Moore's Law; rising clock speeds translated these
  denser circuits into proportional single-core performance gains." Separates
  transistor count (Moore's Law) from performance (clock speed / Dennard
  scaling). Next sentence about clock-frequency barriers flows naturally.
  Build: 80 pages, 0 [?], OK.

### T16 — RSL: repair the two malformed search strings
- finding: review.md C1 (mechanical residue)
- files: partes/rsl.tex
- eligibility: auto
- grounding: String 1 has an unbalanced parenthesis; String 2 mixes curly quotes
  with straight quotes. Make them balanced + straight-quoted WITHOUT changing the
  search semantics.
- acceptance: both strings are syntactically valid as printed; compiles.
- status: done
- notes: rsl.tex line 34 — removed trailing unbalanced `)` from String 1
  (`NOT "distributed systems")}` → `NOT "distributed systems"}`).
  rsl.tex line 37 — removed trailing unbalanced `)` from String 2 and replaced
  the three Unicode curly-quote pairs (U+201C/U+201D around "application",
  "implementation", "use case") with straight ASCII double quotes (U+0022).
  Semantics unchanged; both strings now syntactically valid as printed.
  Build: 80 pages, 0 [?], OK.

### T20 — anexoi.tex: remove or keep the commented template boilerplate
- finding: review.md m14
- files: partes/anexoi.tex
- eligibility: auto
- grounding: it is already commented out in main.tex (harmless).
- acceptance: decided and noted (deletion optional); compiles.
- status: done
- notes: Decision: leave partes/anexoi.tex in place. The file contains IDP class
  template boilerplate (Portuguese description of what "Anexos" are) and is
  already excluded from the compiled PDF via the commented-out
  `%\anexo{Título do Anexo A}{partes/anexoi}` in main.tex. Deletion is optional
  per the task acceptance; keeping it is harmless and avoids any risk to the git
  working tree. No .tex file edited. Build: 80 pages, 0 [?], OK.

---

## Author-reserved (never auto-edit)

### T17 — Bib hygiene (Vajira2018 preprint type; missing pages/location)
- reason: requires real publication metadata; must not be fabricated.
- status: author-reserved

### T18 — RSL aggregate RQ1/RQ2 synthesis + threats-to-validity subsections
- reason: quality content the author explicitly retained (see progress.md).
- status: author-reserved
