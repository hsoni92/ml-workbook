# 10-Limitations of RNNs - Artificial Neural Networks

## Learning Objectives

1. Understand the central idea behind 10-Limitations of RNNs - Artificial Neural Networks.
2. Connect this concept to the broader sequence/evaluation/diagnostics/optimization/responsible-AI pipeline as applicable.
3. Prepare exam-ready explanations, comparisons, and reasoning based on lecture flow.
4. In this video, we will examine the key limitations of recurrent neural networks.

---

## Core Concepts and Deep Notes

- This topic from Week 9 builds conceptual depth around **10-Limitations of RNNs** and should be revised as both a theory question and an application-oriented question.
- Focus on three layers of understanding: definition, mechanism, and implication (how it changes model behavior, training stability, or decision quality).
- In exam settings, score comes from linking intuition to formal reasoning: explain *why* the method exists, *how* it works, and *where* it can fail.
- Treat this lecture as part of a system-level story: data properties -> model design -> optimization/training signals -> evaluation and reliability.

## Detailed Lecture Notes

- In this video, we will examine the key limitations of recurrent neural networks.
- By the end of this video, you will be able to identify the structural challenges of RNN-based models, understand why these challenges persist even with LSTNs and GRUs, and see why alternative sequence modeling approaches were needed.
- Let's begin with an important clarification.
- They introduced memory and recurrence, and architectures like LSTMs and GRUs significantly improved the ability to model long-term dependencies.
- However, despite these successes, RNNs are not without limitations.
- Understanding these limitations helps to explain why newer architectures were developed.
- One of the most fundamental limitations of RNNs is that they process sequences sequentially.
- While gating mechanisms helps to mitigate vanishing gradients, they do not eliminate the problem entirely.
- In practice, performance often degrades when important dependencies span long time intervals.
- Another important limitation is the fixed size of the hidden state.
- Some details are inevitably lost, especially when multiple distant parts of the sequence are important.
- RNNs tend to focus more strongly on recent inputs because information from earlier time steps must pass through many intermediate states.
- Directly relating distant elements in a sequence, such as the beginning and end of a long sentence, is therefore difficult.
- Recurrent neural networks introduced powerful ideas for sequence modeling, but they also come with important limitations.
- In the next video, we will explore why attention mechanisms were introduced and how they addressed many of the limitations we just discussed.

## Key Takeaways from the Lecture Transcription

- In this video, we will examine the key limitations of recurrent neural networks.
- By the end of this video, you will be able to identify the structural challenges of RNN-based models, understand why these challenges persist even with LSTNs and GRUs, and see why alternative sequence modeling approaches were needed.
- Let's begin with an important clarification.
- Recurrent neural networks were a major breakthrough in sequence modeling.
- They introduced memory and recurrence, and architectures like LSTMs and GRUs significantly improved the ability to model long-term dependencies.
- RNN-based models have been successfully used in many real-world applications.
- However, despite these successes, RNNs are not without limitations.
- Understanding these limitations helps to explain why newer architectures were developed.
- As a result, training RNNs on long sequences can be slow and inefficient, especially on modern hardware that is optimized for parallel computation.
- This sequential dependency becomes a serious bottleneck at scale.
- Even with LSTMs and GRUs, modeling very long sequences remains challenging.
- While gating mechanisms helps to mitigate vanishing gradients, they do not eliminate the problem entirely.
- As sequences grow longer, it becomes increasingly difficult for the model to retain and use information from very distant time steps.
- In practice, performance often degrades when important dependencies span long time intervals.
- Another important limitation is the fixed size of the hidden state.
- In RNN-based models, the entire history of the sequence is compressed into a single hidden vector.
- RNNs tend to focus more strongly on recent inputs because information from earlier time steps must pass through many intermediate states.
- Directly relating distant elements in a sequence, such as the beginning and end of a long sentence, is therefore difficult.
- This indirect flow of information limits the model's ability to reason globally across the sequence.
- Now, let us summarize the main points of this video.
- Recurrent neural networks introduced powerful ideas for sequence modeling, but they also come with important limitations.
- Their inherently sequential nature makes training slow and hard to paralyze.
- Even with gating mechanisms, learning very long range and global dependencies remains challenging.
- In the next video, we will explore why attention mechanisms were introduced and how they addressed many of the limitations we just discussed.

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
