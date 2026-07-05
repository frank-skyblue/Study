# DSA Index

[← Back to README](../README.md)

Master table for data structures and algorithms notes.

## Patterns

| Pattern | When To Use | Notes |
| --- | --- | --- |
| [Two Pointers](./patterns/two_pointers.md) | Sorted arrays, paired scans, slow/fast pointer problems. | Good for reducing nested loops. |
| [Sliding Window](./patterns/sliding_window.md) | Contiguous subarray or substring problems. | Track a window invariant. |
| [Binary Search](./patterns/binary_search.md) | Ordered search spaces and monotonic predicates. | Includes binary search on answer. |
| [Dynamic Programming](./patterns/dynamic_programming.md) | Overlapping subproblems with optimal substructure. | Start with state definition. |

## Problems

| # | Problem | Pattern | Difficulty | Status | Key Idea |
| --- | --- | --- | --- | --- | --- |
| 0001 | [Two Sum](./problems/0001_two_sum.md) | Hash map / complement lookup | Easy | Solved | Store `value -> index` while scanning once. |
| 0076 | [Minimum Window Substring](./problems/0076_min_window_substring.md) | Sliding window | Hard | Template | Expand until valid, shrink while valid. |

## Topic Backlog

| Area | Topics |
| --- | --- |
| Foundations | Complexity analysis, arrays and strings, hash maps and sets. |
| Linear data structures | Stacks, queues, linked lists. |
| Trees and heaps | Trees, heaps, priority queues, tries. |
| Graphs | BFS, DFS, topological sort, shortest paths, union find. |
| Paradigms | Recursion, backtracking, dynamic programming, greedy algorithms. |
| Other | Sorting, intervals, bit manipulation, math, number theory. |

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
