# 0242. Valid Anagram

[← Back to DSA Index](../index.md)

> LeetCode 242 — Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
> An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.

Related notes: [Hash Table](../patterns/hash_table.md), [String](../patterns/string.md), [Sorting](../patterns/sorting.md)

---

## Intuition
If s and t are anagrams of each other, then they must have the same count of letters, or equivalently, their sorted form must be equal.

## Approach
B.F.
For each letter in s, find corresponding letter in t, and if so, remove the letter from s and t. If successfully removing all characters from both sides, return True
 => O(n^2) approach

Simply count the letters in both s and t and compare this count to see if they're equal.
> Can actually use a fixed length array as a counter for less overhead, but equivalent in TC.

Alternatively, sort both and compare the sorted string, which trades off O(1) space for O(nlogn) in time.

## Complexity

- Time: O(n)
- Space: O(k), where k is the size of the set of allowed characters in s and t

## Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)

        return count_s == count_t
```
