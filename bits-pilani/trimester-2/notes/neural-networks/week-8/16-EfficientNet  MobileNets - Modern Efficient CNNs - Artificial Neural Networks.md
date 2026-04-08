# 16-EfficientNet  MobileNets - Modern Efficient CNNs - Artificial Neural Networks

## Learning Objectives

1. Motivate efficiency as a first-class CNN objective.
2. Explain MobileNet high-level idea for low-resource deployment.
3. Explain EfficientNet compound scaling principle.

---

## Core Concepts and Deep Notes

- Deployment constraints (latency/memory/energy) require more than raw accuracy.
- MobileNets use lightweight convolution factorization to reduce compute while preserving useful features.
- EfficientNet scales depth, width, and resolution jointly instead of unbalanced single-axis scaling.
- Modern architecture design optimizes accuracy-efficiency trade-offs for real-world use cases.

## Useful Shape Formulas

For input size `H x W`, kernel size `F`, padding `P`, stride `S`:

- Output height: `H_out = floor((H - F + 2P)/S) + 1`
- Output width: `W_out = floor((W - F + 2P)/S) + 1`
- With `K` filters, output depth = `K`

For pooling with window `F_p` and stride `S_p`, apply the same spatial formula per channel.

## Key Takeaways from the Lecture Transcription

- Hello everyone, welcome back to module 8 of Artificial Neural Networks.
- In this video, we will look at modern convolutional neural network architectures that focus on efficiency.
- By the end of this video, you will be able to understand why efficiency has become an important design goal in CNNs and the core ideas behind two influential families of models, Mobile Nets and Efficient Net.
- Before we begin, it's important to note that we will study these architectures at a high level.
- The goal here is to build awareness of the key design ideas, not to go into architectural or implementation details.
- If you are interested in deeper understanding, I strongly encourage you to read the original research papers.

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
