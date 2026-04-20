# Neural Networks - Module 8 Summary: Artificial Neural Networks

## Purpose of This Module

This module introduced **Convolutional Neural Networks (CNNs)** as the main neural architecture for **image and spatial data**.

The central question of the week was:

**Why do CNNs work so well on images, and how did their architecture evolve from early models to modern efficient designs?**

This module matters because it connects low-level mechanics such as convolution and pooling with high-level architectural ideas such as depth, residual learning, and efficiency-aware design.

---

## The Big Picture of Week 8

Week 8 can be understood as one connected progression:

1. **Why dense networks are not enough for images**
2. **How convolution detects local repeating patterns**
3. **How feature maps and channels build structured representations**
4. **How stride, padding, and pooling control geometry and robustness**
5. **How repeated CNN blocks create deep hierarchical feature learning**
6. **How CNN architectures evolved from early feasibility to scalable and efficient modern systems**

So the module is not just a list of terms. It is the story of how CNNs align model design with the structure of visual data.

---

## Core Ideas You Should Retain

### 1. Convolution exploits spatial structure

CNNs are effective because images contain:

- **local structure**,
- **repeating patterns**,
- and meaningful relationships between neighboring pixels.

Convolution captures this through:

- local connectivity,
- weight sharing,
- repeated pattern detection across positions.

### 2. Feature maps are learned spatial responses

Each filter produces one feature map showing where its learned pattern appears strongly.

As layers deepen:

- early maps represent simple patterns,
- later maps represent richer and more abstract structures.

### 3. Geometry is controlled intentionally

Stride, padding, and pooling determine how feature maps evolve:

- stride changes sampling density,
- padding manages border handling and output size,
- pooling reduces size and improves robustness to small shifts.

These are design choices, not implementation trivia.

### 4. CNNs are built from repeated blocks

A practical CNN is not just one convolution. It is a repeated pipeline of:

- convolution,
- optional normalization,
- activation,
- optional pooling.

Stacking these blocks creates hierarchical representations and larger effective receptive fields.

### 5. CNNs separate feature extraction from prediction

Convolutional layers learn spatial features.
The final prediction head combines those features into outputs such as class scores.

So a CNN can be viewed as:

`feature extractor + decision head`

---

## Architecture Evolution in One View

| Architecture | Main contribution |
|---|---|
| **LeNet** | Early practical proof that CNNs work |
| **AlexNet** | Large-scale breakthrough using deeper CNNs, GPUs, ReLU, and dropout |
| **VGG** | Showed the power of simple repeated depth |
| **ResNet** | Made very deep networks trainable with residual connections |
| **MobileNet** | Focused on lightweight design for constrained hardware |
| **EfficientNet** | Focused on balanced scaling for better efficiency |

This progression reflects a clear shift:

- **feasibility** -> **scale** -> **depth** -> **trainability** -> **efficiency**

---

## Exam-Ready Takeaways

- CNNs work well because they encode strong inductive biases for image data.
- **Locality**, **weight sharing**, and **hierarchical representation learning** are the key ideas.
- One filter gives one feature map; many filters give depth.
- Stride, padding, and pooling control how spatial information changes across layers.
- Deeper networks learn more abstract structure, but depth must remain trainable.
- Modern architecture design balances **accuracy**, **optimization**, and **deployment constraints**.

---

## Bridge to the Next Module

So far, the course has focused on models for **spatial data**, especially images.

The next module shifts to a different kind of structure: **sequential and temporal data**, where the order of inputs matters.

There, the main question changes from:

- "How do we exploit spatial locality?"

to:

- "How do we model dependencies across time and sequence order?"

You will therefore move from CNNs to **sequence models** such as **RNNs**, **LSTMs**, and **GRUs**, along with the motivation for **attention** and later transformer-based ideas.
