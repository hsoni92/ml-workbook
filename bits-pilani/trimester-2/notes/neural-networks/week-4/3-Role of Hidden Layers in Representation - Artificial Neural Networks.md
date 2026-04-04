# Role of Hidden Layers in Representation – Artificial Neural Networks (Module 4)

## Learning Objectives

By the end of this video you will:

1. **Explain** what **representation learning** means in neural networks.
2. **Interpret** a hidden neuron as a **feature detector**.
3. **Describe** how hidden layers transform **raw features** into **derived features**.
4. **Explain** why stacking layers increases expressive power (including for problems like **XOR**).

---

## Why Hidden Layers?

- A **single layer** can only learn **linear** transformations. Without hidden layers, we are limited to **linear decision boundaries**.
- Most real-world relationships (images, speech, medical data, financial patterns) are **highly non-linear**.
- **Hidden layers** transform and re-encode data into **internal representations** that make complex patterns easier to separate.

---

## What Is “Representation”?

- **Representation** = how the data is encoded inside the network.
- **Raw input** (e.g. pixels, table values) is the first representation.
- Each hidden layer produces a **new transformed version** of the same data.
- Example: housing price — inputs like bedrooms and size; a hidden unit might encode **spaciousness**, an abstract feature not explicitly in the input. The model **learns** these internal representations.

---

## Hidden Neuron as Feature Detector

- A hidden neuron computes $a = f(\mathbf{w}^T \mathbf{x} + b)$.
- Conceptually: the neuron **responds strongly** when a **specific pattern** appears in the input → it acts as a **feature detector**.
- Different hidden neurons learn to respond to **different patterns**; together they form a **bank of feature detectors**.

---

## Raw vs Derived Features

- **Raw features:** Direct measurements (e.g. pixel intensities).
- **Hidden layers** turn raw features into **derived features**: combinations of inputs, interactions, structural patterns.
- Each new layer works on **features created by the previous layer**, not on the original input.

---

## Hierarchical Representation Learning

- **Stacking layers** → the network learns **hierarchies of representations**.
- **Early layers:** Simple patterns (edges, basic trends).
- **Deeper layers:** Combinations of those patterns (shapes, objects, abstract concepts).
- Example (image → dog/cat/bird): input = raw pixels; layer 1 ≈ edges; layer 2 ≈ corners/contours; deeper layers ≈ shapes and objects.
- This **hierarchical** structure is why deep networks are more powerful than shallow ones.

---

## Trade-off

- More hidden neurons → more feature detectors at one level.
- More hidden layers → more levels of abstraction.
- Together they increase the **set of functions** the network can represent, but also **parameters**, **compute cost**, and **overfitting risk**. There is always a **trade-off** between representation power and model complexity.

---

## Connection to XOR

- **XOR:** Four points; no single linear boundary can separate the classes.
- A **hidden layer** creates **multiple intermediate splits** of the input space; the output layer can then combine them to classify correctly.
- By changing the **representation** in a hidden layer, a problem that was **impossible linearly** becomes solvable. XOR is the smallest example; the same mechanism operates in all deep networks.

---

## Summary

- Hidden layers perform **representation learning**.
- Each hidden neuron behaves like a **feature detector**.
- Raw features are transformed into **increasingly abstract** representations across layers.
- **Stacking layers** creates hierarchies of abstraction — the true source of neural network power.
