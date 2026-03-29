# Optimisation Algorithms – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Understand** the role of **optimization** in training deep neural networks.
2. **See** that **gradients alone** do not tell the network how to update parameters — the **optimizer** does.
3. **Recognize** how optimization affects **speed**, **stability**, and **convergence** of training.

---

## Where We Are

- We know how networks **compute predictions** (forward pass) and **gradients** (backpropagation).
- **Gradients** tell us the direction and sensitivity of the loss w.r.t. parameters.
- **Optimization** decides **how** to use those gradients: step size, direction, and update rule.

---

## What Optimization Controls

- **How fast** the network learns.
- **How large** the updates are (step size).
- **Which direction** we move in (and whether we smooth it, e.g. with momentum).
- **Whether** training **converges** or diverges.
- **How** we avoid bad regions (e.g. saddle points, sharp minima).

---

## Why It Matters

- A **poor** optimizer can make learning **very slow** or cause **divergence**.
- **Backpropagation** gives gradients; **optimization** decides how to apply them.
- **Good** optimization → faster convergence and better performance.
- **Poor** optimization → slow learning, divergence, or getting stuck on plateaus.
- Modern breakthroughs in neural network training rely on **strong** optimization techniques.

---

## What This Module Covers

- **Foundations:** Gradient descent, role of **learning rate**, effect of **batch size**, how **momentum** smooths updates.
- **Adaptive optimizers:** **RMSProp** and **Adam** (per-parameter learning rates).
- **Learning rate scheduling:** e.g. cosine annealing, step decay, warm-up.
- **Challenges:** Noisy gradients, saddle points, exploding updates; **practical** tools like **gradient clipping** and **optimizer selection**.

---

## Takeaway

- By the end of this module you will have a solid **toolkit** to make deep learning models **converge faster**, more **smoothly**, and more **reliably**.
