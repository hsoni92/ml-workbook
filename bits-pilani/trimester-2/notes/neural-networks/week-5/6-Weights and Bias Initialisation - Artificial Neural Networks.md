# Weights and Bias Initialisation – Artificial Neural Networks (Module 5)

## Learning Objectives

By the end of this video you will:

1. **Explain** why initialization is crucial for **stable** training.
2. **Explain** why **zero** initialization of weights **fails**.
3. **Understand** what goes wrong with **naive random** initialization.
4. **Describe** how **Xavier** and **He** initialization stabilize gradient flow.
5. **Explain** why **bias** initialization is treated differently from **weight** initialization.

---

## Why Initialization Matters

- At the start of training the network “knows nothing”; every **weight** and **bias** needs an **initial** value.
- These values affect how **activations** scale, how **gradients** scale, and whether learning starts **smoothly** or **fails** immediately.
- **Bad** initialization can block learning; **good** initialization can make deep networks trainable. Initialization is the **starting point** of the entire learning process.

---

## Why Not Initialize All Weights to Zero?

- **Symmetry:** If all weights are zero, every neuron in a layer gets the **same** input and produces the **same** output.
- During backprop, every neuron gets the **same** gradient → they **stay identical** forever.
- The network can **never** learn different features; all neurons become **clones** → **symmetry-breaking** problem.
- So **weights must not** be initialized to zero.

---

## Why Zero Bias Is OK

- **Bias** does **not** multiply inputs; it does **not** create symmetry across neurons.
- Setting all biases to **zero** does **not** block learning or make neurons identical.
- **\( \mathbf{b} = \mathbf{0} \)** is standard. In ReLU networks, a **small positive** bias is sometimes used to reduce dead neurons, but zero bias is fine in most architectures.

---

## What Makes a Good Initialization?

- Activations should **not** blow up or collapse to zero.
- Gradients should keep a **healthy magnitude** across layers.
- In other words: **preserve stable variance** in both the **forward** and **backward** passes. Modern initialization methods are built on this idea.

---

## Naive Random Initialization

- Suppose \( W \sim \mathcal{N}(0, \sigma^2) \).
- **\( \sigma \) too small:** Weighted sums shrink → activations get smaller layer by layer → **gradients vanish**.
- **\( \sigma \) too large:** Weighted sums explode → activations become huge → **gradients explode**.
- Naive random initialization often **fails**, especially for **deeper** networks.
- Each layer computes \( z = \sum_i w_i x_i \); variance of \( z \) depends on number of inputs, variance of inputs, and variance of weights. Through many layers this variance is **multiplied**; without care it grows or shrinks **exponentially** → vanishing or exploding gradients.

---

## Xavier Initialization

- Designed for **sigmoid** and **tanh** networks.
- Chooses weight variance so that **variance is stable** across layers (forward and backward).
- **Gaussian:** \( W \sim \mathcal{N}\big(0, \frac{1}{n_{\text{in}}}\big) \), where \( n_{\text{in}} \) = number of inputs to the layer.
- **Uniform:** sample from \( \mathcal{U}\big(-\sqrt{\frac{6}{n_{\text{in}} + n_{\text{out}}}}, \sqrt{\frac{6}{n_{\text{in}} + n_{\text{out}}}}\big) \).
- For tanh/sigmoid, Xavier **dramatically** improves training stability. For **ReLU** networks, Xavier is **not** ideal.

---

## He Initialization

- ReLU **zeros** out about half the inputs → effective variance is **halved**.
- **He** initialization compensates: \( W \sim \mathcal{N}\big(0, \frac{2}{n_{\text{in}}}\big) \).
- The factor **2** keeps activations and gradients well-scaled for the **ReLU** family.
- Modern deep networks with ReLU (and variants) almost always use **He** initialization.

---

## Bias Initialization

- **Bias** does not multiply signals → it does **not** drive variance propagation or vanishing/exploding gradients.
- **\( \mathbf{b} = \mathbf{0} \)** is standard.
- Optionally, a **small positive** bias in ReLU networks can help avoid dead neurons.

---

## Summary

- **Zero weights** break learning (symmetry); **zero bias** is usually fine.
- **Naive** random initialization often leads to **vanishing** or **exploding** gradients.
- **Xavier** stabilizes **sigmoid/tanh** networks; **He** stabilizes **ReLU** networks.
- Good initialization is a **foundation** for healthy training, not a minor tuning detail.
