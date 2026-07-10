# DSA Index

[← Back to README](../README.md)

Master table for data structures and algorithms notes.

## Book

Structured reading track for _Introduction to Algorithms_ (CLRS, 4th ed.).

| Chapter | Title                                                         | Status         |
| ------- | ------------------------------------------------------------- | -------------- |
| 2       | [Getting Started](./book/02_getting_started/notes.md)         | 🔄 In progress |
| 3       | [Growth of Functions](./book/03_growth_of_functions/notes.md) | ⬜ Not started |
| 4       | [Divide and Conquer](./book/04_divide_and_conquer/notes.md)   | ⬜ Not started |

→ [Full reading log and progress tracker](./book/index.md)

## Patterns

| Pattern                                                  | When To Use                                              | Notes                             |
| -------------------------------------------------------- | -------------------------------------------------------- | --------------------------------- |
| [Array](./patterns/array.md)                             | Index-based access, prefix sums, single-pass scans.      | Foundation for most other patterns. |
| [String](./patterns/string.md)                           | Character counts, substrings, anagram checks.            | Often pairs with hash maps or sorting. |
| [Hash Table](./patterns/hash_table.md)                   | Lookups, frequency counts, complement searches.          | Trade space for $O(1)$ lookups.   |
| [Sorting](./patterns/sorting.md)                         | Order reveals duplicates, pairs, or interval structure.  | Often unlocks a linear follow-up. |
| [Two Pointers](./patterns/two_pointers.md)               | Sorted arrays, paired scans, slow/fast pointer problems. | Good for reducing nested loops.   |
| [Sliding Window](./patterns/sliding_window.md)           | Contiguous subarray or substring problems.               | Track a window invariant.         |
| [Binary Search](./patterns/binary_search.md)             | Ordered search spaces and monotonic predicates.          | Includes binary search on answer. |
| [Dynamic Programming](./patterns/dynamic_programming.md) | Overlapping subproblems with optimal substructure.       | Start with state definition.      |

## Topic Backlog

| Area                   | Topics                                                           |
| ---------------------- | ---------------------------------------------------------------- |
| Foundations            | Complexity analysis, arrays and strings, hash maps and sets.     |
| Linear data structures | Stacks, queues, linked lists.                                    |
| Trees and heaps        | Trees, heaps, priority queues, tries.                            |
| Graphs                 | BFS, DFS, topological sort, shortest paths, union find.          |
| Paradigms              | Recursion, backtracking, dynamic programming, greedy algorithms. |
| Ordering               | Sorting, intervals, sweep line.                                  |
| Other                  | Bit manipulation, math, number theory.                           |

## Problem Note Template

````markdown
# 0000. Problem Name

> Link / prompt summary.

## Intuition

## Approach

## Complexity

- Time:
- Space:

## Solution

```javascript
const solve = () => {};
```

## Edge Cases

## Key Takeaways
````
