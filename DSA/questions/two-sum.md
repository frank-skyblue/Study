# Two Sum

[← Back to Hash Maps & Sets](../template.md#hash-maps--sets)

> LeetCode 1 — Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`.
> You may assume each input has exactly one solution, and you may not use the same element twice.

---

## Approach: Hash Map (One Pass)

Instead of checking every pair (O(n²)), store each number's index as we scan the array. For each value, ask: *have I already seen its complement (`target - num`)?*

**Time:** O(n)  
**Space:** O(n)

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
  // Map: value -> index where we first saw that value
  const seen = new Map();

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];

    // The number we need to pair with `num` to reach `target`
    const complement = target - num;

    // If complement was seen before, we found our pair
    if (seen.has(complement)) {
      return [seen.get(complement), i];
    }

    // Record this value and its index for future lookups
    seen.set(num, i);
  }

  // Problem guarantees one solution; this line is unreachable
  return [];
};
```

---

## Walkthrough

Example: `nums = [2, 7, 11, 15]`, `target = 9`

| Step | `i` | `num` | `complement` | `seen` (after step) | Result        |
| ---- | --- | ----- | ------------ | ------------------- | ------------- |
| 1    | 0   | 2     | 7            | `{ 2: 0 }`          | —             |
| 2    | 1   | 7     | 2            | `{ 2: 0, 7: 1 }`    | `[0, 1]` ✓    |

At index 1, complement `2` is already in the map at index 0 → return `[0, 1]`.

---

## Why Not Brute Force?

```javascript
// O(n²) time, O(1) space — fine for tiny inputs, not ideal for interviews
const twoSumBruteForce = (nums, target) => {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
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

- **Pattern:** complement lookup with a hash map
- Store **value → index** (not index → value) so `seen.has(complement)` is O(1)
- Check for complement **before** inserting the current number (avoids using the same element twice when `complement === num`)
