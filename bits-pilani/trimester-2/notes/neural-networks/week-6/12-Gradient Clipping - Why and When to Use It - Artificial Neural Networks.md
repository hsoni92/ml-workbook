# Gradient Clipping – Why and When to Use It – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Understand** what **gradient clipping** is and why **exploding** gradients can break training.
2. **Identify** when gradient clipping is **useful** in practice.
3. **Distinguish** clipping by **value** vs clipping by **norm**.

---

## The Problem: Exploding Gradients

- In deep networks, gradients can sometimes grow **extremely large**.
- When that happens: parameter updates become **huge**, the loss can **spike**, and training can become **unstable** or **crash** (e.g. NaN).
- Exploding gradients are common in **RNNs**, **very deep** models, and **early** training when parameters are poorly initialized. **One** bad update can ruin an otherwise stable run.

---

## What Gradient Clipping Does

- **Before** applying an update, we check the **size** of the gradient.
- If it is within a **reasonable** range → leave it **unchanged**.
- If it is **too large** → **scale it down**.
- So **no single** update can be catastrophically large. Clipping **limits** the magnitude of updates **without** changing the overall optimization process: it prevents sudden jumps, **stabilizes** training when gradients spike, and lets learning **continue** instead of diverging.

---

## Gradient Clipping Is a Safeguard

- Clipping is **not** a cure-all; it is a **safety** mechanism, not a replacement for good optimization (learning rate, initialization, etc.).

---

## Two Types of Clipping

1. **Clipping by value:** Limit **each** gradient component to a fixed range (e.g. $[-c, c]$). **Simple**, but can **distort** the **direction** of the gradient.
2. **Clipping by norm (most common):** If the **norm** of the whole gradient vector exceeds a threshold, **scale** the entire vector down. This **preserves direction** while **limiting magnitude**.

---

## When to Use Gradient Clipping

- Most useful when training is **unstable**: e.g. **recurrent** models, **very deep** networks, or **large** learning rates.
- If you see **sudden** loss spikes or **exploding** gradients early in training, clipping can help **stabilize** the process.
- **Well-behaved** models may **not** need gradient clipping at all.

---

## What Clipping Does Not Do

- It does **not** improve **generalization**.
- It does **not** fix **vanishing** gradients.
- It does **not** replace good **learning rate** or **initialization** choices.
- It **only** prevents **extreme** updates; it does **not** solve deeper optimization issues.

---

## Summary

- **Exploding** gradients cause **unstable** training.
- **Gradient clipping** limits the **magnitude** of updates.
- **Norm-based** clipping is most common and preserves **direction**.
- It acts as a **safety** mechanism in unstable settings and should be **combined** with good optimization practices.
