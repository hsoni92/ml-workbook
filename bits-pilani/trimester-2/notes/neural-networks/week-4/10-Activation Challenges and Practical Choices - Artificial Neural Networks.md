# Activation Challenges and Practical Choices – Artificial Neural Networks (Module 4)

## Learning Objectives

By the end of this video you will:

1. **Identify** main challenges from poor activation choices (saturation, dead neurons).
2. **Understand** how activation functions affect **training dynamics**.
3. **Apply** practical guidelines for choosing activations in real networks.

---

## Why Activation Choice Matters

- Activation functions strongly affect **how** a network trains, **converges**, and stays **stable**.
- A bad choice can cause very **slow** learning, **unstable** training, or **no** learning.
- Activation selection is a **core architectural** decision, not a minor detail.

---

## Saturation (Sigmoid and Tanh)

- For very large positive or negative inputs, sigmoid and tanh **flatten**.
- In these regions, a large change in input gives only a **tiny** change in output.
- During training → learning signals become **very weak** → parameter updates **very small** → learning **slows down**.
- Saturation also leads to **vanishing gradients**: when signals go backward through many layers, small values multiply and become even smaller, so **early** layers get almost no learning signal. The deeper the network, the harder it is for the first layers to learn.

---

## Dying ReLU

- ReLU outputs **0** for all negative inputs.
- If a neuron starts getting **always** negative inputs during training, it outputs 0 for every input and **stops contributing** — a **dead ReLU**.
- This can reduce the **effective capacity** of the network. Mitigations: **Leaky ReLU**, **PReLU**.

---

## Exploding Activations

- In some deep networks, activations can **grow very large** as they pass through layers (e.g. poor initialization, great depth, unstable activation–weight interaction).
- Can lead to **numerical overflow**, **instability**, and **training failure**.
- Activation choice is tied to **weight initialization** and **depth**.

---

## Guidelines: Hidden Layers

- **Default:** Use **ReLU** for hidden layers.
- If you see many **inactive/dead** neurons → try **Leaky ReLU**.
- For **very deep** networks, prefer the **ReLU family**.
- **Avoid** sigmoid in deep hidden layers — it usually slows or destabilizes training.

---

## Guidelines: Output Layer

- **Binary classification** → **sigmoid**.
- **Multi-class classification** → **softmax**.
- **Regression** → **linear** output (no activation).

Output activation is chosen by **how we want to interpret** the prediction (probability vs real value), not mainly by training speed.

---

## Trade-offs Summary

| Activation | Pros | Cons |
|------------|------|------|
| **Sigmoid** | Probabilistic output | Saturation, vanishing gradients |
| **Tanh**   | Zero-centered       | Still saturates |
| **ReLU**   | Fast, stable        | Dying ReLU |
| **ReLU variants** | Reduce dead neurons | Slightly more parameters (e.g. PReLU) |
| **Softmax** | Multi-class probabilities | For output only |

No single activation is perfect; each reflects specific design goals and trade-offs. Good activation choices are a key reason deep networks are **practical** and **effective** today.
