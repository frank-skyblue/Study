# Data Structures & Algorithms Notes

> Template for organizing DSA study notes. Fill in each section as you learn.
> Delete placeholder prompts when you add your own notes.

---

## Table of Contents

### Foundations

- [Complexity Analysis](#complexity-analysis)
- [Arrays & Strings](#arrays--strings)
- [Hash Maps & Sets](#hash-maps--sets)
- [Two Pointers](#two-pointers)
- [Sliding Window](#sliding-window)
- [Binary Search](#binary-search)

### Linear Data Structures

- [Stacks & Queues](#stacks--queues)
- [Linked Lists](#linked-lists)

### Trees & Heaps

- [Trees](#trees)
- [Heaps & Priority Queues](#heaps--priority-queues)
- [Tries](#tries)

### Graphs

- [Graphs](#graphs)
- [Union Find](#union-find)

### Algorithmic Paradigms

- [Recursion & Backtracking](#recursion--backtracking)
- [Dynamic Programming](#dynamic-programming)
- [Greedy Algorithms](#greedy-algorithms)

### Other Topics

- [Sorting & Searching](#sorting--searching)
- [Intervals](#intervals)
- [Bit Manipulation](#bit-manipulation)
- [Math & Number Theory](#math--number-theory)

---

## Reusable Section Template

Use this structure for each topic:

```markdown
### Summary
<!-- One-paragraph overview of the topic and when to use it -->

### Key Concepts
-

### Patterns & Techniques
-

### Time & Space Complexity
| Operation / Approach | Time | Space | Notes |
| -------------------- | ---- | ----- | ----- |
|                      |      |       |       |

### Code Template
<!-- Language of choice -->

### Common Problems
| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

### Mistakes & Edge Cases
-

### Key Takeaways
-
```

---

## Foundations

### Complexity Analysis

#### Summary

#### Key Concepts

- Big O notation (time & space)
- Best, average, and worst case
- Amortized analysis
- Common complexity classes: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)

#### Reference Table

| n       | O(1) | O(log n) | O(n) | O(n log n) | O(n²) |
| ------- | ---- | -------- | ---- | ---------- | ----- |
| 10      |      |          |      |            |       |
| 100     |      |          |      |            |       |
| 1,000   |      |          |      |            |       |
| 1,000,000 |    |          |      |            |       |

#### Key Takeaways

---

### Arrays & Strings

#### Summary

#### Key Concepts

- Indexing, slicing, iteration
- In-place vs extra space
- Mutable vs immutable strings

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

### Hash Maps & Sets

#### Summary

#### Key Concepts

- Key-value lookups
- Frequency counting
- Set membership

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
| [Two Sum](./questions/two-sum.md) | Hash map (complement lookup) | Easy | One-pass O(n) |

#### Key Takeaways

---

### Two Pointers

#### Summary

#### Key Concepts

- Opposite ends (left/right)
- Same direction (slow/fast)
- Sorted array prerequisite

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

### Sliding Window

#### Summary

#### Key Concepts

- Fixed-size window
- Variable-size window
- Window invariant

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

### Binary Search

#### Summary

#### Key Concepts

- Search space reduction
- Lower bound / upper bound
- Binary search on answer

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

## Linear Data Structures

### Stacks & Queues

#### Summary

#### Key Concepts

- LIFO (stack) vs FIFO (queue)
- Monotonic stack / monotonic queue
- Deque (double-ended queue)

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

### Linked Lists

#### Summary

#### Key Concepts

- Singly vs doubly linked
- Dummy head node
- Fast & slow pointers (cycle detection, middle)

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

## Trees & Heaps

### Trees

#### Summary

#### Key Concepts

- Binary tree traversals (inorder, preorder, postorder, level-order)
- Binary search tree (BST) properties
- Balanced trees (AVL, Red-Black — overview)
- Tree height, depth, diameter

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

### Heaps & Priority Queues

#### Summary

#### Key Concepts

- Min-heap vs max-heap
- Top-K problems
- Merge K sorted lists

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

### Tries

#### Summary

#### Key Concepts

- Prefix tree structure
- Insert, search, startsWith
- Word search / autocomplete use cases

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

## Graphs

### Graphs

#### Summary

#### Key Concepts

- Representations: adjacency list, adjacency matrix
- Directed vs undirected, weighted vs unweighted
- BFS, DFS
- Topological sort
- Shortest path (Dijkstra, Bellman-Ford)
- Minimum spanning tree (Kruskal, Prim)

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

### Union Find

#### Summary

#### Key Concepts

- Disjoint set union (DSU)
- Path compression
- Union by rank / size
- Connected components

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

## Algorithmic Paradigms

### Recursion & Backtracking

#### Summary

#### Key Concepts

- Base case and recursive case
- State space tree
- Pruning
- Subsets, permutations, combinations

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

### Dynamic Programming

#### Summary

#### Key Concepts

- Overlapping subproblems
- Optimal substructure
- Top-down (memoization) vs bottom-up (tabulation)
- 1D vs 2D DP
- State definition

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

### Greedy Algorithms

#### Summary

#### Key Concepts

- Locally optimal choice
- Proof of correctness (exchange argument, greedy stays ahead)
- When greedy fails

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

## Other Topics

### Sorting & Searching

#### Summary

#### Key Concepts

- Comparison sorts: merge, quick, heap
- Non-comparison sorts: counting, bucket, radix
- Stability and in-place properties

#### Comparison Table

| Algorithm | Time (avg) | Time (worst) | Space | Stable |
| --------- | ---------- | ------------ | ----- | ------ |
| Merge     |            |              |       |        |
| Quick     |            |              |       |        |
| Heap      |            |              |       |        |

#### Key Takeaways

---

### Intervals

#### Summary

#### Key Concepts

- Sorting by start or end
- Merging overlapping intervals
- Meeting rooms / scheduling

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

### Bit Manipulation

#### Summary

#### Key Concepts

- AND, OR, XOR, NOT, shifts
- Common tricks (check bit, set bit, count bits)
- Subsets via bitmask

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---

### Math & Number Theory

#### Summary

#### Key Concepts

- GCD / LCM (Euclidean algorithm)
- Modular arithmetic
- Prime numbers / sieve
- Combinatorics basics

#### Patterns & Techniques

-

#### Code Template

#### Common Problems

| Problem | Pattern | Difficulty | Notes |
| ------- | ------- | ---------- | ----- |
|         |         |            |       |

#### Key Takeaways

---
