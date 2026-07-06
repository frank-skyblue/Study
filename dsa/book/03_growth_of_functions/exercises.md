# Chapter 3 Exercises

[← Back to CLRS Index](../index.md) · [← Back to DSA Index](../../index.md)

Notes: [Chapter 3 Notes](./notes.md)

---

## 3.1

### 3.1-1

> Let f(n) and g(n) be asymptotically nonneg functions. Show that max(f(n), g(n)) = Θ(f(n) + g(n)).

We need to show c₁·(f+g) ≤ max(f,g) ≤ c₂·(f+g) for large n.

**Upper bound:** max(f,g) ≤ f + g, so c₂ = 1 works.

**Lower bound:** max(f,g) ≥ f/2 and max(f,g) ≥ g/2, so:

$$
\max(f,g) \geq \frac{f + g}{2}
$$

Therefore c₁ = 1/2 works. Combined: max(f,g) = Θ(f + g). ∎

---

### 3.1-2

> Show that for any real constants a and b with b > 0, (n + a)^b = Θ(n^b).

For large enough n, |a| ≤ n/2, so:

$$
\frac{n}{2} \leq n + a \leq \frac{3n}{2}
$$

Raising to the bth power (b > 0 preserves inequality direction):

$$
\left(\frac{1}{2}\right)^b n^b \leq (n+a)^b \leq \left(\frac{3}{2}\right)^b n^b
$$

Both bounding constants are positive, so (n+a)^b = Θ(n^b). ∎

---

### 3.1-3

> Explain why the statement "the running time of algorithm A is at least O(n²)" is meaningless.

O(n²) is an upper bound — it says the running time grows *at most* as fast as n². Saying "at least O(n²)" says "at least at most n²" which is contradictory and conveys no useful information. The correct statement would use Ω(n²) to say the running time grows *at least* as fast as n².

---

### 3.1-4

> Is 2^(n+1) = O(2^n)? Is 2^(2n) = O(2^n)?

**2^(n+1) = O(2^n):** Yes. 2^(n+1) = 2 · 2^n, so c = 2 satisfies 2^(n+1) ≤ c · 2^n for all n ≥ 1.

**2^(2n) = O(2^n):** No. 2^(2n) = (2^n)², so 2^(2n) / 2^n = 2^n → ∞. No constant c can bound this ratio, so 2^(2n) ≠ O(2^n).

---

### 3.1-5

> Prove Theorem 3.1: f(n) = Θ(g(n)) iff f(n) = O(g(n)) and f(n) = Ω(g(n)).

**(⟹)** If f = Θ(g), then by definition ∃ c₁, c₂, n₀ with c₁·g ≤ f ≤ c₂·g for n ≥ n₀.
- The right inequality f ≤ c₂·g gives f = O(g).
- The left inequality c₁·g ≤ f gives f = Ω(g). ∎

**(⟸)** If f = O(g), then ∃ c₂, n₁ with f ≤ c₂·g for n ≥ n₁. If f = Ω(g), then ∃ c₁, n₂ with c₁·g ≤ f for n ≥ n₂. Take n₀ = max(n₁, n₂). Then c₁·g ≤ f ≤ c₂·g for all n ≥ n₀, so f = Θ(g). ∎

---

### 3.1-6

> Prove that the running time of an algorithm is Θ(g(n)) iff its worst-case running time is O(g(n)) and its best-case running time is Ω(g(n)).

The worst-case running time T_worst(n) = O(g(n)) means every input of size n takes at most c·g(n) steps — i.e., T(n) ≤ c₂·g(n).

The best-case running time T_best(n) = Ω(g(n)) means some input of size n requires at least c·g(n) steps — i.e., T(n) ≥ c₁·g(n).

Since T_best(n) ≤ T(n) ≤ T_worst(n), combining both bounds gives c₁·g(n) ≤ T(n) ≤ c₂·g(n), which is exactly Θ(g(n)). ∎

---

### 3.1-7

> Prove that o(g(n)) ∩ ω(g(n)) is the empty set.

Suppose f ∈ o(g) ∩ ω(g). Then:
- f ∈ o(g) ⟹ f(n)/g(n) → 0 as n → ∞.
- f ∈ ω(g) ⟹ f(n)/g(n) → ∞ as n → ∞.

A function cannot have both limits simultaneously, so no such f exists. ∎

---

### 3.1-8

> Extend asymptotic notation to functions of two variables.

O(g(m,n)) = { f(m,n) : ∃ positive constants c, m₀, n₀ such that 0 ≤ f(m,n) ≤ c·g(m,n) for all m ≥ m₀ or n ≥ n₀ }.

Ω and Θ extend analogously.

**Use case:** Graph algorithms where complexity depends on both V (vertices) and E (edges), e.g., Dijkstra runs in O((V + E) lg V).

---

## 3.2

### 3.2-1

> Show that if f(n) and g(n) are monotonically increasing functions, then so are f(n) + g(n) and f(g(n)).

**f + g:** If m ≤ n, then f(m) ≤ f(n) and g(m) ≤ g(n), so f(m)+g(m) ≤ f(n)+g(n). ∎

**f(g(n)):** If m ≤ n, then g(m) ≤ g(n) because g is monotonically increasing. Then f(g(m)) ≤ f(g(n)) because f is monotonically increasing and g(m) ≤ g(n). ∎

---

### 3.2-2

> Prove that ⌈lg n⌉! is polynomially bounded.

We need to show ⌈lg n⌉! = O(nᵏ) for some constant k.

Using lg(n!) = Θ(n lg n) (from Stirling), we get:

$$
\lg(\lceil \lg n \rceil !) = \Theta(\lceil \lg n \rceil \cdot \lg \lceil \lg n \rceil) = O(\lg n \cdot \lg \lg n)
$$

Since lg n · lg lg n = o(lg² n) = o(lg n²), this is O(k · lg n) for a suitable k.

Therefore ⌈lg n⌉! = O(2^(k lg n)) = O(nᵏ) — it is polynomially bounded. ∎

---

### 3.2-3

> Is lg(n!) = Θ(n lg n)? Is n! = ω(2^n)?

**lg(n!) = Θ(n lg n):** Yes, from Stirling's approximation: lg(n!) = Σ lg k ≈ ∫₁ⁿ lg x dx = Θ(n lg n).

**n! = ω(2^n):** Yes. n! / 2^n = ∏(k/2) for k=1..n. For n ≥ 4, more than half the terms exceed 1 and grow without bound, so the ratio → ∞.

---

### 3.2-4

> Prove or disprove: 2^⌈lg n⌉ = Θ(n).

**True.** Since lg n ≤ ⌈lg n⌉ < lg n + 1:

$$
2^{\lg n} \leq 2^{\lceil \lg n \rceil} < 2^{\lg n + 1} = 2n
$$

And 2^(lg n) = n, so n ≤ 2^⌈lg n⌉ < 2n. This gives c₁ = 1, c₂ = 2, confirming 2^⌈lg n⌉ = Θ(n). ∎
