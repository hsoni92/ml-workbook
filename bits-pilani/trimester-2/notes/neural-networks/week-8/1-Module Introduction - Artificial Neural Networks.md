# Neural Networks - Module 8 Introduction: Artificial Neural Networks

## Learning Objectives

By the end of this module, you should be able to:

1. Explain why **fully connected networks** are a poor fit for image data at scale.
2. Describe how **convolution**, **weight sharing**, and **local connectivity** exploit spatial structure.
3. Distinguish clearly between **filters**, **feature maps**, **channels**, **stride**, **padding**, and **pooling**.
4. Trace how a CNN transforms raw pixels into increasingly abstract representations.
5. Compare major CNN families from **LeNet** to **ResNet**, **MobileNet**, and **EfficientNet**.

---

## Why We Need a New Architecture

So far, the course has focused mainly on **fully connected neural networks**, where the input is treated as a flat vector. That assumption is reasonable for many tabular problems, but it is restrictive for images.

Images have two important properties:

1. **Spatial locality**: neighboring pixels are related, and meaningful patterns such as edges and corners arise from small local groups of pixels.
2. **Pattern repetition**: the same useful pattern can appear at many different locations in the image.

A dense network does not naturally exploit either of these properties. It treats each input position separately and quickly becomes expensive as image size grows.

---

## Why Dense Layers Struggle on Images

If we flatten an image into one long vector, we lose the idea that nearby pixels belong together. This causes two problems:

- The model does not explicitly capture **local neighborhood structure**.
- The number of parameters grows very quickly, making training inefficient and data-hungry.

For image-like data, this is wasteful because we already know that visual patterns are usually **local** and often **repeat** across positions.

---

## The Core CNN Idea

Convolutional Neural Networks (CNNs) are designed specifically for **spatial data**. They address the limitations above through three core ideas:

- **Local connectivity**: a neuron looks only at a small region of the input instead of the entire image.
- **Weight sharing**: the same filter is reused across many spatial locations.
- **Hierarchical feature learning**: simple patterns are learned first, then combined into more complex ones in deeper layers.

This means a CNN learns **what** to detect without having to relearn the same detector separately for every location.

---

## Intuition: From Pixels to Meaning

CNNs usually build representations in stages:

- **Early layers** detect simple patterns such as edges, corners, and basic contrast changes.
- **Middle layers** combine these into textures, curves, and repeated motifs.
- **Deeper layers** combine earlier features into shapes, parts, and more semantic structures.

This is why CNNs are often described as learning a **hierarchy of features**.

---

## What This Module Covers

This week follows a natural progression:

| Stage | Main question | What you should learn |
|---|---|---|
| Convolution basics | What is convolution? | Local pattern matching with shared weights |
| Feature representation | What do filters and feature maps mean? | How learned detectors create spatial responses |
| Geometry control | What do stride and padding do? | How feature-map size changes across layers |
| Compression | Why pooling? | Downsampling and small-shift robustness |
| Architecture building | How do blocks combine? | Full CNN pipeline from input to prediction |
| Historical evolution | How did CNNs improve over time? | LeNet, AlexNet, VGG, ResNet, MobileNet, EfficientNet |

---

## Big-Picture Flow

```text
Image
  -> convolutional filters detect local patterns
  -> multiple feature maps are formed
  -> activations and pooling shape the representation
  -> stacked layers grow abstraction and receptive field
  -> final feature tensor is converted into predictions
```

---

## Why This Module Matters

CNNs became the foundation of modern computer vision because they align the model architecture with the structure of the data. They are more parameter-efficient than naive dense models, learn reusable pattern detectors, and build rich representations layer by layer.

Even when later architectures become more sophisticated, these CNN ideas remain central:

- exploit structure in the data,
- build hierarchical representations,
- balance accuracy with computation and memory.

---

## Module Takeaways

- Images should not be treated as just unordered vectors.
- CNNs use **locality** and **weight sharing** to learn efficiently.
- Deeper CNNs turn low-level visual signals into higher-level concepts.
- Architectural choices affect not just accuracy, but also optimization, memory, and deployment cost.

**Bridge to the next note:** the first building block behind all of this is the **convolution operation** itself.
