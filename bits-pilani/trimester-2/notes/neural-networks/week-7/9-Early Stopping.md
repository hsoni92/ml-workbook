# Early Stopping – Artificial Neural Networks (Module 7)

## Learning Objectives

By the end of this video you will:

1. **Define** **early stopping** and how it is applied during training.
2. **Explain** **why** it reduces overfitting (limits effective complexity and memorization).
3. **Describe** the role of a **validation set**, **best checkpoint**, and **patience**.
4. **Recognize** early stopping as **regularization** that needs **no** architecture change.

---

## The Problem: More Training Is Not Always Better

- Overfitting often appears **gradually**: **training loss** can keep **falling** while **unseen** performance **worsens**.
- Continuing optimization past that point can **hurt** **generalization**.
- **Early stopping** encodes the idea that **extra** epochs are not always beneficial.

---

## Core Procedure

1. During training, **monitor** a metric on a **validation** set (e.g. validation **loss** or **accuracy**).
2. Track the **best** validation performance seen so far and **save** (or retain) the corresponding **weights**.
3. If validation performance **does not improve** for a set number of **epochs** or **steps** (**patience**), **stop** training.
4. **Return** the weights from the **best validation** epoch—not necessarily the final epoch.

This stops learning **before** the model spends long stretches **memorizing** noise and **fine-tuning** to training idiosyncrasies.

---

## Why Early Stopping Acts Like Regularization

- Stopping earlier **limits** how far optimization can drive parameters toward **very low** training loss.
- It **restricts** how **large** weights may grow and how **tightly** the model can fit **noise**.
- Effectively **biases** the solution toward **simpler** / **less over-trained** minima that often **generalize** better.

---

## Reading the Curves

- **Training loss** often **decreases** throughout training.
- **Validation loss** often **decreases** at first, reaches a **minimum**, then **rises** as overfitting sets in.
- Early stopping targets the parameters at (or near) the **minimum validation** region.

---

## Practical Considerations

- **Patience:** wait through **small** validation fluctuations so you do not stop on **noise** in the metric.
- **Checkpointing:** **restore** weights from the **best** validation epoch (standard practice).
- **Representative validation set:** early stopping is only as good as the validation distribution’s match to **real** deployment conditions.

---

## Summary

- **Early stopping** = monitor validation → stop when it **stops improving** (with patience) → keep **best** weights.
- **No** architecture change; pairs well with **L2**, **dropout**, **augmentation**, etc.
- **Next:** **Data augmentation** as a **data-level** strategy for generalization.

---

## Exam-style cues

- **Explain** early stopping as a form of regularization.
- **State** why the final epoch’s weights are not always the right choice.
- **Define** patience and best-checkpoint selection.
