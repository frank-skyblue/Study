# 0217. Contains Duplicate

[← Back to DSA Index](../index.md)

> LeetCode 217 — Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

Related notes: [Array](../patterns/array.md), [Hash Table](../patterns/hash_table.md), [Sorting](../patterns/sorting.md)

---

## Intuition
The natural and efficient data structure to track duplicates is a set, so this question is simply a wrapper on
sets.

## Approach
B.F.

For each num, check whether there's a duplicate of num in nums => O(n^2) approach

Use a set to keep track of seen elements as we iterate through nums. Return immediately if we detect a duplicate,
and if we cannot find a duplicate after going through every number, return False.

Can also sort, but that's slightly higher time complexity for the trade off of having O(1) space.

## Complexity

- Time: O(n)
- Space: O(n)

## Solution

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
```