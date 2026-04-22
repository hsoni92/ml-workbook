# L1 and L2 Regularization – Artificial Neural Networks (Module 7)

## Learning Objectives

By the end of this video you will:

1. **Explain** why **regularization** is needed even when optimization **minimizes training loss**.
2. **Write** the **regularized objective** (data loss + weighted penalty).
3. **Contrast** **L2** (weight decay) and **L1** penalties and their **geometric** interpretations.
4. **Interpret** how each penalty shapes **weights**, **sparsity**, and **generalization**.

---

## Optimization vs Preferable Solutions

- Deep networks often have **very high capacity**. Optimizers can drive **training loss** down yet still **overfit**.
- Optimization answers **how** to reduce loss on the training set; it does **not** by itself answer **which** solutions (among many low-loss ones) **generalize** better.
- **Regularization** **biases** learning toward **simpler**, often **more stable** solutions by **constraining** or **penalizing** complexity.

---

## Regularized Loss

- Instead of minimizing **only** the data loss $L_{\text{data}}(\theta)$, we minimize a **regularized** objective:

$$
J(\theta) = L_{\text{data}}(\theta) + \lambda \, \Omega(\theta)
$$

- **$\Omega(\theta)$** = penalty on model complexity (here, a function of **weights**).
- **$\lambda \geq 0$** controls the **trade-off**:
  - **Larger $\lambda$** → stronger push toward **simplicity** (smaller penalty weights / sparser solutions, depending on $\Omega$).
  - **Smaller $\lambda$** → more emphasis on **fitting** the data.

---

## L2 Regularization (Weight Decay)

- Penalty: **sum of squared weights** (often $\frac{1}{2}\sum_i w_i^2$ is used for cleaner derivatives—equivalent up to rescaling $\lambda$).
- **Large** weights are penalized **more** than small ones (quadratic growth).
- Encourages **many small** weights spread across features rather than a few **very large** ones.
- **Common in deep learning:** tends to yield **smoother**, **more stable** models and often **better generalization**.

**Geometry (two weights):**

- **Loss contours** (without regularization): often **elliptical** around an unregularized minimum.
- **L2 constraint** region: a **disk** (L2 ball). The regularized solution is where a loss contour **first touches** the disk—often **shrinking** all weights **toward zero** but **rarely** setting exact zeros (smooth boundary).
- Effect: reduces **any single parameter’s** dominance → **less sensitivity** to noise → **smoother** decision boundaries in classification settings.

### Visual: L2 ball vs L1 ball (two weights)

```text
   w2                    L2: circle      L1: diamond (rotated square)
    |                        ___              /\
    |    ___---'''---___   /    \            /  \
    |   /              \  |      |          /    \
----+--/----------------\-+------+-- w1    /______\
```

The regularized solution often lies where a **loss contour** first touches the **constraint set**—corners of the diamond favor **sparse** weights (L1).

---

## L1 Regularization

- Penalty: **sum of absolute values** of weights, $\sum_i |w_i|$.
- Encourages **sparsity**: many weights can be driven **exactly to zero** → **feature selection** / effective removal of connections.

**Geometry:**

- **L1** constraint region: **diamond** (ℓ1 ball) with **corners on the axes**.
- Optima often land on **corners** → some coordinates **exactly zero**.

**Shape of the penalty:**

- **L2:** smooth **quadratic** → **gradual** shrinkage.
- **L1:** **nondifferentiable** corners at zero (in coordinate directions) → some weights **collapse** to **exactly** zero.

---

## When L1 vs L2 (Typical Practice)

| Aspect | L2 | L1 |
|--------|----|----|
| Typical effect | Small spread-out weights | Sparsity, exact zeros |
| Common use in deep nets | **Very common** default-style penalty | When **sparsity** is desired |
| Boundary | Smooth (disk) | Sharp corners (diamond) |

---

## Summary

- **Regularization** changes the **objective** to penalize complexity; **$\lambda$** sets data fit vs simplicity.
- **L2** penalizes large weights smoothly, encourages **distributed** small weights, and is widely used in deep networks.
- **L1** encourages **sparsity** and **feature selection** via diamond-shaped constraints.
- Both aim to **reduce overfitting** and improve **generalization**.
- **Next:** **Dropout**—a **stochastic** regularizer especially useful in **deep** networks.

---

## Exam-style cues

- **Write** $J = L_{\text{data}} + \lambda \Omega$ and explain $\lambda$.
- **Compare** L1 vs L2 geometrically and in terms of sparsity.
- **Explain** why minimizing training loss alone does not prevent overfitting.
