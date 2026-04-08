# 11-Fully Connected Layers After Convs - Artificial Neural Networks

## Learning Objectives

1. Explain the transition from spatial feature maps to final predictions.
2. Define flattening and what it does/does not learn.
3. Describe roles of feature extractor vs classifier head.

---

## Core Concepts and Deep Notes

- Conv stack outputs HxWxC feature tensors that encode what+where information.
- Flatten reshapes to vector (length H*W*C) without learnable parameters.
- Fully connected layers aggregate global evidence to produce logits/regression outputs.
- Pipeline view: convolutional backbone (feature extraction) + dense head (decision making).

## Useful Shape Formulas

For input size `H x W`, kernel size `F`, padding `P`, stride `S`:

- Output height: `H_out = floor((H - F + 2P)/S) + 1`
- Output width: `W_out = floor((W - F + 2P)/S) + 1`
- With `K` filters, output depth = `K`

For pooling with window `F_p` and stride `S_p`, apply the same spatial formula per channel.

## Key Takeaways from the Lecture Transcription

- Welcome back to module 8 of Artificial Neural Networks.
- In this video, we will study the role of fully connected layers in convolutional neural networks.
- By the end of this video, you will be able to understand why fully connected layers are used after convolutional layers, how spatial feature maps are converted into predictions, and how this transition from the convolutional neural networks are used after convolutional neural networks.
- Let's begin by recalling what convolutional layers gives us.
- After passing through several convolutional blocks, the network produces feature maps.
- These feature maps preserve spatial structure and contain multiple channels, each corresponding to a different learned pattern.

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
