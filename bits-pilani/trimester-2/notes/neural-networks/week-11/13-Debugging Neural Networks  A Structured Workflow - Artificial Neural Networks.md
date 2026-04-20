# Debugging Neural Networks: A Structured Workflow - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain why neural network debugging requires a **structured workflow**.
2. Use **gradients**, **activations**, and **parameters** as the three core diagnostic layers.
3. Trace a broken training run from symptom to root cause and then to verified fix.

---

## Why Trial-and-Error Is Not Enough

This lesson steps back from individual failure modes and asks a broader question:

> How should we debug neural networks systematically?

The need for structure comes from the fact that deep models often fail **silently**.

- Loss may decrease a little, but useful learning may not be happening.
- Training may appear stable, while internal representations are collapsing.
- Random hyperparameter changes may occasionally help, but they do not explain the real cause.

That is why professional debugging is not based on guessing. It is based on **internal evidence**.

---

## The Three Core Diagnostic Layers

The whole module is organized around three internal signals:

### 1. Gradients

Gradients tell us whether learning signals are flowing through the network.

### 2. Activations

Activations tell us whether neurons are alive, responsive, and operating in useful regimes.

### 3. Parameters

Parameters tell us whether the model is actually changing in a healthy way.

The key insight is that every major failure mode studied in the module shows up in at least one of these three signals.

---

## A Practical Debugging Workflow

The lesson demonstrates a broken network and then applies the workflow step by step.

### Step 1: Observe the external symptom

The intentionally bad configuration uses:

- excessive depth,
- a very high learning rate,
- and no normalization.

The observed symptoms are:

- training loss jumps quickly,
- then plateaus at a high value,
- and the model fails to make meaningful progress.

### Step 2: Inspect gradient norms

The gradient norm spikes early and then stays high instead of decaying in a healthy way.

This points to **optimizer instability**.

### Step 3: Inspect layer-wise gradient flow

Later inspection shows that the final layer-wise gradients become almost zero.

This means the network has entered a regime where effective learning has collapsed.

### Step 4: Inspect activations

The fraction of dead ReLUs increases sharply, reaching very high levels in some layers.

This shows that the bad optimization setup is not just affecting gradients. It is also damaging the activation regime of the network.

### Step 5: Inspect parameters

Weight norms appear stable, which is useful because it prevents us from blaming the wrong mechanism.

This reinforces an important diagnostic lesson: not every signal needs to look broken. The goal is to identify the combination that best explains the failure.

---

## Root Cause Reasoning in the Example

Putting the signals together, the lesson concludes:

1. the learning rate is too high,
2. unstable early updates kill ReLU activations,
3. dead ReLUs block gradient flow,
4. gradient flow collapses,
5. training stalls without explicit numerical explosion.

This is a strong example of why loss alone is not enough. The real failure becomes clear only when multiple internal diagnostics are combined.

---

## Fixing the Model

The primary fix in the transcript is to reduce the learning rate dramatically, from `10` to `0.01`.

This works because smaller update steps:

- prevent activation collapse,
- keep gradients more stable,
- and allow ReLUs to remain active.

Secondary fixes are also mentioned, such as:

- better initialization,
- batch normalization,
- leaky ReLU,
- and gradient clipping.

But the lesson is careful to emphasize that these do not replace correcting a fundamentally wrong learning rate.

---

## Verification After the Fix

After lowering the learning rate:

- training loss decreases smoothly,
- gradient norms decay more normally,
- and the dead ReLU problem is reduced.

This final verification step is essential. Debugging is not complete when you propose a fix. It is complete when the internal signals confirm that the hypothesis was correct.

---

## Key Takeaways

- Neural network debugging should follow a structured workflow, not random experimentation.
- Gradients, activations, and parameters form the three core diagnostic layers.
- Multiple signals together give stronger evidence than any single plot alone.
- Learning rate is often the first thing to inspect because it can silently trigger a chain of failures.

**Bridge to the next topic:** the workflow so far has used custom plots and manual inspection. The next lesson shows how to monitor the same signals using **TensorBoard**.
