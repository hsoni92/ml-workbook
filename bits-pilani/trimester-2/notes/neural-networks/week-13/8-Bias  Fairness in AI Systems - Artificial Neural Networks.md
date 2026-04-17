# 8-Bias  Fairness in AI Systems - Artificial Neural Networks

## Learning Objectives

1. Understand the central idea behind 8-Bias  Fairness in AI Systems - Artificial Neural Networks.
2. Connect this concept to the broader sequence/evaluation/diagnostics/optimization/responsible-AI pipeline as applicable.
3. Prepare exam-ready explanations, comparisons, and reasoning based on lecture flow.
4. In this video, we will discuss bias and fairness in AI systems.

---

## Core Concepts and Deep Notes

- This topic from Week 13 builds conceptual depth around **8-Bias  Fairness in AI Systems** and should be revised as both a theory question and an application-oriented question.
- Focus on three layers of understanding: definition, mechanism, and implication (how it changes model behavior, training stability, or decision quality).
- In exam settings, score comes from linking intuition to formal reasoning: explain *why* the method exists, *how* it works, and *where* it can fail.
- Treat this lecture as part of a system-level story: data properties -> model design -> optimization/training signals -> evaluation and reliability.

## Detailed Lecture Notes

- In this video, we will discuss bias and fairness in AI systems.
- By the end of this video, you will be able to understand what bias means in the context of AI, identify some common sources of fit, and why fairness must be treated as a separate concern from model accuracy.
- And finally, you will understand the need for fairness evaluation and mitigation.
- When we talk about bias in AI, we are not talking about opinions or intent.
- Bias refers to systematic differences in how a model behaves across different groups.
- This kind of bias is often invisible if we only look at aggregate performance metrics.
- Bias most commonly comes from data, not from malicious intent.
- Consider historical bias.
- Another example is representation bias.
- There is also measurement bias.
- Finally, deployment bias occurs when a model is used in a context different from the one it was trained for.
- One of the most important ideas here is that accuracy and fairness are not the same thing.
- Fairness requires us to look at who the model is right or wrong for.
- This is why fairness is not just a technical issue.
- In the next video, we will look at fairness metrics and detection techniques and see how fairness can be quantified in practice.

## Key Takeaways from the Lecture Transcription

- In this video, we will discuss bias and fairness in AI systems.
- By the end of this video, you will be able to understand what bias means in the context of AI, identify some common sources of fit, and why fairness must be treated as a separate concern from model accuracy.
- And finally, you will understand the need for fairness evaluation and mitigation.
- When we talk about bias in AI, we are not talking about opinions or intent.
- Bias refers to systematic differences in how a model behaves across different groups.
- For example, imagine a loan approval model that has a lower approval rate for one demographic group, even when applicants have similar financial profiles.
- The model may be accurate overall, but its errors are not evenly distributed.
- This kind of bias is often invisible if we only look at aggregate performance metrics.
- If past hiring decisions favored certain groups, a model trained on historical hiring data will learn and reproduce those patterns.
- Another example is representation bias.
- If a face recognition data set contains far fewer images of certain skin tones, the model will perform worse on those groups.
- There is also measurement bias.
- For instance, using zip code as a proxy for credit worthiness can unintentionally encode socioeconomic or racial information.
- Finally, deployment bias occurs when a model is used in a context different from the one it was trained for.
- For example, a healthcare model trained in one country but deployed in another.
- One of the most important ideas here is that accuracy and fairness are not the same thing.
- Fairness requires us to look at who the model is right or wrong for.
- Unfair AI systems can have serious real-world consequences.
- In finance, they can deny opportunities.
- In healthcare, they can delay or miss direct treatment.
- In legal or administrative systems, they can reinforce existing inequalities.
- This is why fairness is not just a technical issue.
- It is an ethical, legal and social responsibility.
- In the next video, we will look at fairness metrics and detection techniques and see how fairness can be quantified in practice.

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
