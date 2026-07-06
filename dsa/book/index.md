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

| Date        | Chapter | Sections | Notes                              |
| ----------- | ------- | -------- | ---------------------------------- |
| Jul 5, 2026 | 2       | 2.1, 2.2 | insertion sort + loop invariant    |
| —           | —       | —        | Add an entry each reading session. |

## Focus Areas & Order

**Context:** Intermediate background, interview-focused (FAANG-style), 2–3 year track, ~2–4 hrs/week on CLRS specifically (paired with algorithms/DS half of a broader system-design study plan).

**Method per chapter:** Read for intuition → implement from scratch → 5–8 targeted exercises (skip pure-proof ones) → 3–5 matching interview problems → log complexity/gotchas in a running notes doc.

---

## Tier 1 — Core, go deep

| Order | Chapters   | Topic                                                              | Notes                                                                                         |
| ----- | ---------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| 1     | Ch 2–3     | Insertion sort, analyzing/asymptotic notation                      | Quick refresh pass                                                                            |
| 2     | Ch 4.1–4.5 | Divide-and-conquer, recurrences, master method                     | Skip 4.6 (proof) & 4.7 (Akra-Bazzi) — skim only                                               |
| 3     | Ch 5.1–5.2 | Hiring problem, indicator random variables                         | Partial — skip rest of Ch 5                                                                   |
| 4     | Ch 6–9     | Heapsort, Quicksort, linear-time sorting, order statistics         | Full depth, all sections                                                                      |
| 5     | Ch 10–13   | Elementary DS, Hash Tables, BSTs, Red-Black Trees                  | Full depth, all sections                                                                      |
| 6     | Ch 14–16   | Dynamic Programming, Greedy, Amortized Analysis                    | **Highest leverage for interviews** — don't rush                                              |
| 7     | Ch 20–24   | Graphs: BFS/DFS/topo/SCC, MST, shortest paths, all-pairs, max flow | Full depth; skip 22.4–22.5, focus on Floyd-Warshall in Ch 23, Ford-Fulkerson concept in Ch 24 |

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

## Phasing (approx., 2–4 hrs/week)

- **Months 1–4:** Ch 2–4 (skip 4.6/4.7), Ch 6–9
- **Months 5–9:** Ch 10–13
- **Months 10–15:** Ch 14–16 ⭐ (core interview leverage)
- **Months 16–20:** Ch 20–24
- **Months 21–24:** Ch 19, 18, 17, 25
- **Months 25–30+:** Ch 34 (conceptual), flexible Tier 3 reading, increasing weight on mock interviews + system design

**Standing rule:** Pair every chapter with targeted practice problems as you go — don't save practice for "after."
