# 4-Feature Maps - Extracting Patterns from Images - Artificial Neural Networks

## Learning Objectives

1. Define feature maps and interpret their values spatially.
2. Connect one filter to one feature map.
3. Explain why deeper feature maps become more abstract.

---

## Core Concepts and Deep Notes

- Feature maps are response maps, not raw pixel images.
- Each map preserves where a pattern occurs, not just whether it occurs.
- Multiple filters yield multiple maps, each highlighting different cues (edges, textures, orientation-specific structures).
- In deeper layers, maps encode combinations of earlier primitives (hierarchical abstraction).

## Useful Shape Formulas

For input size `H x W`, kernel size `F`, padding `P`, stride `S`:

- Output height: `H_out = floor((H - F + 2P)/S) + 1`
- Output width: `W_out = floor((W - F + 2P)/S) + 1`
- With `K` filters, output depth = `K`

For pooling with window `F_p` and stride `S_p`, apply the same spatial formula per channel.

## Key Takeaways from the Lecture Transcription

- Welcome back to Module 8 of Artificial Neural Network.
- In this video, we focus on understanding feature maps.
- By the end of this video, you will be able to explain what a feature map represents, how feature maps capture spatial patterns in an image, and how they relate to the filters learned by a convolutional neural network.
- From the previous video, we know that a convolution applies a filter across an image and produces a grid of output values.
- Each of these values comes from a local computation between the filter and a small region of the image.
- When we collect all these output values together, we obtain what is called a feature map.

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
