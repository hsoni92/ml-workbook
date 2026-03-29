# What is a Multi-Layer Perceptron (MLP) – Artificial Neural Networks (Module 4)

## Learning Objectives

By the end of this video you will:

1. **Understand** the basic structure of an MLP.
2. **Explain** how **feed-forward** information flows in MLPs.
3. **Identify** the key parameters of each layer (weights, biases).
4. **Recognize** how multiple layers combine to form complex transformations.

---

## Definition of an MLP

- A **multi-layer perceptron (MLP)** is a **feed-forward** neural network composed of:
  - **Input layer** — holds the raw feature vector; no computation.
  - **One or more hidden layers** — where transformations occur.
  - **Output layer** — produces the final prediction.
- Information flows **strictly in one direction**: input → hidden layers → output. No cycles, no feedback.

---

## Fully Connected Architecture

- In most standard MLPs, **every neuron in one layer** is connected to **every neuron in the next layer**.
- Example: 2 inputs \( (x_1, x_2) \), one hidden layer with 3 neurons, another hidden layer with 3 neurons, one output \( y \). Each input connects to all three neurons of the first hidden layer; hidden layers are fully interconnected; last hidden layer is fully connected to \( y \).

---

## Parameters of an MLP

- **Every layer** has a **weight matrix** \( \mathbf{W} \) and a **bias vector** \( \mathbf{b} \).
- These define the function computed by the network.

---

## What One Layer Does (Mathematically)

Each layer performs two steps:

1. **Linear transformation:** \( \mathbf{z}^{(L)} = \mathbf{W}^{(L)} \mathbf{a}^{(L-1)} + \mathbf{b}^{(L)} \)
2. **Nonlinear activation:** \( \mathbf{a}^{(L)} = f(\mathbf{z}^{(L)}) \)

- \( \mathbf{a}^{(L-1)} \): input to the layer (output from the previous layer).
- \( \mathbf{W}, \mathbf{b} \): weights and biases for this layer.
- \( f \): activation function.
- \( \mathbf{a}^{(L)} \): new representation passed to the next layer.

---

## Small Dimensional Example

- **Input:** 2 features \( (x_1, x_2) \); **first hidden layer:** 3 neurons; **output layer:** 1 neuron.
- **Layer 1:** \( \mathbf{W}_1 \) has shape \( 3 \times 2 \), \( \mathbf{b}_1 \) length 3. \( \mathbf{W}_1 \mathbf{x} \) has shape \( 3 \times 1 \).
- **Layer 2:** \( \mathbf{W}_2 \) has shape \( 1 \times 3 \). \( \mathbf{W}_2 \mathbf{a}_1 \) has shape \( 1 \times 1 \) (single output \( y \)).
- As data moves forward, the **dimension of the representation** can change at each layer; the network **reshapes the feature space** at every layer.

---

## MLP as Composition of Functions

- An MLP is **not** one big formula; it is a **composition** of many simpler transformations.
- Conceptually: \( \mathbf{a}_{\text{out}} = f_L \circ f_{L-1} \circ \cdots \circ f_1(\mathbf{x}) \).
- Each layer refines the representation; this **repeated transformation** is what gives multilayer networks their power.

---

## Summary

- An **MLP** is a feed-forward network of neurons with **input**, **hidden**, and **output** layers.
- Each layer does a **linear transformation** followed by **nonlinear activation**.
- Data representation is **repeatedly transformed** from layer to layer.
- MLPs form the **core architectural template** of deep neural networks.
