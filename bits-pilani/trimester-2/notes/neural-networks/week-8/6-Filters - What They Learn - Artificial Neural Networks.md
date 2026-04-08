# 6-Filters - What They Learn - Artificial Neural Networks

## Learning Objectives

1. Interpret filters as learnable pattern detectors.
2. Contrast early-layer and deep-layer filters.
3. Explain how backprop learns useful filters from data.

---

## Core Concepts and Deep Notes

- Filters start random and are optimized by gradient descent through task loss.
- Early filters often detect edges/corners/color transitions.
- Middle/deep filters combine earlier activations into textures, parts, and semantic motifs.
- CNN strength comes from automatic feature learning rather than hand-crafted descriptors.

## Useful Shape Formulas

For input size `H x W`, kernel size `F`, padding `P`, stride `S`:

- Output height: `H_out = floor((H - F + 2P)/S) + 1`
- Output width: `W_out = floor((W - F + 2P)/S) + 1`
- With `K` filters, output depth = `K`

For pooling with window `F_p` and stride `S_p`, apply the same spatial formula per channel.

## Key Takeaways from the Lecture Transcription

- Hello everyone, welcome back to module 8 of Artificial Neural Networks.
- In this video, we will focus on understanding convolutional filters.
- By the end of this video, you will have a clear picture of what filters represent, how they learn to detect patterns and how the kinds of patterns learned by filters change as we move deeper into a convolutional neural network.
- Let's begin by clarifying what a filter actually is.
- A filter is simply a small set of learnable waves used in the convolution operation.
- However, instead of thinking of filters as just numbers, it is more useful to think of them as defining a pattern the network is looking for.

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
