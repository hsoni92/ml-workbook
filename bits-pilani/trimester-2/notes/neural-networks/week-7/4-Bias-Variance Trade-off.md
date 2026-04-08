# Bias–Variance Trade-off – Artificial Neural Networks (Module 7)

## Learning Objectives

By the end of this video you will:

1. **Define** **bias** and **variance** as components of prediction behavior.
2. **Relate** high/low bias and variance to **underfitting** and **overfitting**.
3. **Explain** the **trade-off**: reducing one can **increase** the other as **model complexity** changes.
4. **Use** this framework to reason about **model complexity**, **data**, and **training** choices.

---

## Two Sources of Error on Unseen Data

Errors on unseen data do not come from a single cause:

- Some error comes from **oversimplified** assumptions: the model **cannot** represent the truth well (**bias**).
- Some error comes from **sensitivity** to the particular training sample: the fit **changes** a lot if training data changes (**variance**).

**Bias** and **variance** name these two sources of **generalization** difficulty.

---

## Bias

- **Bias** ≈ error due to **simplifying assumptions** built into the model family.
- A **high-bias** model is **too rigid**: it **under-represents** the true complexity of the relationship.
- Tends to make **systematic** mistakes; more training data **may not** fix the misspecification if the model class is wrong.
- **Typical link:** **high bias** ↔ **underfitting** (important patterns missed).

---

## Variance

- **Variance** ≈ sensitivity of the learned model to **which** training examples were seen.
- A **high-variance** model can **change a lot** when trained on slightly different datasets.
- Fits **noise** as well as signal → **unstable** predictions on new points.
- **Typical link:** **high variance** ↔ **overfitting**.

---

## The Trade-off

- Bias and variance are **not** independent in practice when you tune **model complexity**:
  - As **complexity increases**, **bias** tends to **decrease** and **variance** tends to **increase**.
  - As **complexity decreases**, **bias** tends to **increase** and **variance** tends to **decrease**.
- **Improving** one aspect often **worsens** the other—hence **bias–variance trade-off**.
- **Good generalization** usually lies **between** extremes: flexible enough to capture real patterns, **stable** enough not to chase noise.

---

## Connection to Underfitting and Overfitting

| Situation | Bias (typical) | Variance (typical) |
|-----------|----------------|---------------------|
| **Underfitting** | High | Low |
| **Overfitting** | Low | High |
| **Balanced / good fit** | Moderate | Moderate |

---

## Summary

- **Bias** = structural error from **too-simple** models; **variance** = **instability** across training sets and noise fitting.
- **Complexity** moves bias and variance in **opposite** directions—classic **trade-off**.
- Design and training aim to **balance** both for **low** generalization error.
- **Next:** recognizing **overfitting in practice** (symptoms and early warnings).

---

## Exam-style cues

- **Define** bias vs variance in your own words.
- **Map** underfitting/overfitting to bias/variance.
- **Explain** why increasing model complexity reduces bias but often increases variance.
