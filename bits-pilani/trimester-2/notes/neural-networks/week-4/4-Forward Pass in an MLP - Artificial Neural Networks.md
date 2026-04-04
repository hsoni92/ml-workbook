# Forward Pass in an MLP – Artificial Neural Networks (Module 4)

## Learning Objectives

By the end of this video you will:

1. **Define** what a **forward pass** means in a neural network.
2. **Describe** the step-by-step computation inside a neuron during execution.
3. **Understand** how activations flow **layer by layer** to produce a prediction.
4. **Interpret** how the output layer converts internal activations into **task-specific** predictions.

---

## What Is a Forward Pass?

- Once an MLP is defined and trained, every prediction is produced by a **forward pass**.
- **Forward pass** = executing the stored computations of the network on a **single input**.
- No learning happens here — only **numerical computation** that turns one input into one prediction.

---

## Flow of One Input

- Input vector $\mathbf{x}$ is fed into the **first hidden layer**.
- The network is not “deciding” yet; it is beginning a **sequence of transformations**.
- The **same** input $\mathbf{x}$ is **not** reused at every layer; each layer works on the **transformed version** produced by the previous layer.

---

## Computation Inside One Neuron

Each neuron does four steps:

1. Multiply each input by its corresponding **weight**.
2. **Sum** all weighted inputs.
3. Add the **bias**.
4. Apply the **activation function** $f$.

Mathematically:
$$
z = \sum_i w_i x_i + b, \qquad a = f(z)
$$
This happens at **runtime** for every input; one output number per neuron.

---

## Layer-by-Layer Flow

- After the first hidden layer finishes, its **output vector** is passed to the second hidden layer.
- The second hidden layer does the same neuron-wise computation and produces a new **activation vector**.
- This continues until the signal reaches the **output layer**.
- **Important:** The original input $\mathbf{x}$ is **never used again directly**; each layer only sees the representation from the previous layer.

---

## Output Layer

- The **output layer** converts the last hidden activation vector into a prediction suited to the task:
  - **Binary classification:** typically a **probability**.
  - **Multi-class classification:** class scores or **probabilities**.
  - **Regression:** a **real-valued** output.
- After this, the forward pass is complete and the network has produced its prediction.

---

## Why It Matters

- The forward pass is the **core computation** of a neural network.
- Every prediction in real systems (image recognition, recommendation, medical diagnosis) is produced by a forward pass.
- Training will repeatedly use this same forward computation and then adjust weights based on **observed errors** (via backpropagation).

---

## Summary

- A **forward pass** is the execution of a trained MLP on a single input.
- It consists of **neuron-level** computations repeated **layer by layer**.
- Neurons in a layer compute **in parallel**.
- The **final layer** converts internal activations into a **task-specific** prediction.
- This forward computation is what training will later try to **improve**.
