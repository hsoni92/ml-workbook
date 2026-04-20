# Why NNs Fail Under Perturbations - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Define **robustness** in the context of neural networks.
2. Explain why small input changes can cause large prediction changes.
3. Distinguish **robustness** from **generalization**.
4. Justify why perturbation-based tests are a necessary evaluation tool.

---

## What Robustness Asks

A robust model should remain reasonably stable when the input is changed **slightly** but its underlying meaning has not changed.

Examples of such small changes include:

- noise,
- blur,
- small measurement shifts,
- natural feature variation.

If the input is semantically the same, we usually expect the prediction to remain similar.

---

## Why This Topic Matters

A common misconception is that high test accuracy guarantees reliable behavior. In practice, a neural network can be:

- accurate,
- even reasonably calibrated,
- and still **fragile** under tiny perturbations.

This shows that **robustness is a separate evaluation property**.

Standard test sets evaluate single examples as they are given. They usually do **not** test what happens in the neighborhood around each example.

---

## What Counts as a Perturbation

In this module, a perturbation means a **small realistic change** to the input that should not change the true label.

Examples:

- slight sensor noise,
- small pixel noise in an image,
- mild feature jitter in tabular data,
- minor measurement variation.

So the key issue is not whether the input changed at all. The key issue is whether the change should have changed the model's decision.

---

## Why Neural Networks Fail Under Perturbations

| Cause | Mechanism | Outcome |
| --- | --- | --- |
| **Highly nonlinear decision boundaries** | Small input movement can cross a boundary | Prediction flips |
| **High-dimensional input spaces** | Tiny changes along many directions can accumulate | Confidence changes unexpectedly |
| **Training objective** | Standard training optimizes average accuracy, not local stability | Hidden fragility remains |
| **Overconfidence** | Model may stay very certain even when wrong | Unsafe behavior |

The transcript emphasizes that even a tiny perturbation can produce a large change in the model's **logits**, which can then flip the predicted label.

---

## A Concrete Example

The transcript gives a vivid illustration:

- on the original input, the model is **85% confident** that an image is a **polar bear**,
- after a small perturbation, it becomes **100% confident** that it is a **dishwasher**.

The important point is not the exact classes. The important point is the combination of:

- **very small input change**,
- **drastic label flip**,
- **high confidence while wrong**.

That combination is especially dangerous in real systems.

---

## Robustness vs Generalization

| Property | Main Question | Can One Be Good While the Other Is Bad? |
| --- | --- | --- |
| **Generalization** | Does the model work on new examples from the same broad distribution? | Yes |
| **Robustness** | Is the model stable around a specific example under small perturbations? | Yes |

A model can generalize well on standard test data and still be locally unstable.

So for trustworthy deployment, we need **both**:

- good generalization,
- good robustness.

---

## Why Standard Evaluation Misses This

A standard test set typically checks only the clean input:

```text
Clean input -> prediction looks correct
```

Robustness evaluation checks the nearby neighborhood:

```text
Clean input -> correct prediction
Small perturbation -> same meaning
Model output changes sharply -> robustness failure
```

Without perturbation-based tests, this kind of fragility can remain invisible.

---

## Summary and Exam-Ready Takeaways

- **Robustness** asks whether predictions remain stable under small, label-preserving input changes.
- Neural networks may fail because of **nonlinear boundaries**, **high-dimensional inputs**, and training that optimizes **average accuracy rather than local stability**.
- A model can be **accurate and calibrated** yet still fragile.
- **Robustness** and **generalization** are related but distinct ideas.
- Perturbation-based evaluation is necessary because standard test sets do not probe local behavior around each sample.

**Bridge to next topic:** After understanding why perturbation failures happen, the next step is to test them directly using **perturbation tests and sensitivity curves**.
