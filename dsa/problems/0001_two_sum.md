# 0001. Two Sum

[← Back to DSA Index](../index.md)

> LeetCode 1 — Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`.
> You may assume each input has exactly one solution, and you may not use the same element twice.

Related notes: [Array](../patterns/array.md), [Hash Table](../patterns/hash_table.md)

---

## Intuition
Go through the array, keeping track of numbers we've seen so far with a mapping to their index.

At the same time, for each number, check whether the complement (target - num) has already been seen.
If it has been seen, simply retrieve the index from the mapping and return the indicies.

## Approach
B.F.

Iterate through all tuples => O(n^2)

Use a hashmap from the number to the index.

Note that if we do not need the indexes, we can approach using a slightly slower but constant space
algorithm:
- Sort nums array => O(nlogn)
- Initialize 2 pointers from each end and calculate sum at each step
  - If sum is less than target, increment left pointer
  - If sum is greater than target, decrement right pointer.
- Q: What if we "pass by" a correct value, or why can't we increment the right pointer or
decrement the left pointer?
  - Suppose that the right pointer lands on the correct value, then that means the sum at that time
  is less than the target, which means the left pointer will increment from that point on. In no
  case will we need to increment the right pointer.

## Complexity

- Time: O(n)
- Space: O(n)

## Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            want = target - num
            if want in num_to_index:
                return [i, num_to_index[want]]
            num_to_index[num] = i
        
        return [-1, -1]
```

## Key Takeaways
Two sum can be solved both with hashmap and sorting. Sorting is preferred when we need to eliminate 
duplicates (in the case of 3 sum).
