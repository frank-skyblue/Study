# CLRS Reading Log

[← Back to DSA Index](../index.md)

Reading track for _Introduction to Algorithms_, 4th ed. (Cormen, Leiserson, Rivest, Stein).

## Progress

| #   | Chapter             | Notes                                      | Exercises                                          | Status         |
| --- | ------------------- | ------------------------------------------ | -------------------------------------------------- | -------------- |
| 2   | Getting Started     | [notes](./02_getting_started/notes.md)     | [exercises](./02_getting_started/exercises.md)     | ⬜ Not started |
| 3   | Growth of Functions | [notes](./03_growth_of_functions/notes.md) | [exercises](./03_growth_of_functions/exercises.md) | ⬜ Not started |
| 4   | Divide and Conquer  | [notes](./04_divide_and_conquer/notes.md)  | [exercises](./04_divide_and_conquer/exercises.md)  | ⬜ Not started |

**Status key:** ⬜ Not started · 🔄 In progress · ✅ Complete

## Reading Log

| Date        | Chapter | Sections  | Notes                                                                                               |
| ----------- | ------- | --------- | --------------------------------------------------------------------------------------------------- |
| Jul 5, 2026 | 2       | 2.1, 2.2  | insertion sort + loop invariant                                                                     |
| Jul 8, 2026 | 2,3     | 2.3, 3.\* | divide and conquer + merge sort + recurrence, skimmed over running times, as only big O is relevant |

## Focus Areas & Order

**Context:** Intermediate background, interview-focused (FAANG-style), 2–3 year track, ~2–4 hrs/week on CLRS specifically (paired with algorithms/DS half of a broader system-design study plan).

**Method per chapter:** Read for intuition → implement from scratch → 5–8 targeted exercises (skip pure-proof ones) → 3–5 matching interview problems → log complexity/gotchas in a running notes doc.

---

## Tier 1 — Core CLRS chapters (lightened)

| Order | Chapters   | Topic                                                              | Notes                                                                                                                           |
| ----- | ---------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Ch 2–3     | Insertion sort, analyzing/asymptotic notation                      | Quick refresh pass                                                                                                              |
| 2     | Ch 4.1–4.5 | Divide-and-conquer, recurrences, master method                     | Skip 4.6 (proof) & 4.7 (Akra-Bazzi) — skim only                                                                                |
| 3     | Ch 5.1–5.2 | Hiring problem, indicator random variables                         | Partial — skip rest of Ch 5                                                                                                     |
| 4     | Ch 6–9     | Heapsort, Quicksort, linear-time sorting, order statistics         | Ch 9 (median-of-medians): know it exists and why it matters; no deep mastery needed                                             |
| 5     | Ch 10–13   | Elementary DS, Hash Tables, BSTs, Red-Black Trees                  | Implement hash tables and BSTs yourself; for RB-trees, understand the balancing invariant and when to reach for a balanced tree — skip proving rotation correctness |
| 6     | Ch 14–16   | Dynamic Programming, Greedy, Amortized Analysis                    | **Highest leverage for interviews** — supplement heavily with problem sets; DP mastery comes from problem volume, not re-reading |
| 7     | Ch 20–24   | Graphs: BFS/DFS/topo/SCC, MST, shortest paths, all-pairs, max flow | Skip 22.4–22.5; max flow (Ch 24) is conceptual-only unless specifically prepping Google                                         |

---

## Tier 2 — Solid single pass, moderate depth

| Order | Chapters     | Topic                               | Notes                                       |
| ----- | ------------ | ----------------------------------- | ------------------------------------------- |
| 8     | Ch 19        | Disjoint Sets (Union-Find)          | Bump priority — common in interviews        |
| 9     | Ch 18        | B-Trees                             | Good for systems/DB literacy                |
| 10    | Ch 17        | Augmenting Data Structures          | Read for the augmentation pattern           |
| 11    | Ch 25.1–25.2 | Bipartite matching, stable marriage | Conceptual; 25.3 (Hungarian) lower priority |

---

## Tier 3 — Read once for exposure, don't grind

| Chapters     | Topic                                                    | Notes                                                                      |
| ------------ | -------------------------------------------------------- | -------------------------------------------------------------------------- |
| Ch 26–27     | Parallel & Online Algorithms                             | Skim for ideas; Ch 27 has systems/caching relevance                        |
| Ch 31–32     | Number Theory, String Matching                           | KMP/Rabin-Karp intuition only                                              |
| Ch 33        | Machine-Learning Algorithms                              | Optional, low interview relevance                                          |
| Ch 34        | NP-Completeness                                          | Worth real conceptual time (34.1–34.3, 34.5); skip proof mechanics in 34.4 |
| Ch 35, 28–30 | Approximation Algos, Matrix Ops, Linear Programming, FFT | Skim only; revisit if domain-specific need arises                          |
| App. A–D     | Math background                                          | Reference only, dip in as needed                                           |

---

## Running concurrently the whole time

### Pattern-based problem set

Use **NeetCode 150** or **Grind 169**, done repeatedly — not once.

- **First pass:** learn the patterns
- **Later passes:** build speed and clean communication

CLRS is the "why does this work" reference. A pattern resource drives your weekly practice from the start. The textbook alone will not get you interview-ready even after a full read-through — it was not written for that.

### Mock interviews (especially years 2–3)

Verbalizing your approach, clarifying requirements, and discussing tradeoffs is graded separately from correctness at senior level. It is a skill that needs deliberate practice, not just knowledge.

### Company-specific calibration (late prep)

| Company       | What to expect                                                                               |
| ------------- | -------------------------------------------------------------------------------------------- |
| Amazon        | LC medium + heavy behavioral (Leadership Principles) — do not neglect the behavioral half    |
| Google        | Harder problems, strong emphasis on optimal complexity and edge cases; max-flow worth knowing |
| Meta          | Speed + correctness on mediums; less exotic                                                  |
| Stripe        | Practical/API-design-flavored problems alongside algorithms                                  |
| Uber/Pinterest | Fairly standard LC medium/hard mix                                                           |

---

## Phasing (approx., 2–4 hrs/week on CLRS)

- **Months 1–6:** CLRS Tier 1 (lightened per above) interleaved with 3–5 problems/week per topic as you finish each chapter
- **Months 6–18:** Steady problem-solving cadence — aim for 200–300 problems total (easy/medium/hard, weighted toward medium); revisit CLRS only as a reference when a concept feels shaky
- **Last 6–12 months:** Mock interviews, timed practice, revisiting weakest patterns, company-specific prep, and system design in parallel (graded separately and often weighted equally or more at senior level)

**Standing rule:** Let problem patterns drive your weekly practice from day one. Use CLRS as a reference shelf, not a reading list to finish before you start solving.
