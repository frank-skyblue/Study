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
| [Two Pointers](./patterns/two_pointers.md)               | Sorted arrays, paired scans, slow/fast pointer problems. | Good for reducing nested loops.   |
| [Sliding Window](./patterns/sliding_window.md)           | Contiguous subarray or substring problems.               | Track a window invariant.         |
| [Binary Search](./patterns/binary_search.md)             | Ordered search spaces and monotonic predicates.          | Includes binary search on answer. |
| [Dynamic Programming](./patterns/dynamic_programming.md) | Overlapping subproblems with optimal substructure.       | Start with state definition.      |

## Sorting

Sorting is useful when order reveals structure: duplicates become adjacent, extremes move to the ends, and many pair or interval problems become easier to scan.

For comparison-based sorting, the typical lower bound is:

$$
\Omega(n \log n)
$$

Common sorting choices:

| Algorithm      | Average Time  | Worst Time    | Space       | Stable | Notes                                                  |
| -------------- | ------------- | ------------- | ----------- | ------ | ------------------------------------------------------ |
| Bubble Sort    | $O(n^2)$      | $O(n^2)$      | $O(1)$      | Yes    | Mostly useful for learning swaps and invariants.       |
| Insertion Sort | $O(n^2)$      | $O(n^2)$      | $O(1)$      | Yes    | Good for small or nearly sorted inputs.                |
| Merge Sort     | $O(n \log n)$ | $O(n \log n)$ | $O(n)$      | Yes    | Divide, sort halves, then merge.                       |
| Quick Sort     | $O(n \log n)$ | $O(n^2)$      | $O(\log n)$ | No     | Fast in practice with good pivots.                     |
| Heap Sort      | $O(n \log n)$ | $O(n \log n)$ | $O(1)$      | No     | Uses a heap to repeatedly extract the max or min.      |
| Counting Sort  | $O(n + k)$    | $O(n + k)$    | $O(k)$      | Yes    | Works when values fall in a bounded integer range `k`. |

When sorting first enables a linear scan, total complexity is often:

$$
O(n \log n) + O(n) = O(n \log n)
$$

## Problems

| #    | Problem                                                             | Pattern                      | Difficulty | Status   | Key Idea                                    |
| ---- | ------------------------------------------------------------------- | ---------------------------- | ---------- | -------- | ------------------------------------------- |
| 0001 | [Two Sum](./problems/0001_two_sum.md)                               | Hash map / complement lookup | Easy       | Solved   | Store `value -> index` while scanning once. |
| 0076 | [Minimum Window Substring](./problems/0076_min_window_substring.md) | Sliding window               | Hard       | Template | Expand until valid, shrink while valid.     |

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

## Pattern

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
