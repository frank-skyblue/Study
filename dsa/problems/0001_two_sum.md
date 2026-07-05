# 0001. Two Sum

[← Back to DSA Index](../index.md)

> LeetCode 1 — Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`.
> You may assume each input has exactly one solution, and you may not use the same element twice.

Related notes: [Two Pointers](../patterns/two_pointers.md), [Sliding Window](../patterns/sliding_window.md)

---

## Pattern

Hash map / complement lookup.

## Approach: Hash Map (One Pass)

Instead of checking every pair, store each number's index as you scan the array. For each value, ask: *have I already seen its complement (`target - num`)?*

**Time:** O(n)  
**Space:** O(n)

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
  const seen = new Map();

  for (let i = 0; i < nums.length; i += 1) {
    const num = nums[i];
    const complement = target - num;

    if (seen.has(complement)) {
      return [seen.get(complement), i];
    }

    seen.set(num, i);
  }

  return [];
};
```

---

## Walkthrough

Example: `nums = [2, 7, 11, 15]`, `target = 9`

| Step | `i` | `num` | `complement` | `seen` After Step | Result |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 2 | 7 | `{ 2: 0 }` | - |
| 2 | 1 | 7 | 2 | `{ 2: 0, 7: 1 }` | `[0, 1]` |

At index 1, complement `2` is already in the map at index 0, so return `[0, 1]`.

---

## Why Not Brute Force?

```javascript
const twoSumBruteForce = (nums, target) => {
  for (let i = 0; i < nums.length; i += 1) {
    for (let j = i + 1; j < nums.length; j += 1) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }

  return [];
};
```

The hash map trades extra space for a single pass through the array.

---

## Key Takeaways

- Store **value → index** so `seen.has(complement)` is O(1).
- Check for the complement **before** inserting the current number to avoid using the same element twice.
- This is not a two-pointer problem when original indices are required and the input is unsorted.
