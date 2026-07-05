# Dynamic Programming

[← Back to DSA Index](../index.md)

Use dynamic programming when a problem has overlapping subproblems and the best answer for a larger state can be built from smaller states.

Related patterns: [Binary Search](./binary_search.md), [Sliding Window](./sliding_window.md)

## Workflow

1. Define the state: what does `dp[i]` or `dp[i][j]` mean?
2. Define the transition: how do smaller states produce the current state?
3. Define base cases.
4. Choose top-down memoization or bottom-up tabulation.
5. Check whether space can be compressed.

## Top-Down Template

```javascript
const solveWithMemo = (n) => {
  const memo = new Map();

  const dfs = (state) => {
    if (state <= 1) {
      return state;
    }

    if (memo.has(state)) {
      return memo.get(state);
    }

    const answer = dfs(state - 1) + dfs(state - 2);
    memo.set(state, answer);
    return answer;
  };

  return dfs(n);
};
```

## Bottom-Up Template

```javascript
const fibonacci = (n) => {
  if (n <= 1) {
    return n;
  }

  const dp = Array.from({ length: n + 1 }, () => 0);
  dp[1] = 1;

  for (let i = 2; i <= n; i += 1) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
};
```

## Watch For

- A vague state definition usually causes the rest of the solution to break.
- Memoization stores answers for states, not just visited flags.
- Bottom-up order must guarantee dependencies are already computed.

## Practice

| Problem | Notes |
| --- | --- |
| Climbing Stairs | 1D DP. |
| House Robber | Choose/take recurrence. |
| Longest Common Subsequence | 2D DP over prefixes. |
