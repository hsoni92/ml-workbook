# 5-Perturbation based Methods - Artificial Neural Networks

## Learning Objectives

1. Understand the central idea behind 5-Perturbation based Methods - Artificial Neural Networks.
2. Connect this concept to the broader sequence/evaluation/diagnostics/optimization/responsible-AI pipeline as applicable.
3. Prepare exam-ready explanations, comparisons, and reasoning based on lecture flow.
4. By the end of this video, you will be able to understand the core idea behind perturbation-based methods, how LIME and SHAP generate explanations and work at a high level, and what their strengths and limitations are.

---

## Core Concepts and Deep Notes

- This topic from Week 13 builds conceptual depth around **5-Perturbation based Methods** and should be revised as both a theory question and an application-oriented question.
- Focus on three layers of understanding: definition, mechanism, and implication (how it changes model behavior, training stability, or decision quality).
- In exam settings, score comes from linking intuition to formal reasoning: explain *why* the method exists, *how* it works, and *where* it can fail.
- Treat this lecture as part of a system-level story: data properties -> model design -> optimization/training signals -> evaluation and reliability.

## Detailed Lecture Notes

- In this video, we study about perturbation-based explainability, focusing on LIME and SHAP.
- By the end of this video, you will be able to understand the core idea behind perturbation-based methods, how LIME and SHAP generate explanations and work at a high level, and what their strengths and limitations are.
- The fundamental idea here is simple.
- If a small change in an input feature causes a large change in the prediction, that feature must be important.
- Perturbation-based methods systematically apply this idea by modifying inputs and observing the model's response.
- LIME focuses on explaining a single prediction.
- It generates many perturbed versions of the input around that point, queries the black box model, and then fits a simple interpretable model locally.
- The explanation comes from this local surrogate, not from the original model itself.
- SHAP takes a more principled approach rooted in game theory.
- Each feature is treated as a player contributing to the final prediction.
- SHAP computes how much each feature contributes on average across all possible feature combinations.
- This gives SHAP strong theoretical guarantees but at higher computational cost.

## Key Takeaways from the Lecture Transcription

- In this video, we study about perturbation-based explainability, focusing on LIME and SHAP.
- By the end of this video, you will be able to understand the core idea behind perturbation-based methods, how LIME and SHAP generate explanations and work at a high level, and what their strengths and limitations are.
- The fundamental idea here is simple.
- If a small change in an input feature causes a large change in the prediction, that feature must be important.
- Perturbation-based methods systematically apply this idea by modifying inputs and observing the model's response.
- LIME focuses on explaining a single prediction.
- It generates many perturbed versions of the input around that point, queries the black box model, and then fits a simple interpretable model locally.
- The explanation comes from this local surrogate, not from the original model itself.
- SHAP takes a more principled approach rooted in game theory.
- Each feature is treated as a player contributing to the final prediction.
- SHAP computes how much each feature contributes on average across all possible feature combinations.
- This gives SHAP strong theoretical guarantees but at higher computational cost.
- Conceptually, LIME is faster and more heuristic, while SHAP is slower but more theoretically grounded.
- Both produce local explanations but SHAP explanations are more consistent across runs and models.
- One major advantage of perturbation-based methods is that they are model agnostic.
- They can work with any black box model, neural networks, tree-based models or ensembles, making them very practical for use.
- They can be computationally expensive, sensitive to how perturbations are generated, local explanations may not generalize, and sometimes misleading if perturbations move inputs off the true data manifold.
- Now, let us summarize the main points of this video.
- Perturbation-based methods like LIME and SHAP are powerful tools for explainability.
- They explain predictions by probing sensitivity.
- They explain predictions by probing sensitivity.
- LIME uses local surrogate models, while SHAP uses principal feature attribution.
- They provide flexible model agnostic explanations, but their results must be interpreted with care.
- In the next video, we will look at explainability methods designed specifically for deep neural networks, including GradCam and integrated gradients.

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
