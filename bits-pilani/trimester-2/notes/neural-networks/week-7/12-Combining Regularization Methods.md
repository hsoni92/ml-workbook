# Combining Regularization Methods – Artificial Neural Networks (Module 7)

## Learning Objectives

By the end of this video you will:

1. **Explain** why **multiple** regularizers are often used **together**.
2. **Map** each technique to a **different lever** (parameters, noise, duration, data).
3. **Recognize** **common combinations** used in practice.
4. **Avoid** pitfalls: **interactions**, **over-regularization** (underfitting), **unstable** training.

---

## Why Combine?

- **No** single method removes **all** overfitting causes.
- Techniques operate at **different** points:
  - **Parameter constraints** (e.g. **L2**),
  - **Stochastic structure** (**dropout**, **batch** statistics),
  - **Stopping** optimization (**early stopping**),
  - **Data diversity** (**augmentation**),
  - **Implicit dynamics** (**batch size**, **LR**).
- **Combining** attacks overfitting from **several angles** → often **more robust** models.

---

## Complementary Roles (Module Summary)

| Technique | Primary effect (lecture view) |
|-----------|-------------------------------|
| **L2** | Limits weight magnitude; **smoother** solutions |
| **Dropout** | Reduces **co-adaptation**; noise during training |
| **Batch normalization** | Stabilizes activations; **noise** from batch statistics |
| **Early stopping** | Limits **over-training**; picks **best** val checkpoint |
| **Data augmentation** | Increases **effective** data diversity |

---

## Common Combinations (Examples from Lecture)

- **L2 + data augmentation** — control complexity while broadening seen variations.
- **Batch normalization + moderate dropout** — BN’s noise may **reduce** need for **very** heavy dropout.
- **Early stopping + learning rate scheduling** — jointly control **how long** and **how** aggressively you optimize.
- **Smaller batch sizes + L2** — noisy gradients plus weight penalty (common experimental recipe).

---

## Interactions and Pitfalls

- **BN + very strong dropout + very small batches** can make training **unstable** (too much stochasticity).
- **Too many** strong regularizers at once → **underfitting**; **maximizing** regularization is **not** the goal.
- **Balance** strengths; **tune** with **validation** performance.

---

## Incremental Practice Workflow

1. **Baseline** (simple model + reasonable defaults).
2. **Add one** regularization or training change **at a time**.
3. **Watch** validation metrics; **adjust** strength **gradually**.
4. This **isolates** each method’s effect and avoids **unnecessary** complexity.

---

## Summary

- Effective regularization is usually **selective combination**, not “apply everything maximally.”
- **Complementary** methods address **different** failure modes; **interactions** matter.
- **Validation monitoring** and **incremental** tuning are **essential**.
- **Next:** a **practical checklist** for diagnosis and prevention.

---

## Exam-style cues

- **Give** two sensible combinations and **justify** why they complement each other.
- **Explain** why stacking many strong regularizers can cause underfitting.
- **Describe** an incremental ablation-style tuning strategy.
