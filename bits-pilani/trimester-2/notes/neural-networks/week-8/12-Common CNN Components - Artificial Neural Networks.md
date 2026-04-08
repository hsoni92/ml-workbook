# 12-Common CNN Components - Artificial Neural Networks

## Learning Objectives

1. List common supporting components in practical CNNs.
2. Explain placement and role of activation, batch norm, and dropout.
3. Relate component choices to optimization stability and generalization.

---

## Core Concepts and Deep Notes

- Nonlinear activations prevent stacked convolutions from collapsing to a linear map.
- BatchNorm (typically after conv, before activation) stabilizes training dynamics and often regularizes.
- Dropout is mainly used in dense layers in CNN pipelines; too much dropout in conv blocks can hurt spatial learning.
- Modern CNN quality depends on well-composed blocks, not only number of conv layers.

## Useful Shape Formulas

For input size `H x W`, kernel size `F`, padding `P`, stride `S`:

- Output height: `H_out = floor((H - F + 2P)/S) + 1`
- Output width: `W_out = floor((W - F + 2P)/S) + 1`
- With `K` filters, output depth = `K`

For pooling with window `F_p` and stride `S_p`, apply the same spatial formula per channel.

## Key Takeaways from the Lecture Transcription

- Welcome back to Module 8 of Artificial Neural Networks.
- In this video, we will look at several components that are commonly used in modern convolutional neural networks.
- By the end of this video, you will be able to identify the components used in CNNs, understand where they are placed within the pipelines, and explain how they contribute to effective learning and good generalization.
- So far, we have focused mainly on convolutional layers and how they extract spatial features.
- However, modern CNNs are rarely built using convolutions alone.
- Additional components are introduced to make training more stable, improve generalization, and enable deeper architectures.

## Common Exam Pitfalls

- Confusing local feature extraction (convolutional layers) with global decision making (final dense layers).
- Ignoring shape transformations across layers; always track spatial size and channel depth.
- Treating architectural choices as isolated; in practice, filter count, stride, padding, pooling, and normalization interact.

## Summary

- This note captures the lecture's core idea, operational mechanics, and design trade-offs for exam-ready understanding.
- Revise with formulas, block-level intuition, and architecture-level reasoning together for stronger conceptual clarity.

## Exam-Style Cues

- Define the central concept in one precise paragraph.
- Draw a small forward-pass example and explain dimensional changes at each stage.
- Contrast this topic with a closely related concept and justify when each is preferable.
- State one practical design trade-off and its effect on accuracy, compute, and generalization.
