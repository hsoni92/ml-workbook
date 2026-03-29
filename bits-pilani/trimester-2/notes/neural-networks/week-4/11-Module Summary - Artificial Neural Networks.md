# Neural Networks – Module 4 Summary: Artificial Neural Networks

## Purpose of This Module

Module 4 builds the **foundation** of **multi-layer perceptrons (MLPs)** and **activation functions**. The goal is to understand how **hidden layers**, **forward pass**, **expressive power**, and **non-linearity** combine into the core computational blueprint of neural networks.

---

## What We Learned (Flow of Module 4)

| Topic | Content |
|-------|--------|
| **MLP** | Feed-forward network: input layer, one or more hidden layers, output layer; fully connected; each layer = linear transform + activation. |
| **Forward pass** | Execution on one input: neuron-level compute (weighted sum + bias + activation) repeated layer by layer; output layer produces task-specific prediction. |
| **Hidden layers** | Representation learning; each neuron as feature detector; raw → derived features; hierarchical representations (simple → complex). |
| **Expressive power** | Set of functions the model can represent; **width** = more detectors at one level; **depth** = hierarchical composition; depth usually more parameter-efficient. |
| **Activation functions** | Essential for non-linearity; without them, stacking layers collapses to one linear map. |
| **Sigmoid / tanh** | Classical; sigmoid \( (0,1) \), tanh \( (-1,1) \) zero-centered; both **saturate** → vanishing gradients. |
| **ReLU family** | ReLU = \( \max(0,z) \); no saturation for \( z>0 \); default for hidden layers; **dying ReLU** mitigated by Leaky ReLU, PReLU. |
| **Softmax** | Converts logits to probability distribution over classes; for **multi-class** output layer. |
| **Practical choices** | Hidden: ReLU (or Leaky ReLU); output: sigmoid (binary), softmax (multi-class), linear (regression). |

---

## Key Intuitions to Retain (Exam-Ready)

1. **MLP** = feed-forward, layered: linear transform + activation per layer; parameters = weight matrices and bias vectors per layer.
2. **Forward pass** = one run of the network on one input; no learning, only computation.
3. **Hidden layers** learn representations; stacking gives **hierarchical** features (e.g. edges → shapes → objects).
4. **Without activation functions**, deep nets collapse to a single linear model; **with** them, we get real expressive power.
5. **ReLU** (and variants) are the default for hidden layers; **sigmoid** (binary) and **softmax** (multi-class) for output by task type.
6. **Saturation** (sigmoid/tanh) and **dying ReLU** are the main pitfalls; choice of activation affects **training dynamics** and **stability**.

---

## Big Picture

We moved from:

- **Single neurons** (perceptron, logistic) and their **limits (XOR)**
→ **MLP** structure and **forward pass**
→ **Representation learning** and **expressive power** (depth vs width)
→ **Activation functions** as the source of non-linearity
→ **Practical** activation choices (ReLU family, sigmoid, softmax) and their **trade-offs**.

---

## Bridge to the Next Module

In Module 5 we shift from **how the network computes** to **how it learns**:

- **Forward pass**, **loss**, and **backpropagation** as a complete learning loop.
- How **gradients** propagate through layers.
- **Loss functions** (e.g. MSE, cross-entropy) and their effect on learning.
- **Vanishing and exploding gradients** and how to mitigate them.
- How these pieces form **end-to-end training** of neural networks.
