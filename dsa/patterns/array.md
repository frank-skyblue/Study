# Array

[← Back to DSA Index](../index.md)

Arrays store elements in contiguous memory with $O(1)$ random access by index. Many problems reduce to a single pass, two pointers, or prefix structures over the sequence.

## Key Properties

| Operation     | Time       | Notes                                      |
| ------------- | ---------- | ------------------------------------------ |
| Access by index | $O(1)$   | Direct memory offset.                      |
| Search (unsorted) | $O(n)$ | Linear scan.                               |
| Search (sorted)   | $O(\log n)$ | Binary search.                          |
| Insert / Delete at end | $O(1)$ | Amortised for dynamic arrays.        |
| Insert / Delete at middle | $O(n)$ | Shift required.                   |

## Common Techniques

- **Single pass** — accumulate a result while scanning left to right once.
- **Two pointers** — use a left and right pointer that move inward or at different speeds.
- **Prefix sums** — precompute cumulative sums so any subarray sum is $O(1)$.
- **Sorting first** — sort to bring duplicates or extremes together, then scan linearly.

## Problems

| #    | Problem                                                             | Pattern                      | Difficulty |
| ---- | ------------------------------------------------------------------- | ---------------------------- | ---------- |
| 0001 | [Two Sum](../problems/0001_two_sum.md)                              | Hash map / complement lookup | Easy       |
| 0217 | [Contains Duplicate](../problems/0217_contains_duplicate.md)        | Hash set / sorting           | Easy       |
