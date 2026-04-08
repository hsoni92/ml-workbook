# 5-Channels  Multiple Filters - Artificial Neural Networks

## Learning Objectives

1. Explain convolution with multi-channel inputs (e.g., RGB).
2. Clarify why one filter still produces one output map.
3. Relate number of filters to output depth and representational richness.

---

## Core Concepts and Deep Notes

- For input HxWxC, each filter has spatial size FxF and depth C.
- Convolution is computed channel-wise and summed across channels at each spatial location.
- One filter -> one output feature map; K filters -> output depth K.
- As networks deepen, spatial size often decreases while depth increases to encode richer pattern families.

## Useful Shape Formulas

For input size `H x W`, kernel size `F`, padding `P`, stride `S`:

- Output height: `H_out = floor((H - F + 2P)/S) + 1`
- Output width: `W_out = floor((W - F + 2P)/S) + 1`
- With `K` filters, output depth = `K`

For pooling with window `F_p` and stride `S_p`, apply the same spatial formula per channel.

## Key Takeaways from the Lecture Transcription

- Welcome back to Module 8 of Artificial Neural Networks.
- In this video, we will extend our understanding of convolution to more realistic settings.
- By the end of this video, you will be able to understand what channels represent in CNN inputs and feature maps, how convolution operates on multichannel inputs, and why convolutional layers typically use multiple filters.
- So far, we have mostly talked about images as two-dimensional grids.
- However, real-world images usually have multiple channels.
- For example, grayscale images have a single channel, while RGB images have three channels, red, green, and blue.

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
