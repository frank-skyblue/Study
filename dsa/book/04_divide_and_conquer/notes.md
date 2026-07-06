# Chapter 4 — Divide and Conquer

[← Back to CLRS Index](../index.md) · [← Back to DSA Index](../../index.md)

Exercises: [4.1](./exercises.md#41) · [4.2](./exercises.md#42) · [4.3](./exercises.md#43) · [4.4](./exercises.md#44) · [4.5](./exercises.md#45)

Related: [Getting Started](../02_getting_started/notes.md) · [Dynamic Programming](../../patterns/dynamic_programming.md) · [Binary Search](../../patterns/binary_search.md)

---

## 4.1 The Maximum-Subarray Problem

> **Problem:** Given an array of numbers, find the contiguous subarray with the largest sum.

This is only interesting when the array can contain negative numbers. An all-positive array's maximum subarray is the whole array.

### Divide-and-Conquer Approach

Split the array at midpoint. The maximum subarray must be in one of three locations:
1. Entirely in the left half.
2. Entirely in the right half.
3. Crossing the midpoint.

Cases 1 and 2 are solved recursively. Case 3 can be solved in Θ(n) by extending outward from the midpoint in both directions.

```javascript
const findMaxCrossingSubarray = (nums, low, mid, high) => {
  let leftSum = -Infinity;
  let sum = 0;
  let maxLeft = mid;

  for (let i = mid; i >= low; i -= 1) {
    sum += nums[i];
    if (sum > leftSum) {
      leftSum = sum;
      maxLeft = i;
    }
  }

  let rightSum = -Infinity;
  sum = 0;
  let maxRight = mid + 1;

  for (let j = mid + 1; j <= high; j += 1) {
    sum += nums[j];
    if (sum > rightSum) {
      rightSum = sum;
      maxRight = j;
    }
  }

  return { left: maxLeft, right: maxRight, sum: leftSum + rightSum };
};

const findMaxSubarray = (nums, low, high) => {
  if (low === high) {
    return { left: low, right: high, sum: nums[low] };
  }

  const mid = Math.floor((low + high) / 2);
  const leftResult = findMaxSubarray(nums, low, mid);
  const rightResult = findMaxSubarray(nums, mid + 1, high);
  const crossResult = findMaxCrossingSubarray(nums, low, mid, high);

  if (leftResult.sum >= rightResult.sum && leftResult.sum >= crossResult.sum) {
    return leftResult;
  }

  if (rightResult.sum >= leftResult.sum && rightResult.sum >= crossResult.sum) {
    return rightResult;
  }

  return crossResult;
};
```

### Recurrence and Complexity

$$
T(n) = 2T(n/2) + \Theta(n)
$$

Solving (Case 2 of Master Theorem): **T(n) = Θ(n lg n)**.

### Kadane's Algorithm — Θ(n)

The divide-and-conquer solution is Θ(n lg n). A simpler linear solution exists:

```javascript
const maxSubarrayKadane = (nums) => {
  let maxSum = nums[0];
  let currentSum = nums[0];

  for (let i = 1; i < nums.length; i += 1) {
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    maxSum = Math.max(maxSum, currentSum);
  }

  return maxSum;
};
```

**Insight:** At each position, we either extend the previous subarray or start a new one — whichever is larger. This is the DP approach studied further in later chapters.

---

## 4.2 Strassen's Matrix-Multiplication Algorithm

Standard matrix multiplication of two n×n matrices requires Θ(n³) operations (n² dot products, each costing Θ(n)).

### Naive Divide and Conquer

Partition each n×n matrix into four n/2 × n/2 submatrices. Each multiplication requires 8 recursive calls, giving:

$$
T(n) = 8T(n/2) + \Theta(n^2)
$$

By Master Theorem: T(n) = Θ(n³) — no improvement.

### Strassen's Method

Strassen reduces the 8 recursive multiplications to 7 by computing intermediate products:

$$
T(n) = 7T(n/2) + \Theta(n^2)
$$

By Master Theorem (Case 1): **T(n) = Θ(n^{lg 7}) ≈ Θ(n^{2.807})**.

The 7 products (P₁–P₇) are linear combinations of submatrix sums; the full construction is algebraically complex but the key idea is that multiplication is more expensive than addition.

**Practical note:** Strassen has large constant factors and is only faster than naive multiplication in practice for very large matrices.

---

## 4.3 The Substitution Method for Solving Recurrences

The substitution method has two steps:
1. **Guess** the form of the solution.
2. Use **mathematical induction** to prove the guess is correct and find the constants.

### Example: T(n) = 2T(⌊n/2⌋) + n

**Guess:** T(n) = O(n lg n), i.e., T(n) ≤ cn lg n.

**Inductive step:** Assume T(⌊n/2⌋) ≤ c⌊n/2⌋ lg⌊n/2⌋. Substitute:

$$
T(n) \leq 2 \cdot c\frac{n}{2}\lg\frac{n}{2} + n = cn(\lg n - 1) + n = cn\lg n - cn + n \leq cn\lg n
$$

The last inequality holds when c ≥ 1. The base case must also be verified.

### Avoiding Pitfalls

- **Asymptotic notation in inductive hypotheses:** You must prove T(n) ≤ cn lg n for an exact constant c — not just "O(n lg n)". Plugging O(·) into the hypothesis and deriving O(·) is circular.
- **Subtracting a lower-order term:** If the straightforward guess doesn't work, try subtracting a lower-order term (e.g., guess T(n) ≤ cn lg n − dn).

---

## 4.4 The Recursion-Tree Method

Draw the recursion as a tree where each node is the cost of the work done at that level (not the recursive calls). Sum across all levels.

### Example: T(n) = 3T(n/4) + cn²

- **Root cost:** cn²
- **Level 1:** 3 nodes, each costing c(n/4)² = cn²/16. Level total: 3cn²/16.
- **Level 2:** 9 nodes, each cn²/256. Level total: 9cn²/256.
- **Level k:** 3ᵏ nodes. Level total: (3/16)ᵏ cn².
- **Depth:** log₄ n levels.

Sum of levels (geometric series with ratio 3/16 < 1):

$$
\sum_{k=0}^{\log_4 n} \left(\frac{3}{16}\right)^k cn^2 < \frac{cn^2}{1 - 3/16} = \frac{16}{13}cn^2 = O(n^2)
$$

**Guess from tree:** T(n) = O(n²). Then verify with substitution method.

### When the Tree Is Unbalanced

When subproblems have different sizes (e.g., T(n) = T(n/3) + T(2n/3) + cn), the tree is not a perfect structure. Sum the cost level by level; the longest root-to-leaf path determines the depth.

---

## 4.5 The Master Method

The master method solves recurrences of the form:

$$
T(n) = aT(n/b) + f(n), \quad a \geq 1,\ b > 1
$$

The critical quantity is **n^(log_b a)** — the rate at which leaves accumulate work.

### Three Cases

| Case | Condition | Solution |
| --- | --- | --- |
| 1 | f(n) = O(n^(log_b a − ε)) for some ε > 0 | T(n) = Θ(n^(log_b a)) |
| 2 | f(n) = Θ(n^(log_b a)) | T(n) = Θ(n^(log_b a) · lg n) |
| 3 | f(n) = Ω(n^(log_b a + ε)) and regularity condition | T(n) = Θ(f(n)) |

**Intuition:**
- Case 1: Leaves dominate. Total cost is determined by how many leaves there are.
- Case 2: Each level costs the same. Multiply by the number of levels (lg n).
- Case 3: Root (top-level work) dominates. Total cost is the root's cost.

### Common Applications

| Recurrence | a | b | f(n) | n^(log_b a) | Case | Result |
| --- | --- | --- | --- | --- | --- | --- |
| T(n) = 2T(n/2) + n | 2 | 2 | n | n | 2 | Θ(n lg n) |
| T(n) = 2T(n/2) + n² | 2 | 2 | n² | n | 3 | Θ(n²) |
| T(n) = 4T(n/2) + n | 4 | 2 | n | n² | 1 | Θ(n²) |
| T(n) = 4T(n/2) + n² | 4 | 2 | n² | n² | 2 | Θ(n² lg n) |
| T(n) = 4T(n/2) + n³ | 4 | 2 | n³ | n² | 3 | Θ(n³) |
| T(n) = 7T(n/2) + n² | 7 | 2 | n² | n^(lg 7) | 1 | Θ(n^(lg 7)) |

### When the Master Method Does Not Apply

The master method requires f(n) and n^(log_b a) to be polynomially comparable. If the gap is only logarithmic — e.g., f(n) = n lg n and n^(log_b a) = n — neither Case 1 nor Case 3 applies. Use the recursion-tree or substitution method instead.

---

## Key Takeaways

- Divide-and-conquer naturally produces recurrences; the master method is the fastest way to solve standard ones.
- The three-way comparison (n^(log_b a) vs f(n)) is the heart of the master method — identify which side dominates.
- The recursion-tree method builds geometric series intuition and should be confirmed with substitution.
- Strassen shows that even an "obvious" cubic bound can be beaten by rearranging recursive calls.
- Maximum-subarray has a Θ(n lg n) divide-and-conquer solution but Kadane's algorithm solves it in Θ(n).
