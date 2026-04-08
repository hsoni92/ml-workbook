# 15-VGG  ResNet - Artificial Neural Networks

## Learning Objectives

1. Explain depth-driven progress from VGG to ResNet.
2. Describe degradation/optimization issues in very deep plain nets.
3. Explain how residual connections solve gradient-flow problems.

---

## Core Concepts and Deep Notes

- VGG used uniform stacks of 3x3 conv layers, proving depth with simple design can be powerful.
- Very deep plain networks face optimization degradation (higher training error despite more capacity).
- ResNet introduced shortcut/skip paths to learn residual mappings F(x)+x.
- Residual learning enables stable training of very deep models and became foundational for modern architectures.

## Useful Shape Formulas

For input size `H x W`, kernel size `F`, padding `P`, stride `S`:

- Output height: `H_out = floor((H - F + 2P)/S) + 1`
- Output width: `W_out = floor((W - F + 2P)/S) + 1`
- With `K` filters, output depth = `K`

For pooling with window `F_p` and stride `S_p`, apply the same spatial formula per channel.

## Key Takeaways from the Lecture Transcription

- Welcome back to Module 8 of Artificial Neural Networks.
- In this video, we will study two influential Convolutional Neural Network architectures, VGG and ResNet.
- By the end of this video, you will be able to understand why researchers began exploring deeper CNNs, what design ideas VGG introduced and how ResNet solved key challenges associated with training very deep networks.
- As we saw in earlier lessons, stacking convolutional layers allows CNNs to learn hierarchical representations.
- This naturally led researchers to ask whether simply making networks deeper would lead to better performance.
- Empirically, deeper CNNs often outperformed better on challenging visual tasks.

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
