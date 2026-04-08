# 7-Stride  Padding - Controlling Output Size - Artificial Neural Networks

## Learning Objectives

1. Explain stride and its effect on sampling density.
2. Explain padding and border-information preservation.
3. Compute output shape under stride/padding choices.

---

## Core Concepts and Deep Notes

- Larger stride skips positions, reducing output resolution and compute cost.
- Padding adds border values (usually zeros) so edge regions are processed more fairly.
- "Same"-style padding helps preserve spatial dimensions; no padding shrinks maps quickly across layers.
- Design trade-off: efficiency vs fine spatial detail retention.

## Useful Shape Formulas

For input size `H x W`, kernel size `F`, padding `P`, stride `S`:

- Output height: `H_out = floor((H - F + 2P)/S) + 1`
- Output width: `W_out = floor((W - F + 2P)/S) + 1`
- With `K` filters, output depth = `K`

For pooling with window `F_p` and stride `S_p`, apply the same spatial formula per channel.

## Key Takeaways from the Lecture Transcription

- Hello everyone, welcome back to module 8 of Artificial Neural Networks.
- In this video, we will study two important design choices in convolutional layers, stride and padding.
- By the end of this video, you will be able to understand how stride affects the movement of the filter, why padding is introduced and how these choices control the spatial size of feature maps.
- Each convolution operation changes the spatial dimension of its input.
- If we apply multiple convolutions without careful design, feature maps can shrink very quickly.
- This makes output size an important design consideration rather than a side effect of convolution.

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
