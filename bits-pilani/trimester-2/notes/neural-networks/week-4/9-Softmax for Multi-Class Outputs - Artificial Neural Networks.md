# Softmax for Multi-Class Outputs – Artificial Neural Networks (Module 4)

## Learning Objectives

By the end of this video you will:

1. **Explain** why **softmax** is needed for **multi-class** classification.
2. **State** its mathematical definition.
3. **Interpret** its outputs as a **probability distribution** over classes.
4. **Distinguish** softmax from **sigmoid**.

---

## From Binary to Multi-Class

- **Sigmoid** is for **binary** classification (two outcomes).
- Many tasks have **many** classes: e.g. 10 digits, many topics, hundreds of image categories.
- The model must output **one probability per class**, all **non-negative** and **summing to 1** → **softmax** is designed for this.

---

## Logits

- Before softmax, the last layer outputs a vector of **real numbers** — the **logits** (raw scores per class).
- Logits can be positive or negative, large or small; they do **not** yet form a probability distribution.

---

## Softmax Definition

For logit vector $\mathbf{z} = (z_1, \ldots, z_K)$, the softmax output for class $i$ is:
$$
p_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
$$
**Properties:**

- Every output is in $(0, 1)$.
- Outputs **sum to 1**.
- **Larger** logits get **larger** probabilities.
- Softmax turns arbitrary reals into a **valid categorical probability distribution**.

---

## Numerical Example

- Logits: $\mathbf{z} = (2, 1, 0.1)$.
- $e^{\mathbf{z}} \approx (7.3, 2.7, 1.1)$, sum $\approx 11.2$.
- Softmax: class 1 ≈ 0.66, class 2 ≈ 0.24, class 3 ≈ 0.1.
- Highest probability goes to class 1; all classes get some probability mass.

---

## What Softmax Does

1. **Exponentiation** makes all values **strictly positive**.
2. **Normalization** (divide by sum) forces total probability to be **exactly 1**.
3. It preserves **relative dominance**: if one logit is much larger, its probability is close to 1 and others stay small.
4. So it turns **relative confidence** among classes into **normalized probabilities**.

---

## Sigmoid vs Softmax

- **Sigmoid:** One output, one **probability**; for **binary** classification.
- **Softmax:** A **vector** of probabilities, one per class; they **compete** (sum to 1); for **multi-class** classification.
- **Sigmoid** models one event in isolation; **softmax** models a **mutually exclusive** set of classes.

---

## Summary

- **Softmax** is the standard output activation for **multi-class** classification.
- It maps **logits** to a **probability distribution** over classes: positive, sum to 1, competition between classes.
- It **generalizes** the role of sigmoid from binary to multi-class.
