# 1-Module Introduction - Artificial Neural Networks

## Learning Objectives

1. Explain why MLP-style fully connected modeling is inefficient for images.
2. Define spatial locality, weight sharing, and hierarchical feature learning.
3. Motivate the full CNN pipeline covered in this module.

---

## Core Concepts and Deep Notes

- Images have local correlation: nearby pixels jointly form meaningful patterns (edges/corners/textures).
- The same visual pattern can occur at many locations; this motivates reusing one detector across positions.
- CNNs replace dense all-to-all connections with local receptive fields + shared filters, reducing parameters and improving sample efficiency.
- Representation hierarchy: low-level primitives -> motifs/textures -> object parts -> semantic objects.

## Useful Shape Formulas

For input size `H x W`, kernel size `F`, padding `P`, stride `S`:

- Output height: `H_out = floor((H - F + 2P)/S) + 1`
- Output width: `W_out = floor((W - F + 2P)/S) + 1`
- With `K` filters, output depth = `K`

For pooling with window `F_p` and stride `S_p`, apply the same spatial formula per channel.

## Key Takeaways from the Lecture Transcription

- Welcome to module 8 of Artificial Neural Networks.
- In this module, we will study a new class of models designed specifically for spatial data, convolutional neural networks, that power the modern computer vision system.
- So far in this course, we have focused primarily on fully connected neural networks.
- We studied how multilayer perceptrons learn representations, how information flows forward through layers, and how these models are trained using backpropagation and optimization techniques.
- A key assumption in all of this was that the input is treated as a flat vector.
- Each input dimension is handled independently without any notion of structure or relationships between neighboring inputs.

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
