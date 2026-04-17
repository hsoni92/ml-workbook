# 4-Feature Importance  Saliency Maps - Artificial Neural Networks

## Learning Objectives

1. Understand the central idea behind 4-Feature Importance  Saliency Maps - Artificial Neural Networks.
2. Connect this concept to the broader sequence/evaluation/diagnostics/optimization/responsible-AI pipeline as applicable.
3. Prepare exam-ready explanations, comparisons, and reasoning based on lecture flow.
4. By the end of this video, you will be able to understand what feature importance means, how saliency maps work at a high level, and what their strengths and limitations are.

---

## Core Concepts and Deep Notes

- This topic from Week 13 builds conceptual depth around **4-Feature Importance  Saliency Maps** and should be revised as both a theory question and an application-oriented question.
- Focus on three layers of understanding: definition, mechanism, and implication (how it changes model behavior, training stability, or decision quality).
- In exam settings, score comes from linking intuition to formal reasoning: explain *why* the method exists, *how* it works, and *where* it can fail.
- Treat this lecture as part of a system-level story: data properties -> model design -> optimization/training signals -> evaluation and reliability.

## Detailed Lecture Notes

- In this video, we begin our study of concrete explainability methods.
- We start with feature importance and saliency maps the simplest and most intuitive ways to understand neural network predictions.
- By the end of this video, you will be able to understand what feature importance means, how saliency maps work at a high level, and what their strengths and limitations are.
- At its core, feature importance answers a simple question, which inputs mattered most?
- Depending on the context, we may ask this globally, that is across the entire data set, or locally for a single prediction.
- For example, which words influenced a sentiment prediction, or which pixels influenced an image classification.
- In deep learning, especially for images, feature importance is visualized using saliency maps.
- A saliency map assigns an important score to each input pixel, highlighting the regions that influence the prediction.
- Most saliency methods rely on gradients.
- If changing a pixel slightly causes a large change in the output, that pixel is considered important.
- We visualize this sensitivity as a heat map over the input.
- Saliency maps are extremely useful for debugging.

## Key Takeaways from the Lecture Transcription

- In this video, we begin our study of concrete explainability methods.
- We start with feature importance and saliency maps the simplest and most intuitive ways to understand neural network predictions.
- By the end of this video, you will be able to understand what feature importance means, how saliency maps work at a high level, and what their strengths and limitations are.
- At its core, feature importance answers a simple question, which inputs mattered most?
- Depending on the context, we may ask this globally, that is across the entire data set, or locally for a single prediction.
- For example, which words influenced a sentiment prediction, or which pixels influenced an image classification.
- In deep learning, especially for images, feature importance is visualized using saliency maps.
- A saliency map assigns an important score to each input pixel, highlighting the regions that influence the prediction.
- Most saliency methods rely on gradients.
- If changing a pixel slightly causes a large change in the output, that pixel is considered important.
- We visualize this sensitivity as a heat map over the input.
- Saliency maps are extremely useful for debugging.
- They help us see whether a model is focusing on meaningful regions or relying on spurious patterns.
- However, they show influence, not the reasoning.
- Saliency maps can be noisy and unstable.
- They are not causal explanations and should not be treated as definitive evidence of understanding.
- This is a recurring theme in explainability.
- Now, let us summarize the main points of this video.
- Feature importance identifies influential inputs.
- Saliency maps extend this idea to deep networks.
- They are intuitive and visual but limited.
- Hence, they are best used as diagnostic tools, not proofs.
- In the next video, we move beyond gradients to perturbation-based methods like line and shape, which take a very different approach to explanation.

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
