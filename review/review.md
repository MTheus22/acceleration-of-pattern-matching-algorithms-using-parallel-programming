# Final Critical Review — TCC: *Acceleration of Pattern Matching Algorithms Using Parallel Programming*

**Date:** 2026-06-18
**Method:** Seven parallel hostile-examiner agents, one per section + one cross-cutting
consistency pass. Every quantitative claim cross-checked against the canonical
source of truth: `../parallel-aho-corasick/runs/overnight/sweep.db` (2026-05-29
sweep, 265 runs, baseline `sequential` = 239.60 MB/s) and
`../parallel-aho-corasick/docs/tcc-synthesis.html`.

## Headline verdict

- **Data integrity: excellent.** All 60+ numeric claims in Results, plus every
  Abstract/Conclusion headline, trace exactly to `sweep.db`. No discarded
  pre-2026-05-29 figures (7.49× / 4.13× / 1.83×) survive anywhere. Correctness
  is genuinely validated (`v_correctness`: `distinct_match_counts = 1` for all
  workloads). Citations reconcile perfectly (24 keys, 0 missing, 0 orphan).
  YARA framing is clean (example, not subject).
- **Weaknesses are framing / presentation rigor / the RSL chapter** — not
  fabricated numbers. The "ready to send" premise is refuted by the Critical
  items below.

---

## 🔴 CRITICAL — block submission

### C1. RSL chapter is unfinished and fails as a systematic review (`rsl.tex`)
- PRISMA funnel ends in **literal placeholders**: lines 91–96 are commented out
  and still read "*Y primary studies*" / "*Z studies*" with an orphaned "(30)".
  **The final included-study count is never stated in prose.**
- Counts don't reconcile: ~196 records kept (Table 2) → "30" → only **9–10
  papers actually reviewed**, while **24 PDFs and 24 summaries exist**. No
  de-duplication count, no exclusion-with-reasons.
- **Protocol contradicts the corpus**: EC2 + the "Title excl.: GPU" filter
  exclude non-CPU platforms, yet most reviewed papers *are*
  GPU/FPGA/ASIC/SIMD/MPI (Thambawita, Deyannis, Jepsen, Sitaridi, Qu…).
- Missing the three mandatory SLR components: **quality assessment**,
  **synthesis/taxonomy**, **threats-to-validity of the review**.
- IC numbering skips **IC5**; EC numbering skips **EC3**. Search strings have
  **unbalanced parentheses** (String 1) and **smart quotes** mixed with straight
  quotes (String 2) — they would not run as printed.
- **Owner decision:** user will handle RSL entirely. Not auto-edited.

### C2. Introduction and Abstract describe two different theses (`introduction.tex`, `abstract.tex`)
- Abstract commits hard to **intrusion detection** (Snort/Suricata/ET, NIDS).
  The Introduction **never mentions NIDS/IDS/Snort/Suricata once** — it motivates
  via bioinformatics + YARA. The evaluation domain first appears in Results with
  no setup.
- **No research gap is stated.** Intro line 11 even undercuts the contribution
  ("*prior literature demonstrates parallelizing AC is both viable and
  effective*") without stating what remains open (the memory-bound/cache-overflow
  regime on hybrid P/E-core CPUs — which the Abstract treats as the contribution).
- Objectives (lines 21–23) are activity verbs with no measurable criteria; **no
  explicit research questions**, although the Abstract makes sharp, falsifiable
  claims that *are* answerable RQs.

### C3. Conclusion numeric framing (`conclusion.tex`)
- Leads with **4.79×** (the *smaller canonical-corpus* peak) as if it were the
  at-scale number; the multi-gigabyte figure is **4.52×**. The two scenarios are
  compressed into one headline.
- The thesis's own stated key finding — the memory-bound **2.85× peak-and-regress
  past 6 threads** (Results: "the most important observation of the scaling
  analysis") — **never appears in the Conclusion at all**.

---

## 🟠 MAJOR

### M1. Theoretical Framework omits the concepts Results depends on (`fundamentacao.tex`)
- **No DFA-vs-NFA distinction.** Only the NFA (goto/failure/output) is described.
  But the 507 MiB automaton / "cache blowout" / DRAM-bound headline is a property
  of the *flattened DFA transition table*. The framework describes a structure
  that cannot explain the thesis's own central finding.
- **Memory-bandwidth-bound vs compute-bound never defined.** Neither are cache
  coherence, false sharing, NUMA, or the LLC — the load-bearing concepts of the
  entire discussion.
- **P-core/E-core heterogeneity absent** — framework assumes homogeneous cores,
  so the ~4-thread knee has no conceptual support.
- Work-partitioning / boundary-overlap problem (the central correctness hazard)
  is never set up.

### M2. Measurement rigor under-specified (`methodology.tex`)
- Repetition count hedged as "*three or more*"; ground truth is exactly
  `warmup=2, iters=5` (phases A–C), `warmup=1, iters=3` (D), `warmup=0, iters=1`
  (build). State the per-phase table.
- **Dispersion promised but never shown.** Principle (iv) says noise is
  "*reported explicitly*," yet headline speedups carry no error bars/CI — while
  the data shows CV up to **66%** (email corpus) and **53%** (Phase D). With n=5
  and CV>50%, a bare mean is not a stable estimator.
- Unsourced "≈25 GB/s peak bandwidth" (measured how?). Clocks labeled 4.4/3.3 GHz
  never reached under load per env snapshot. Thread affinity asserted in one
  sentence with no P/E core-fill order — the most important confounder for a
  hybrid-core study. GCC version, full flags, exact kernel unpinned. Performance
  thread grid {1,2,4,6,8,10,12} never stated in text (and the correctness grid
  {1,2,3,4,7,8} is inconsistent with it).

### M3. Parallel efficiency promised, never reported
- Objective 2 (intro:22) names speedup, throughput, **and parallel efficiency**;
  methodology defines it (`eq:efficiency`) — but **no efficiency number appears**
  in Results or Conclusion. Either report it (≈0.38 = 4.52×/12) or drop it.

### M4. Conclusion mapping & appendix reproducibility (`conclusion.tex`, `apendicei.tex`)
- Conclusion never closes the loop objective-by-objective.
- Appendix gives canonical SQL for everything **except** the E2E times
  (4.48×/3.04×) — the most prominent end-to-end numbers are the least auditable.
  It also never states where `sweep.db` lives, yet claims results are "audited
  independently."

---

## 🟡 MINOR (cleanup)

| ID | Finding | File | Status |
|----|---------|------|--------|
| m1 | Malformed `\cite{AhoCorasick1975},{Gusfield1997}` (missing backslash → renders literal) | fundamentacao:261 | ✅ fixed |
| m2 | Amdahl "even a small sequential fraction (**s large**)" — contradiction | fundamentacao:70 | ✅ fixed |
| m3 | `S_{\text{escalado}}` (Portuguese) in English body | fundamentacao:82 | ✅ fixed |
| m4 | Leftover `% TODO adicionar coesão` in source | fundamentacao:100 | ✅ fixed |
| m5 | Typo "efficientily"; "highly multi-pattern-matching" (missing adj.) | introduction:5 | ✅ fixed |
| m6 | SimpleWiki "~1.2 GiB" → ~1.19 GiB (actual 1,275,540,181 B; consistency w/ ~1.32, ~10.59) | methodology:83 | ✅ fixed |
| m7 | Results figure mixes `_flat`/`enron_x8` searchers (4.52×/2.79×) with prose's `dynamic`/canonical (4.79×/2.85×) without naming them in the caption | results | ⏳ author (content/figure) |
| m8 | Amdahl/serial-fraction lens never invoked to explain the ~4.5× ceiling on the *moderate* (non-memory-bound) dictionary | results | ⏳ author (content) |
| m9 | Abstract "saturates near **2.85×**" vs Figure 1 **2.79×** at T=12 — reconcile wording | abstract:20 | ⏳ author (framing) |
| m10 | 240.7 vs 241.0 vs canonical 239.60 MB/s baseline — confirm same campaign / footnote (verified: different sweep phases, not an error) | results | ⏳ author (optional footnote) |
| m11 | Moore's Law "every eighteen months" / conflates transistor count with single-core *performance* | introduction:1 | ⏳ author (content) |
| m12 | `Vajira2018` is an arXiv preprint typed `@article`; four bib entries miss `pages`/`location` | referencias.bib | ⏳ author (bib hygiene) |
| m13 | "55 MiB" vs "55.23 MiB" / "507 MiB" vs "506.78 MiB" cosmetic rounding | results | ⏳ author (cosmetic) |
| m14 | `anexoi.tex` is template boilerplate (correctly commented out in main.tex) — optionally delete | anexoi.tex | ⏳ author (optional) |

---

## Cross-check ledger (verified against `sweep.db` / `tcc-synthesis.html`)

| Quantity | Thesis | Source | Match |
|----------|--------|--------|-------|
| Sequential baseline (Snort/Enron) | 239.60 MB/s | 239.60 | ✓ |
| Best search speedup, moderate dict, canonical | 4.79× / 1148.1 MB/s | 4.792 / 1148.09 | ✓ |
| Best search speedup, multi-GiB | 4.52× / 1087.1 MB/s | 4.524 / 1087.13 | ✓ |
| Memory-bound peak (canonical, ~6T) | 2.85× | 2.853 | ✓ |
| Memory-bound 12T (~10.6 GiB) | 2.79× | 2.791 | ✓ |
| Throughput drop, automaton 42× L3 | 74.0% | 74.0% | ✓ |
| Flattened-layout gain (ET, 1 thread) | +13.0% | +13.0% | ✓ |
| Build speedup (ET, 8 threads) | 1.55× | 1.552 | ✓ |
| End-to-end (Snort full) | 4.48× | 4.48× | ✓ |
| End-to-end (Emerging Threats) | 3.04× | 3.04× | ✓ |
| Automaton footprint (full ET) | 506.78 MiB | 506.78 | ✓ |
| Corpus sizes | Enron 1.32 / x8 10.59 / Wiki 1.19 GiB | 1.324 / 10.589 / 1.188 | ✓ |
| Discarded 7.49× / 4.13× / 1.83× | absent | — | ✓ (none present) |

---

## Suggested order of attack (for the author)

1. **RSL** (C1) — biggest defense risk, needs your real screening numbers.
2. **Intro/Abstract scope + gap + RQs** (C2) — shared root with the NIDS framing.
3. **Add dispersion/CV to headline numbers** (M2) — turn the noisy platform into
   a reported strength rather than a hidden weakness.
4. **Framework: add DFA/NFA, memory-bound, false sharing, P/E cores** (M1) — so
   Results has a foundation.
5. **Conclusion 2.85× + efficiency + objective closure** (C3, M3, M4).
6. Remaining minor items in the table above.
