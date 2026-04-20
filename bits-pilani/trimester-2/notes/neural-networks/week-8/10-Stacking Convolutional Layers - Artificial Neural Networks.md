# Stacking Convolutional Layers - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain why a single convolutional layer is not enough for complex vision tasks.
2. Describe how stacking layers creates **hierarchical representations**.
3. Explain how depth increases the **effective receptive field**.
4. Discuss why deeper networks need careful architectural design.

---

## Why Stack Layers at All?

A single convolutional layer is good at detecting simple local patterns such as:

- edges,
- corners,
- basic textures.

But real images contain much more complex structure. To recognize an object, the network must combine many simpler cues into more meaningful patterns.

That is why CNNs stack multiple convolutional layers instead of relying on only one.

---

## The Main Idea: Hierarchical Feature Learning

When layers are stacked, the output of one layer becomes the input to the next.

This naturally creates a hierarchy:

- **early layers** detect simple visual primitives,
- **middle layers** combine them into textures, motifs, and repeated structures,
- **deeper layers** combine those into object parts and higher-level evidence.

So depth allows the network to move from **simple local patterns** to **complex semantic structure**.

---

## Growing Context: The Receptive Field Idea

A deeper layer does not look at raw pixels directly. It looks at feature maps that already summarize local regions from previous layers.

As a result, deeper units are influenced by a larger portion of the original input. This is often described as a larger **effective receptive field**.

Intuition:

- one layer sees a small local patch,
- the next layer sees combinations of nearby patches,
- deeper layers indirectly summarize a much larger region of the image.

This is one reason stacked CNNs can represent whole shapes and object parts instead of only tiny edges.

---

## How the Representation Changes with Depth

As a CNN becomes deeper, two trends are common:

1. **Spatial dimensions decrease** because of stride or pooling.
2. **Feature depth increases** because more filters are used.

This means the network gradually trades:

- exact positional detail,
- for richer and more abstract feature representation.

You can think of this as moving from "Where exactly is every small edge?" to "What higher-level structure is present?"

---

## Example Intuition

In a simple image classifier:

- the first hidden layers may respond to edge directions,
- later layers may respond to fur-like textures or curved outlines,
- still deeper layers may combine those into evidence for categories such as dog, cat, or bird.

The important point is that no single layer does everything. Recognition emerges through **progressive composition**.

---

## Why More Depth Is Not Always Trivial

Depth is powerful, but adding layers blindly does not automatically improve a model.

Very deep plain networks may become harder to optimize because:

- gradients can weaken,
- training can become unstable,
- added layers may not be used effectively.

This is why later architectures such as **ResNet** introduced skip connections to make depth easier to train.

---

## Summary

- A single convolutional layer captures only limited local structure.
- Stacking layers enables **hierarchical feature learning**.
- Deeper layers effectively see larger input regions through growing receptive fields.
- CNN depth usually trades spatial precision for semantic richness.
- Depth helps only when the architecture remains trainable.

**Bridge to the next note:** after stacking convolutional layers, the next question is how these spatial feature maps are converted into the final prediction. That leads to **fully connected layers after convolutions**.
