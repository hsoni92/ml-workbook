# What is Optimisation – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Define** what optimization means in neural networks.
2. **Understand** the **goal** of training and what the **optimizer** controls.
3. **See** the role of **weights and biases** in training.
4. **Explain** why optimization is **more than** just computing gradients.

---

## Goal of Training

- When we train a neural network, the main objective is to **minimize the loss**.
- The loss measures how far the model’s predictions are from the correct output.
- **Optimization** = finding values of **weights and biases** that make the loss as **small as possible**.
- The optimizer explores different parameter combinations and tries to move the model into a region where it performs well.

---

## The Loss Surface

- A network has many parameters (thousands or millions), so the loss is not a simple curve but a **high-dimensional surface**.
- This **landscape** has valleys, hills, plateaus, ridges, and **saddle points**.
- There can be **local minima** and (ideally) a **global minimum**.
- **Optimization** = navigating this landscape efficiently, avoiding bad regions that slow or block learning.

---

## Why Optimization Is Tricky

- Real loss surfaces are **difficult**: high-dimensional, gradients can be **noisy** or inconsistent.
- Some regions are **nearly flat** (plateaus); others are **very steep**.
- **Poor** learning rate choices can make training very slow or **unstable**.
- Optimization is **not** just “apply the formula” — it requires **strategies** that help the model navigate this terrain.

---

## What the Optimizer Controls

1. **Step size** — the **learning rate**.
2. **Directional smoothing** — e.g. **momentum**.
3. **Per-parameter** adjustments — **adaptive** optimizers (e.g. RMSProp, Adam).
4. **Stability** — e.g. **gradient clipping**, normalization.

Together, these choices determine **convergence speed**, **final accuracy**, and **training stability** — i.e. how **fast** and how **reliably** the model learns.

---

## Summary

- **Optimization** = adjusting parameters to **minimize** the loss.
- Loss surfaces are **highly complex**; a good **strategy** is essential.
- **Learning rate**, **momentum**, and **adaptive** updates all shape training dynamics.
- These ideas form the foundation for the rest of this module.
