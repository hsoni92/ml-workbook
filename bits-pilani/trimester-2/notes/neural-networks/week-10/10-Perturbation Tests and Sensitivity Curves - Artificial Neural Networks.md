# 10-Perturbation Tests and Sensitivity Curves - Artificial Neural Networks

## Learning Objectives

1. Understand the central idea behind 10-Perturbation Tests and Sensitivity Curves - Artificial Neural Networks.
2. Connect this concept to the broader sequence/evaluation/diagnostics/optimization/responsible-AI pipeline as applicable.
3. Prepare exam-ready explanations, comparisons, and reasoning based on lecture flow.
4. In this video, we will see a demo of perturbation tests and sensitivity curves.

---

## Core Concepts and Deep Notes

- This topic from Week 10 builds conceptual depth around **10-Perturbation Tests and Sensitivity Curves** and should be revised as both a theory question and an application-oriented question.
- Focus on three layers of understanding: definition, mechanism, and implication (how it changes model behavior, training stability, or decision quality).
- In exam settings, score comes from linking intuition to formal reasoning: explain *why* the method exists, *how* it works, and *where* it can fail.
- Treat this lecture as part of a system-level story: data properties -> model design -> optimization/training signals -> evaluation and reliability.

## Detailed Lecture Notes

- In this video, we will see a demo of perturbation tests and sensitivity curves.
- So far, we have evaluated neural networks using accuracy, loss, calibration.
- In this demo, we ask a new question.
- How stable is a neural network when the input is slightly perturbed?
- This property is known as robustness.
- As we run this demo, focus on how predictions behave under small input noise, how performance changes as perturbations increase, whether degradation is gradual or sudden.
- This behavior is summarized using a sensitivity curve.
- Now let's start with the demo.
- As always, we'll just import the standard libraries and fix the seed.
- Here again, we are using a clean data set for binary classification.
- Let's create our data set.
- Then we will train a standard neural network normally.

## Key Takeaways from the Lecture Transcription

- In this video, we will see a demo of perturbation tests and sensitivity curves.
- So far, we have evaluated neural networks using accuracy, loss, calibration.
- In this demo, we ask a new question.
- How stable is a neural network when the input is slightly perturbed?
- This property is known as robustness.
- As we run this demo, focus on how predictions behave under small input noise, how performance changes as perturbations increase, whether degradation is gradual or sudden.
- This behavior is summarized using a sensitivity curve.
- Now let's start with the demo.
- Now let's look at the baseline performance of the model without any perturbation.
- So we see that the baseline accuracy is around 95%.
- Now to apply perturbation, what we do is we apply some small Gaussian noise to the input features.
- The key idea here is that the real world data is never exact.
- So the model should adapt to these kinds of degradation.
- This is the function for adding the noise.
- So now what we are doing is we will gradually increase the perturbation strength and measure the accuracy.
- Then we will plot the sensitivity curve.
- Now let us summarize the main points of this video.
- Perturbation tests evaluate robustness explicitly.
- Sensitivity curves reveal how models fail.
- Accuracy alone cannot capture robustness.
- Robust models degrade gracefully under noise.
- Robustness is critical in real-world noisy environments.
- If a model fails under tiny perturbations, it cannot be trusted in production.
- In the next video, we will study uncertainty more explicitly using entropy and multi-class probability distributions.

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
