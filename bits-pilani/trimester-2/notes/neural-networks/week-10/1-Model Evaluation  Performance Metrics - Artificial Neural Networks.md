# Model Evaluation and Performance Metrics - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain why **training a model** and **trusting a model** are not the same thing.
2. Describe why evaluation in neural networks is **harder than in many classical models**.
3. List the major dimensions of evaluation in this module: **performance, generalization, calibration, robustness, and uncertainty**.
4. Outline an exam-ready workflow for evaluating a trained neural network.

---

## Why This Module Starts with Evaluation

So far, the course has focused on how neural networks are built and trained. But training is only the beginning.

A neural network may:

- achieve very high training accuracy and still **overfit**,
- produce the correct label but with **misleading confidence**,
- fail when the input is changed only slightly,
- look strong on a benchmark but behave poorly in practice.

This is why evaluation is a central part of deep learning, not an afterthought.

---

## Why Evaluating Neural Networks Is More Challenging

Classical evaluation often emphasizes a final score such as accuracy. Neural networks require a broader view for three main reasons:

1. **High capacity**: deep models can fit very complex patterns, including noise or spurious correlations.
2. **Probabilistic outputs**: they usually output probabilities, not just labels, so we must ask whether those probabilities are trustworthy.
3. **Hidden failure modes**: many important failures are not visible from one aggregate metric.

For example, a fraud detector may show **99% accuracy** while still assigning **very high fraud probability to legitimate transactions**. Accuracy alone would hide that the model is confidently wrong.

> **Core idea:** A neural network is not fully evaluated when we know only how often it is right. We must also know how it behaves, how confident it is, and how stable it remains.

---

## A Multi-Dimensional View of Evaluation

| Evaluation Dimension | Main Question | Typical Tools |
| --- | --- | --- |
| **Predictive performance** | How often is the model correct? | Accuracy, precision, recall, F1, ROC-AUC, PR-AUC |
| **Generalization** | Does performance hold on unseen data? | Train/validation/test split, learning curves |
| **Confidence quality** | Are predicted probabilities honest? | Reliability diagram, ECE, Brier score |
| **Robustness** | Are predictions stable under small input changes? | Perturbation tests, sensitivity curves |
| **Uncertainty** | Does the model know when it is unsure? | Entropy, confidence histograms, ensembles |

Each dimension answers a different question. None of them can fully replace the others.

---

## How This Module Fits Into the Course

Earlier modules explained **how neural networks learn** through backpropagation, optimization, regularization, and generalization. This module shifts the focus from:

- **training a model** to
- **evaluating whether the trained model can be trusted**.

The next modules then build on this by asking how to **diagnose internal failures** and **improve models systematically**.

---

## Evaluation Pipeline

An exam-ready evaluation flow for neural networks is:

```text
Define the task and error costs
-> choose suitable metrics
-> keep clean train/validation/test splits
-> evaluate predictive performance
-> inspect generalization behavior
-> check calibration of probabilities
-> stress-test with perturbations
-> analyze uncertainty
-> decide whether the model is deployable
```

This sequence matters because deployment decisions depend on more than one number.

---

## Quick Example: Why Accuracy Is Not Enough

Suppose a fraud detection model is highly accurate overall. That still does not tell us:

- whether it misses too many fraud cases,
- whether it raises too many false alarms,
- whether its confidence scores are reliable,
- whether it remains stable when inputs are slightly noisy.

So even when the headline metric looks strong, the model may still be unsafe or unhelpful in practice.

---

## Summary and Exam-Ready Takeaways

- Evaluation in deep learning is **multi-dimensional**.
- Neural networks are harder to evaluate because they have **high capacity**, produce **probabilities**, and exhibit **hidden failure modes**.
- A good evaluation framework should cover:
  - **predictive performance**,
  - **generalization**,
  - **calibration**,
  - **robustness**,
  - **uncertainty**.
- The right metric depends on the **application**, the **cost of errors**, and the **decision setting**.

**Bridge to next topic:** Before using advanced evaluation tools, we first need to answer a basic question: **why exactly is evaluating neural networks more subtle than evaluating classical models?**
