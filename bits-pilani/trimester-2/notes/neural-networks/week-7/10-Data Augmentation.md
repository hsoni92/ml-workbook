# Data Augmentation – Artificial Neural Networks (Module 7)

## Learning Objectives

By the end of this video you will:

1. **Define** **data augmentation** and its **goal** (effective diversity without changing labels).
2. **Explain** **why** augmentation improves **generalization**, especially with **limited** data.
3. **Identify** common augmentations for **images**, **text**, and **audio** (examples from the lecture).
4. **Apply** domain judgment: augmentations must reflect **realistic** variation.

---

## Motivation: Limited Labeled Data

- Deep models usually need **large**, **diverse** data to generalize.
- Collecting **many** labels is often **expensive** or **infeasible**.
- **Small** datasets increase **overfitting** risk (memorizing specifics instead of **invariant** patterns).

---

## Key Idea

- **Artificially expand** the training set by applying **transformations** that **preserve the label**.
- Each transformed sample is treated as an **additional** training example.
- Exposes the model to **many plausible views** of the same underlying object or utterance → encourages **robust** features.

**Example (images):** flips, rotations, crops, blur, exposure/contrast changes—**if** they still depict the **same class**.

### Visual: one label many views

```text
  original image  →  flip  crop  jitter  ...  →  same class label y
```

---

## Why It Helps Generalization

- Increases **diversity** without changing the **task definition**.
- Reduces memorization of **exact** pixels/tokens/samples.
- Encourages **invariance** (or equivariance, depending on design) to **small realistic** input changes.
- Features learned tend to be **more stable** on **unseen** data.

---

## Modalities (Lecture Examples)

| Modality | Example augmentations |
|----------|------------------------|
| **Images** | Rotations, flips, cropping, color / lighting adjustments |
| **Text** | Synonym replacement, paraphrasing (must preserve meaning/label) |
| **Audio** | Noise injection, time shifting |

In **every** case: augmentations must **preserve** the **semantic label** and reflect **plausible** real-world variation.

---

## Caveats

- **Especially** useful when data are **small**.
- **Poor** augmentations (unrealistic or label-altering) can **confuse** the model and **hurt** performance.
- **Domain knowledge** is critical to choose **valid** transforms.

---

## Summary

- **Data augmentation** = label-preserving transforms → **more diverse** training signal.
- Complements **model-level** regularizers (L2, dropout, etc.) and is often central in strong **pipelines**.
- **Next:** **Training setup** (batch size, learning rate, capacity, validation monitoring).

---

## Exam-style cues

- **Define** data augmentation vs collecting more real data.
- **Give** two image augmentations and state when they would be **invalid** for a task.
- **Explain** how augmentation reduces overfitting.
