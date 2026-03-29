# Chain Rule – Artificial Neural Networks (Module 2)

## Learning Objectives

By the end of this video you will:

1. **Understand** why the chain rule is essential for **composite functions**.
2. **Apply** the chain rule to compute derivatives through **intermediate variables**.
3. **Compute** sensitivities with respect to **inputs** and **parameters**.
4. **Recognize** the chain rule as the **mathematical backbone** of deep neural networks.

---

## Why We Need the Chain Rule

- Many real-world systems are **not** described by a single simple equation. They are **compositions** of simpler functions.
- In such systems, the **output** depends on **intermediate variables**, and those intermediate variables depend on the **input**. So the effect of the input on the output is **indirect**.
- To compute sensitivities correctly in such systems we **must** use the **chain rule**.
- **Neural networks** are exactly of this form: **deep compositions** of many simple functions. So before studying neural network training, we must master the chain rule.

---

## Simplest Composite Function

- \( u = 3x \)
- \( y = u^2 \) (so \( y \) depends on \( x \) only through \( u \)).

We want \( \frac{dy}{dx} \). We **cannot** differentiate \( y \) directly with respect to \( x \) because \( y \) is given in terms of \( u \). So we use the **chain rule**:

\[
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
\]

Sensitivity **flows** from \( y \) → \( u \) → \( x \).

- \( \frac{du}{dx} = 3 \), \( \frac{dy}{du} = 2u \) ⇒ \( \frac{dy}{dx} = 2u \cdot 3 = 6u = 18x \).

---

## Two-Layer-Like Composite Function

- \( u = w_1 x + b_1 \)
- \( y = u^2 \)

Here:
- **Input:** \( x \)
- **Parameters:** \( w_1 \), \( b_1 \)
- **Intermediate:** \( u \)
- **Output:** \( y \)

**Important:** \( y \) depends on \( x \), \( w_1 \), and \( b_1 \) **only through \( u \)**. So **every** derivative of \( y \) with respect to any of these must be computed **via the chain rule through \( u \)**.

We want:
- \( \frac{dy}{dx} \)
- \( \frac{dy}{dw_1} \)
- \( \frac{dy}{db_1} \)

---

## Applying the Chain Rule

### 1. \( \frac{dy}{dx} \)

\[
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
\]

- \( u = w_1 x + b_1 \) ⇒ \( \frac{du}{dx} = w_1 \) (\( b_1 \) constant).
- \( y = u^2 \) ⇒ \( \frac{dy}{du} = 2u \).

So:
\[
\frac{dy}{dx} = 2u \cdot w_1.
\]

### 2. \( \frac{dy}{dw_1} \)

\[
\frac{dy}{dw_1} = \frac{dy}{du} \cdot \frac{du}{dw_1}
\]

- \( \frac{du}{dw_1} = x \) (treat \( x \), \( b_1 \) constant).
- \( \frac{dy}{du} = 2u \).

So:
\[
\frac{dy}{dw_1} = 2u \cdot x.
\]

### 3. \( \frac{dy}{db_1} \)

\[
\frac{dy}{db_1} = \frac{dy}{du} \cdot \frac{du}{db_1}
\]

- \( \frac{du}{db_1} = 1 \) (only \( b_1 \) varies).
- \( \frac{dy}{du} = 2u \).

So:
\[
\frac{dy}{db_1} = 2u.
\]

---

## Pattern and Extension to Deep Networks

- **Most real systems** are built as **functions of functions** → chain rule is needed.
- In a two-layer composite, **every** derivative of the output **passes through** the intermediate variable. So each **total** derivative is a **product of local** derivatives.
- This **same mechanism** extends to much deeper systems. That is why the **chain rule is the mathematical backbone** of all multilayer (and deep) neural networks: it is exactly what backpropagation implements.

---

## Summary (Quick Revision)

| Idea | Detail |
|------|--------|
| **Composite functions** | Output depends on input via intermediate variables → use chain rule. |
| **Two-layer example** | All derivatives of \( y \) go through \( u \): \( \frac{dy}{d(\cdot)} = \frac{dy}{du} \frac{du}{d(\cdot)} \). |
| **Total derivative** | Product of **local** derivatives along the path. |
| **Deep networks** | Chain rule extends naturally to many layers → backbone of backpropagation. |

> **Exam tip:** For any variable that affects \( y \) only through \( u \), always write \( \frac{dy}{d(\cdot)} = \frac{dy}{du} \cdot \frac{du}{d(\cdot)} \).
