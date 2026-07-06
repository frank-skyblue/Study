# Chapter 2 Exercises

[← Back to CLRS Index](../index.md) · [← Back to DSA Index](../../index.md)

Notes: [Chapter 2 Notes](./notes.md)

---

## 2.1

### 2.1-1

> Illustrate the operation of insertion sort on the array ⟨31, 41, 59, 26, 41, 58⟩.

Each row shows the state after inserting element at position `i`:

| i | Array State | Key | Action |
| --- | --- | --- | --- |
| 0 | **[31]**, 41, 59, 26, 41, 58 | — | Initial single-element sorted region. |
| 1 | **[31, 41]**, 59, 26, 41, 58 | 41 | 41 > 31, insert after 31. |
| 2 | **[31, 41, 59]**, 26, 41, 58 | 59 | 59 > 41, insert after 41. |
| 3 | **[26, 31, 41, 59]**, 41, 58 | 26 | 26 < 59, 31, 41 — shift all right, insert at front. |
| 4 | **[26, 31, 41, 41, 59]**, 58 | 41 | 41 < 59, not < 41 — insert between second 41 and 59. |
| 5 | **[26, 31, 41, 41, 58, 59]** | 58 | 58 < 59, not < 41 — insert before 59. |

---

### 2.1-2

> Rewrite insertion sort to sort in monotonically decreasing order.

Change the comparison in the inner `while` condition from `>` to `<`:

```javascript
const insertionSortDescending = (nums) => {
  for (let i = 1; i < nums.length; i += 1) {
    const key = nums[i];
    let j = i - 1;

    while (j >= 0 && nums[j] < key) {
      nums[j + 1] = nums[j];
      j -= 1;
    }

    nums[j + 1] = key;
  }

  return nums;
};
```

---

### 2.1-3

> Write pseudocode for linear search — scan the array for value `v` and return its index, or NIL if not found. State and prove the loop invariant.

```javascript
const linearSearch = (nums, v) => {
  for (let i = 0; i < nums.length; i += 1) {
    if (nums[i] === v) {
      return i;
    }
  }

  return null;
};
```

**Loop invariant:** At the start of iteration `i`, `v` does not appear in `nums[0..i-1]`.

- *Initialization:* Before `i = 0`, the sub-array is empty — trivially, `v` is not there.
- *Maintenance:* If `v` is not in `nums[0..i-1]` and `nums[i] !== v`, then `v` is not in `nums[0..i]`.
- *Termination:* The loop ends either because `nums[i] === v` (return `i`) or because `i = n` and `v` is not in the entire array (return `null`).

---

### 2.1-4

> Consider adding two n-bit binary integers a and b stored in n-element arrays A and B. Write pseudocode to store the result in an (n+1)-element array C.

```javascript
const addBinary = (A, B) => {
  const n = A.length;
  const C = new Array(n + 1).fill(0);
  let carry = 0;

  for (let i = n - 1; i >= 0; i -= 1) {
    const sum = A[i] + B[i] + carry;
    C[i + 1] = sum % 2;
    carry = Math.floor(sum / 2);
  }

  C[0] = carry;

  return C;
};
```

The extra element `C[0]` holds the final carry bit (the potential overflow into the (n+1)th position).

---

## 2.2

### 2.2-1

> Express the function n³/1000 + 100n² − 100n + 3 in Θ notation.

$$
\Theta(n^3)
$$

The dominant term as n → ∞ is n³. All lower-order terms and constants are dropped.

---

### 2.2-2

> Write pseudocode for selection sort. What are the loop invariant, the best-case and worst-case running times, and is selection sort better than insertion sort?

```javascript
const selectionSort = (nums) => {
  for (let i = 0; i < nums.length - 1; i += 1) {
    let minIndex = i;

    for (let j = i + 1; j < nums.length; j += 1) {
      if (nums[j] < nums[minIndex]) {
        minIndex = j;
      }
    }

    if (minIndex !== i) {
      [nums[i], nums[minIndex]] = [nums[minIndex], nums[i]];
    }
  }

  return nums;
};
```

**Loop invariant:** At the start of iteration `i`, `nums[0..i-1]` contains the `i` smallest elements in sorted order.

**Time:** Θ(n²) in both best and worst case — the inner loop always scans the full remaining unsorted region regardless of input order.

**Versus insertion sort:** Insertion sort runs in Θ(n) on an already-sorted input; selection sort cannot take advantage of existing order. For nearly sorted data, insertion sort is faster.

---

### 2.2-3

> Consider linear search. Assuming all elements are equally likely to be the target, how many elements are checked on average? In the worst case? Express in Θ notation.

- **Average case:** (n+1)/2 elements checked → **Θ(n)**
- **Worst case:** n elements checked → **Θ(n)**

Both cases are Θ(n) because the constant factor (1/2) is absorbed.

---

### 2.2-4

> How can we modify almost any algorithm to have a good best-case running time?

Add a special-case check at the start for inputs that are already in the desired output state and return immediately. For example, check if an array is already sorted before running insertion sort.

This is generally a surface trick — it improves only best-case performance and does not change average or worst-case behavior.

---

## 2.3

### 2.3-1

> Illustrate the operation of merge sort on ⟨3, 41, 52, 26, 38, 57, 9, 49⟩.

```
Divide:
[3, 41, 52, 26, 38, 57, 9, 49]
        /                \
[3, 41, 52, 26]      [38, 57, 9, 49]
    /       \              /       \
[3, 41]  [52, 26]   [38, 57]   [9, 49]
  / \      / \        / \        / \
[3][41] [52][26]   [38][57]   [9][49]

Conquer (merge back up):
[3, 41]  [26, 52]   [38, 57]   [9, 49]
    \       /              \       /
[3, 26, 41, 52]      [9, 38, 49, 57]
        \                /
[3, 9, 26, 38, 41, 49, 52, 57]
```

---

### 2.3-2

> Rewrite the merge procedure without using sentinels, instead stopping as soon as one array is exhausted and copying the remainder of the other array.

This is the standard implementation above in [notes.md](./notes.md) — the `while` loop exits when either sub-array is exhausted, and `concat` appends the remaining elements.

---

### 2.3-3

> Use mathematical induction to show that T(n) = n lg n when n is an exact power of 2.

**Claim:** T(n) = n lg n for n = 2ᵏ.

**Base case (n = 2):** T(2) = 2T(1) + 2 = 2(1) + 2 = ... actually the recurrence gives T(2) = 2T(1) + 2 = 4. And 2 lg 2 = 2 · 1 = 2. *(The exact constant depends on the Θ(1) and Θ(n) hidden constants — the key is the form n lg n, not the exact constant.)*

**Inductive step:** Assume T(n/2) = (n/2) lg(n/2). Then:

$$
T(n) = 2 \cdot \frac{n}{2} \lg\frac{n}{2} + n = n(\lg n - 1) + n = n \lg n - n + n = n \lg n
$$

The induction holds. ∎

---

### 2.3-4

> Express insertion sort as a recurrence.

$$
T(n) = \begin{cases} \Theta(1) & \text{if } n = 1 \\ T(n-1) + \Theta(n) & \text{if } n > 1 \end{cases}
$$

To insert the nth element into a sorted sub-array of n-1 elements requires at most n-1 comparisons and shifts — hence Θ(n) per step. This gives a total of Θ(n²).

---

### 2.3-5

> Referring back to the searching problem, observe that if the sequence is sorted we can check the midpoint of the sequence against v and eliminate half of the sequence from further consideration. Give pseudocode for **binary search** and argue that its worst-case running time is Θ(lg n).

```javascript
const binarySearch = (nums, v) => {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (nums[mid] === v) {
      return mid;
    }

    if (nums[mid] < v) {
      left = mid + 1;
      continue;
    }

    right = mid - 1;
  }

  return null;
};
```

Each iteration halves the search space. Starting from n elements, after k iterations at most ⌈n/2ᵏ⌉ elements remain. The loop terminates when that count reaches 1, meaning k ≈ lg n iterations. Each iteration is Θ(1), so worst-case time is **Θ(lg n)**.

See also: [Binary Search pattern notes](../../patterns/binary_search.md).

---

### 2.3-6

> Can we use binary search to improve the worst-case running time of insertion sort to Θ(n lg n)?

**No.** Binary search can find the correct *position* to insert in Θ(lg n) instead of Θ(n). However, inserting still requires *shifting* all elements to the right of that position — which takes Θ(n) time in the worst case. Sorting n elements this way still gives Θ(n) · Θ(n) = **Θ(n²)** overall.

Binary search reduces comparisons, but insertion sort's bottleneck is the number of writes (shifts), not comparisons.

---

### 2.3-7

> Describe an Θ(n lg n) algorithm that, given a set S of n integers and another integer x, determines whether there exist two elements in S that sum to exactly x.

1. Sort S using merge sort: **Θ(n lg n)**.
2. For each element `s` in S, use binary search to look for `x - s` in S (excluding `s` itself): **Θ(n lg n)** total.

```javascript
const hasPairWithSum = (S, x) => {
  const sorted = [...S].sort((a, b) => a - b);

  for (let i = 0; i < sorted.length; i += 1) {
    const target = x - sorted[i];
    let left = 0;
    let right = sorted.length - 1;

    while (left <= right) {
      const mid = left + Math.floor((right - left) / 2);

      if (mid === i) {
        if (left === mid) left += 1;
        else right -= 1;
        continue;
      }

      if (sorted[mid] === target) return true;
      if (sorted[mid] < target) left = mid + 1;
      else right = mid - 1;
    }
  }

  return false;
};
```

Total: **Θ(n lg n)**.

*Note:* A hash-map solution runs in Θ(n) average time — see [Two Sum](../../problems/0001_two_sum.md).
