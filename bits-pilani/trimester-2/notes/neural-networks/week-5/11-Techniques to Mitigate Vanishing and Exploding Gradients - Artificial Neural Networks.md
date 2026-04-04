# Techniques to Mitigate Vanishing and Exploding Gradients – Artificial Neural Networks (Module 5)

## Learning Objectives

By the end of this video you will:

1. **See** how **initialization**, **activation functions**, **gradient clipping**, and **normalization layers** help keep gradient flow stable.
2. **Apply** these techniques as the foundation of stable deep learning training.

---

## Four Categories of Techniques

To prevent gradients from **shrinking** or **exploding**, modern networks rely on:

1. **Weight initialization** — designed for stable variance.
2. **Activation functions** — that do not kill gradients.
3. **Gradient clipping** — to cap update size.
4. **Normalization layers** — to stabilize activations across the network.

Together these form the **foundation** of stable deep learning training.

---

## 1. Weight Initialization

- **Xavier (Glorot):** Keeps variance of activations and gradients **consistent** across layers. Works well with **sigmoid** and **tanh**.
- **He:** Scaled for **ReLU**-type activations. Because ReLU zeros half the inputs, it uses larger variance (e.g. $\frac{2}{n_{\text{in}}}$) to compensate.
- **Goal of both:** Keep forward and backward signals from **shrinking** or **exploding** as they move through the network. Without good initialization, other techniques are much less effective.

---

## 2. Activation Functions

- **Sigmoid** and **tanh** saturate easily → derivatives near **zero** → deep networks with them were hard to train.
- **ReLU:** Derivative **1** for positive inputs → gradients pass through **without** shrinking.
- **Leaky ReLU, GELU**, and other variants extend this idea.
- Using the **right** activation **greatly** reduces the risk of vanishing gradients and is a big reason deep learning became feasible.

---

## 3. Gradient Clipping

- **Exploding gradients:** Many layers with derivatives &gt; 1 → very large gradients → **unstable** training.
- **Gradient clipping:** If the **gradient norm** exceeds a threshold, **scale it down** so updates stay **bounded**.
- Widely used in **RNNs**, **LSTMs**, and **transformers**, where exploding gradients are common. Think of it as a **safety cap** on gradient size.

---

## 4. Normalization Layers

- **Batch Normalization:** Normalizes activations **within a batch**. Keeps activations in a **healthy range** → derivatives in a healthy range. Reduces **internal covariate shift** and helps **deeper** networks train.
- **Layer Normalization:** Normalizes at the **feature** level; common in **transformers** where batch statistics are not always reliable.
- By **standardizing** activations, normalization layers stabilize both the **forward** and **backward** passes and help prevent **vanishing** and **exploding** gradients.

---

## Summary

- Gradients can **vanish** or **explode** because of **repeated multiplication** in deep networks.
- **Proper initialization** keeps variances balanced (Xavier for sigmoid/tanh, He for ReLU).
- **ReLU** and its variants let gradients pass through layers.
- **Gradient clipping** limits damage from **exploding** updates.
- **Normalization layers** stabilize activations and gradients.
- Together, these techniques form the **backbone** of modern deep network training.
