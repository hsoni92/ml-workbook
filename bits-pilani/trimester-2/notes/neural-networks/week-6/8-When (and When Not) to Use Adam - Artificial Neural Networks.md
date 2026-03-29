# When (and When Not) to Use Adam – Artificial Neural Networks (Module 6)

## Learning Objectives

By the end of this video you will:

1. **Identify** when **Adam** is a strong choice and when it may **not** be ideal.
2. **Understand** the trade-off between **fast convergence** and **generalization**.
3. **Apply** guidelines for choosing **Adam vs other** optimizers in real training.

---

## When Adam Is a Good Choice

- Adam works **well out of the box**, needs **little** tuning, handles **noisy** gradients, and **converges quickly** early on.
- It is **robust** across many architectures. So Adam is often the **default** and is widely used in **NLP**, **vision**, and **transformers**.
- For a **new** project or a **new** architecture, Adam is usually a **safe first** choice.
- Adam tends to work best when training is **difficult or unstable**: deep/complex architectures, **sparse** gradients, **noisy** gradients (e.g. large mini-batch training), and during **early** experimentation when you want **fast** feedback and **minimal** hyperparameter tuning.

---

## When Adam May Not Be Best

- When **final generalization** is critical, models trained with Adam sometimes converge to **sharp** minima that **generalize worse**.
- For **fine-tuning** pre-trained models or **well-conditioned** problems, **SGD with momentum** often gives **better final** accuracy.
- So Adam is **fast** but not always best for the **last** stage of training.

---

## Trade-off

- **Adam:** Fast convergence, easy to use; may sacrifice some **generalization**.
- **SGD with momentum:** Slower, needs more tuning; often gives **better final** performance.
- Neither is **universally** better; the right choice depends on **goals**.

---

## Combining Both: Common Strategy

- **Start** with **Adam** to quickly reach a good region of the loss landscape.
- When training **stabilizes**, **switch** to **SGD with momentum** to **fine-tune** and improve generalization.
- This gives the benefits of **both** optimizers.

---

## Common Mistakes to Avoid

1. Using Adam **blindly** without considering the task.
2. **Never** adjusting learning rates.
3. Using Adam for **final** fine-tuning without **evaluating** whether SGD would do better.
4. **Assuming** Adam always outperforms other optimizers.

Optimizers are **tools**, not magic; choosing them **thoughtfully** makes a real difference.

---

## Summary

- **Adam** is an excellent **default**, especially for **complex** or **noisy** problems and for **fast** convergence in early training.
- **SGD with momentum** often performs **better** for **final** fine-tuning and generalization.
- **Switching** optimizers during training (e.g. Adam → SGD) is a **common** and **effective** practice.
