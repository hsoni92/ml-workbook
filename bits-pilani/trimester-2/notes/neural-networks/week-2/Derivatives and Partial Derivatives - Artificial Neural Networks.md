# Derivatives and Partial Derivatives – Artificial Neural Networks (Module 2)

## Learning Objectives

By the end of this video you will:

1. **Understand** derivatives as a measure of **sensitivity** and **rate of change**.
2. **Explain** why derivatives are essential for **learning** in neural networks.
3. **Differentiate** between derivatives and **partial derivatives**.
4. **Interpret** the role of partial derivatives in **multivariable** neural network systems.

---

## From Computation to Learning

- In the previous lesson we saw how neural network computations are built from vectors, matrices, and dot products.
- **Computation alone does not imply learning.** A neural network **learns** by **adjusting its weights**.
- To know **how** to adjust them, we must know: **how does the output change when a weight changes?**
- This idea of **sensitivity** is captured mathematically by **derivatives**. So derivatives are the **core mathematical tool** that makes learning in neural networks possible.

---

## Derivative: Rate of Change and Sensitivity

### Simple Example

- Line: \( y = 5x \). At \( x = 2 \), \( y = 10 \). At \( x = 2.001 \), \( y = 10.005 \).
- **Change in \( y \)** per **change in \( x \):**
  \[
  \frac{\Delta y}{\Delta x} = \frac{10.005 - 10}{2.001 - 2} = \frac{0.005}{0.001} = 5.
  \]
- So: if we change \( x \) by 1 unit, \( y \) changes by 5 units.

### Definition (Single Variable)

- The **derivative** \( \frac{dy}{dx} \) measures **how fast the output \( y \) changes when the input \( x \) changes**.
- **Geometrically:** It is the **slope of the tangent line** to the curve at that point.
- **In a learning system:** This slope tells us whether **increasing** a parameter will **increase** the output, **decrease** it, or have **little effect**. That is exactly what we need to update weights.

---

## Why Partial Derivatives?

- In neural networks, the **output** is not a function of a **single** variable. It depends on **many** inputs and **many** weights: \( y = f(x_1, x_2, \ldots, x_n) \).
- To adjust **each** parameter correctly, we need to know how the output changes with respect to **each variable individually**, with the others held fixed. That leads to **partial derivatives**.

### Definition

- The **partial derivative** \( \frac{\partial y}{\partial x_i} \) measures how \( y \) changes when **only \( x_i \)** is changed and **all other variables are kept fixed**.
- **Intuition:** “Turn one knob at a time while freezing all the others.” In neural network learning we effectively adjust one weight while treating the others as temporarily fixed.

---

## Geometric View (Two Variables)

- Consider a surface \( f(x, y) = x^2 + y^2 \).
- A **partial derivative** corresponds to **slicing** the surface along one direction and taking the **slope along that slice**.
- **Example:** Fix \( y = 1 \). Then \( f(x, 1) = x^2 + 1 \) is a curve in \( x \). The partial derivative \( \frac{\partial f}{\partial x} = 2x \) is the slope of this curve (e.g. at \( x = 1 \), slope \( = 2 \)).

---

## Summary (Quick Revision)

| Concept | Meaning |
|---------|--------|
| **Derivative** | Measures sensitivity / rate of change of output with respect to one input. |
| **Multivariable systems** | Require **partial derivatives** (one per variable). |
| **Learning in neural networks** | Is driven by these sensitivities with respect to the **parameters** (weights, biases). |

In the next video we learn about the **gradient vector**: collecting all partial derivatives into one object that points in the direction of steepest increase.
