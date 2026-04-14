# Underfitting and Overfitting – Artificial Neural Networks (Module 7)

## Learning Objectives

By the end of this video you will:

1. **Define** **underfitting** and **overfitting**.
2. **Explain** how **model capacity** and **data** jointly drive these behaviors.
3. **Diagnose** underfitting vs overfitting using **training** vs **generalization** error.
4. **Recognize** common **causes** of each failure mode.

---

## The Goal: Appropriate Fit

- Training aims not only to “fit” data, but to fit **appropriately**.
- **Too simple** a model → may miss real structure (**underfitting**).
- **Too complex** a model (relative to data) → may fit **noise** and idiosyncrasies (**overfitting**).
- Both lead to **poor generalization**. The key is **how** the model fits, not just whether loss goes down on training data.

---

## Underfitting

- Occurs when the model is **too simple** for the task (relative to the true pattern).
- Cannot capture the **underlying structure**; may behave like an overly rigid predictor (e.g. a line where the relationship is nonlinear).
- **Typical outcome:** **poor** performance on **training** data **and** **poor** on **unseen** data.

**Common causes:**

- **Insufficient model capacity** (too few layers/units, overly constrained architecture).
- **Overly restrictive assumptions** (e.g. linear model for a nonlinear problem).
- **Inadequate features** (inputs do not carry enough information).
- **Excessive regularization** (penalties or constraints so strong that the model cannot fit even real signal).

In short: the model has **not learned enough**.

---

## Overfitting

- Occurs when the model is **too complex relative** to the amount and noise level of data.
- Often achieves **very low training error** by fitting training points **extremely** well.
- Instead of learning **general** patterns, it **memorizes** **noise** and **spurious** details specific to the training set.
- **Typical outcome:** **excellent** training metrics but **worse** performance on **unseen** data.

---

## Diagnostic Table: Training vs Generalization Error

| Regime | Training error | Generalization error (val/test) |
|--------|----------------|----------------------------------|
| **Underfitting** | High | High |
| **Good fit** | Low | Low |
| **Overfitting** | Low | High |

This comparison is a **practical diagnostic** for model behavior.

### Visual: fit to data (cartoon)

```text
Underfit          Good fit              Overfit
  ·    ·            ·    ·                ·    ·
    ——            ~  curve  ~          (((((())))))
  ·    ·            ·    ·         wiggly curve hits every ·
  (line misses      (smooth            (memorizes noise)
   the pattern)     trend)
```

---

## Model Capacity and Data

- **Capacity** = expressive power of the network (what functions it can represent).
- **Low capacity** → hard to represent complex patterns → **underfitting** risk.
- **High capacity** → can represent very complex functions → **overfitting** risk rises, especially with **limited** or **noisy** data.
- The **same architecture** can underfit or overfit depending on **data amount**, **quality**, and **training setup**. So under/overfitting are properties of the **model–data–training** combination, not the model alone.

---

## Summary

- **Underfitting:** too simple → high train and high test/val error.
- **Overfitting:** too complex for data → low train error, high test/val error; memorization and noise fitting.
- **Capacity vs data** explains **which** failure mode dominates.
- **Next:** **bias–variance** as a theoretical lens on the same behaviors.

---

## Exam-style cues

- **Classify** a scenario (high/low train and val error) as underfit, good fit, or overfit.
- **List** causes of underfitting and overfitting.
- **Explain** why capacity alone does not determine the outcome without considering data.
