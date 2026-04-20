# Flat vs Sharp Minima - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Distinguish between **flat minima** and **sharp minima**.
2. Explain why two models with similar training loss may still generalize differently.
3. Relate flatness and sharpness to **sensitivity under parameter perturbation**.
4. Connect training choices such as **batch size**, **learning rate**, and **SGD noise** to the type of solution reached.

---

## The Main Question

From the previous note, we know that deep networks can reach many low-loss solutions. But these solutions are not equally useful.

So the important question is:

**If two models achieve almost the same training loss, why can one generalize well while the other overfits?**

One useful geometric answer comes from the distinction between **flat** and **sharp** minima.

---

## Flat vs Sharp Minima

| Property | Flat Minimum | Sharp Minimum |
| --- | --- | --- |
| Local behavior of loss | Changes slowly nearby | Rises quickly nearby |
| Sensitivity to parameter changes | Low | High |
| Intuition | Wide valley | Narrow pit |
| Generalization tendency | Often better | Often weaker |

A **flat minimum** is a region where many nearby parameter settings still give similarly low loss.

A **sharp minimum** is a region where only a very small neighborhood gives low loss; even tiny changes can increase the loss quickly.

```text
Flat valley:   \______/
Sharp valley:    \__/
```

---

## Why This Distinction Matters

The key idea is **sensitivity**.

- If a solution lies in a **flat** region, small changes in the parameters do not hurt it much.
- If a solution lies in a **sharp** region, small parameter changes can degrade performance quickly.

This makes flat solutions seem more **robust** and often more likely to perform well on unseen data.

In contrast, sharp solutions can indicate that the network has adapted too specifically to the training set.

> **Useful intuition:** The width of the valley matters, not just the depth.

---

## Connection to Generalization

Flat minima are often associated with better generalization because they tolerate small parameter variation. That tolerance suggests the model has learned a more stable pattern rather than a brittle fit.

Sharp minima, on the other hand, are more sensitive. A small change in weights can change the loss significantly, which suggests the solution may depend too heavily on exact training details.

That is why two models can have:

- similar training loss,
- but very different test performance.

---

## Why Training Choices Influence the Result

The type of minimum reached is not random. It depends partly on the training process.

| Training Choice | Typical Influence |
| --- | --- |
| **Smaller batch / noisier SGD** | Can encourage exploration of wider regions |
| **Learning rate schedule** | Affects how training explores and settles |
| **Regularization** | Can discourage brittle solutions |

The transcript also emphasizes that the inherent noise in stochastic gradient descent can bias training toward **wider** low-loss regions.

So optimization choices affect generalization indirectly, not just by reducing loss faster.

---

## Important Caution

Flatness is not a perfectly absolute quantity. It can depend on how parameters are scaled and on the precise formulation of the loss.

So this topic should be understood mainly as a **qualitative geometric intuition**, not as a single universal scalar that must always be computed exactly.

In exam answers, it is safest to say:

- flat vs sharp minima provide a **useful intuition** for generalization,
- rather than claiming a strict universal law.

---

## Summary and Exam-Ready Takeaways

- Deep networks can reach many **low-loss solutions**.
- A **flat minimum** is less sensitive to small parameter perturbations.
- A **sharp minimum** is more sensitive and often more brittle.
- Flat minima are often associated with **better generalization**, while sharp minima are more often linked with **overfitting**.
- Training choices such as **batch size**, **learning rate**, and **SGD noise** influence which kind of solution is reached.

**Bridge to next topic:** Geometric intuition is useful, but in practice we diagnose overfitting through **observable training and validation patterns**.
