# Adaptive vs Scheduled LR – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Distinguish** clearly between **adaptive** and **scheduled** learning rates.
2. **Understand** the **strengths** and **limitations** of each.
3. **Choose** between them (or combine them) in real training scenarios.

---

## Two Ways to Control Learning Rates

1. **Adaptive learning rates:** The **optimizer** automatically adjusts step size **per parameter** based on **gradient history** (e.g. RMSProp, Adam).
2. **Scheduled learning rates:** We **explicitly** change the learning rate **over time** with a **predefined** schedule (e.g. step decay, cosine annealing, warm-up).

Both aim to choose the **right** step size, but in **different** ways.

---

## Adaptive Optimizers (e.g. Adam)

- **Strengths:** Very effective in **early** training; handle **noisy** and **sparse** gradients; need **little** tuning; **fast** convergence. Because each parameter has its own effective learning rate, they are **robust** when gradient magnitudes **vary** across layers. Good **default** when starting training or trying new architectures.
- **Limitations:** Can converge to **sharp** minima that **generalize** worse; give **less** explicit control over learning dynamics, especially **later** in training. So they are **not** always ideal for **fine-tuning** or squeezing out the **best** final performance.

---

## Scheduled Learning Rates

- **Strengths:** **Precise** control over how step size **changes over time**; especially useful in **later** stages when **fine-tuning** matters.
- **Use:** When training is **stable** and you care about **final** performance.

---

## Combining Both

- Many pipelines **combine** the two:
  - **Adam with fixed LR:** Simple, fast baseline.
  - **Adam with LR schedule:** Better **stability** and convergence.
  - **Adam first** for fast, stable progress → then **switch** to **SGD with momentum** and an **LR schedule** for fine-tuning. This uses the strengths of **both** adaptive and scheduled methods.

---

## Rule of Thumb

- **Use adaptive** optimizers when training is **difficult**, **noisy**, or **exploratory**.
- **Use scheduled** learning rates when training is **stable** and you care about **final** performance.
- There is **no** universal best; the right choice depends on **model**, **data**, and **goals**.

---

## Summary

- **Adaptive** methods adjust learning rates **per parameter** automatically.
- **Scheduled** methods **explicitly** control step size **over time**.
- **Adaptive** methods are **fast** and **robust** early; **scheduled** methods give **better control** and often **better** final results.
- **Combining** both is **common** and **effective**.
