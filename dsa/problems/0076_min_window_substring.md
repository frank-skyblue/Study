# 0076. Minimum Window Substring

[← Back to DSA Index](../index.md)

> LeetCode 76 — Given strings `s` and `t`, return the minimum window substring of `s` that contains every character in `t`, including duplicates.

Related notes: [Sliding Window](../patterns/sliding_window.md), [Two Pointers](../patterns/two_pointers.md)

---

## Pattern

[Sliding window](../patterns/sliding_window.md) with character frequencies.

## Intuition

Expand the right side of the window until it contains all required characters. Once valid, shrink from the left to find the smallest valid window ending at the current right pointer.

## Approach

1. Count required characters from `t`.
2. Move `right` through `s`, adding characters to the window.
3. Track how many required character counts are fully satisfied.
4. While the window is valid, update the best answer and move `left`.

## Complexity

- Time: O(n + m), where `n = s.length` and `m = t.length`.
- Space: O(k), where `k` is the number of distinct characters in `s` and `t`.

## Solution

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
const minWindow = (s, t) => {
  if (t.length === 0 || s.length < t.length) {
    return "";
  }

  const requiredCounts = new Map();

  for (const char of t) {
    requiredCounts.set(char, (requiredCounts.get(char) ?? 0) + 1);
  }

  const windowCounts = new Map();
  const requiredUniqueCount = requiredCounts.size;
  let formedCount = 0;
  let left = 0;
  let bestStart = 0;
  let bestLength = Infinity;

  for (let right = 0; right < s.length; right += 1) {
    const rightChar = s[right];
    windowCounts.set(rightChar, (windowCounts.get(rightChar) ?? 0) + 1);

    if (
      requiredCounts.has(rightChar) &&
      windowCounts.get(rightChar) === requiredCounts.get(rightChar)
    ) {
      formedCount += 1;
    }

    while (left <= right && formedCount === requiredUniqueCount) {
      const windowLength = right - left + 1;

      if (windowLength < bestLength) {
        bestStart = left;
        bestLength = windowLength;
      }

      const leftChar = s[left];
      windowCounts.set(leftChar, windowCounts.get(leftChar) - 1);

      if (
        requiredCounts.has(leftChar) &&
        windowCounts.get(leftChar) < requiredCounts.get(leftChar)
      ) {
        formedCount -= 1;
      }

      left += 1;
    }
  }

  if (bestLength === Infinity) {
    return "";
  }

  return s.slice(bestStart, bestStart + bestLength);
};
```

## Edge Cases

- `s` is shorter than `t`.
- `t` contains duplicate characters.
- No valid window exists.
- The best window appears at the start or end of `s`.

## Key Takeaways

- `formedCount` should count fully satisfied character requirements, not total matched characters.
- Shrink the window only after it is valid.
- Update the best answer before removing the left character.
