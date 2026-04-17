# 10-Mitigation Strategies for Responsible AI - Artificial Neural Networks

## Learning Objectives

1. Understand the central idea behind 10-Mitigation Strategies for Responsible AI - Artificial Neural Networks.
2. Connect this concept to the broader sequence/evaluation/diagnostics/optimization/responsible-AI pipeline as applicable.
3. Prepare exam-ready explanations, comparisons, and reasoning based on lecture flow.
4. By the end of this video, you will be able to understand where bias mitigation can occur in an AI pipeline, what common strategies look like in practice, why mitigation always involves trade-offs, and appreciate why mitigation is a continuous process.

---

## Core Concepts and Deep Notes

- This topic from Week 13 builds conceptual depth around **10-Mitigation Strategies for Responsible AI** and should be revised as both a theory question and an application-oriented question.
- Focus on three layers of understanding: definition, mechanism, and implication (how it changes model behavior, training stability, or decision quality).
- In exam settings, score comes from linking intuition to formal reasoning: explain *why* the method exists, *how* it works, and *where* it can fail.
- Treat this lecture as part of a system-level story: data properties -> model design -> optimization/training signals -> evaluation and reliability.

## Detailed Lecture Notes

- In this video, we discuss the question, once bias is detected, what can we actually do to mitigate it?
- By the end of this video, you will be able to understand where bias mitigation can occur in an AI pipeline, what common strategies look like in practice, why mitigation always involves trade-offs, and appreciate why mitigation is a continuous process.
- Bias mitigation can happen at multiple points in the machine learning life cycle.
- Another example is correcting the bias labels.
- If historical decisions were unfair, blindly learning from them will perpetuate the bias.
- For instance, we might add a fairness constraint to the loss function that penalizes large differences in error rates across the groups.
- A more advanced example is adversarial de-biasing where the model is trained not only to make predictions but also to prevent another model from inferring protected attributes from its internal representations.
- A key reality is that fairness interventions often reduce overall accuracy.
- Improving fairness for one group may worsen outcomes for another.
- Different groups will have different fairness goals.
- This means mitigation is not purely a technical optimization problem.
- Bias can be mitigated at multiple stages, each with its own strengths and limitations.
- Trade-offs are unavoidable and must be made explicit.
- In the next video, we shift our focus to the future, exploring emerging trends in deep learning architectures that are shaping modern AI systems, starting with the Transformers.

## Key Takeaways from the Lecture Transcription

- In this video, we discuss the question, once bias is detected, what can we actually do to mitigate it?
- By the end of this video, you will be able to understand where bias mitigation can occur in an AI pipeline, what common strategies look like in practice, why mitigation always involves trade-offs, and appreciate why mitigation is a continuous process.
- Bias mitigation can happen at multiple points in the machine learning life cycle.
- We can intervene before training, during training, or after predictions are made.
- These are commonly referred to as pre-processing, in-processing, and post-processing strategies.
- Pre-processing strategies focus on the data.
- For example, suppose a hiring dataset contains far fewer examples from a particular group.
- One approach is to rebalance the dataset through resampling or re-weighting so that the model does not underlearn patterns from that group.
- For instance, we might add a fairness constraint to the loss function that penalizes large differences in error rates across the groups.
- A more advanced example is adversarial de-biasing where the model is trained not only to make predictions but also to prevent another model from inferring protected attributes from its internal representations.
- Post-processing strategies act after the model has made predictions.
- For example, a loan approval system might use different decision thresholds for different groups to equalize the false negative rates.
- These approaches are often easier to implement but may raise concerns about transparency and policy justification.
- A key reality is that fairness interventions often reduce overall accuracy.
- Improving fairness for one group may worsen outcomes for another.
- Different groups will have different fairness goals.
- Domain risk and stakeholder priorities all matter.
- Now, let us summarize the main points of this video.
- Bias can be mitigated at multiple stages, each with its own strengths and limitations.
- There is no universal solution.
- Trade-offs are unavoidable and must be made explicit.
- Responsible AI requires conscious design decisions, documentation and ongoing monitoring, not one-time fixes.
- In the next video, we will see you in the next video.
- In the next video, we shift our focus to the future, exploring emerging trends in deep learning architectures that are shaping modern AI systems, starting with the Transformers.

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
