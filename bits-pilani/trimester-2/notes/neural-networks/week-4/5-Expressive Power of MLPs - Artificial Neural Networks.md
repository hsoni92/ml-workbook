# Expressive Power of MLPs – Artificial Neural Networks (Module 4)

## Learning Objectives

By the end of this video you will:

1. **Understand** what **expressive power** of a neural network means.
2. **See** how **width** and **depth** affect expressive power.
3. **Compare** shallow-wide vs deep-narrow networks.
4. **Explain** why **depth** plays a central role in modern deep learning.

---

## What Is Expressive Power?

- **Expressive power** = the **set of functions** the model can represent.
- A model with higher expressive power can represent **more complex and varied** input–output relationships.
- For neural networks, expressive power is controlled mainly by:
  - **Depth:** number of layers.
  - **Width:** number of neurons per layer.
- This is about **capacity**, not yet about training or performance.

---

## Shallow vs Deep Networks

- **Shallow:** One hidden layer (or none).
- **Deep:** Multiple hidden layers stacked.
- Both can, in principle, approximate complex functions; the **efficiency** with which they do so differs.

---

## Increasing Width

- Adding more neurons to the **same** hidden layer increases the number of **feature detectors** at a **single** level of abstraction.
- This allows **finer partitions** of the input space.
- **Universal Approximation Theorem:** A network with **one** hidden layer can approximate any continuous function if it has **enough** neurons — but the number of neurons may need to be **exponentially large**, making such networks impractical.

---

## Increasing Depth

- **Depth** = stacking multiple layers; each layer works on the representation from the previous one.
- The network builds features **hierarchically**: simple features first, then combined into more complex ones.
- **Key advantage:** Many complex functions can be represented with **far fewer parameters** than a very wide but shallow network.
- Depth enables **efficient function composition**.

---

## Width vs Depth Trade-off

- **Wide, shallow:** Tries to learn many features **at once** in one layer.
- **Deep, narrow:** Learns features **gradually** across multiple levels of abstraction.
- For many real-world problems, **deep** networks are more **parameter-efficient**: same class of functions with **fewer** neurons and parameters than an extremely wide shallow network.
- This is a major reason modern design **favors depth** over extreme width.

---

## Why Depth Matches Real-World Structure

- Many problems have **inherent hierarchical structure**:
  - **Vision:** edges → shapes → objects.
  - **Language:** characters → words → phrases → meaning.
- Deep networks naturally match this **hierarchical composition** of features, which is why they are effective for vision, speech, and language.

---

## Summary

- **Expressive power** = class of functions the network can represent.
- **Width** gives more feature detectors at one level; **depth** enables **hierarchical** composition of features.
- Although shallow networks with enough width can approximate any function in theory, **deep** networks usually achieve the same power with **far fewer parameters**.
- **Depth** is central in modern deep learning architectures.
