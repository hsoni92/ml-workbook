# Common Pitfalls – Overfitting and Underfitting – Machine Learning (Module 3)

## Learning Objectives

By the end of this video you will:

1. **Define** **underfitting** and **overfitting** in terms of model complexity, train error, and test error.
2. **Interpret** the **complexity–error** curve (train vs test error vs model complexity).
3. **Explain** the **goal of generalization** and the “sweet spot” for model complexity.
4. **Relate** overfitting to **learning noise** and **rote learning**; underfitting to **too-simple** models.
5. **Describe** the **binary classification** picture: good decision boundary vs overfit (fitting noisy points).

---

## Two Types of Error

- **Train error:** Error when we **train** on training data and **evaluate on the same** training data.
- **Test error:** Error when we **train** on training data and **evaluate on separate test** data.

We **plot** both against **model complexity** (e.g. tree depth, number of parameters).

---

## Model Complexity vs Error (Typical Picture)

- **X-axis:** Model complexity (low → high).  
- **Y-axis:** Error.

**Train error:** As complexity **increases**, train error generally **decreases** and can go very low (model can fit training data very well, even memorize it).

**Test error:** As complexity **increases**, test error first **decreases** then **increases**. So there is a **sweet spot** in the middle.

---

## Underfitting

- **When:** Model is **too simple** for the data (low complexity).
- **Symptoms:** **High train error** and **high test error**.
- **Reason:** Model **cannot capture** the underlying pattern in the data (e.g. linear model for a nonlinear problem).
- **Result:** Poor performance everywhere; the model is **not useful**.

---

## Overfitting

- **When:** Model is **too complex**; it has **over-learned** the training data, including **noise** and **outliers**.
- **Symptoms:** **Low train error** but **high test error**.
- **Reason:** Model **memorizes** training examples (rote learning) instead of learning **general** patterns. On **new** (test) data it performs poorly.
- **Result:** Looks great on training data, **fails** on unseen data. **Dangerous** in production.

**Analogy:** Student memorizes exact practice exam answers; in the real exam (slightly different questions), the student fails. Memorization ≠ generalization.

---

## Good Fit (Sweet Spot)

- **Where:** **Moderate** complexity where **train and test error** are **both relatively low** and **close to each other**.
- **Meaning:** Model has learned **general** patterns, not noise. It will perform **similarly** on new data (good **generalization**).

---

## Generalization (Formal Idea)

- **Generalization** = the model’s ability to **learn** from training data and make **accurate predictions** on **new, unseen** samples drawn from the **same** (or similar) distribution.
- We want the model to **adapt** to the true underlying pattern, not to the exact training set. A **good** model **generalizes** well (low test error when train and test are from the same distribution).

---

## Visual (Binary Classification)

- **Good fit:** Decision boundary **separates** the two classes in a **smooth, sensible** way; a few **noisy** points may be on the “wrong” side, and we **do not** bend the boundary to fit every such point.
- **Overfitting:** Decision boundary is **twisted** so that it **correctly** classifies (almost) every training point, including **noisy** ones. The boundary becomes **too specific** to the training set and will **misclassify** many test points.

---

## Bias–Variance Intuition (Optional)

- **Underfitting** → **high bias** (model is too rigid/simple).
- **Overfitting** → **high variance** (model is too sensitive to the training set; changing data changes the model a lot).
- **Sweet spot** → **balanced** bias and variance.

---

## Summary Table

| | Underfitting | Good fit | Overfitting |
|--|--------------|----------|-------------|
| **Complexity** | Too low | Moderate | Too high |
| **Train error** | High | Low | Very low |
| **Test error** | High | Low | High |
| **Generalization** | Poor | Good | Poor |

---

## Exam-Oriented Points

- **Underfitting:** High train + high test error; model too simple.
- **Overfitting:** Low train + high test error; model memorizes training data (noise, outliers).
- **Goal:** **Generalization** — good performance on **unseen** data; aim for the **sweet spot** in complexity.
- **Good model** = one that **generalizes** well; use an **independent test set** to measure that.

Use this note for exam questions on “what is overfitting/underfitting,” “how do train and test error behave with complexity,” and “what is generalization.”
