# Optimisation Pitfalls – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Identify** common **optimization pitfalls** when training neural networks.
2. **Understand** why loss may **stagnate** or behave **erratically**.
3. **Recognize** these issues and build intuition for **diagnosing** training problems.

---

## When Training Goes Wrong

- Training does not always **explode** or **crash**. Often it **starts** normally, then **slows**, **stalls**, or **fluctuates** without clear improvement.
- These issues are often due to **optimization** challenges rather than code bugs or data problems.

---

## Saddle Points

- A **saddle point** is a region where the **gradient** is close to **zero** but the point is **not** a minimum (like the shape of a horse saddle).
- In **high-dimensional** spaces, saddle points are **far more common** than local minima.
- Optimizers can **get stuck** or move **very slowly** near saddle points, so it can look like training has converged when it has **not**.

---

## Plateaus

- **Plateaus** are regions of the loss surface that are **very flat**; gradients are **tiny** and learning progresses **very slowly**.
- Training may look **stuck** even though the optimizer is still making (very small) progress.
- Plateaus are common in **deep** networks and in models with **saturating** activation functions.

---

## Noisy Updates (Mini-Batch)

- **Mini-batch** training adds **randomness** to gradient updates.
- **Helpful:** Noise can let the optimizer **escape** saddle points.
- **Cost:** Loss can **fluctuate**, making convergence **harder to interpret**. Understanding this **trade-off** is important when diagnosing training.

---

## Poor Conditioning

- **Poor conditioning** means the loss surface has **very different** curvature in different directions: some directions **steep**, others **nearly flat**.
- This causes **zigzag** updates, **slow** progress, and **high** sensitivity to the learning rate.
- **Momentum**, **adaptive** optimizers, and **normalization** help address this.

---

## Optimization vs Modeling Problems

- **Loss does not decrease** or behaves **erratically** → usually an **optimization** issue (learning rate, optimizer, conditioning, etc.).
- **Loss decreases** but **performance** is poor → more likely **model capacity** or **data** (architecture, labels, features). This distinction helps decide **what** to fix.

---

## How to Respond

- When you hit optimization issues, possible responses: **adjust** learning rate, **switch** optimizer, **add** momentum or **gradient clipping**, or **improve** initialization. These target **training dynamics**, not the model architecture.

---

## Summary

- **Optimization** issues are common in neural network training.
- **Saddle points** and **plateaus** slow learning.
- **Noise** (e.g. from mini-batch) affects convergence behaviour.
- **Poor conditioning** leads to inefficient updates.
- **Diagnosing** these issues is an essential skill.
