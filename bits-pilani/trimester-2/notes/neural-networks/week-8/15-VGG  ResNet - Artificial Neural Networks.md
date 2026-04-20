# VGG and ResNet - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain why researchers kept pushing CNNs to greater depth.
2. Describe the main design idea behind **VGG**.
3. Explain the **degradation problem** in very deep plain networks.
4. Describe how **ResNet** uses residual connections to make deep training practical.

---

## Why Depth Became the Next Big Question

Once CNNs proved successful, a natural question followed:

**If deeper networks can learn richer representations, why not keep adding more layers?**

This question led to two influential milestones:

- **VGG**, which emphasized simple repeated depth,
- **ResNet**, which made very deep models much easier to train.

---

## VGG: The Power of Simple Repetition

VGG showed that strong performance could be obtained by using a very clean and uniform design:

- repeated small `3 x 3` convolutions,
- pooling at regular intervals,
- increasing depth through repeated blocks.

Its contribution was not architectural complexity. In fact, its strength was the opposite: **simplicity and consistency**.

### What VGG taught

- depth matters,
- stacking multiple small convolutions can work very well,
- a simple repeated design can already learn powerful image representations.

---

## The Limitation of Plain Deep Networks

As people kept increasing depth, an important problem appeared.

One might expect that a deeper network should always do at least as well as a shallower one, since it has more capacity. But in practice, very deep plain networks sometimes showed **higher training error**.

This is called the **degradation problem**.

Important distinction:

- this is not only an overfitting issue,
- it is an **optimization difficulty**.

So the problem was not that deep networks were too expressive. The problem was that they became hard to train effectively.

---

## ResNet: Residual Learning

ResNet introduced a powerful idea: **skip connections** or **residual connections**.

Instead of forcing a block to learn a full transformation directly, ResNet lets the block learn a residual correction:

`y = x + F(x)`

Here:

- `x` is the input,
- `F(x)` is the residual mapping learned by the block,
- the output adds the original signal back through the shortcut path.

This simple idea changed the training dynamics of deep networks.

---

## Why Residual Connections Help

Residual connections make it easier for:

- information to flow forward,
- gradients to flow backward,
- optimization to remain stable as depth increases.

As a result, networks with dozens or even hundreds of layers became much more trainable.

So ResNet's key insight was not merely "make the network deeper." It was:

**make deep networks easier to optimize.**

---

## VGG vs ResNet

| Aspect | VGG | ResNet |
|---|---|---|
| Main idea | Simple repeated plain blocks | Residual blocks with skip connections |
| View of depth | Depth itself is powerful | Depth needs optimization support |
| Strength | Clear, uniform architecture | Trainability at much greater depth |
| Limitation | Expensive and harder to optimize when very deep | More complex block design |

---

## Common Confusions

- ResNet is not just "a deeper VGG." The skip connections fundamentally change learning behavior.
- The degradation problem is not only about overfitting. It can increase **training error**, which signals an optimization issue.
- More layers help only if the architecture lets those layers be trained effectively.

---

## Summary

- **VGG** highlighted the power of depth through a simple repeated design.
- Very deep plain networks exposed the **degradation problem**.
- **ResNet** introduced residual connections that improved signal and gradient flow.
- This made very deep CNNs practical and strongly influenced later architectures.

**Bridge to the next note:** after learning how to build deeper CNNs, the next challenge became different: how do we make CNNs more **efficient** for real deployment? That leads to **MobileNet** and **EfficientNet**.
