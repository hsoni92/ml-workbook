# How Convolution Works - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Describe the convolution computation at **one spatial location**.
2. Explain how a filter **slides** across an image.
3. Interpret the output as a **feature map**.
4. Compute output dimensions from **kernel size**, **stride**, and **padding**.

---

## The Computation at One Location

A convolution begins with:

- an input image or feature map,
- a small filter (kernel),
- and a chosen spatial location.

At one location, the filter is placed on top of a small patch of the input. Then:

1. multiply corresponding input values and filter weights,
2. sum all those products,
3. add the bias,
4. write the result as **one output value**.

That single number tells us how strongly the filter matches that local region.

---

## Simple Numerical Intuition

Suppose we take a `3 x 3` image patch and a `3 x 3` filter. We multiply entries position by position and sum them.

The exact number is usually less important than its meaning:

- a **large response** means the patch resembles the learned pattern,
- a **small response** means the match is weak,
- the result summarizes one local comparison.

So each output cell is not arbitrary; it is a **local evidence score** for the pattern encoded by the filter.

---

## Sliding the Filter

The local computation above happens **repeatedly**, not just once.

After computing one output value:

- the filter shifts to the next valid location,
- the same multiplication-and-sum process is repeated,
- another output value is produced.

Collecting all these output values gives a **feature map**.

The crucial point is that the filter weights **do not change** as the filter moves. This reuse of the same weights is called **weight sharing**.

---

## Why Weight Sharing Matters

Weight sharing gives two major benefits:

1. **Fewer parameters** than a fully connected layer.
2. The same detector can recognize a pattern at different spatial locations.

So if a vertical edge appears on the left side of the image or the right side, the same filter can respond to both.

---

## From One Filter to One Feature Map

Each filter produces **one** two-dimensional output map. That map shows where the learned pattern appears strongly.

- **High values**: strong pattern match
- **Low values**: weak or no match

If a layer uses multiple filters, each filter creates its own feature map, and those maps are stacked together.

---

## Output Size Formula

For input height `H`, input width `W`, kernel size `K`, padding `P`, and stride `S`:

- `H_out = floor((H - K + 2P) / S) + 1`
- `W_out = floor((W - K + 2P) / S) + 1`

This formula matters because convolution does not just extract features; it also changes the **geometry** of the representation.

---

## What Each Parameter Controls

| Parameter | Main role | Practical effect |
|---|---|---|
| **Kernel size `K`** | Size of local neighborhood examined | Larger kernels see more context per step |
| **Stride `S`** | How far the filter moves each time | Larger stride reduces output size |
| **Padding `P`** | Extra border values around the input | Helps preserve edges and control size |
| **Number of filters** | Number of learned detectors | Sets output depth |

---

## Important Distinctions

- The **output depth** equals the **number of filters**, not the number of input channels.
- In standard 2D convolution, each filter spans **all input channels**.
- In deep learning libraries, the operation is often technically **cross-correlation**, but in ML it is still commonly called convolution.

---

## Summary

- Convolution works by repeated **local weighted sums**.
- One local computation gives **one output value**.
- Sliding the same filter across the input creates a **feature map**.
- Weight sharing is the key reason convolution is efficient and location-flexible.
- Output dimensions depend on **kernel size**, **stride**, and **padding**.

**Bridge to the next note:** once the computation is clear, the next question is what these outputs actually **mean**. That leads us to **feature maps**.
