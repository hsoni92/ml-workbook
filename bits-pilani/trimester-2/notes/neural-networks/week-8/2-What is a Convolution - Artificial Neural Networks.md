# What is a Convolution - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Define **convolution** in the CNN context.
2. Explain why it is useful for **spatial data** such as images.
3. Interpret convolution as a form of **local pattern matching**.
4. Distinguish between **filter/kernel**, **receptive field**, and **feature map**.

---

## Why Convolution Is Needed

Meaningful information in images is not usually carried by a single pixel in isolation. Instead, useful visual cues such as **edges**, **corners**, and **small textures** arise from relationships between **neighboring pixels**.

If we use a fully connected layer directly on an image:

- every input pixel is treated independently,
- the same pattern at two different locations looks like two unrelated cases,
- parameter count becomes very large.

So we need an operation that can detect the **same local pattern repeatedly across the image**. That is the role of convolution.

---

## Core Definition

A **convolution** applies a small learnable filter to a local region of the input and produces a response indicating how strongly that local region matches the pattern encoded by the filter.

In CNNs, the words **filter** and **kernel** are usually used interchangeably.

---

## Convolution as Pattern Matching

The most intuitive way to think about convolution is:

- the filter represents a pattern the network is trying to detect,
- the filter is compared with a small image patch,
- a strong match gives a large response,
- a weak match gives a small response.

So convolution answers the question:

**"Where in the image does this pattern appear strongly?"**

```text
good match between patch and filter -> strong response
poor match between patch and filter -> weak response
same pattern at another location    -> same filter can detect it there too
```

---

## Key Terms

| Term | Meaning | Important distinction |
|---|---|---|
| **Filter / kernel** | Small learnable weight matrix | The detector itself |
| **Local receptive field** | Small input region used for one output value | Not the whole image |
| **Weight sharing** | Same filter reused at all positions | Major reason CNNs are efficient |
| **Feature map** | Spatial grid of responses from one filter | One filter produces one feature map |

---

## Why Convolution Works Better Than Dense Layers

Convolution is well suited to images because it encodes two useful assumptions:

1. **Locality**: nearby pixels matter together.
2. **Reusability**: a useful pattern should be detectable anywhere, not only at one fixed position.

This gives CNNs a much better **inductive bias** for image data than a naive dense network.

---

## Mathematical Form

For one output location `(i, j)` in the single-channel case:

`y(i, j) = sum_u sum_v x(i+u, j+v) * w(u, v) + b`

You do not need to memorize the notation mechanically. The real idea is:

- take a local patch,
- multiply corresponding entries,
- sum them,
- add bias,
- store one output value.

---

## What Convolution Allows a CNN to Learn

- **Early layers** usually learn simple detectors such as edges or contrast transitions.
- **Deeper layers** combine earlier responses into textures, shapes, and object parts.
- The same learned detector can respond to a pattern even when the pattern shifts position.

This is one of the main reasons CNNs perform so well on spatial tasks.

---

## Common Confusions

- A convolution filter is **learned from data**; it is not usually handcrafted.
- One filter does **not** capture every useful pattern. CNNs use many filters.
- A first-layer filter usually does **not** detect full objects. It detects simple local structure.

---

## Summary

- Convolution is a **local operation** applied repeatedly across the input.
- It can be understood as **learned pattern matching**.
- **Weight sharing** makes detection efficient and reusable across positions.
- One filter produces one **feature map**, showing where that pattern appears.

**Bridge to the next note:** now that we know what convolution is conceptually, the next step is to see **how it is computed step by step**.
