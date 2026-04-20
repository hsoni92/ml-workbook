# End to End Example - Simple CNN Architecture - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Trace the forward pass of a simple CNN from input to output.
2. Explain the role of each stage in the pipeline.
3. Relate shape changes to representation changes.
4. See how most CNN architectures are variations of the same high-level blueprint.

---

## Why an End-to-End Example Helps

By this point, the individual CNN components should be familiar:

- convolution,
- feature maps,
- pooling,
- activations,
- fully connected layers.

But exam understanding requires more than isolated definitions. You should also be able to explain how these components form one coherent pipeline from **raw image** to **final prediction**.

---

## The Problem Setting

Suppose we are given an image and want to predict:

- a class label, or
- some other output such as a regression value.

To do that, the network must:

1. extract useful spatial patterns,
2. compress and organize them,
3. combine them into a global decision.

That is exactly what a CNN pipeline is built to do.

---

## A Simple CNN Pipeline

```text
input image
  -> convolution + batch normalization + activation
  -> pooling
  -> deeper convolution blocks
  -> final feature maps
  -> flattening (or global pooling)
  -> fully connected layers
  -> output prediction
```

This basic structure appears in many CNNs, even when the details become more sophisticated.

---

## Stage-by-Stage Intuition

### 1. Early feature extraction

The first convolutional layers detect simple local patterns such as:

- edges,
- corners,
- small textures.

At this stage, the network is learning the visual building blocks of the input.

### 2. Controlled downsampling

Pooling or strided operations reduce spatial resolution.

This:

- lowers computation,
- makes features more compact,
- and increases robustness to small spatial shifts.

### 3. Higher-level representation

Deeper convolutional layers combine earlier features into richer patterns and more abstract structures.

As the network goes deeper:

- exact location becomes less important,
- semantic meaning becomes more important.

### 4. Prediction head

After the final feature maps are produced, they are converted into a form suitable for global reasoning:

- flattened into a vector, or
- summarized through global pooling.

Then dense layers or another prediction head produce the final output.

---

## Example Shape Trace

A simple illustrative flow might look like:

`32 x 32 x 3 -> 32 x 32 x 32 -> 16 x 16 x 32 -> 16 x 16 x 64 -> 8 x 8 x 64 -> vector -> logits`

The key pattern is:

- **height and width shrink** over time,
- **feature depth often grows**,
- representation becomes more abstract and task-oriented.

---

## The Most Important Insight

The final prediction depends on the entire network, not only the last layer.

Earlier layers matter because they determine what information is available to later layers. CNNs are trained **end to end**, so every stage is shaped by the final task objective.

That is why even a simple CNN should be understood as one connected system rather than as unrelated parts.

---

## Summary

- A CNN follows a structured flow from raw pixels to prediction.
- Early layers detect local patterns; deeper layers build richer abstractions.
- Pooling and stride control representation size and robustness.
- Flattening or global pooling bridges the convolutional backbone to the prediction head.
- Most real CNN architectures are expanded or improved versions of this same overall pattern.

**Bridge to the next note:** after understanding the basic pipeline, the next step is to see how CNN architectures evolved historically, starting with **LeNet** and **AlexNet**.
