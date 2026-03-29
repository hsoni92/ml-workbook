# Computational Graphs – Artificial Neural Networks (Module 5)

## Learning Objectives

By the end of this video you will:

1. **Define** a **computational graph** and how nodes and operations are represented.
2. **Explain** what a **local gradient** is.
3. **See** how the **chain rule** operates on the graph.
4. **Understand** why computational graphs make backpropagation **efficient** and **systematic**.

---

## What Is a Computational Graph?

- A **computational graph** is a graphical representation of a mathematical expression.
- **Nodes:** Variables or intermediate values.
- **Edges:** Mathematical operations that transform one value into another.
- The graph shows **step by step** how the final output is built from the input.

---

## Simple Example

- \( u = 3x \), \( y = u^2 \).
- As a graph: input node \( x \) → multiply by 3 → node \( u \) → square → node \( y \).
- Even this small expression has a clear **chain** structure.

---

## Forward Pass on the Graph

- Evaluate each node in order: start with \( x \), compute \( u = 3x \), then \( y = u^2 \).
- **Store** every intermediate value at its node.
- This storage is **essential**: these values are **reused** when computing gradients in the **backward** pass.

---

## Local Gradient

- At each **edge**, the **local gradient** is the derivative of that node’s **output** w.r.t. its **direct input**.
- Example: \( u = 3x \) → local gradient \( \frac{du}{dx} = 3 \).
- \( y = u^2 \) → local gradient \( \frac{dy}{du} = 2u \).
- Each small operation contributes its **local** derivative; backpropagation is built from these.

---

## Chain Rule on the Graph

- To get the **global** derivative \( \frac{dy}{dx} \), the graph tells us: \( \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} \).
- So \( \frac{dy}{dx} = 2u \cdot 3 \).
- **Key idea:** A **global** gradient is the **product of local gradients** along a path in the graph.

---

## One Graph for Forward and Backward

- **Forward pass:** Compute and **store** all intermediate values.
- **Backward pass:** Start at the output and propagate gradients **backward** through the same graph using **stored** values and **local** derivatives at each node.
- One **static** graph supports both **computation** and **differentiation**.

---

## Summary

- Any neural network computation can be represented as a **computational graph**.
- Each edge has a **local gradient**.
- **Global** gradients are obtained by **multiplying** local gradients along paths (chain rule).
- **Backpropagation** = systematic **backward** traversal of this graph to compute all parameter gradients efficiently.
