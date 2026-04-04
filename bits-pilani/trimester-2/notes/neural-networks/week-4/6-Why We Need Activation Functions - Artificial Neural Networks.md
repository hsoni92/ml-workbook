# Why We Need Activation Functions – Artificial Neural Networks (Module 4)

## Learning Objectives

By the end of this video you will:

1. **Understand** why **purely linear** neural networks are fundamentally limited.
2. **See** how **activation functions** introduce non-linearity.
3. **Explain** why stacking **linear** layers collapses into a **single linear** model.
4. **Recognize** that activation functions are the **true source** of expressive power in deep networks.

---

## Thought Experiment: No Activation Functions

- Suppose every layer only does $\mathbf{z} = \mathbf{W}\mathbf{x} + \mathbf{b}$ with **no** activation.
- Each layer is then just a **linear** mapping.

---

## Stacking Linear Layers Collapses

- **Layer 1:** $\mathbf{z}_1 = \mathbf{W}_1 \mathbf{x} + \mathbf{b}_1$
- **Layer 2:** $\mathbf{z}_2 = \mathbf{W}_2 \mathbf{z}_1 + \mathbf{b}_2$

Substituting:
$$
\mathbf{z}_2 = \mathbf{W}_2 (\mathbf{W}_1 \mathbf{x} + \mathbf{b}_1) + \mathbf{b}_2 = \mathbf{W}_2 \mathbf{W}_1 \mathbf{x} + \mathbf{W}_2 \mathbf{b}_1 + \mathbf{b}_2
$$
This is still a **single linear transformation** of $\mathbf{x}$. No matter how many purely linear layers we stack, the **entire network collapses** into one linear model. **Depth alone does not add power** if all layers are linear.

---

## Consequences of Purely Linear Networks

- Purely linear models can only learn **straight-line** decision boundaries (or hyperplanes in higher dimensions).
- They **cannot** represent XOR, curved boundaries, or complex feature interactions — as we already saw with the perceptron.
- Without activation functions, we **cannot escape** this limitation no matter how many linear layers we add.

---

## Role of Activation Functions

- An **activation function** applies a **nonlinear** transformation to each neuron’s output: $a = f(z)$.
- This **breaks** the linearity of the network.
- Once non-linearity is introduced, **stacking layers no longer collapses** into one linear map.
- Each layer becomes a **nonlinear** transformation of the previous layer’s output.

---

## What Non-linearity Enables

- The first layer can learn **nonlinear** features of the input.
- The second layer can learn **nonlinear** combinations of those features.
- Deeper layers can represent **highly complex, nested** nonlinear relationships.
- This allows: **curved** decision boundaries, **complex** feature interactions, **hierarchical** abstractions — the reason deep networks are powerful.

---

## Takeaway

- **Without** activation functions, an MLP is just a **linear** model, no matter how deep.
- **With** activation functions, even a **single** hidden layer can approximate any continuous function on a compact domain (**Universal Approximation Theorem**).
- **Activation functions** are why deep learning works as we know it.
