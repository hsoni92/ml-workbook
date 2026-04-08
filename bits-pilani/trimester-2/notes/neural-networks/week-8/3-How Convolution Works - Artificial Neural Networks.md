# 3-How Convolution Works - Artificial Neural Networks

## Learning Objectives

1. Compute convolution output at one location.
2. Explain sliding across all valid positions to build a feature map.
3. Relate weight sharing to parameter efficiency and generalization.

---

## Core Concepts and Deep Notes

- Per-position computation: elementwise multiply patch and kernel, then sum products (plus bias in practice).
- Repeating this over positions forms a 2D feature map of responses.
- High feature-map values indicate strong local matches to the filter pattern.
- Output-size intuition (no padding): (H-F+1) x (W-F+1) for stride 1; with stride/padding use general formula below.

## Useful Shape Formulas

For input size `H x W`, kernel size `F`, padding `P`, stride `S`:

- Output height: `H_out = floor((H - F + 2P)/S) + 1`
- Output width: `W_out = floor((W - F + 2P)/S) + 1`
- With `K` filters, output depth = `K`

For pooling with window `F_p` and stride `S_p`, apply the same spatial formula per channel.

## Key Takeaways from the Lecture Transcription

- Welcome back to Module 8 of Artificial Neural Networks.
- In this video, we will focus on how the convolution operation works in practice.
- By the end of this video, you will be able to explain how a convolution is computed step by step, understand how a filter moves across an image, and you will be able to interpret how these local computations together form an output feature map.
- Let's begin by looking at the components involved in a convolution.
- A convolution takes an input image or feature map and a small grid of learnable weights called a filter or kernel.
- The filter is much smaller than the image and contains the parameters that the network learns.

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
