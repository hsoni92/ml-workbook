# EfficientNet and MobileNets: Modern Efficient CNNs - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain why **efficiency** became a major design goal in CNNs.
2. Describe the core idea behind **MobileNet**.
3. Describe the core idea behind **EfficientNet**.
4. Explain why modern architecture design balances **accuracy**, **computation**, and **deployability**.

---

## Why Efficiency Matters

Earlier CNN discussions often focused mainly on accuracy. But real systems are deployed under constraints such as:

- limited memory,
- limited compute,
- latency requirements,
- power constraints on mobile or edge devices.

In such settings, a highly accurate model may still be impractical if it is too large or too slow.

So modern CNN design is not only about "Can this model predict well?" It is also about:

**"Can this model run where we actually need it?"**

---

## MobileNet: Efficiency Through Lightweight Convolution

MobileNet was designed for resource-constrained environments such as smartphones and edge devices.

Its key idea is to reduce computation by separating two things that standard convolution does together:

1. **spatial filtering**,
2. **channel mixing**.

This is done through **depthwise separable convolution**.

### Intuition

```text
standard convolution:
  learns spatial and channel interactions in one expensive step

depthwise separable convolution:
  1) depthwise convolution handles spatial filtering per channel
  2) pointwise 1 x 1 convolution mixes information across channels
```

This greatly reduces parameter count and computation while preserving much of the useful representational ability.

---

## EfficientNet: Efficiency Through Better Scaling

EfficientNet approaches efficiency from a different angle.

Instead of changing one operation inside the network, it asks:

**How should we scale a CNN when we want a larger model?**

Traditionally, models were often scaled in an unbalanced way:

- only deeper,
- or only wider,
- or only with higher input resolution.

EfficientNet argues that better performance comes from scaling **depth**, **width**, and **resolution** together in a balanced way. This is called **compound scaling**.

---

## Why Balanced Scaling Helps

If we scale only one dimension, we may underuse the others:

- more depth alone may not use resolution efficiently,
- more width alone may saturate quickly,
- more resolution alone can raise compute sharply without enough model capacity.

EfficientNet's contribution is the idea that scaling should be **coordinated**, not arbitrary.

So the model becomes larger in a more principled way for a given computational budget.

---

## MobileNet vs EfficientNet

| Model family | Main question | Core idea |
|---|---|---|
| **MobileNet** | How do we make convolution itself cheaper? | Use lightweight depthwise separable convolution |
| **EfficientNet** | How do we scale a CNN more intelligently? | Use balanced compound scaling |

Both aim for better efficiency, but they attack the problem from different angles.

---

## Bigger Design Lesson

These models reflect a broader shift in CNN thinking:

- earlier architectures emphasized representation power and depth,
- modern architectures must also account for deployability.

So architecture choice now depends not only on benchmark accuracy, but also on where the model will run and how much cost is acceptable.

---

## Common Confusions

- Lower FLOPs do not always guarantee lower real-world latency on every hardware platform.
- An efficient model is not automatically the best choice for every deployment target.
- The purpose of this topic is high-level architectural understanding, not detailed implementation memorization.

---

## Summary

- Modern CNN design must balance **accuracy** with **efficiency**.
- **MobileNet** reduces cost through lightweight convolutional design.
- **EfficientNet** improves scaling through a balanced strategy across depth, width, and resolution.
- These architectures show that better models are not only deeper or wider, but often **smarter in design**.

**Bridge to the next note:** the final step for this module is to connect all these ideas into one unified **module summary**.
