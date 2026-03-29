# Why Adaptive Methods Were Needed – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Understand** limitations of **SGD** and **momentum** (single learning rate for all parameters).
2. **See** challenges from **sparse** and **noisy** gradients.
3. **Explain** the motivation for **adaptive** optimizers like **RMSProp** and **Adam**.

---

## Single Learning Rate for All Parameters

- **SGD** uses **one global** learning rate for **all** parameters.
- But parameters **behave differently**: some are very sensitive, some barely affect the loss; some need **large** steps, others **tiny** ones.
- Forcing **one** learning rate on all parameters → some learn **too slowly**, others become **unstable**. This mismatch gets worse as networks get **deeper** and parameter scales **diverge**.

---

## Sparse Data and Sparse Gradients

- In **NLP**, recommender systems, and high-dimensional sparse inputs, many features are **zero** most of the time.
- Their weights get **very infrequent** gradients.
- **SGD** treats all weights the same, so **rarely** updated weights move very little — they learn at a **fraction** of the speed of frequently updated ones.
- **Adaptive** optimizers give each parameter an **effective** learning rate so that **rare** gradients can still have a meaningful impact.

---

## Variable Gradient Magnitudes Across Layers

- In deep networks, gradient **magnitudes** can vary a lot **across layers**.
- **Mini-batch** SGD adds **noise**. With a **single** learning rate, parameters with **large** gradients may **overshoot**, while those with **small** gradients **barely** move.
- We need **per-parameter** step sizes based on **gradient history**. Adaptive methods do exactly that: they use **past** gradients to **adjust** the step size automatically.

---

## Plateaus and Saddle Points

- Even with **momentum**, SGD struggles on **plateaus** (gradient near zero) and **saddle points** (flat in one direction, steep in another).
- **Large** learning rate → divergence; **small** learning rate → very slow learning.
- We want a method that **adapts** step size to **curvature** and **gradient consistency**. Adaptive optimizers **approximate** this by using **gradient statistics** to tune the learning rate.

---

## What Adaptive Methods Do

- They address one main limitation of SGD: **different parameters need different learning rates**.
- Adaptive optimizers compute **per-parameter** learning rates from **gradient history**.
- **Noisy** parameters get **dampened** updates; **sparse** parameters get **boosted** updates; **stable** directions get **accelerated** updates. Each parameter learns at a **speed that fits** its own behaviour.

---

## Summary

- **SGD** and **momentum** are limited by using **one** learning rate for **all** parameters.
- Deep networks need **different** step sizes across parameters and layers.
- **Sparse** gradients, **noisy** gradients, and **varying** curvature all make plain SGD behave poorly.
- **Adaptive** optimizers (e.g. RMSProp, Adam) were designed to address these issues.
