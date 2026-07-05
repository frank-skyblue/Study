# Two Pointers

[← Back to DSA Index](../index.md)

Use two pointers when a problem asks about pairs, ranges, partitioning, or linked-list movement and each pointer can move monotonically.

Related patterns: [Sliding Window](./sliding_window.md), [Binary Search](./binary_search.md)

## Common Forms

| Form | Shape | Typical Use |
| --- | --- | --- |
| Opposite ends | `left = 0`, `right = n - 1` | Pair sums, palindrome checks, sorted arrays. |
| Same direction | `slow`, `fast` | Removing duplicates, compacting arrays, cycle detection. |
| Runner gap | `fast` starts ahead | Find nth node from end, middle node variants. |

## Template

```javascript
const hasPairWithTarget = (nums, target) => {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    const sum = nums[left] + nums[right];

    if (sum === target) {
      return true;
    }

    if (sum < target) {
      left += 1;
      continue;
    }

    right -= 1;
  }

  return false;
};
```

## Watch For

- Sorting changes original indices; keep pairs when indices matter.
- Pointer movement must preserve the invariant that a skipped value cannot be part of a better answer.
- Use early returns for found answers and invalid edge cases.

## Practice

| Problem | Notes |
| --- | --- |
| Two Sum II | Sorted input, opposite-end pointers. |
| Valid Palindrome | Skip non-alphanumeric characters. |
| Container With Most Water | Move the shorter wall. |

## Related Notes

- [Two Sum](../problems/0001_two_sum.md) shows why unsorted index-returning problems often need a hash map instead.
