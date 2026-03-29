# Popular LR Schedules – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Understand** why learning rate **schedules** are used in practice.
2. **Identify** commonly used strategies: **step decay**, **exponential decay**, **cosine annealing**, **warm-up**.
3. **Describe** how they work at a high level and **when** each is typically used.

---

## What Is a Learning Rate Schedule?

- A **schedule** defines how the learning rate **changes** as training progresses.
- Instead of keeping it **constant**, we often **start** with a relatively **large** value and **gradually reduce** it.
- **Idea:** Training needs **large** steps early and **smaller**, more precise steps later. Schedules **match** step size to the current phase.

---

## Step Decay

- Learning rate **stays constant** for a while, then **drops** at predefined steps/epochs.
- Example: 0.1 for first 30 epochs, then 0.01, then 0.001.
- **Pros:** Early training gets large steps; later training gets smaller, more stable updates.
- **Cons:** You must choose **when** and **how much** to decay; may need tuning.

---

## Exponential Decay

- Learning rate **decreases smoothly** over time; at each step or epoch it is **multiplied** by a fixed factor.
- **Pros:** Smooth, predictable decay.
- **Cons:** If decay is too **aggressive**, the learning rate can become **too small too early** and slow training.

---

## Cosine Annealing

- Learning rate follows a **cosine-shaped** curve: starts **high**, decreases **smoothly**, becomes **very small** near the end.
- **Pros:** Smooth transition, avoids sudden changes in dynamics; very **popular**, especially for **large** models; often used with **warm restarts**.
- **Cons:** None major; widely used in modern deep learning.

---

## Warm-up

- At the **start** of training, instead of a large learning rate, we **start small** and **gradually increase** it over a few steps or epochs.
- **Why:** Reduces **unstable** updates early; especially important for **large batch sizes** and **transformers**.
- After warm-up, we typically switch to another schedule (e.g. **cosine** or **step** decay).

---

## Combined Pattern

- A common pattern: **short warm-up** → **main** decay schedule (e.g. cosine annealing or step decay).
- This gives **stability** at the start, **fast** progress in the middle, and **precise** fine-tuning near the end.

---

## Which Schedule to Use?

- **No single best** schedule for all problems.
- **Step decay:** Simple; works well for many **CNN**-based models.
- **Exponential decay:** When you want **smooth** reduction.
- **Cosine annealing:** Popular in **modern** deep learning and **large-scale** training.
- **Warm-up:** Almost **mandatory** for **transformers** and **large-batch** training.
- The right choice depends on **model**, **data**, and **training** setup.

---

## Summary

- Learning rate **schedules** adjust step size **over time**.
- **Step decay**, **cosine annealing**, and **warm-up** are widely used.
- **Scheduling** almost always improves **training stability** and **convergence**.
