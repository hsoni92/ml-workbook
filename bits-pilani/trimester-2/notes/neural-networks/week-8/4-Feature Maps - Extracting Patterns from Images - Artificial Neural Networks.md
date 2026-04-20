# Feature Maps - Extracting Patterns from Images - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain what a **feature map** represents.
2. Interpret high and low activations in a feature map.
3. Relate **one filter** to **one feature map**.
4. Describe how feature maps become more abstract in deeper CNN layers.

---

## What Is a Feature Map?

When a convolutional filter is applied across an image, it produces a grid of output values. That grid is called a **feature map**.

A feature map can be understood as a **spatial response map**:

- high values indicate places where the filter matches strongly,
- low values indicate weak or no match.

So a feature map does not merely say **whether** a pattern exists. It also tells us **where** it appears.

---

## Why Feature Maps Matter

Feature maps are important because they preserve **spatial structure** while transforming the original input into a more useful representation.

This is a big advantage over flattening early:

- the network keeps track of location,
- different patterns can be separated into different channels,
- later layers can build on these structured responses.

In short, feature maps let CNNs learn progressively richer representations without immediately discarding spatial information.

---

## One Filter, One Map

Each convolutional filter is trained to detect a particular kind of pattern. When one filter is applied to an image, it produces exactly **one feature map**.

Examples:

- one filter may respond strongly to **vertical edges**,
- another may respond to **horizontal edges**,
- another may respond to **simple textures**.

Using multiple filters gives multiple feature maps, each highlighting a different aspect of the input.

```text
input image
  -> filter A detects one pattern -> feature map A
  -> filter B detects another     -> feature map B
  -> filter C detects another     -> feature map C
stack the maps -> richer representation for the next layer
```

---

## Feature Maps Are Not Raw Images

This is an important distinction:

- an image stores **pixel intensities**,
- a feature map stores **responses of a learned detector**.

So feature maps are not ordinary images in the usual sense. They are **learned representations** of what patterns the network has found useful.

---

## What Changes with Depth

Feature maps in different layers carry different kinds of information:

| Layer depth | Typical patterns represented | Interpretation |
|---|---|---|
| **Early layers** | Edges, corners, contrast changes | Low-level visual structure |
| **Middle layers** | Textures, curves, repeated motifs | Intermediate composition |
| **Deeper layers** | Object parts or more semantic combinations | Higher-level abstraction |

This is one of the clearest ways to understand **hierarchical feature learning** in CNNs.

---

## How to Read a Feature Map Intuitively

- **Sparse high activations** often mean the filter is selective and responds only where its pattern is present.
- **Mostly low activations** may mean the pattern is absent or the filter is not very useful.
- **Widespread activations** can indicate a broadly matching or less selective pattern.

The key point is that an activation value is evidence of a **pattern match**, not a final prediction by itself.

---

## Common Confusions

- Feature maps are **learned**, not handcrafted.
- A high feature-map value does **not** directly mean a class label has been predicted.
- Multiple feature maps together form the representation used by deeper layers.

---

## Summary

- A feature map is the output of applying **one filter** across the input.
- It shows **where** a learned pattern appears strongly.
- Feature maps preserve spatial organization while transforming the data.
- As CNN depth increases, feature maps usually become more **abstract** and **semantic**.

**Bridge to the next note:** once feature maps are clear, the next step is to understand how CNNs handle **multiple input channels** and why they use **multiple filters** at each layer.
