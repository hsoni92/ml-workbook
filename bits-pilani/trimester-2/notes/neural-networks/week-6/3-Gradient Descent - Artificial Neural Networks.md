# Gradient Descent – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Explain** the intuition behind **gradient descent**.
2. **Interpret** what the **gradient** represents.
3. **State** the **update rule** and why it moves us in the right direction.
4. **Explain** why the **learning rate** is such an important hyperparameter.

---

## Intuition

- Training can be visualised as standing on a **curved landscape** (the loss function).
- **Gradient descent:** Look at the **slope** and take a step **downhill**.
- If the slope is **negative** (loss increases to the left), move **right** (increase the parameter).
- If the slope is **positive** (loss increases to the right), move **left** (decrease the parameter).
- Where the slope is **flat**, we are near a minimum. **Following the slope** is the basis of all such optimization.

---

## What the Gradient Tells Us

- The **gradient** is how much the loss changes if we **nudge** the parameters slightly.
- **Positive** gradient → increasing the parameter **increases** the loss → we should **decrease** the parameter.
- **Negative** gradient → increasing the parameter **decreases** the loss → we should **increase** the parameter.
- The gradient points in the direction of **steepest increase** of the loss, so we move in the **opposite** direction to **reduce** the loss.

---

## Update Rule

\[
\theta_{\text{new}} = \theta_{\text{old}} - \eta \cdot \nabla L
\]

- \( \theta \): parameter (weight) we update.
- \( \eta \): **learning rate**.
- \( \nabla L \): **gradient** of the loss w.r.t. \( \theta \) (slope at the current point).
- The **gradient** gives the **direction**; the **learning rate** controls **how big** the step is. Every parameter in the network follows this same rule during training.

---

## Learning Rate: Critical Hyperparameter

- **Too small:** Very small steps → training **extremely slow**.
- **Too large:** Can **overshoot** the minimum or **diverge** (loss increases instead of decreasing).
- A **well-chosen** learning rate gives **smooth**, efficient progress downhill. So **learning rate tuning** is a central part of model training.

---

## From 1D to High Dimensions

- We often draw **simple curves** to explain gradient descent.
- Real networks live in spaces with **millions** of dimensions; the gradient is a **vector** of slopes for every weight and bias.
- The **core idea** is unchanged: take a step in the direction that **most reduces** the loss. The logic of gradient descent is the same in one dimension or a million.

---

## Summary

- **Gradient descent** minimizes the loss by stepping **downhill**.
- The **gradient** points toward steepest **increase**, so we move **opposite** to it.
- **Update rule:** \( \theta \leftarrow \theta - \eta \nabla L \).
- The **learning rate** controls how **fast** or how **safely** we descend. This is the foundation for all optimizers that follow.
