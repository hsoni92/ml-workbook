# Why Fixed LR is Limiting – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Understand** why a **single fixed** learning rate throughout training is often **suboptimal**.
2. **See** how the **needs** of training **change over time**.
3. **Explain** why **adapting** the learning rate helps both **speed** and **stability**.

---

## What the Learning Rate Controls

- The learning rate controls **how big** a step the optimizer takes at each update.
- It affects **how fast** the model learns, **how stable** training is, and **whether** the model converges at all.
- With a **fixed** learning rate we assume the **same** step size is right at **every** stage — from the first update to the last. In practice this is **rarely** true.

---

## Early vs Late Training

- **Early:** Model is **far** from the optimum; gradients are usually **large**; **bigger** steps help make **rapid** progress.
- **Later:** Model is **close** to a minimum; gradients are **smaller**; **large** steps can cause **oscillation** or prevent convergence.
- So the learning rate we want **early** is **different** from the one we want **near the end**.

---

## Failure Modes

**Learning rate too large:**
- Optimizer **overshoots** the minimum; updates keep **bouncing**; loss may **oscillate** or **increase**; training can become **unstable** or **diverge**. Often looks like a loss curve that **refuses** to decrease smoothly.

**Learning rate too small:**
- Training is **very slow**; tiny progress per step; the model **struggles** on flat regions and **wastes** computation. Stable but **inefficient** and often **impractical** for large models.

---

## The Compromise Problem

- A **fixed** learning rate forces a **bad** compromise:
  - **Large** LR → fast start, **poor** finish.
  - **Small** LR → stable but **very slow**.
- What we **want**: **large** steps **early** (exploration) and **small** steps **later** (fine-tuning). A **fixed** learning rate **cannot** satisfy both.

---

## Learning Rate Scheduling

- **Instead** of keeping the learning rate constant, we **change it over time** to match the phase of training.
- **Scheduling** allows: **fast** initial learning, **smoother** convergence later, and **better** final performance.
- This idea is **widely** used in modern neural network training.

---

## Summary

- The learning rate controls **how big** each update is.
- Training has **different phases** with **different** needs.
- A **single fixed** learning rate is a **poor** compromise.
- **Adjusting** the learning rate over time improves both **speed** and **stability** and motivates **learning rate schedules**.
