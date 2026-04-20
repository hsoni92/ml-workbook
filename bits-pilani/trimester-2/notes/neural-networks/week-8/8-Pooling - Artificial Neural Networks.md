# Pooling - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain what **pooling** is and why CNNs use it.
2. Distinguish between **max pooling** and **average pooling**.
3. Explain how pooling changes **height**, **width**, and **channels**.
4. Contrast pooling with **strided convolution**.

---

## Why Pooling Is Introduced

After convolution, feature maps often still contain a lot of fine-grained spatial detail. But in many visual tasks, tiny shifts in position should not completely change the model's decision.

For example, if an edge or texture moves slightly, we usually still want the network to recognize that the pattern is present.

Pooling is introduced to help the network focus more on:

- **whether** a pattern exists,
- and a little less on its exact pixel-level location.

This makes the representation more compact and often more robust.

---

## What Pooling Does

Pooling looks at a small local region of a feature map and replaces that region with a summary value.

Important properties:

- pooling is applied **independently to each channel**,
- pooling has **no learnable parameters**,
- pooling usually reduces **height** and **width**,
- pooling usually keeps the **number of channels unchanged**.

So pooling is a fixed summarization step, not a learned feature detector.

---

## Common Types of Pooling

### Max pooling

Takes the **largest** value in the local window.

Interpretation:

- if one strong activation appears in the region, max pooling keeps that strong evidence,
- this is useful when the presence of a feature matters more than exact placement.

### Average pooling

Takes the **mean** value in the local window.

Interpretation:

- produces a smoother summary of the region,
- keeps average activation strength rather than only the strongest response.

---

## Why Pooling Helps

Pooling provides three practical benefits:

1. **Downsampling**: reduces the spatial size of feature maps.
2. **Efficiency**: smaller feature maps reduce later computation.
3. **Small-shift robustness**: slight translations or distortions matter less.

For example, a `2 x 2` pooling operation with stride `2` usually halves both height and width.

---

## Pooling vs Strided Convolution

Both pooling and strided convolution reduce spatial resolution, but they do not mean the same thing.

| Operation | Nature | Main role |
|---|---|---|
| **Pooling** | Fixed summarization | Downsampling and local robustness |
| **Strided convolution** | Learned operation | Downsampling while also learning new features |

So pooling says, "summarize what is already there," while strided convolution says, "learn features while reducing size."

---

## What Pooling Does Not Do

- It does **not** increase the number of channels.
- It does **not** learn new weights.
- It does **not** always help in every architecture or task.

Excessive pooling can remove too much spatial detail, which may be harmful when precise localization matters.

---

## Summary

- Pooling summarizes local regions of feature maps.
- **Max pooling** keeps the strongest activation; **average pooling** keeps the mean.
- Pooling reduces spatial size, keeps channels unchanged, and improves robustness to small shifts.
- It is parameter-free and differs from strided convolution, which performs learned downsampling.

**Bridge to the next note:** now that filters, stride, padding, and pooling are clear individually, the next step is to see how they work **together inside a convolutional block**.
