# Putting it Together - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Describe a typical **convolutional block**.
2. Explain the role of **convolution**, **activation**, **stride/padding**, and **pooling** together.
3. Track how the tensor shape changes through a block.
4. Discuss the trade-off between **representation power** and **spatial resolution**.

---

## Why This Note Matters

Understanding each CNN component in isolation is useful, but real networks are not built as disconnected operations. In practice, CNNs are built by **repeating small blocks of operations**.

So the real question is not only:

**"What does convolution do?"**

but also:

**"How do all these pieces work together as data flows through the network?"**

---

## A Typical Convolutional Block

A common CNN block looks like:

`Convolution -> BatchNorm (optional) -> Activation -> Pooling (optional)`

Not every architecture uses exactly the same sequence, but this pattern captures the main idea.

---

## Role of Each Component

### 1. Convolution

- extracts local patterns,
- produces multiple feature maps,
- often increases representation depth.

### 2. Stride and padding

- determine how convolution moves across the input,
- control border handling,
- help determine the output spatial size.

### 3. Activation

- introduces nonlinearity,
- allows the network to model more complex relationships than a purely linear stack.

### 4. Pooling

- reduces spatial resolution,
- improves robustness to small spatial changes,
- helps control computation.

---

## Shape Example

Suppose the input to a block is `H x W x C`.

If we apply:

- a `3 x 3` convolution,
- `K` filters,
- stride `1`,
- padding `1`,

then the convolution output becomes:

`H x W x K`

If we then apply `2 x 2` pooling with stride `2`, the output becomes approximately:

`H/2 x W/2 x K`

This example shows a common CNN pattern:

- spatial dimensions gradually decrease,
- channel depth often increases.

---

## Why Repeated Blocks Work

When these blocks are stacked repeatedly:

- early blocks capture simple local structure,
- deeper blocks combine earlier features into richer patterns,
- the network gradually shifts from raw visual detail toward more abstract meaning.

So CNN intelligence comes not from one layer alone, but from the repeated transformation of the representation across many blocks.

---

## Design Trade-offs

Designing a good CNN block involves balancing competing goals:

| Choice | Advantage | Risk |
|---|---|---|
| More filters | Richer representation | More computation and memory |
| Larger stride or more pooling | Faster shrinking and lower cost | Loss of fine spatial detail |
| Preserving more spatial size | Better detail retention | Higher computational burden |

This is why CNN design is always about **trade-offs**, not just "more is better."

---

## Common Confusions

- A practical CNN "layer" often means a **block**, not just a convolution alone.
- Pooling is not mandatory in every block.
- The best block structure depends on the task: classification, localization, efficiency, and depth needs can differ.

---

## Summary

- CNNs are built from **repeated blocks**, not isolated operations.
- Convolution learns patterns, activation adds nonlinearity, stride/padding control geometry, and pooling downsamples.
- Block design determines both the **quality of learned features** and the **cost of computation**.
- As blocks repeat, spatial detail usually decreases while semantic richness increases.

**Bridge to the next note:** once one block is clear, the next idea is natural: why do CNNs stack **many convolutional layers** instead of stopping at one?
