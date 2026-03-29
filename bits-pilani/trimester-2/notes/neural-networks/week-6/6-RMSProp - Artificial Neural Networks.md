# RMSProp – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Understand** the intuition behind **RMSProp** and how it **adapts** learning rates automatically.
2. **See** why it works better than plain SGD in **noisy** and **unbalanced** gradient settings.
3. **State** the **update rule** that powers RMSProp.

---

## The Problem

- In deep networks, **not all** parameters behave the same: some get **large** gradients, others **small** or **infrequent** ones.
- With a **single** learning rate: parameters with **large** gradients can **overshoot** and destabilize; those with **small** gradients **barely** move and learn slowly.
- **SGD** has no built-in way to handle this imbalance. **RMSProp** was designed to address it.

---

## Core Idea

- **RMSProp** keeps a **running average** of how **large** the gradients have been **recently** for each parameter.
- If a parameter **consistently** sees **large** gradients → RMSProp **reduces** its effective step size.
- If it sees **small** gradients → RMSProp **increases** its effective learning rate.
- So instead of **one global** learning rate, each parameter gets a **dynamically adjusted** step size. This **balances** learning across parameters, **dampens** unstable directions, **boosts** slow ones, and **smooths** updates when gradients are noisy or sparse.

---

## Update Rule

**Running average of squared gradients:**
\[
v_t = \beta \cdot v_{t-1} + (1 - \beta) \cdot g_t^2
\]
This captures how large the gradients have been recently.

**Parameter update:**
\[
\theta_t = \theta_{t-1} - \frac{\eta}{\sqrt{v_t} + \epsilon} \cdot g_t
\]

- **Key:** The **denominator** scales the step. When gradients are **large**, \( v_t \) is large → **smaller** updates. When gradients are **small**, \( v_t \) is small → **larger** updates. So RMSProp **adapts** the learning rate automatically per parameter.

---

## Why RMSProp Works Well

- **Reduces** oscillations in steep directions → more **stable** training.
- Handles **noisy** mini-batch gradients well.
- Lets parameters with **sparse** gradients learn **faster**.
- **Continuously** adjusts learning rate during training.
- It became popular for **RNNs** and early deep models where gradient instability was a major issue.

---

## Practical Defaults

- **\( \beta \approx 0.9 \)** (for the running average).
- **\( \eta \approx 0.001 \)** (learning rate).
- **\( \epsilon \approx 10^{-8} \)** (numerical stability).
- These often work with **little** tuning, which made RMSProp attractive in practice.

---

## Limitation

- RMSProp **adapts** learning rates but does **not** explicitly use **momentum** (moving average of gradients).
- So it can still move **slowly** in directions where gradients are **consistent but small**. This limitation led to **Adam**, which combines RMSProp with **momentum**.

---

## Summary

- **RMSProp** adapts learning rates **per parameter** using **squared** gradients.
- It **reduces** step size where gradients are large/noisy and **boosts** it where they are small.
- This **stabilizes** training and **speeds up** convergence; RMSProp laid the foundation for **Adam**, one of the most widely used optimizers today.
