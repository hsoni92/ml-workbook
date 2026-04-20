# Ensuring Reproducibility - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. **Define** reproducibility in the context of deep learning experiments.
2. **Identify** the major sources of randomness that make repeated runs differ.
3. **Explain** why reproducibility is necessary for fair comparison and debugging.
4. **List** the practical controls required to make experiments reproducible.

---

## What Reproducibility Means

Reproducibility means rerunning the same experiment under the same conditions and obtaining the same result, or at least a statistically consistent result when exact determinism is difficult.

This sounds simple, but deep learning makes it surprisingly difficult because training contains many hidden sources of stochasticity.

---

## Why Reproducibility Matters

The lecture makes a strong point: lack of reproducibility is not just an academic inconvenience. It is dangerous for practical work.

If results are not reproducible:

- you cannot trust claimed improvements,
- you cannot compare experiments fairly,
- and debugging becomes much harder because you do not know whether a change in outcome came from your code or from randomness.

So reproducibility is not extra polish. It is part of the method.

---

## Why Deep Learning Runs Differ

Training can vary from run to run because of several sources of randomness and variation.

| Source | How It Changes Results |
|---|---|
| **Random initialization** | Different starting weights lead optimization down different paths |
| **Data split randomness** | Different train/validation partitions change what the model sees |
| **Data order and shuffling** | Batch sequence changes update history |
| **Stochastic layers** | Methods like dropout intentionally inject randomness |
| **Non-deterministic hardware behavior** | Some GPU operations vary because of execution order |
| **Software and environment drift** | Framework, driver, and package differences can alter outcomes |

The important lesson is that "same code" does not automatically mean "same experiment."

---

## The Lecture Demonstration

The notebook gives a clear demonstration of the problem.

- First, the same code is run twice **without** fixing seeds.
- The two runs produce different accuracies: **94.0%** and **93.6%**.

Then the experiment is repeated with seed control and fixed split randomness:

- numpy seed is fixed,
- PyTorch seed is fixed,
- data splitting randomness is fixed.

This time, repeated runs produce the **same** value: **92.3%** in both cases.

The conclusion is straightforward:

**Reproducibility does not happen automatically. It must be engineered.**

---

## Reproducibility Checklist

| Control Item | What To Do |
|---|---|
| **Random seeds** | Fix seeds across all relevant libraries and workers |
| **Data splits** | Use deterministic train/validation/test splits |
| **Hyperparameter logging** | Record exact settings used in every run |
| **Checkpoints** | Save model states so results can be revisited |
| **Environment tracking** | Record framework versions, packages, drivers, and hardware context |
| **Log hygiene** | Keep runs separate instead of mixing outputs in one folder |

This checklist converts reproducibility from a vague idea into concrete practice.

---

## Why Reproducibility Helps Debugging

Suppose accuracy changes after you edit a model or training script.

Without reproducibility, you do not know whether the difference came from:

- the code change,
- the random initialization,
- a different split,
- or a changed environment.

With reproducibility controls in place, you can isolate causes much more reliably. That is why reproducibility is essential not only for reporting results, but also for diagnosing problems.

---

## Different Levels of Reproducibility

- **Exact reproducibility**: repeated runs produce exactly the same outputs and metrics.
- **Statistical reproducibility**: repeated runs are not bit-for-bit identical, but their behavior remains consistent.
- **Conclusion reproducibility**: repeated experiments support the same overall conclusion, such as one model being consistently better than another.

This distinction is useful because some hardware or software settings make exact determinism hard, but the experiment should still support stable conclusions.

---

## Common Mistakes

- Fixing only one seed while leaving data splitting or shuffling uncontrolled.
- Reusing the same log directory for different experiments.
- Changing package versions without recording them.
- Assuming reproducibility is guaranteed because the code file did not change.

---

## Summary

- Reproducibility means being able to rerun an experiment under the same conditions and obtain the same or statistically consistent result.
- Deep learning makes this difficult because of randomness in initialization, data order, stochastic operations, and environment details.
- Reproducibility is essential for **trustworthy comparison**, **reliable debugging**, and **sound conclusions**.

**Bridge to the next note:** once experiments are reproducible, the next step is to organize them into a complete end-to-end workflow for professional model development.
