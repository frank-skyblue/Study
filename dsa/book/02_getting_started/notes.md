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

1. **Divide** the problem into one or more subproblems that are smaller instances of the same problem
2. **Conquer** the subproblems by solving them recursively
3. **Combine** the subproblem solutions to form a solution to the original problem

### Merge Sort

**Divide** subarray `A[p:r]` to be sorted into 2 halves. Ex. Compute midpoint _q_ of `A[p:r]` and divide into
`A[p:q]` and `A[q+1:r]`.
**Conquer** by sorting each of the subarrays recursively using merge sort again.
**Combine** the two sorted subarrays back into `A[p:r]`, producing the sorted answer

The sort _bottoms out_ when it has reached an array with a single element, which is sorted by definition.

```text
 1  MERGE(A,p,q,r)
 2  nL = q - p + 1                              // length of A[p : q]
 3  nR = r - q                                  // length of A[q + 1 : r]
 4  let L[0:nL - 1] and R[0 : nR - 1] be new arrays
 5  for i = 0 to nL - 1                         // copy A[p : q] into L[0 : nL - 1]
 6    L[i] = A[p + i]
 7  for j = 0 to nR - 1                         // copy A[q + 1 : r] into R[0 : nR - 1]
 8    R[j] = A[q + 1 + j]
 9
10  i = 0                                       // i indexes smallest remaining element in L
11  j = 0                                       // j indexes smallest remaining element in R
12  k = p                                       // k indexes the location in A to fill
13  // As long as both L and R has an unmerged element, copy the smallest unmerged element back to A[p:r]
14  while i < nL and j < nR
15    if L[i] <= R[j]
16      A[k] = L[i]
17      i = i + 1
18    else
19      A[k] = R[j]
20      j = j + 1
21    k = k + 1
22  // Copy over the remaining elements in L and R, if any remaining
23  while i < nL
24    A[k] = L[i]
25    i = i + 1
26    k = k + 1
27  while j < nR
28    A[k] = R[j]
29    j = j + 1
30    k = k + 1
31
32  MERGE_SORT(A,p,r)
33    // Base case, single element
34    if p >= r
35      return
36    // split array into 2 halves, and sort both halves
37    q = floor(p + r / 2)
38    MERGE_SORT(A,p,q)
39    MERGE_SORT(A,p,q + 1,r)
40    MERGE(A,p,q,r)
```

### Complexity

Combining 2 sorted halves takes _O(n)_ intuitively, and the depth of the recursion tree is _O(nlog(n))_.

Recurrence equation.

Let _T(n)_ be the worst-case running time on a problem of size _n_

If the problem size is small enough, say _n < n0_ for some _n0 > 0_. The straightforward
solution is _O(1)_ time

Suppose that the division of the problem yields _a_ sub problems each with size _n/b_.

It takes _T(n/b)_ time to solve one subproblem of size _n/b_, and so it takes _aT(n/b)_ time to solve all _a_ problems.

If it takes _D(n)_ time to divide the problem into subproblems and _C(n)_ time to combine the solutions to the subproblems into the solution of the problem, we get recurrence

$$
T(n) = \begin{cases} \Theta(1) & \text{if } n < n_0 \\ D(n) + aT(n/b) + C(n) & \text{otherwise} \end{cases}
$$

For merge sort, _C(n) = O(n)_, _D(n) = O(1)_. So recurrence is

$$
T(n) = 2T(n/2) + O(n)
$$

Which we can show with master theorem, that it is _O(nlog(n))_, but can also argue with
intuition, ex. depth x O(n)

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
