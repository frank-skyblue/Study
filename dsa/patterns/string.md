# String

[← Back to DSA Index](../index.md)

Strings are sequences of characters. Many problems reduce to counting characters, comparing order, or scanning contiguous substrings with a window or two pointers.

## Key Properties

| Operation        | Time       | Notes                                      |
| ---------------- | ---------- | ------------------------------------------ |
| Access by index  | $O(1)$     | Like arrays in most languages.             |
| Search substring | $O(n \cdot m)$ | `n` = string length, `m` = pattern length. |
| Concatenation    | $O(n + m)$ | May allocate a new string.                 |
| Sort characters  | $O(n \log n)$ | Useful for anagram and order checks.  |

## Common Techniques

- **Frequency count** — use a map or fixed-size array (26 letters) to compare character counts.
- **Sort and compare** — sort both strings and check equality for anagram-style problems.
- **Two pointers** — scan from both ends or move pointers at different speeds.
- **Sliding window** — track a contiguous substring invariant for search or replacement problems.
- **Build with array** — append to a list or array, then join once for efficient construction.

## Problems

| #    | Problem                                                      | Pattern                    | Difficulty |
| ---- | ------------------------------------------------------------ | -------------------------- | ---------- |
| 0242 | [Valid Anagram](../problems/0242_valid_anagram.md)           | Frequency count / sorting  | Easy       |
