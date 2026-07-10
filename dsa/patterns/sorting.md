# Sorting

[← Back to DSA Index](../index.md)

Sorting is useful when order reveals structure: duplicates become adjacent, extremes move to the ends, and many pair or interval problems become easier to scan.

## Lower Bound

For comparison-based sorting, the typical lower bound is:

$$
\Omega(n \log n)
$$

## Algorithms

| Algorithm      | Average Time  | Worst Time    | Space       | Stable | Notes                                                  |
| -------------- | ------------- | ------------- | ----------- | ------ | ------------------------------------------------------ |
| Bubble Sort    | $O(n^2)$      | $O(n^2)$      | $O(1)$      | Yes    | Mostly useful for learning swaps and invariants.       |
| Insertion Sort | $O(n^2)$      | $O(n^2)$      | $O(1)$      | Yes    | Good for small or nearly sorted inputs.                |
| Merge Sort     | $O(n \log n)$ | $O(n \log n)$ | $O(n)$      | Yes    | Divide, sort halves, then merge.                       |
| Quick Sort     | $O(n \log n)$ | $O(n^2)$      | $O(\log n)$ | No     | Fast in practice with good pivots.                     |
| Heap Sort      | $O(n \log n)$ | $O(n \log n)$ | $O(1)$      | No     | Uses a heap to repeatedly extract the max or min.      |
| Counting Sort  | $O(n + k)$    | $O(n + k)$    | $O(k)$      | Yes    | Works when values fall in a bounded integer range `k`. |

## Common Techniques

- **Sort then scan** — sorting first often reduces an $O(n^2)$ brute-force to $O(n \log n)$.
- **Adjacent comparison** — after sorting, duplicates or near-duplicates are neighbours.
- **Two-pointer on sorted array** — once sorted, use two pointers for pair or sum problems.

When sorting first enables a linear scan, total complexity is often:

$$
O(n \log n) + O(n) = O(n \log n)
$$

## Problems

| #    | Problem                                                             | Pattern            | Difficulty |
| ---- | ------------------------------------------------------------------- | ------------------ | ---------- |
| 0217 | [Contains Duplicate](../problems/0217_contains_duplicate.md)        | Hash set / sorting | Easy       |
| 0242 | [Valid Anagram](../problems/0242_valid_anagram.md)                  | Frequency count / sorting | Easy  |
