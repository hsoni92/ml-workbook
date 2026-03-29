# Variants of Gradient Descent – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Understand** three ways to run gradient descent: **batch**, **mini-batch**, and **stochastic (SGD)**.
2. **Compare** how they differ and what **trade-offs** they offer.
3. **Explain** why **mini-batch SGD** is the standard today.
4. **See** how **variance** (noise) in gradients affects optimization.

---

## Why Not Always Use the Full Dataset?

- For **small** datasets, computing the gradient on the **entire** dataset was feasible.
- **Modern** datasets often have **millions** of samples → one full gradient per update is **slow**, **expensive**, and **memory-intensive**.
- So we choose **how much data** to use per update. That choice gives **batch**, **stochastic**, and **mini-batch** gradient descent.

---

## Batch Gradient Descent

- Uses the **entire** dataset to compute **one** gradient update.
- **Pros:** Updates are **stable**, **smooth**, and point in a good direction.
- **Cons:** Very **slow** on large datasets, **memory-heavy**, and does not use GPU parallelism well.
- **Use:** Rarely in neural network training, except for small datasets or convex problems.

---

## Stochastic Gradient Descent (SGD)

- Updates the model using **one sample** at a time.
- **Pros:** Updates are **very fast**; the **noise** can help escape saddle points and sharp minima.
- **Cons:** Updates are **very noisy**; the loss can bounce around instead of decreasing smoothly; convergence is **harder to interpret**.
- **Use:** Useful for **online** or **streaming** settings; rarely used **alone** for full-batch training.

---

## Mini-Batch Gradient Descent

- Uses a **small batch** of samples (e.g. 32–512) per update.
- **Pros:** Good **GPU** parallelism, gradient estimate **stable enough**, **enough** noise to help generalization, and **much faster** than full-batch.
- **Why it’s default:** Balances **speed** and **stability**; this is the standard method for training neural networks.

---

## Effect of Batch Size

- **Small** batch (e.g. 16, 32): **Noisier** gradients; can improve **generalization** and help escape bad regions.
- **Large** batch (e.g. 1024+): **Smoother** gradients, but may converge to **sharp** minima and may need learning rate tuning or **warm-up**.
- For many tasks, batch sizes between **32** and **256** work well. Batch size is one of the most important **hyperparameters**.

---

## Summary

| Method       | Data per update | Stability     | Speed   |
|-------------|-----------------|---------------|---------|
| **Batch GD**   | Whole dataset   | Very stable   | Slow    |
| **SGD**        | One sample      | Noisy         | Very fast |
| **Mini-batch** | Small subset    | Fast & stable | Default |

- All variants differ only in **how much data** they use per update.
- **Mini-batch SGD** hits a good **trade-off** between speed and stability.
- **Batch size** affects convergence, generalization, and gradient noise. **Noise** is not always bad — sometimes it is what the optimizer needs to keep making progress.
