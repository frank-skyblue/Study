# Chapter 3 — Growth of Functions

[← Back to CLRS Index](../index.md) · [← Back to DSA Index](../../index.md)

Exercises: [3.1](./exercises.md#31) · [3.2](./exercises.md#32)

Related: [Divide and Conquer](../04_divide_and_conquer/notes.md) · [Dynamic Programming](../../patterns/dynamic_programming.md)

---

## 3.1 Asymptotic Notation

Asymptotic notation describes how a function behaves as n → ∞, ignoring constants and lower-order terms. The five notations form a vocabulary for comparing algorithm efficiency.

### Θ — Tight Bound

> Θ(g(n)) = { f(n) : ∃ positive constants c₁, c₂, n₀ such that 0 ≤ c₁·g(n) ≤ f(n) ≤ c₂·g(n) for all n ≥ n₀ }

f(n) = Θ(g(n)) means g(n) is simultaneously an upper and lower bound for f(n). It "sandwiches" f.

**Example:** f(n) = 3n² + 14n = Θ(n²) because for large n, c₁·n² ≤ 3n² + 14n ≤ c₂·n².

### O — Upper Bound (Big-Oh)

> O(g(n)) = { f(n) : ∃ positive constants c, n₀ such that 0 ≤ f(n) ≤ c·g(n) for all n ≥ n₀ }

f(n) = O(g(n)) means f grows **at most as fast** as g. This is the bound most commonly stated in practice.

**Example:** Insertion sort worst case is O(n²). It is also O(n³), O(2ⁿ) — O sets an upper limit, not a tight one.

### Ω — Lower Bound

> Ω(g(n)) = { f(n) : ∃ positive constants c, n₀ such that 0 ≤ c·g(n) ≤ f(n) for all n ≥ n₀ }

f(n) = Ω(g(n)) means f grows **at least as fast** as g.

**Example:** Insertion sort is Ω(n) because even in the best case it must examine all n elements.

### Theorem: Θ iff O and Ω

$$
f(n) = \Theta(g(n)) \iff f(n) = O(g(n)) \text{ and } f(n) = \Omega(g(n))
$$

### o — Strict Upper Bound (little-oh)

> o(g(n)): f grows **strictly slower** than g. The ratio f(n)/g(n) → 0 as n → ∞.

**Example:** n = o(n²) because n/n² = 1/n → 0.

### ω — Strict Lower Bound (little-omega)

> ω(g(n)): f grows **strictly faster** than g. The ratio f(n)/g(n) → ∞ as n → ∞.

**Example:** n² = ω(n) because n²/n = n → ∞.

### Summary Table

| Notation | Intuition | Relation f vs g | Limit |
| --- | --- | --- | --- |
| Θ(g) | Tight bound | f ≈ g | 0 < lim f/g < ∞ |
| O(g) | Upper bound | f ≤ g | lim f/g < ∞ |
| Ω(g) | Lower bound | f ≥ g | lim f/g > 0 |
| o(g) | Strict upper | f ≪ g | lim f/g = 0 |
| ω(g) | Strict lower | f ≫ g | lim f/g = ∞ |

### Asymptotic Properties

| Property | Statement |
| --- | --- |
| **Transitivity** | f = Θ(g), g = Θ(h) ⟹ f = Θ(h). Same for O, Ω, o, ω. |
| **Reflexivity** | f = Θ(f), f = O(f), f = Ω(f). |
| **Symmetry** | f = Θ(g) ⟺ g = Θ(f). |
| **Transpose symmetry** | f = O(g) ⟺ g = Ω(f). |

---

## 3.2 Standard Notations and Common Functions

### Monotonicity

A function f is **monotonically increasing** if m ≤ n ⟹ f(m) ≤ f(n), and **strictly increasing** if m < n ⟹ f(m) < f(n).

### Floors and Ceilings

$$
\lfloor x \rfloor \leq x \leq \lceil x \rceil, \quad \lceil x \rceil - \lfloor x \rfloor \leq 1
$$

In algorithm analysis, floor and ceiling differences do not affect asymptotic class.

### Modular Arithmetic

$$
a \mod n = a - n \lfloor a/n \rfloor
$$

### Polynomials

A polynomial p(n) = Θ(nᵈ) where d is the degree. Any polynomial is dominated by any exponential: for b > 1, nᵏ = o(bⁿ).

### Logarithms

Key identities used in analysis:

$$
\lg(mn) = \lg m + \lg n \qquad \lg(m/n) = \lg m - \lg n \qquad \lg(n^k) = k \lg n
$$

$$
a^{\log_b n} = n^{\log_b a}
$$

Change of base: log_b(n) = lg(n) / lg(b), so all logarithm bases are asymptotically equivalent (differ only by a constant factor).

Any polylogarithm grows slower than any polynomial: lgᵏ n = o(nᵉ) for any k > 0 and ε > 0.

### Exponentials

Any exponential with base > 1 eventually dominates any polynomial:

$$
n^k = o(b^n) \quad \text{for } b > 1, k > 0
$$

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots
$$

### Factorials

Stirling's approximation:

$$
n! = \sqrt{2\pi n} \left(\frac{n}{e}\right)^n \left(1 + \Theta\!\left(\frac{1}{n}\right)\right)
$$

From this: n! = o(nⁿ) and n! = ω(2ⁿ). Also lg(n!) = Θ(n lg n).

### Iterated Logarithm

lg\* n (log star) = minimum number of times you apply lg before the result ≤ 1.

$$
\lg^* 2 = 1, \quad \lg^* 4 = 2, \quad \lg^* 16 = 3, \quad \lg^* 65536 = 4, \quad \lg^*(2^{65536}) = 5
$$

Grows extremely slowly — for all practical values of n, lg\* n ≤ 5. Appears in algorithms like union-find with path compression.

### Fibonacci Numbers

$$
F_n = F_{n-1} + F_{n-2}, \quad F_0 = 0, F_1 = 1
$$

Closed form (Binet's formula):

$$
F_n = \frac{\phi^n - \hat\phi^n}{\sqrt{5}}, \quad \phi = \frac{1+\sqrt5}{2} \approx 1.618
$$

Because |φ̂| < 1, Fₙ = Θ(φⁿ/√5) — Fibonacci numbers grow exponentially.

---

## Key Takeaways

- Θ is the most informative bound; O is the most commonly stated (since worst-case upper bounds are easiest to prove).
- All log bases are asymptotically equivalent — only the exponent or function class matters.
- Growth hierarchy (slowest to fastest): 1, lg\* n, lg n, lgᵏ n, √n, n, n lg n, n², n³, …, 2ⁿ, n!
- Constants and lower-order terms never affect asymptotic class but do matter for practical performance at small n.
