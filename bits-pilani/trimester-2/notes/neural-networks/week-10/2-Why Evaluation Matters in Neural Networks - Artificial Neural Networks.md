# Why Evaluation Matters in Neural Networks - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain why **high accuracy alone is insufficient** for neural networks.
2. Identify common hidden failure modes such as **memorization**, **overconfidence**, and **fragility under perturbation**.
3. Distinguish between **performance**, **confidence**, and **robustness** as separate evaluation dimensions.
4. Use the phrase **"accuracy is necessary but not sufficient"** correctly in an exam answer.

---

## The Common Misconception

When a model reports high accuracy, it is tempting to conclude that the model is reliable. In neural networks, that conclusion is often incomplete.

A deep model may:

- memorize training examples,
- exploit background or shortcut cues instead of real structure,
- perform well on a benchmark but fail in deployment,
- make very confident predictions even when it is wrong.

So the real question is not just, **"Is the model accurate?"** but also **"Can the model be trusted?"**

---

## Why Accuracy Alone Is Insufficient

Accuracy compresses all model behavior into one number. That is useful, but it hides several important details.

### 1. High accuracy does not prove the model learned the right pattern

A model may achieve strong performance by relying on **spurious correlations**. For example, an image classifier may appear to detect an object correctly but may actually be using the **background** rather than the object itself.

### 2. High-capacity models can fit noise

Deep networks are highly expressive. With enough parameters, they can fit extremely complex patterns and even **random labels**. This means strong training performance can be misleading.

### 3. Probabilities add another layer of evaluation

Neural networks often produce probability distributions, not just class labels. Two models can have the same accuracy but very different confidence behavior:

- one may be cautious,
- another may be extremely confident even when wrong.

In applications such as healthcare or finance, this difference matters a lot.

### 4. Aggregate metrics can hide subgroup failures

A model may perform well on average while still failing badly on:

- minority classes,
- rare but important examples,
- slightly shifted real-world inputs.

---

## Hidden Failure Modes in Neural Networks

| Situation | Why It Happens | Hidden Risk |
| --- | --- | --- |
| High training accuracy | Model memorizes training data or noise | Poor generalization |
| High test accuracy | Test set may not expose edge cases | False sense of trust |
| Strong softmax confidence | Softmax score is not guaranteed to be calibrated | Confident wrong predictions |
| Good average metric | Dominant classes drive the average | Minority-class failures stay hidden |
| Slight input change | Nonlinear decision boundaries can be locally unstable | Prediction flips under perturbation |

These failures often do not show up when we inspect only one score.

---

## Why Evaluation Must Be Multi-Dimensional

Reliable evaluation of neural networks must consider several perspectives together:

- **Predictive performance**: How often is the model right?
- **Generalization**: Does it still work on unseen data?
- **Confidence quality**: Are its probabilities honest?
- **Robustness**: Does it remain stable under small changes?

Each perspective reveals a different aspect of model behavior. Ignoring one of them can lead to misleading conclusions.

---

## A Practical Way to Interpret "Good Model"

A neural network is not truly "good" just because it is accurate.

A useful and trustworthy model should be:

- **reasonably correct**,
- **appropriately confident**,
- **stable under small perturbations**,
- **evaluated in a way that reflects application risk**.

That is why module 10 uses a broader evaluation framework instead of a one-number approach.

---

## Summary and Exam-Ready Takeaways

- **Accuracy is necessary but not sufficient.**
- Neural networks require more careful evaluation because they are **high-capacity**, produce **probabilistic outputs**, and exhibit **hidden failure modes**.
- Common hidden failures include:
  - memorization,
  - overconfidence,
  - sensitivity to perturbations,
  - poor minority-class behavior.
- Good evaluation must jointly consider **performance, generalization, confidence, and robustness**.

**Bridge to next topic:** Since accuracy alone is not enough, we next revisit the classical metrics - **accuracy, precision, recall, and F1** - and interpret them properly for neural network outputs.
