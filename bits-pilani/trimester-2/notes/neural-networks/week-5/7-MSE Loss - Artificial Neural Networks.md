# MSE Loss – Artificial Neural Networks (Module 5)

## Learning Objectives

By the end of this video you will:

1. **Understand** why we need **loss functions** in training.
2. **State** what **MSE** measures and why it fits **regression**.
3. **See** that MSE is the default for regression but **not** ideal for classification.

---

## Why We Need a Loss Function

- When the network makes a prediction, we need a **single number** that says how good or bad it is.
- The **loss function** provides that number: how wrong the model is.
- During training, **backpropagation** uses this number to compute **gradients** and update weights. Different **tasks** need different loss functions.

---

## Mean Squared Error (MSE)

**Definition:**
$$
\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2
$$
- $\hat{y}$: predicted value; $y$: true value.
- We take the **error** $(y - \hat{y})$, **square** it, and **average** over examples.
- Result: a **smooth**, **non-negative** measure of how far predictions are from the truth.

---

## Geometric View

- MSE measures the **squared distance** between the true point and the predicted point (in output space).
- In **regression**, where predictions are on a **continuous** scale, we want the network to place predictions as **close as possible** to the true value — MSE does exactly that.
- **Squaring** penalizes **large** errors more than small ones and yields **smooth** gradients.

---

## When to Use MSE

- **Default loss for regression** when the output is a **continuous** value (e.g. house prices).
- It directly measures **distance** in numerical space.
- For **classification**, MSE behaves **poorly**; we will see a better choice (cross-entropy) in the next video.

---

## Summary

- We need loss functions to **quantify error** during training.
- **MSE** = average **squared** distance between prediction and truth.
- Squaring **heavily** penalizes large errors and gives smooth gradients.
- MSE is **ideal for regression** but **not** for classification.
