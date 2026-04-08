# 14-LeNet - AlexNet  Early CNN Breakthroughs - Artificial Neural Networks

## Learning Objectives

1. Understand why early CNNs were limited despite good ideas.
2. Explain LeNet contributions and architecture pattern.
3. Explain why AlexNet was a turning point in deep learning.

---

## Core Concepts and Deep Notes

- LeNet established end-to-end conv+pool+dense learning for vision (notably digit recognition).
- Historical bottlenecks: smaller datasets, limited compute, weaker training ecosystems.
- AlexNet scaled depth/width and leveraged ReLU, GPU training, and dropout.
- Breakthrough impact: CNNs surpassed traditional feature-engineering pipelines at scale.

## Useful Shape Formulas

For input size `H x W`, kernel size `F`, padding `P`, stride `S`:

- Output height: `H_out = floor((H - F + 2P)/S) + 1`
- Output width: `W_out = floor((W - F + 2P)/S) + 1`
- With `K` filters, output depth = `K`

For pooling with window `F_p` and stride `S_p`, apply the same spatial formula per channel.

## Key Takeaways from the Lecture Transcription

- Hello everyone, welcome back to module 8 of Artificial Neural Networks.
- In this video, we will study the early evolution of convolutional neural networks.
- By the end of this video, you will be able to understand the historical context behind CNNs, the key ideas demonstrated by Leeneth, and why AlexNet marked a major breakthrough that revived the interest in deep learning.
- The core ideas behind convolutional neural networks existed well before the recent deep learning boom.
- However, early CNNs were typically shallow, trained on small datasets, and applied to relatively constrained problems.
- At the time, limited computational power and lack of large label datasets made it difficult to train deep models effectively.

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
