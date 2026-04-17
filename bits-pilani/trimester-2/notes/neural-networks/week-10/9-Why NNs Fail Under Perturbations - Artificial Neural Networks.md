# 9-Why NNs Fail Under Perturbations - Artificial Neural Networks

## Learning Objectives

1. Understand the central idea behind 9-Why NNs Fail Under Perturbations - Artificial Neural Networks.
2. Connect this concept to the broader sequence/evaluation/diagnostics/optimization/responsible-AI pipeline as applicable.
3. Prepare exam-ready explanations, comparisons, and reasoning based on lecture flow.
4. In this video, we will discuss why neural networks fail under perturbations or small changes in the inputs.

---

## Core Concepts and Deep Notes

- This topic from Week 10 builds conceptual depth around **9-Why NNs Fail Under Perturbations** and should be revised as both a theory question and an application-oriented question.
- Focus on three layers of understanding: definition, mechanism, and implication (how it changes model behavior, training stability, or decision quality).
- In exam settings, score comes from linking intuition to formal reasoning: explain *why* the method exists, *how* it works, and *where* it can fail.
- Treat this lecture as part of a system-level story: data properties -> model design -> optimization/training signals -> evaluation and reliability.

## Detailed Lecture Notes

- In this video, we will discuss why neural networks fail under perturbations or small changes in the inputs.
- By the end of this video, you will be able to explain what robustness means, understand why small input changes can cause large changes in model predictions and see why perturbation-based evaluation is necessary.
- The focus here is not on fixes but on understanding why failures happen.
- Let's start with a simple but important question.
- In real world, inputs are rarely clean or exact.
- Measurements are noisy, sensors are imperfect and data naturally varies.
- So, the question is, should a very small change in input lead to a completely different prediction?
- Intuitively, we would expect a reliable model to be stable under such small changes.
- A common misconception is that high accuracy guarantees reliable behavior.
- In practice, a neural network can achieve excellent test accuracy and still behave in a very fragile way.
- It can be accurate and even well calibrated, yet still fail when inputs are slightly perturbed.
- This tells us that robustness is a separate property that must be evaluated explicitly.

## Key Takeaways from the Lecture Transcription

- In this video, we will discuss why neural networks fail under perturbations or small changes in the inputs.
- By the end of this video, you will be able to explain what robustness means, understand why small input changes can cause large changes in model predictions and see why perturbation-based evaluation is necessary.
- The focus here is not on fixes but on understanding why failures happen.
- Let's start with a simple but important question.
- In real world, inputs are rarely clean or exact.
- Measurements are noisy, sensors are imperfect and data naturally varies.
- So, the question is, should a very small change in input lead to a completely different prediction?
- Intuitively, we would expect a reliable model to be stable under such small changes.
- If a model changes its prediction drastically under such changes, that indicates a robustness problem.
- For example, in this particular case, for the original image, the model is 85% confident that it is a polar bear.
- But with small perturbation, now the model is 100% confident that it is a dishwasher.
- Such a drastic change in the labels.
- Why do neural networks fail under small perturbations?
- One reason is that neural networks learn highly non-linear decision boundaries.
- Another reason is the high dimensionality of input spaces, where small changes along certain directions can have a large effect.
- Finally, standard training procedures optimize average performance and not the local stability.
- For trustworthy systems, we need both of them.
- Standard test sets evaluate performance on individual data points.
- They do not probe what happens in the neighborhood around those points.
- Perturbation-based tests explicitly examine local behavior and reveal hidden fragility.
- Without such tests, robustness issues often remain invisible.
- So far, we have built intuition for why neural networks can fail under small perturbations.
- In the next video, we will move from intuition to practice.
- We will apply controlled perturbations to inputs, observe how predictions change and visualize model sensitivity.

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
