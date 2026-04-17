# 4-Batch Size  Its Effects on Training - Artificial Neural Networks

## Learning Objectives

1. Understand the central idea behind 4-Batch Size  Its Effects on Training - Artificial Neural Networks.
2. Connect this concept to the broader sequence/evaluation/diagnostics/optimization/responsible-AI pipeline as applicable.
3. Prepare exam-ready explanations, comparisons, and reasoning based on lecture flow.
4. In this demo, we will study how batch size affects neural network training dynamics.

---

## Core Concepts and Deep Notes

- This topic from Week 12 builds conceptual depth around **4-Batch Size  Its Effects on Training** and should be revised as both a theory question and an application-oriented question.
- Focus on three layers of understanding: definition, mechanism, and implication (how it changes model behavior, training stability, or decision quality).
- In exam settings, score comes from linking intuition to formal reasoning: explain *why* the method exists, *how* it works, and *where* it can fail.
- Treat this lecture as part of a system-level story: data properties -> model design -> optimization/training signals -> evaluation and reliability.

## Detailed Lecture Notes

- We will observe how batch size influences the training loss behavior, gradient noise and stability, and smoothness of optimization.
- Bath size determines how many samples are used to compute one gradient update.
- Importantly, batch size does not change the objective function.
- We will track training loss and gradient norm in our training to measure the noise and stability.
- Now, let's look at the effect of batch size on gradient noise.
- In this particular plot, we see that small batches show high variability in gradient magnitude.
- Large batches produce stable and smooth gradients.
- And full batch gradients are almost deterministic.
- This highlights the trade-off between stability and exploration.
- Batch size controls gradient noise, not the loss function.
- Manually tuning these hyperparameters quickly becomes impractical.
- In the next video, we will see why manual tuning does not scale and how automated hyperparameters search addresses this challenge.

## Key Takeaways from the Lecture Transcription

- In this demo, we will study how batch size affects neural network training dynamics.
- To ensure a controlled experiment, we keep the dataset, model, and optimizer fixed.
- We will vary only the batch size.
- We will observe how batch size influences the training loss behavior, gradient noise and stability, and smoothness of optimization.
- So, what does batch size control?
- Bath size determines how many samples are used to compute one gradient update.
- Small batch sizes means noisy but frequent updates, while large batch sizes result in smooth but less stochastic updates.
- Importantly, batch size does not change the objective function.
- Now, we compare clearly separated batch sizes regimes.
- We will use a small, medium, large, and full batch.
- So, we can see here, we are training with different batch sizes of 16, 64, 256, and the full dataset.
- Now, let's see the effect of batch size on training loss.
- So, in this graph, we can see that small batch sizes produce noisy loss curves.
- Larger batch sizes, larger batch sizes produce smoother and more stable curves.
- And full batch training is the smoothest but updates are less frequent.
- It can help optimization escape the sharp regions.
- Batch size controls gradient noise, not the loss function.
- Small batches result in noisy updates.
- Often better exploration.
- And large batches result in smooth updates and can converge to sharper minima.
- In practice, batch size and learning rate must be tuned together.
- So far, we have seen how learning rate and batch size shape the training behavior.
- Manually tuning these hyperparameters quickly becomes impractical.
- In the next video, we will see why manual tuning does not scale and how automated hyperparameters search addresses this challenge.

## Common Exam Pitfalls

- Writing only definitions without connecting to training behavior, model limitations, or practical consequences.
- Mixing related concepts (for example: model capacity vs generalization, calibration vs accuracy, or explainability vs fairness) without clear boundaries.
- Ignoring assumptions and failure modes; exam questions often test when a method breaks or needs modification.
- Not using the terminology used in class (state, gradients, gates, uncertainty, diagnostics, reproducibility, bias metrics, etc.) in precise context.

## Summary

- This note converts the lecture transcript into exam-focused revision points with conceptual flow, mechanism-level understanding, and practical reasoning.
- Revise this along with nearby lectures in the same week to answer integrative questions that combine design choice, optimization behavior, and evaluation criteria.

## Exam-Style Cues

- Define the core concept in one precise paragraph and state why it is needed in neural-network practice.
- Explain the process/mechanism step-by-step using correct technical terms from the lecture.
- Compare this concept with one close alternative and justify when each is preferred.
- Mention one implementation or diagnostic checklist that improves reliability in real training workflows.
