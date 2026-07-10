# Hash Table

[← Back to DSA Index](../index.md)

Hash tables (maps and sets) give expected $O(1)$ lookup, insertion, and deletion. They are ideal when you need to remember what you have already seen while scanning once.

## Key Properties

| Operation | Average Time | Worst Time | Notes                                        |
| --------- | ------------ | ---------- | -------------------------------------------- |
| Lookup    | $O(1)$       | $O(n)$     | Worst case on hash collision (rare in practice). |
| Insert    | $O(1)$       | $O(n)$     |                                              |
| Delete    | $O(1)$       | $O(n)$     |                                              |

## Common Techniques

- **Complement lookup** — store values seen so far and check if a target complement exists.
- **Frequency count** — count occurrences of elements with a map `value → count`.
- **Seen set** — use a set to detect duplicates in $O(n)$ time and $O(n)$ space.
- **Index map** — store `value → index` to answer "where did I see this?" in $O(1)$.

## Problems

| #    | Problem                                                             | Pattern                      | Difficulty |
| ---- | ------------------------------------------------------------------- | ---------------------------- | ---------- |
| 0001 | [Two Sum](../problems/0001_two_sum.md)                              | Hash map / complement lookup | Easy       |
| 0217 | [Contains Duplicate](../problems/0217_contains_duplicate.md)        | Hash set / sorting           | Easy       |
| 0242 | [Valid Anagram](../problems/0242_valid_anagram.md)                  | Frequency count / sorting    | Easy       |
