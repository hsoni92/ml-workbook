# Introduction to Regression

## 1. Supervised learning: classification vs regression

**Supervised learning** learns a mapping from inputs \(\mathbf{x}\) to outputs \(y\) from **labeled** pairs \((\mathbf{x}_i, y_i)\).

| Task | Output \(y\) | Example |
|------|----------------|---------|
| **Classification** | **Discrete** label from finite set | Spam / not spam; churn / stay |
| **Regression** | **Continuous** (real-valued) quantity | Latency (ms), price, load (CPU %) |

**Why continuity matters:** many targets are **uncountably** many possible values (prices, temperatures). The model must **interpolate** sensibly between training values.

---

## 2. Regression as function approximation

Seek a hypothesis **h** (also written \(f\)) such that \( \hat{y} = h(\mathbf{x}) \approx y \).

- **Univariate:** \(\mathbf{x}\) is one feature (e.g. floor area).
- **Multivariate:** \(\mathbf{x} \in \mathbb{R}^d\) (area, location encoding, bedrooms, …).

**Example (cloud billing):** predict **monthly cost** from usage features—regression, not classification.

---

## 3. Train / test protocol

Split historical data into **training** (fit **h**) and **test** (evaluate on **held-out** examples). On test point \(\mathbf{x}\), compare prediction \(\hat{y}\) to true \(y\) via a **loss** (developed in the next notes).

---

## 4. Linear hypothesis (preview)

**Simple linear:** \(h(x) = \theta_0 + \theta_1 x\) (intercept \(\theta_0\), slope \(\theta_1\)).

**Multiple linear:** \(h(\mathbf{x}) = \theta_0 + \theta_1 x_1 + \cdots + \theta_d x_d = \theta_0 + \boldsymbol{\theta}^T \mathbf{x}\).

Geometrically: a **line** (1D input), **plane** (2D input), **hyperplane** (general \(d\)).

**Parameters** \(\theta_j\) are **learned** by minimizing error on training data (closed form or iterative optimization).

---

## Common Pitfalls / Exam Traps

- Treating **ordered numeric codes** (1,2,3) as categorical without care can distort linear models.
- **Extrapolation:** linear models behave badly **outside** training range of features.
- Confusing **regression** with “predicting any number”—classification can use numeric codes but **finite** set.

---

## Quick Revision Summary

- **Regression:** predict **continuous** \(y\); classification predicts **discrete** labels.
- Goal: learn **h** with small prediction error on unseen data.
- **Train/test** split evaluates **generalization**.
- **Linear** models: parameters \(\theta\); hyperplane in feature space.
- Real use cases: pricing, forecasting, SLA latency prediction.
