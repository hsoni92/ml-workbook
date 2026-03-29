# Numerical Stability in Neural Network Training – Artificial Neural Networks (Module 2)

## Learning Objectives

By the end of this video you will:

1. **Understand** why numerical stability is critical in deep learning computations.
2. **Identify** common numerical issues: **overflow** and **underflow**.
3. **Explain** the **log-sum-exp trick** used to stabilize exponential operations.
4. **Recognize** key practical techniques used for stable neural network training.

---

## Finite Precision in Practice

- So far we treated computations as **exact**. In reality, every computation on a computer uses **finite numerical precision**.
- Deep learning uses **exponentials**, **repeated multiplications**, and **very small probabilities**. This combination makes **numerical instability** not only possible but **common**.
- If numerical stability is ignored:
  - Models can produce **infinities**, **zeros**, or **NaNs**.
  - Training can **silently fail** with no obvious coding error.
  - Gradients can become zero or undefined, and the process may diverge or appear to converge without learning.

---

## Overflow

- **Overflow** occurs when a number is **too large** to be represented in the computer’s floating-point system.
- **Example:** \( e^{1000} \) is extremely large. On a typical machine it cannot be stored and is represented as **infinity**.
- Once **infinity** appears, subsequent operations become meaningless. This is one of the most dangerous failure modes in deep learning.

---

## Underflow

- **Underflow** is the opposite: a number becomes **so small** that it is rounded down to **exactly zero**.
- **Example:** \( e^{-1000} \) is a very small positive number mathematically, but in floating-point arithmetic it is stored as **zero**.
- When that happens, any gradient or probability information carried by that value is **permanently lost**.

---

## Why Deep Learning Is Especially Sensitive

1. **Long chains of multiplications** — small errors or extremes can amplify.
2. **Exponential functions** — values can grow or shrink very fast.
3. **Very small probabilities** — easily underflow to zero.

Each of these can cause numerical problems on its own; **together** they make stable numerical computation a **central concern** in all deep learning systems.

---

## Unstable Expression: Sum of Exponentials

A very common unstable expression is:

\[
\sum_i e^{z_i}
\]

- If **one** \( z_i \) is large → \( e^{z_i} \) can **overflow**.
- If **all** \( z_i \) are very negative → all \( e^{z_i} \) can **underflow** to zero.
- This expression appears inside **probability** computations (e.g. softmax), so it **must** be handled carefully.

---

## Log-Sum-Exp Trick (Stabilization)

**Identity (for any \( \alpha \)):**

\[
\log \left( \sum_i e^{z_i} \right) = \alpha + \log \left( \sum_i e^{z_i - \alpha} \right)
\]

**Derivation (outline):**

- \( \sum_i e^{z_i} = e^\alpha \sum_i \frac{e^{z_i}}{e^\alpha} = e^\alpha \sum_i e^{z_i - \alpha} \).
- Take log: \( \log \sum_i e^{z_i} = \alpha + \log \sum_i e^{z_i - \alpha} \).

**Choice of \( \alpha \):** Take \( \alpha = \max_i z_i \).

**Why this helps:**

- After subtracting the maximum, the **largest** exponent is \( e^0 = 1 \).
- All other terms are \( e^{z_i - \alpha} \in (0, 1] \).
- So no term is excessively large, and none shrink to zero too quickly. The computation stays in a **numerically safe** range for a wide variety of inputs.

---

## Other Practical Stabilization Techniques

- **Work in the log domain** when possible (e.g. log-probabilities).
- **Subtract the maximum** before exponentiation (as in log-sum-exp).
- **Add a small \( \varepsilon \)** to denominators to avoid **division by zero**.
- **Avoid** direct multiplication of **long chains of probabilities** (use sums of log-probabilities instead).

All practical deep learning systems rely heavily on these simple but critical numerical techniques.

---

## Consequences of Ignoring Numerical Stability

- Computations produce **NaNs** and **infinities**.
- Gradients can become **zero** or **undefined**.
- Training may **diverge** or **appear** to converge while learning nothing.
- These failures are often **silent** (no clear error message).

So **numerical stability is not optional** — it is a **fundamental requirement** for any reliable deep learning system.

---

## Summary (Quick Revision)

| Concept | Detail |
|---------|--------|
| **Precision** | All deep learning is done in **finite** numerical precision. |
| **Overflow** | Numbers too large → infinity → invalid computation. |
| **Underflow** | Numbers too small → zero → loss of information. |
| **Log-sum-exp** | Standard way to stabilize \( \log \sum_i e^{z_i} \) by using \( \alpha = \max_i z_i \). |
| **Stable computation** | Required for reliable deep learning; use log domain, subtract max, small \( \varepsilon \), avoid long probability chains. |

> **Exam tip:** Log-sum-exp trick: use \( \alpha = \max_i z_i \) so that \( e^{z_i - \alpha} \le 1 \) and no overflow/underflow; then \( \log \sum e^{z_i} = \alpha + \log \sum e^{z_i - \alpha} \).
