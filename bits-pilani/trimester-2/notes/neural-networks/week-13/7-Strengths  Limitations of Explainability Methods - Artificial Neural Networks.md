# 7-Strengths  Limitations of Explainability Methods - Artificial Neural Networks

## Learning Objectives

1. Understand the central idea behind 7-Strengths  Limitations of Explainability Methods - Artificial Neural Networks.
2. Connect this concept to the broader sequence/evaluation/diagnostics/optimization/responsible-AI pipeline as applicable.
3. Prepare exam-ready explanations, comparisons, and reasoning based on lecture flow.
4. By the end of this video, you will be able to compare explainability approaches, identify when an explanation is useful and when it is misleading.

---

## Core Concepts and Deep Notes

- This topic from Week 13 builds conceptual depth around **7-Strengths  Limitations of Explainability Methods** and should be revised as both a theory question and an application-oriented question.
- Focus on three layers of understanding: definition, mechanism, and implication (how it changes model behavior, training stability, or decision quality).
- In exam settings, score comes from linking intuition to formal reasoning: explain *why* the method exists, *how* it works, and *where* it can fail.
- Treat this lecture as part of a system-level story: data properties -> model design -> optimization/training signals -> evaluation and reliability.

## Detailed Lecture Notes

- In this video, we critically reflect on all the explainability methods we have studied so far.
- Rather than introducing new techniques, the goal here is to understand what these methods can and cannot tell us.
- By the end of this video, you will be able to compare explainability approaches, identify when an explanation is useful and when it is misleading.
- You will be able to recognize their limitations and avoid common misinterpretations when using them in practice.
- We have covered a wide range of explainability methods, from simple saliency maps to more principled approaches like shape and integrated gradients.
- Despite their differences, all of them aim to provide insight into why a model made a particular prediction.
- Explainability methods are undeniably useful.
- They improve transparency and trust.
- They help us debug models, identify spurious correlations and build trust with stakeholders.
- In regulated or high-stakes domains, they are often essential.
- However, these methods also have serious limitations.
- Most explanations are local, dependent on assumptions and sensitive to noise.

## Key Takeaways from the Lecture Transcription

- In this video, we critically reflect on all the explainability methods we have studied so far.
- Rather than introducing new techniques, the goal here is to understand what these methods can and cannot tell us.
- By the end of this video, you will be able to compare explainability approaches, identify when an explanation is useful and when it is misleading.
- You will be able to recognize their limitations and avoid common misinterpretations when using them in practice.
- We have covered a wide range of explainability methods, from simple saliency maps to more principled approaches like shape and integrated gradients.
- Despite their differences, all of them aim to provide insight into why a model made a particular prediction.
- Explainability methods are undeniably useful.
- They improve transparency and trust.
- However, these methods also have serious limitations.
- Most explanations are local, dependent on assumptions and sensitive to noise.
- They can also be unstable across similar inputs.
- Importantly, they do not provide causal guarantees.
- One of the biggest risks is overconfidence.
- Just because an explanation looks intuitive, does not mean it reflects the true reasoning of the model.
- Or we cannot just assume that the highlighted features are the true causes and one explanation method.
- The correct way to use explainability is as a diagnostic and investigative tool.
- Lastly, we should focus on patterns and not individual examples.
- Now, let us summarize the main points of this video.
- Explainability methods are powerful but limited.
- Explainability improves transparency, reveals influence and not causation.
- No method provides complete transparency and eliminates uncertainty completely.
- A responsible practitioner treats explanations with both curiosity and skepticism.
- In the next video, we move beyond explanations of individual predictions and examine a broader issue.
- Fairness, bias and responsibility in AI systems.

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
