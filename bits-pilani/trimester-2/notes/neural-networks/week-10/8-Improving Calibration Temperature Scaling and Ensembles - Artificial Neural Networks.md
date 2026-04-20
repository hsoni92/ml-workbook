# Improving Calibration: Temperature Scaling and Ensembles - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain why calibration can be improved **after training**.
2. Describe how **temperature scaling** changes predicted probabilities.
3. Explain why **ensembles** often improve confidence quality.
4. Distinguish between improving **accuracy** and improving **calibration**.

---

## Why We Need Calibration Improvement

In the previous note, we saw that a neural network can be accurate yet still poorly calibrated. That naturally leads to the next question:

**Can we improve the quality of predicted probabilities without retraining the whole model from scratch?**

The transcript introduces two answers:

- **temperature scaling**, a simple post-hoc correction,
- **ensembles**, which improve reliability by averaging multiple models.

---

## Two Main Approaches

| Method | Core Idea | Typical Accuracy Effect | Typical Calibration Effect | Cost |
| --- | --- | --- | --- | --- |
| **Temperature scaling** | Rescale logits using a single scalar temperature before sigmoid/softmax | Usually little change | Often noticeably better | Low |
| **Ensembles** | Average predictions from multiple models | Often stable or slightly better | Often improves | Higher |

Both methods target **confidence quality**, but they do so in different ways.

---

## Temperature Scaling

### Core Idea

Temperature scaling adjusts the logits before converting them into probabilities.

If `T > 1`, the predicted distribution becomes **softer**, which often reduces overconfidence.

```text
Train model
-> freeze model weights
-> choose temperature T on validation data
-> rescale logits
-> recompute probabilities
-> re-check reliability diagram and ECE
```

### Why It Helps

- It directly targets **overly peaked probabilities**.
- It usually keeps the **ranking of predictions** similar.
- It is a **post-processing step**, so full retraining is not required.

### Demo Detail from the Transcript

The transcript uses a model with about **95% accuracy** before calibration. After applying temperature scaling with **T = 2**, the reliability curve moves closer to the diagonal while the accuracy remains about **95%**.

This is the main pedagogical point:

> **Calibration can improve even when raw accuracy stays almost unchanged.**

---

## Ensembles

### Core Idea

An ensemble combines predictions from multiple independently trained models and averages them.

The intuition is that individual models may be overconfident in different ways. Averaging can reduce those extreme confidence errors.

### Why Ensembles Help

- different models make slightly different mistakes,
- confidence spikes may cancel out when averaged,
- uncertainty estimates often become more stable.

In the transcript demo, the ensemble behavior is simulated by introducing small variations in logits, and the ECE improves slightly to around **4.1%**.

So ensembles can improve calibration, though the amount of improvement depends on the setting.

---

## Temperature Scaling vs Ensembles

### Temperature Scaling

- simple,
- cheap,
- easy to apply after training,
- mainly fixes confidence without changing the model itself.

### Ensembles

- usually more computationally expensive,
- require multiple models or multiple predictive paths,
- often help both **calibration** and **uncertainty behavior**.

So if the goal is a lightweight correction, temperature scaling is attractive. If the goal is stronger predictive reliability and uncertainty handling, ensembles are often more powerful but more costly.

---

## Practical Caveats

- Calibration parameters should be tuned on **validation data**, not test data.
- Always re-check both:
  - **predictive performance**, and
  - **calibration metrics** such as ECE.
- Better calibration does **not automatically** mean higher accuracy.
- Ensembles may improve trustworthiness but add **compute, memory, and latency** costs.

---

## Summary and Exam-Ready Takeaways

- Calibration can often be improved **after training**.
- **Temperature scaling** softens probabilities by rescaling logits and often improves calibration with little effect on accuracy.
- **Ensembles** improve calibration more indirectly by averaging multiple predictions and reducing extreme confidence.
- Improving **confidence quality** is different from improving **raw accuracy**.
- ECE and reliability diagrams should be compared **before and after** calibration.

**Bridge to next topic:** Calibration handles confidence quality, but another question remains: **why do neural networks fail when the input is only slightly perturbed?**
