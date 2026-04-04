# Neural Networks – Module 6 Summary: Artificial Neural Networks

## Purpose of This Module

Module 6 focuses on **optimization**: how neural networks **learn** by using gradients to update parameters. The emphasis is on **training dynamics** — choosing the right **optimizer**, **learning rate**, and **schedule** together. Stability tools **prevent** failure; they do **not** guarantee success; that distinction is important.

---

## What We Learned (Flow of Module 6)

| Topic | Content |
|-------|--------|
| **Optimization** | Minimizing loss by adjusting weights and biases; navigating a high-dimensional loss surface (valleys, plateaus, saddle points). Optimizer controls step size, momentum, per-parameter scaling, stability (e.g. clipping). |
| **Gradient descent** | Step **downhill** opposite to the gradient; update $\theta \leftarrow \theta - \eta \nabla L$; **learning rate** $\eta$ is critical. |
| **Variants** | **Batch** (full data, stable, slow), **SGD** (one sample, noisy, fast), **mini-batch** (default: balance of speed and stability). **Batch size** affects noise, generalization, convergence. |
| **Adaptive methods** | **Single** LR for all parameters is limiting; **RMSProp** (squared gradients) and **Adam** (momentum + RMSProp, bias correction) give **per-parameter** step sizes. Handle noisy/sparse gradients, fast convergence. |
| **When to use Adam** | Good default for complex/noisy problems; **SGD + momentum** often better for **final** fine-tuning and generalization; **switching** optimizers during training is common. |
| **Fixed LR limiting** | Early training needs **large** steps; late training needs **small** steps; fixed LR is a poor compromise. |
| **LR schedules** | **Step decay**, **exponential**, **cosine annealing**, **warm-up**; match step size to phase of training; **warm-up** important for transformers and large batches. |
| **Adaptive vs scheduled** | Adaptive = per-parameter, automatic; scheduled = explicit change over time; **combining** both is common and effective. |
| **Gradient clipping** | Limits **magnitude** of updates (by value or by **norm**); **safeguard** against exploding gradients in RNNs, deep nets, large LR; does **not** fix vanishing gradients or replace good LR/init. |
| **Pitfalls** | **Saddle points**, **plateaus**, **noise**, **poor conditioning**; distinguish **optimization** issues (loss not decreasing) from **model/data** issues (loss decreases, performance poor). |
| **Convergence** | **Noisy** vs **smooth** descent; both can be valid; **batch size** and **optimizer** shape behaviour; focus on **trends**, not spikes. |

---

## Key Intuitions to Retain (Exam-Ready)

1. **Optimization** = how we **use** gradients to update parameters; it controls **speed**, **stability**, and **convergence**.
2. **Gradient descent** = step opposite to gradient; **learning rate** is the main hyperparameter.
3. **Mini-batch SGD** = default; **batch size** trades off noise vs stability and affects generalization.
4. **Adaptive** optimizers (RMSProp, Adam) give **per-parameter** learning rates; good for noisy/sparse gradients and fast early convergence.
5. **Adam** is a strong default; **SGD + momentum** often better for **final** fine-tuning; **switching** is a common strategy.
6. **LR schedules** (step, cosine, warm-up) match step size to **phase** of training; **fixed** LR is limiting.
7. **Gradient clipping** = safety mechanism for **exploding** gradients; **norm** clipping preserves direction.
8. **Stability** tools prevent failure; they do **not** guarantee success.

---

## Bridge to the Next Module

In the next module we focus on **regularization** and **generalization**:

- How to **prevent overfitting** and build models that perform well on **unseen** data.
- Techniques such as **weight decay**, **dropout**, **early stopping**, and **data augmentation**.
