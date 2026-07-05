# Sliding Window

[← Back to DSA Index](../index.md)

Use sliding window for contiguous subarray or substring problems where adding and removing boundary elements can update the answer efficiently.

Related patterns: [Two Pointers](./two_pointers.md), [Dynamic Programming](./dynamic_programming.md)

## Common Forms

| Form | Use Case | Invariant |
| --- | --- | --- |
| Fixed-size window | Max average, fixed-length substrings | Window length is constant. |
| Variable-size window | Minimum/maximum valid substring | Window satisfies or violates a condition. |
| Frequency window | Anagrams, coverage problems | Counts inside the window match required counts. |

## Variable Window Template

```javascript
const minValidWindow = (items, isValid) => {
  let left = 0;
  let best = Infinity;

  for (let right = 0; right < items.length; right += 1) {
    // Add items[right] to window state.

    while (isValid()) {
      best = Math.min(best, right - left + 1);
      // Remove items[left] from window state.
      left += 1;
    }
  }

  return best === Infinity ? 0 : best;
};
```

## Watch For

- Define what makes a window valid before writing pointer logic.
- Update the answer at the moment the invariant is true.
- Shrink only while validity can be maintained or intentionally broken for the next expansion.

## Practice

| Problem | Notes |
| --- | --- |
| [Minimum Window Substring](../problems/0076_min_window_substring.md) | Need counts and a `formed` counter. |
| Longest Substring Without Repeating Characters | Track last seen positions or frequencies. |
| Find All Anagrams in a String | Fixed-size frequency window. |
