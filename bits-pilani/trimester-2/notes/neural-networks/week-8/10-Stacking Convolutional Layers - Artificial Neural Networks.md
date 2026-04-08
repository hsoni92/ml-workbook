# 10-Stacking Convolutional Layers - Artificial Neural Networks

## Learning Objectives

1. Explain why one conv layer is insufficient for complex semantics.
2. Describe hierarchical representation from shallow to deep layers.
3. Define receptive field growth through layer stacking.

---

## Core Concepts and Deep Notes

- Shallow layers detect primitives; deeper layers compose them into complex structures.
- Each additional layer sees features from previous layers, effectively increasing context/receptive field.
- Depth enables abstraction and class-discriminative representations for tasks like object recognition.
- Common pattern: lower spatial size + higher channel depth as we go deeper.

## Useful Shape Formulas

For input size `H x W`, kernel size `F`, padding `P`, stride `S`:

- Output height: `H_out = floor((H - F + 2P)/S) + 1`
- Output width: `W_out = floor((W - F + 2P)/S) + 1`
- With `K` filters, output depth = `K`

For pooling with window `F_p` and stride `S_p`, apply the same spatial formula per channel.

## Key Takeaways from the Lecture Transcription

- Hello everyone, welcome back to module 8 of Artificial Neural Networks.
- In this video, we will focus on why convolutional neural networks use multiple convolutional layers.
- By the end of this video, you will be able to understand how stacking convolutional layers builds hierarchical representations and how increasing depth allows CNNs to capture increasingly complex patterns in the data.
- Let's begin by considering what a single convolutional layer can achieve.
- A single convolutional layer is effective at detecting simple local patterns such as edges or basic textures.
- However, real-world images contain much more complex structures.

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
