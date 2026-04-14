# Symptoms of Overfitting – Artificial Neural Networks (Module 7)

## Learning Objectives

By the end of this video you will:

1. **Recognize** common **symptoms** of overfitting **during** training.
2. **Interpret** **training** vs **validation** curves and metrics together.
3. **Spot** **early warning signs** before validation performance gets much worse or training waste grows.
4. **Understand** that overfitting usually arises from **model–data–training** interaction, not one factor alone.

---

## Why Symptoms Matter

- Overfitting often develops **gradually** as training continues.
- **Training** loss can keep improving, so **training-only** monitoring **hides** the problem.
- Catching overfitting **early** saves compute and avoids picking or deploying models that **fail** on new data.

---

## Training vs Validation Curves

- A **classic** signal: **training loss** keeps **decreasing**, while **validation loss** **plateaus** or starts **increasing** after some point.
- A **widening gap** between training and validation performance suggests the model is learning **idiosyncrasies** of the training set rather than **general** patterns.

### Visual: widening gap

```text
  metric
    |  train ------
    |        \\      val ___
    |         \\___/     ‾‾‾  val gets worse while train improves
    +------------------------ epoch
```

---

## Unstable Validation Metrics

- **Validation accuracy** (or loss) may **fluctuate** strongly across epochs.
- Small changes in validation split or **random seed** can yield **noticeably** different validation scores.
- Such **instability** often indicates **high sensitivity** to specific training examples—consistent with **overfitting** / high variance.

---

## Model Behavior Beyond Metrics

- Overfitted models may be **very confident** on inputs similar to training yet **poor** on **slightly shifted** or **simple** variations a robust model should handle.
- That pattern points to **memorization** and **fragile** reliance on particular features rather than **stable** structure.

---

## Contributing Situations (Interaction of Factors)

Overfitting is rarely from a **single** cause. Typical **risk factors** include:

- **High-capacity** models on **small** or **noisy** datasets.
- Training for **many epochs** without **validation** monitoring or stopping criteria.
- **Complex** architectures **without** appropriate constraints (regularization, data, or capacity control).

---

## Summary

- Overfitting has **observable** signals—especially **train–val divergence**, **unstable** validation metrics, and **brittle** behavior on small input shifts.
- **Validation** (or hold-out) monitoring is **essential**; training metrics alone are **insufficient**.
- Early recognition supports timely intervention (regularization, stopping, data, architecture)—covered in following videos.

---

## Exam-style cues

- **Describe** a loss curve pattern that suggests overfitting.
- **Explain** why validation instability can indicate overfitting.
- **List** practical situations that increase overfitting risk.
