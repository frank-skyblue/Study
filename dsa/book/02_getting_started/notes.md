# Chapter 2 — Getting Started

[← Back to CLRS Index](../index.md) · [← Back to DSA Index](../../index.md)

Exercises: [2.1](./exercises.md#21) · [2.2](./exercises.md#22) · [2.3](./exercises.md#23)

Related patterns: [Two Pointers](../../patterns/two_pointers.md) · [Dynamic Programming](../../patterns/dynamic_programming.md)

---

## 2.1 Insertion Sort

Sorting is typically done on **keys**, which together with their values (**satellite data**) form a **record**. Ex. For a student
record sheet, key could be things like age, grade, etc., but the values are sorted along with the key.

Insertion sort builds a sorted sub-array one element at a time by taking the next unsorted element and inserting it into its correct position.

**Analogy:** Sorting a hand of playing cards — pick up one card at a time and slide it left into its correct position among the already-sorted cards.

```text
 1  insertion_sort(A, n)
 2  for i = 2 to n
 3    key = A[i]
 4    // Insert A[i] into sorted subarray A[1:i-1]
 5    j = i - 1
 6    while j > 0 and A[j] > key
 7      // Shift element forward
 8      A[j + 1] = A[j]
 9      j = j - 1
10    // Found correct spot
11    A[j + 1] = key
```

### Loop Invariant

A **loop invariant** is a property that holds before the first iteration, is maintained by each iteration, and yields a useful conclusion when the loop ends.

For insertion sort, the invariant on the **for** loop is:

- At the beginning of each iteration, indexed by _i_, the subarray consisting of elements `A[1:i - 1]` are sorted

Three properties must hold:

| Property           | Meaning                                                                              |
| ------------------ | ------------------------------------------------------------------------------------ |
| **Initialization** | True before the first iteration (a single element is trivially sorted).              |
| **Maintenance**    | If true before an iteration, the body keeps it true.                                 |
| **Termination**    | When the loop ends, the invariant gives us what we need — the whole array is sorted. |

Initialization

> Since before the loop starts, `i = 2`, and thus `A[1:1]` is the subarray, and is sorted by default, since it consists of only 1 element

Maintenance

> A formal proof of this would require a loop invariant for the **while** loop. But informally, the body of the **for** loop
> works by moving values in `A[i - 1]`, `A[i - 2]` and so on until we find a correct spot for `A[i]`, thus preserving the loop
> invariant as we increment _i_

Termination

> Once _i_ exceeds n in line 2 (i = n + 1), the **for** loop terminates, and by loop invariant, `A[1:n]` is sorted.

### Complexity

| Case                   | Time  | Notes                                                           |
| ---------------------- | ----- | --------------------------------------------------------------- |
| Best (already sorted)  | Θ(n)  | Inner while loop never executes.                                |
| Worst (reverse sorted) | Θ(n²) | Every element shifts past every sorted element.                 |
| Average                | Θ(n²) | On average, each element shifts past half the sorted sub-array. |

**Space:** Θ(1) — sorts in place.

---

## 2.2 Analyzing Algorithms

### The RAM Model

Analysis assumes a generic **Random Access Machine**:

- Each simple operation (arithmetic, comparison, assignment, array index) takes one step.
- Memory access is uniform — no cache effects.
- Loops and function calls are not simple operations; they are composed of steps.

This model lets us count steps as a function of n, independent of hardware.

### Worst-Case vs. Average-Case

| Analysis         | Definition                                                          | Why It Matters                                            |
| ---------------- | ------------------------------------------------------------------- | --------------------------------------------------------- |
| **Worst-case**   | Maximum steps over all inputs of size n.                            | Provides a guaranteed upper bound.                        |
| **Average-case** | Expected steps over all inputs of size n (requires a distribution). | More realistic but harder to compute.                     |
| **Best-case**    | Minimum steps — rarely useful in isolation.                         | Can be misleading (a sorted input is not representative). |

CLRS primarily analyzes worst-case running time.

### Order of Growth

We care about the **dominant term** as $n \to \infty$. A $\Theta(n^2)$ algorithm running $3n^2 + 14n + 5$ steps is simply $\Theta(n^2)$ — lower-order terms and constants are dropped.

This is formalized in Chapter 3 with asymptotic notation.

---

## 2.3 Designing Algorithms — Divide and Conquer

### The Divide-and-Conquer Paradigm

1. **Divide** the problem into smaller sub-problems of the same type.
2. **Conquer** each sub-problem recursively. Base case: sub-problem small enough to solve directly.
3. **Combine** the sub-problem solutions into an answer for the original problem.

### Merge Sort

```javascript
const mergeSort = (nums) => {
  if (nums.length <= 1) {
    return nums;
  }

  const mid = Math.floor(nums.length / 2);
  const left = mergeSort(nums.slice(0, mid));
  const right = mergeSort(nums.slice(mid));

  return merge(left, right);
};

const merge = (left, right) => {
  const result = [];
  let i = 0;
  let j = 0;

  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) {
      result.push(left[i]);
      i += 1;
    } else {
      result.push(right[j]);
      j += 1;
    }
  }

  return result.concat(left.slice(i), right.slice(j));
};
```

### Complexity

The recurrence for merge sort is:

$$
T(n) = \begin{cases} \Theta(1) & \text{if } n = 1  2T(n/2) + \Theta(n) & \text{if } n > 1 \end{cases}
$$

Solving: **T(n) = Θ(n lg n)** — this holds in all cases (best, average, worst).

### Insertion Sort vs. Merge Sort

| Property        | Insertion Sort                | Merge Sort                           |
| --------------- | ----------------------------- | ------------------------------------ |
| Worst-case time | Θ(n²)                         | Θ(n lg n)                            |
| Best-case time  | Θ(n)                          | Θ(n lg n)                            |
| Space           | Θ(1) in place                 | Θ(n) auxiliary                       |
| Stable          | Yes                           | Yes                                  |
| When to prefer  | Small or nearly sorted inputs | Large inputs where O(n lg n) matters |

---

## Key Takeaways

- A loop invariant must satisfy initialization, maintenance, and termination — this is the formal way to prove an iterative algorithm correct.
- The RAM model lets us analyze algorithms independent of hardware by counting primitive operations.
- Divide-and-conquer trades space for a dramatically better time complexity: Θ(n lg n) vs Θ(n²).
- Recurrences naturally describe divide-and-conquer algorithms; Chapter 4 covers methods to solve them.
