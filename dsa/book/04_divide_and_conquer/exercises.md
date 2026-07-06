# Chapter 4 Exercises

[← Back to CLRS Index](../index.md) · [← Back to DSA Index](../../index.md)

Notes: [Chapter 4 Notes](./notes.md)

---

## 4.1

### 4.1-1

> What does FIND-MAXIMUM-SUBARRAY return when all elements of A are negative?

It returns the subarray containing the single largest (least negative) element. The crossing-subarray step always picks the highest individual value when all values are negative, and the recursion bottoms out at single elements, so the returned sum is the maximum element of the array.

---

### 4.1-2

> Write pseudocode for the brute-force method of solving the maximum-subarray problem. What is its running time?

```javascript
const maxSubarrayBruteForce = (nums) => {
  let maxSum = -Infinity;
  let bestLeft = 0;
  let bestRight = 0;

  for (let i = 0; i < nums.length; i += 1) {
    let sum = 0;

    for (let j = i; j < nums.length; j += 1) {
      sum += nums[j];

      if (sum > maxSum) {
        maxSum = sum;
        bestLeft = i;
        bestRight = j;
      }
    }
  }

  return { left: bestLeft, right: bestRight, sum: maxSum };
};
```

**Running time:** Θ(n²) — two nested loops each running at most n iterations.

---

### 4.1-3

> Implement both the divide-and-conquer and brute-force algorithms. At what problem size n₀ does the divide-and-conquer solution beat the brute-force solution? How does changing the base case affect n₀?

*Empirical exercise — answer depends on implementation and machine.*

Theoretical crossover: divide-and-conquer is Θ(n lg n) while brute force is Θ(n²). For small n (e.g., n < 20–30), the constant factors of the recursive approach (function call overhead, memory allocation) often make brute force faster in practice.

Changing the base case: switching to brute force for sub-arrays of size ≤ k reduces the constant factor. Increasing k raises n₀ because the brute-force base pays less overhead, but eventually the Θ(n²) behavior of brute force dominates for large inputs.

---

### 4.1-4

> Suppose we change the problem so that an empty subarray is allowed, with sum 0. How would you change any of the algorithms to allow an empty subarray to be the result?

Add a final comparison against 0: if the maximum sum is negative, return 0 (empty subarray) instead.

```javascript
const maxSubarrayAllowEmpty = (nums) => {
  const result = maxSubarrayKadane(nums);
  return Math.max(result, 0);
};
```

For the divide-and-conquer version, change the base case from returning `nums[low]` to returning `max(nums[low], 0)`.

---

### 4.1-5

> Use the following ideas to develop a non-recursive, linear-time algorithm for the maximum-subarray problem. Start at the left and process each element. Keep track of the maximum subarray seen so far and the maximum subarray ending at the current position.

This is Kadane's algorithm — see [notes.md](./notes.md).

**Key invariant:** `currentSum` is the maximum sum of any subarray ending at index `i`. Either we extend the previous best ending subarray (`currentSum + nums[i]`), or we start fresh from `nums[i]`.

---

## 4.2

### 4.2-1

> Use Strassen's algorithm to compute the matrix product. Show your work.

*Computational exercise. Apply the 7-multiplication formula to the given 2×2 matrices and verify the result matches the naive product.*

The seven products P₁–P₇ for matrices A = [[a,b],[c,d]] and B = [[e,f],[g,h]]:

| Product | Formula |
| --- | --- |
| P₁ | a · (f − h) |
| P₂ | (a + b) · h |
| P₃ | (c + d) · e |
| P₄ | d · (g − e) |
| P₅ | (a + d) · (e + h) |
| P₆ | (b − d) · (g + h) |
| P₇ | (a − c) · (e + f) |

Result matrix C = AB:
- C[0][0] = P₅ + P₄ − P₂ + P₆
- C[0][1] = P₁ + P₂
- C[1][0] = P₃ + P₄
- C[1][1] = P₅ + P₁ − P₃ − P₇

---

### 4.2-2

> Write pseudocode for Strassen's algorithm.

*See formulas in 4.2-1. The full recursive structure partitions each n×n matrix into four n/2×n/2 submatrices, recursively computes P₁–P₇, then combines.*

Key implementation note: matrix addition is Θ(n²), which is the non-recursive work at each level. This gives the recurrence T(n) = 7T(n/2) + Θ(n²) → Θ(n^(lg 7)).

---

### 4.2-3

> How would you modify Strassen's algorithm to multiply n×n matrices in which n is not an exact power of 2?

Pad each matrix with zeros to the next power of 2: n′ = 2^(⌈lg n⌉). Padding at most doubles n, so n′ < 2n. The asymptotic complexity is unchanged: Θ((2n)^(lg 7)) = Θ(n^(lg 7)).

---

### 4.2-4

> What is the largest k such that if you can multiply 3×3 matrices using k multiplications, you can multiply n×n matrices in o(n^(lg 7)) time?

Using k multiplications for 3×3, the recurrence is T(n) = kT(n/3) + Θ(n²).

By Master Theorem, T(n) = Θ(n^(log₃ k)).

We need log₃ k < lg 7 ≈ 2.807:

$$
k < 3^{2.807} \approx 21.3
$$

So **k = 21** is the largest value.

---

## 4.3

### 4.3-1

> Show that T(n) = T(n−1) + n has solution T(n) = O(n²).

**Guess:** T(n) ≤ cn² for some constant c.

**Inductive step:** Assume T(n−1) ≤ c(n−1)².

$$
T(n) = T(n-1) + n \leq c(n-1)^2 + n = cn^2 - 2cn + c + n = cn^2 - (2c-1)n + c
$$

For c ≥ 1, the term −(2c−1)n + c ≤ 0 for large enough n, so T(n) ≤ cn². ∎

---

### 4.3-2

> Show that T(n) = T(⌈n/2⌉) + 1 has solution T(n) = O(lg n).

**Guess:** T(n) ≤ c lg n.

**Inductive step:** Assume T(⌈n/2⌉) ≤ c lg⌈n/2⌉.

$$
T(n) \leq c\lg\left\lceil\frac{n}{2}\right\rceil + 1 \leq c\lg\frac{n+1}{2} + 1 = c\lg(n+1) - c + 1
$$

For c ≥ 1 and large enough n, c lg(n+1) ≤ c lg n + c, so T(n) ≤ c lg n. ∎

---

### 4.3-3

> We saw that T(n) = 2T(⌊n/2⌋) + n has solution T(n) = O(n lg n). Show that Ω(n lg n) also holds, so T(n) = Θ(n lg n).

**Guess:** T(n) ≥ cn lg n.

**Inductive step:** Assume T(⌊n/2⌋) ≥ c⌊n/2⌋ lg⌊n/2⌋.

$$
T(n) \geq 2 \cdot c\frac{n}{2}\lg\frac{n}{2} + n = cn(\lg n - 1) + n = cn\lg n - cn + n
$$

For c ≤ 1, −cn + n ≥ 0, so T(n) ≥ cn lg n. Combined with the O bound: **T(n) = Θ(n lg n)**. ∎

---

## 4.4

### 4.4-1

> Use a recursion tree to determine a good asymptotic upper bound on T(n) = 3T(⌊n/2⌋) + n. Verify with substitution.

**Recursion tree:**
- Level k: 3ᵏ nodes, each of size n/2ᵏ. Level cost: 3ᵏ · (n/2ᵏ) = n · (3/2)ᵏ.
- Depth: log₂ n levels.
- Leaf count: 3^(log₂ n) = n^(log₂ 3).

Total cost (geometric series, ratio 3/2 > 1, leaf-dominated):

$$
\sum_{k=0}^{\log_2 n} n \cdot \left(\frac{3}{2}\right)^k = O\!\left(n \cdot \left(\frac{3}{2}\right)^{\log_2 n}\right) = O(n \cdot n^{\log_2(3/2)}) = O(n^{\log_2 3})
$$

**Guess:** T(n) = O(n^(log₂ 3)).

**Substitution verification:** Assume T(⌊n/2⌋) ≤ c(n/2)^(log₂ 3).

$$
T(n) \leq 3c\left(\frac{n}{2}\right)^{\log_2 3} + n = \frac{3c}{2^{\log_2 3}} n^{\log_2 3} + n = cn^{\log_2 3} + n
$$

Since log₂ 3 > 1, n = O(n^(log₂ 3)), so T(n) = O(n^(log₂ 3)). ∎

---

### 4.4-2

> Use a recursion tree to determine a good upper bound on T(n) = T(n/2) + n².

**Tree:**
- Level k cost: (n/2ᵏ)².
- Total: Σ n²/4ᵏ — geometric series with ratio 1/4 < 1, so the root dominates.

$$
\sum_{k=0}^{\infty} \frac{n^2}{4^k} = \frac{n^2}{1 - 1/4} = \frac{4n^2}{3} = O(n^2)
$$

**Guess:** T(n) = O(n²). Verified by Master Theorem Case 3.

---

## 4.5

### 4.5-1

> Use the master method to give tight bounds for the following recurrences.

**a) T(n) = 2T(n/4) + 1**

a = 2, b = 4, f(n) = 1, n^(log₄ 2) = n^(1/2) = √n. f(n) = O(n^(1/2 − ε)) → Case 1. **T(n) = Θ(√n).**

**b) T(n) = 2T(n/4) + √n**

n^(log₄ 2) = √n. f(n) = Θ(√n) → Case 2. **T(n) = Θ(√n · lg n).**

**c) T(n) = 2T(n/4) + n**

n^(log₄ 2) = √n. f(n) = n = Ω(n^(1/2 + ε)) → Case 3. Check regularity: 2·(n/4) = n/2 ≤ cn for c = 1/2. **T(n) = Θ(n).**

**d) T(n) = 2T(n/4) + n²**

f(n) = n² = Ω(n^(1/2 + ε)) → Case 3. **T(n) = Θ(n²).**

---

### 4.5-2

> Professor Caesar wants to implement a matrix-multiplication algorithm that is asymptotically faster than Strassen's. He wants to use a divide-and-conquer method, dividing matrices into pieces of size n/4 × n/4. He needs to determine how many sub-problems his algorithm needs to create. What is the largest k such that his algorithm runs in o(n^(lg 7))?

Recurrence: T(n) = kT(n/4) + Θ(n²). By Master Theorem: T(n) = Θ(n^(log₄ k)).

We need log₄ k < lg 7:

$$
k < 4^{\lg 7} = (2^2)^{\lg 7} = 2^{2\lg 7} = 7^2 = 49
$$

**k = 48** is the largest allowable value.

---

### 4.5-3

> Use the master method to show that the recurrence for binary search, T(n) = T(n/2) + Θ(1), has the solution T(n) = Θ(lg n).

a = 1, b = 2, f(n) = Θ(1), n^(log₂ 1) = n⁰ = 1. f(n) = Θ(1) → **Case 2**. T(n) = Θ(lg n). ∎

See also: [Binary Search pattern notes](../../patterns/binary_search.md).

---

### 4.5-4

> Can the master method be applied to T(n) = 4T(n/2) + n² lg n? Why or why not?

a = 4, b = 2, n^(log₂ 4) = n². f(n) = n² lg n.

- Case 2 requires f(n) = Θ(n²). But n² lg n ≠ Θ(n²) — it grows faster by a logarithmic factor.
- Case 3 requires f(n) = Ω(n^(2+ε)) for some ε > 0. But n² lg n is not polynomially larger than n².

**No.** The master method does not apply. Use the recursion-tree or substitution method. (The answer is T(n) = Θ(n² lg² n).)
