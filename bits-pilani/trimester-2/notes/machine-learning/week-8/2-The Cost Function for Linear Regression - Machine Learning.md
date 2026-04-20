# The Cost Function for Linear Regression

## 1. Residuals

For example \(i\): prediction \(\hat{y}_i = h(\mathbf{x}_i)\), truth \(y_i\).

**Residual:** \(e_i = \hat{y}_i - y_i\) (or \(y_i - \hat{y}_i\); be consistent in a given derivation).

**Per-point loss:** squared residual \(e_i^2\) penalizes large errors heavily and is **smooth** (differentiable).

---

## 2. Sum of squared errors (SSE) and mean squared error (MSE)

For \(m\) training points:

\[
\text{SSE} = \sum_{i=1}^{m} (\hat{y}_i - y_i)^2
\]

\[
\text{MSE} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i)^2
\]

Some texts use **\(\frac{1}{2m}\)** for cleaner derivatives; **minimum** is at the same \(\theta\).

**Why squares:**
- Cancels **sign** cancellation in naive summation of raw errors.
- **Penalizes** large errors more than small ones.
- **Differentiable** everywhere (for linear \(\hat{y}\)), enabling gradient-based optimization.

---

## 3. Linear regression cost (univariate)

\(h(x) = \theta_0 + \theta_1 x\).

\[
J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} (\theta_0 + \theta_1 x_i - y_i)^2
\]

**Goal:** choose \(\theta_0,\theta_1\) to **minimize** \(J\).

---

## 4. Convexity and optimization landscape

For **linear regression with squared loss**, \(J(\theta)\) is **convex** in \(\theta\): a single **global** minimum (under full rank design matrix). Surface is **bowl-shaped** in parameter space.

**Methods:** **closed-form** normal equations (solve \(\nabla J = 0\)) or **gradient descent** (next note).

---

## Common Pitfalls / Exam Traps

- **MSE vs RMSE:** \(\sqrt{\text{MSE}}\) has same argmin for \(\theta\) but different **units** as \(y\).
- Using **sum** vs **mean** changes **gradient** scale but not minimum location if step size adjusted.
- **Outliers:** squared loss is **sensitive**; robust alternatives (Huber) exist beyond this module.

---

## Quick Revision Summary

- **Residual** measures fit error per point.
- **SSE / MSE** aggregate squared residuals; standard linear regression objective.
- Squaring: avoids sign cancellation, emphasizes large errors, enables calculus.
- \(J(\theta)\) for linear model is **convex** \(\Rightarrow\) global minimum.
- **1/(2m)** is a derivative convenience, not a different problem.
