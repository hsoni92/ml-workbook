# Evaluation Metrics - Quick Refresher - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Use the **confusion matrix** as the basis for classification metrics.
2. Define and interpret **accuracy, precision, recall, and F1 score**.
3. Explain why the right metric depends on **class balance** and **error cost**.
4. Describe how **decision thresholds** change neural-network evaluation.

---

## Confusion Matrix First, Metrics Next

All major classification metrics are summaries of the **confusion matrix**. If the confusion matrix is clear, the metrics stop feeling like isolated formulas.

| Actual \ Predicted | Positive | Negative |
| --- | --- | --- |
| **Positive** | TP | FN |
| **Negative** | FP | TN |

Each cell tells us a different kind of success or failure:

- **TP**: actual positive, predicted positive
- **FN**: actual positive, predicted negative
- **FP**: actual negative, predicted positive
- **TN**: actual negative, predicted negative

In a fraud detection problem, the positive class might be **fraud** and the negative class **not fraud**.

---

## The Four Core Metrics

| Metric | Formula | Main Question It Answers | Best Used When |
| --- | --- | --- | --- |
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | How many predictions are correct overall? | Classes are balanced and error costs are similar |
| **Precision** | TP / (TP + FP) | When the model predicts positive, how often is it correct? | False positives are costly |
| **Recall** | TP / (TP + FN) | Of all true positives, how many did the model find? | Missing positives is costly |
| **F1 Score** | 2PR / (P + R) | How well does the model balance precision and recall? | Classes are imbalanced and both FP and FN matter |

---

## Metric Intuition, Not Just Formulas

### Accuracy

Accuracy measures overall correctness. It is simple and useful, but it treats all mistakes equally and does not reveal *which kind* of mistake the model is making.

### Precision

Precision focuses on the quality of **positive predictions**.
Question: **"When the model says positive, can I trust it?"**

This matters in settings where false alarms are expensive, such as spam filtering or fraud alerts.

### Recall

Recall focuses on how many real positives are found.
Question: **"Of all the actual positives, how many did the model catch?"**

This matters in settings where missing a positive case is dangerous, such as disease screening.

### F1 Score

F1 combines precision and recall using the **harmonic mean**, so it rewards balance rather than one-sided performance.

It is especially useful when:

- classes are imbalanced, and
- both false positives and false negatives matter.

---

## Mini Example: Fraud Detection

Suppose a model makes **1000 predictions**:

- **60** true positives,
- **40** false positives,
- **20** false negatives,
- **880** true negatives.

Then:

- **Accuracy** = (60 + 880) / 1000 = **94%**
- **Precision** = 60 / (60 + 40) = **60%**
- **Recall** = 60 / (60 + 20) = **75%**

This example shows why accuracy can look strong even when the quality of positive predictions is only moderate.

---

## Why Accuracy Can Be Misleading

In highly imbalanced problems, a model may achieve high accuracy simply by favoring the majority class.

Example: if only **1%** of transactions are fraudulent, a model that predicts "not fraud" almost everywhere can still look very accurate, while being practically useless.

That is why:

- **precision** and **recall** often matter more than raw accuracy,
- and **context** matters more than memorizing formulas.

---

## Threshold Dependence in Neural Networks

Neural networks usually output **probabilities**, not fixed labels. Labels are produced only after choosing a **decision threshold**.

```text
Lower threshold -> more samples predicted positive -> recall goes up, precision often goes down
Higher threshold -> fewer samples predicted positive -> precision goes up, recall often goes down
```

So metrics are not fixed properties of the model alone. They also depend on the evaluation choices we make.

This becomes especially important later when we discuss **calibration**.

---

## How to Choose the Right Metric

When answering an exam or practical question, use this reasoning pattern:

1. Identify whether the dataset is **balanced or imbalanced**.
2. Ask which error is more costly: **false positive** or **false negative**.
3. Choose metrics that align with that cost structure.
4. Avoid saying that **accuracy alone** is enough unless the problem genuinely justifies it.

---

## Summary and Exam-Ready Takeaways

- The **confusion matrix** is the foundation of classification metrics.
- **Accuracy** gives overall correctness but can be misleading in imbalanced settings.
- **Precision** matters when false positives are costly.
- **Recall** matters when false negatives are costly.
- **F1 score** is useful when we need a balance between precision and recall.
- In neural networks, these metrics depend on the **decision threshold** applied to predicted probabilities.

**Bridge to next topic:** Classical metrics tell us *what* happened at the output level. Next, we move deeper and ask how training itself behaves through the geometry of **loss surfaces**.
