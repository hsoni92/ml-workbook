# Boosting and AdaBoost: A Sequential Approach

## 1. Contrast with bagging

| Aspect | Bagging | Boosting |
|--------|---------|----------|
| Training | **Parallel** bootstrap models | **Sequential**; each model targets previous errors |
| Typical base learner | Deep / unpruned trees | **Weak** learners (e.g. **depth-1** decision stumps) |
| Combination | Vote / average, often **equal** weight | **Weighted** combination |
| Main effect | Variance reduction | **Bias** reduction via staged fitting |

---

## 2. Weak learners and decision stumps

A **weak** learner performs only slightly better than chance on hard data. A **decision stump** is a one-split tree: decision boundary is a **half-plane** perpendicular to one axis (parallel to other axes)—very **low variance**, **high bias** alone.

**Boosting idea:** chain many weak rules so their **sum** (or sign) approximates a **complex** boundary.

---

## 3. AdaBoost-style intuition (binary classification sketch)

1. Initialize **equal** weights on all training points.
2. Train a weak classifier (stump) on weighted data.
3. **Increase** weights on **misclassified** points; **decrease** weights on correct ones.
4. Repeat; each round focuses more on **hard** examples.
5. **Final** classifier: **weighted vote** of weak classifiers (weights depend on each round’s error).

```mermaid
flowchart LR
  D1[Weighted data] --> M1[Weak model 1]
  M1 --> W[Update weights]
  W --> D2[Weighted data]
  D2 --> M2[Weak model 2]
  M2 --> Dot[...]
  Dot --> MF[Weak model T]
  MF --> H[Weighted combination]
```

**Key property:** **sequential**—stage \(t\) depends on \(1..t-1\); **cannot** parallelize the training loop (unlike bagging).

---

## 4. Weighted average vs majority vote

Boosting typically outputs **sign** or **weighted sum** of weak hypotheses—not plain majority vote. Larger weight \(\Rightarrow\) more reliable weak learner in the sequence.

---

## 5. Modern relatives

**Gradient boosting** (XGBoost, LightGBM, CatBoost) fits stages by **gradient descent** in function space; AdaBoost is a historic, clean special case for exponential loss.

---

## Common Pitfalls / Exam Traps

- **Boosting vs bagging parallelism:** boosting is **inherently sequential**.
- **Overfitting:** boosting can overfit if rounds **too many** / depth too high—needs **regularization**, early stopping, CV.
- **Stumps:** axis-aligned only; combination creates **nonlinear** boundaries.

---

## Quick Revision Summary

- **Boosting:** sequential weak learners; **reweight** mistakes; **weighted** aggregate.
- **Stumps:** depth-1 trees; simple weak rules.
- Targets **bias** reduction; complements **bagging’s** variance focus.
- **Not parallel** in standard form.
- **AdaBoost:** classical instance reweighting + weighted vote.
- Practice: use **gradient boosting** frameworks with validation and early stopping.
