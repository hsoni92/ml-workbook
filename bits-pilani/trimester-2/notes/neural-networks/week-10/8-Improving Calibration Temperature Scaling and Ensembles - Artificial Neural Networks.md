# 8-Improving Calibration Temperature Scaling and Ensembles - Artificial Neural Networks

## Learning Objectives

1. Understand the central idea behind 8-Improving Calibration Temperature Scaling and Ensembles - Artificial Neural Networks.
2. Connect this concept to the broader sequence/evaluation/diagnostics/optimization/responsible-AI pipeline as applicable.
3. Prepare exam-ready explanations, comparisons, and reasoning based on lecture flow.
4. In this video, we will study temperature scaling and ensembles to improve the calibration of the models.

---

## Core Concepts and Deep Notes

- This topic from Week 10 builds conceptual depth around **8-Improving Calibration Temperature Scaling and Ensembles** and should be revised as both a theory question and an application-oriented question.
- Focus on three layers of understanding: definition, mechanism, and implication (how it changes model behavior, training stability, or decision quality).
- In exam settings, score comes from linking intuition to formal reasoning: explain *why* the method exists, *how* it works, and *where* it can fail.
- Treat this lecture as part of a system-level story: data properties -> model design -> optimization/training signals -> evaluation and reliability.

## Detailed Lecture Notes

- In this video, we will study temperature scaling and ensembles to improve the calibration of the models.
- In the previous video, we saw that a neural network can be accurate but still poorly calibrated.
- In this demo, we will look at how we can improve the quality of predicted probabilities without retraining the model.
- We will study two methods, temperature and ensembles.
- The model here is already trained.
- We will use the same model again.
- So, let's start the demo.
- We are here importing the standard libraries like we always do and setting up a seed for reproducibility.
- We will use the same dataset that we used earlier and we are using the same neural network model.
- Now, let's train the same model for around 50 epochs.
- Now, let's look at the model's accuracy before applying any kind of calibration.
- So, like before, we see that the accuracy this time also is around 95%.

## Key Takeaways from the Lecture Transcription

- In this video, we will study temperature scaling and ensembles to improve the calibration of the models.
- In the previous video, we saw that a neural network can be accurate but still poorly calibrated.
- In this demo, we will look at how we can improve the quality of predicted probabilities without retraining the model.
- We will study two methods, temperature and ensembles.
- The model here is already trained.
- We will use the same model again.
- So, let's start the demo.
- We are here importing the standard libraries like we always do and setting up a seed for reproducibility.
- So, while applying temperature scaling, what we do is we rescale the logits and then apply the sigmoid function.
- So, here we are applying a temperature scaling with T is equal to 2.
- After applying temperature scaling, this is how the reliability diagram looks now.
- You can see that the green line is much closer to the diagonal while the orange line which is before the temperature scaling is slightly away.
- Now, let's see what happens to the accuracy.
- So, before and after temperature scaling, the accuracy is around 95% only.
- So, it is not impacting the accuracy in any way.
- Now, let's see what happens to the model.
- So, orange line shows for a single model and the green line shows the curve for the ensemble of five different models.
- So, here we see that ECE has not improved much.
- Now, let's summarize the main points of this video.
- Temperature scaling directly fixes confidence without changing the accuracy.
- Ensembles improve calibration indirectly via averaging.
- Both approaches reduce overconfidence.
- Calibration is essential when probabilities drive decisions.
- In the next video, we will understand why neural networks fail under perturbations.

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
