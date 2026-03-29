# Adam – Momentum and RMSProp – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Understand** the intuition behind **Adam** and how it combines **momentum** and **RMSProp**.
2. **Interpret** the Adam update rule at a high level.
3. **Appreciate** why Adam became the **default** optimizer in many applications.

---

## Combining Two Ideas

- **Momentum** smooths updates and accelerates learning in **consistent** directions.
- **RMSProp** adapts learning rates **per parameter** to handle noisy and uneven gradients.
- Each alone solves only **part** of the problem. **Adam** combines **momentum** (direction) and **adaptive scaling** (stability) in one optimizer.
- So Adam can move **fast** in consistent directions, stay **stable** in noisy or steep regions, and handle **sparse** gradients well.

---

## What Adam Tracks

- **Two** running statistics per parameter:
  1. **Average of recent gradients** (first moment) — like **momentum**; gives the **direction** to move.
  2. **Average of squared gradients** (second moment) — the **RMSProp** part; controls **how big** each step should be.
- So Adam knows **where** to go and **how far** to go, **separately** for each parameter.

---

## Bias Correction

- These averages **start at zero**, so early in training they **underestimate** the true moments.
- Adam uses **bias correction** early in training to correct this. The important idea: Adam tracks both **direction** and **scale** of gradients over time.

---

## The Update Step

- The final update uses **both** corrected moments.
- **Direction** comes from the **momentum** term; **step size** is scaled by the **square root** of the second moment (variance).
- So updates are **smooth**, learning rates **adapt per parameter**, and **early** training is stabilized by bias correction. Adam effectively **normalizes** updates while keeping useful **directional** information.

---

## Why Adam Works Well in Practice

- Handles **noisy** mini-batch gradients.
- Works well with **sparse** gradients.
- **Minimal** tuning (defaults work for many tasks).
- **Fast** convergence and works across **many** architectures.
- So Adam is often the **default** optimizer for training deep neural networks.

---

## Limitations

- Adam can sometimes converge to **sharp** minima that **generalize worse** than solutions found by SGD.
- It can **mask** poor learning rate choices and make **debugging** harder.
- Many practitioners **switch** from Adam to **SGD** (with momentum) for **fine-tuning** in the final stages of training.

---

## Summary

- **Adam** combines **momentum** and **RMSProp** in one optimizer.
- It tracks both **gradient direction** and **scale** (first and second moments).
- **Bias correction** stabilizes early updates.
- It is **fast**, **adaptive**, and **widely** used, but **not** universally optimal; the next video discusses **when** to use Adam and when to avoid it.
