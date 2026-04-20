# Perturbation Tests and Sensitivity Curves - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain how **perturbation tests** are performed.
2. Interpret a **sensitivity curve** for model robustness.
3. Distinguish between **graceful degradation** and **sharp collapse**.
4. Explain why two models with similar clean accuracy can still have very different robustness.

---

## From Intuition to Measurement

In the previous note, robustness was introduced conceptually. This note turns that idea into a practical evaluation procedure.

The central question is:

**What happens to model performance as input perturbation strength increases?**

Perturbation tests answer this by applying controlled changes to the input and re-evaluating the model at each level.

---

## Typical Test Setup

| Step | What We Do | What We Observe |
| --- | --- | --- |
| 1 | Evaluate the model on clean validation or test data | Baseline metric |
| 2 | Apply perturbation at strength `s` | Perturbed inputs |
| 3 | Re-evaluate the model | Metric at that perturbation level |
| 4 | Repeat for multiple values of `s` | Degradation pattern |
| 5 | Plot metric against perturbation strength | Sensitivity curve |

Common perturbations may include:

- Gaussian noise,
- blur,
- occlusion,
- feature jitter.

The transcript demo uses **Gaussian noise** added gradually to the input features.

---

## Demo Intuition from the Transcript

The notebook demo:

- trains a standard neural network on a clean binary classification dataset,
- obtains a baseline accuracy of around **95%**,
- then increases the noise level step by step,
- and measures how accuracy changes.

This setup is useful because it isolates one idea clearly:

> **Clean accuracy alone does not tell us how stable the model is under realistic disturbance.**

---

## What Is a Sensitivity Curve?

A **sensitivity curve** plots a performance metric such as accuracy against perturbation strength.

```text
Metric
  |
  |------\             flat or slow decline -> robust behavior
  |       \__
  |          \____      steep early drop -> fragile behavior
  +-----------------> perturbation strength
```

The shape of the curve matters more than a single point.

---

## How to Read the Curve

### Flat or slowly declining curve

This suggests the model is relatively robust. Performance degrades gradually as the perturbation becomes stronger.

This is often described as **graceful degradation**.

### Steep early drop

This suggests the model is fragile. Even small perturbations cause a sharp fall in performance.

This is often described as **sharp collapse** or **high sensitivity**.

---

## What to Report in a Robustness Evaluation

When describing a perturbation test, it is useful to report:

- the **baseline metric** at zero perturbation,
- the **rate of degradation** as perturbation increases,
- whether the decline is **gradual or sudden**,
- the perturbation level where performance begins to collapse,
- comparisons between models with similar clean accuracy.

This gives a much richer picture than saying only that one model was accurate on the original test set.

---

## Why Sensitivity Curves Are Valuable

Two models may have:

- the same clean-data accuracy,
- but very different robustness profiles.

One model may degrade slowly, while another may fail almost immediately once noise is introduced.

So sensitivity curves reveal behavior that standard evaluation can easily miss.

---

## Summary and Exam-Ready Takeaways

- **Perturbation tests** evaluate robustness by applying controlled input changes and re-measuring performance.
- A **sensitivity curve** shows how quickly performance degrades as perturbation strength increases.
- **Graceful degradation** suggests robustness; **sharp collapse** suggests fragility.
- Robustness testing **complements** standard test-set evaluation rather than replacing it.
- Two models with the same clean accuracy can still differ greatly in robustness.

**Bridge to next topic:** Robustness asks whether predictions stay stable. The next note asks a different question: **when the model produces a probability distribution over many classes, how do we read its uncertainty?**
