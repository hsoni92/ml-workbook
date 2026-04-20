# Calibration Fundamentals - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Define **calibration** for neural-network predictions.
2. Distinguish **accuracy** from **confidence quality**.
3. Interpret a **reliability diagram** at a conceptual level.
4. Explain what **Expected Calibration Error (ECE)** measures.

---

## Calibration in One Line

A model is **well calibrated** when its predicted confidence matches how often it is actually correct.

If a model says **80% confidence**, then among many such predictions we should expect it to be correct about **80% of the time**.

Calibration is therefore about **honesty of confidence**, not just correctness.

---

## Why Calibration Matters

Up to this point in the module, we have focused heavily on accuracy and generalization. But when a model outputs probabilities, another question becomes crucial:

**Should we trust the model's confidence?**

This matters whenever probabilities drive actions such as:

- medical triage,
- fraud alerts,
- risk scoring,
- abstain-or-review systems.

A model can be accurate overall and still assign misleading confidence scores.

---

## Accuracy vs Calibration

These are related, but they are not the same.

- **Accuracy** asks: *How often is the model right?*
- **Calibration** asks: *When the model is this confident, how often is it actually right?*

So a model can be:

- **accurate but miscalibrated**, or
- **less accurate but better calibrated**.

That is why calibration deserves its own evaluation tools.

---

## Overconfidence and Underconfidence

Two common types of miscalibration are:

### Overconfidence

The model assigns confidence that is **higher than justified** by its actual correctness.

Example: the model often predicts with **80% confidence**, but only **60%** of those predictions are correct.

### Underconfidence

The model assigns confidence that is **lower than justified** by its actual correctness.

Both are problematic because downstream decisions often rely directly on these probability values.

---

## Reliability Diagram

A **reliability diagram** helps compare predicted confidence with observed accuracy.

The usual workflow is:

```text
Collect predicted probabilities
-> group predictions into confidence bins
-> compute empirical accuracy within each bin
-> compare average confidence with actual accuracy
```

If the model is perfectly calibrated, the points lie near the **diagonal**.

- Points **below** the diagonal suggest **overconfidence**.
- Points **above** the diagonal suggest **underconfidence**.

---

## Expected Calibration Error (ECE)

While a reliability diagram gives a visual picture, **ECE** gives a numerical summary.

ECE measures the average gap between:

- what confidence the model predicted, and
- what accuracy was actually observed,

across confidence bins.

So:

- **lower ECE** means better calibration,
- **higher ECE** means confidence and reality disagree more strongly.

The transcript's demo reports a model with around **95% accuracy** but an **ECE of about 4.5%**, showing that strong accuracy still leaves room for confidence mismatch.

---

## Why Neural Networks Often Need Calibration Checks

Modern neural networks are highly expressive and often produce very confident outputs.

A common mistake is to interpret:

- **softmax probabilities**, or
- **sigmoid outputs**

as automatically trustworthy confidence estimates.

They are not guaranteed to be reliable unless calibration is actually evaluated.

> **Key distinction:** Softmax gives a normalized probability distribution, but not necessarily a well-calibrated one.

---

## Summary and Exam-Ready Takeaways

- A model is **calibrated** when predicted confidence matches empirical correctness.
- **Accuracy** and **calibration** are different ideas.
- A neural network can be **accurate yet poorly calibrated**.
- **Reliability diagrams** visualize confidence vs observed accuracy.
- **ECE** summarizes the average confidence-accuracy mismatch.
- Calibration matters whenever probabilities are used in real decisions.

**Bridge to next topic:** Once we know how to detect miscalibration, the next question is how to **improve calibration** using methods such as **temperature scaling** and **ensembles**.
