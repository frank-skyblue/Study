# Binary Search

[← Back to DSA Index](../index.md)

Use binary search when the input is sorted or when the answer space has a monotonic true/false boundary.

Related patterns: [Two Pointers](./two_pointers.md), [Dynamic Programming](./dynamic_programming.md)

## Decision Checklist

- Is there an ordered search space?
- Can half of the space be discarded after each check?
- For "binary search on answer", can a candidate answer be validated with a monotonic predicate?

## Exact Match Template

```javascript
const binarySearch = (nums, target) => {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const middle = left + Math.floor((right - left) / 2);

    if (nums[middle] === target) {
      return middle;
    }

    if (nums[middle] < target) {
      left = middle + 1;
      continue;
    }

    right = middle - 1;
  }

  return -1;
};
```

## Lower Bound Template

```javascript
const lowerBound = (nums, target) => {
  let left = 0;
  let right = nums.length;

  while (left < right) {
    const middle = left + Math.floor((right - left) / 2);

    if (nums[middle] < target) {
      left = middle + 1;
      continue;
    }

    right = middle;
  }

  return left;
};
```

## Watch For

- Pick inclusive (`left <= right`) or half-open (`left < right`) boundaries deliberately.
- Avoid infinite loops by ensuring every branch moves a boundary.
- Validate empty arrays and one-element arrays.

## Practice

| Problem | Notes |
| --- | --- |
| Search Insert Position | Lower bound. |
| Find First and Last Position | Two lower-bound searches. |
| Koko Eating Bananas | Binary search on answer. |
