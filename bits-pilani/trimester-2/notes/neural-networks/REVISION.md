# Neural Networks — Detailed Revision for Recollection

## How to use this sheet

- Revise one section at a time in this order: **what it is -> why it matters -> when to use -> common confusion**.
- Use formulas only as memory anchors; focus on interpretation, not derivation.
- After each section, answer the self-check questions without looking.
- If you get stuck, revisit the relevant week notes and rewrite the answer in your own words.

---

## Foundations and workflow (Weeks 1-6)

### What it is

This part covers how neural networks are built and trained:

- Core building blocks: neuron, weights, bias, layers, feed-forward flow.
- Math toolkit: vectors, matrices, derivatives, gradients, chain rule.
- First models: perceptron and logistic neuron; linear separability and XOR limitation.
- MLPs and activation functions: ReLU family, sigmoid, tanh, softmax.
- Learning mechanism: forward pass, loss, backpropagation, gradient-based updates.
- Optimization stack: mini-batch gradient descent, Adam/RMSProp, learning-rate schedules, clipping.

Key anchors:

- Layer pre-activation: $z = Wx + b$
- Binary logistic output: $\hat{y} = \sigma(z)$
- Gradient descent update: $\theta \leftarrow \theta - \eta \nabla_\theta L$

### Why it matters

- Without this foundation, deeper topics (CNNs, RNNs, transformers) become memorized terms instead of connected ideas.
- Most training failures are still explained by these basics: bad gradients, poor initialization, wrong loss, unstable step sizes.

### When to use

- Use perceptron-style thinking when checking linear separability.
- Use logistic/sigmoid output for binary classification probabilities.
- Use softmax output for multi-class classification.
- Use ReLU family in hidden layers when you need stable deep training.
- Use Adam for fast early progress; consider SGD with momentum for late fine-tuning.

### Common confusion and correction

- Confusion: "Backpropagation and optimization are the same."
  Correction: backprop computes gradients; optimizer uses them to update parameters.
- Confusion: "Stacking linear layers automatically makes model powerful."
  Correction: without non-linear activations, stacked linear maps collapse into one linear map.
- Confusion: "Zero initialization is safe everywhere."
  Correction: zero weights break symmetry; use Xavier/He initialization.

### Self-check

- Why can a single perceptron not solve XOR, and how do hidden layers fix it?
- What practical issue appears with sigmoid/tanh in deep nets, and why does ReLU help?
- In one sentence: difference between backpropagation and gradient descent?

---

## Data preprocessing and quality (Weeks 2, 7, 12)

### What it is

This part is about making data and training setup reliable before large model changes:

- Shape discipline for vectors/matrices/tensors in forward and backward passes.
- Input scaling/normalization and numerically stable computation.
- Data quality checks: label quality, leakage, class imbalance, split integrity.
- Regularization-oriented setup: augmentation, dropout, weight decay, early stopping.
- Reproducibility controls: fixed seeds, fixed splits, logged experiments, checkpointing.

### Why it matters

- Neural networks are sensitive to data scale, noise, and split mistakes.
- Many "model problems" are actually data or workflow problems.
- Reproducibility is required to trust improvements.

### When to use

- Use normalization when feature scales differ strongly.
- Use data augmentation when overfitting appears on image/audio/text-like transformations.
- Use early stopping when validation loss worsens despite training loss improving.
- Use strong experiment tracking whenever hyperparameter tuning starts.

### Common confusion and correction

- Confusion: "One lucky run proves the model is better."
  Correction: compare across controlled runs and fixed validation protocol.
- Confusion: "Batch size only changes runtime."
  Correction: it also changes gradient noise and optimization behavior.
- Confusion: "Regularization is only dropout."
  Correction: regularization is a toolbox (weight decay, dropout, augmentation, early stopping, normalization, architecture choice).

### Self-check

- Why does changing batch size affect optimization trajectory?
- When does validation loss indicate overfitting even if training accuracy rises?
- Which minimum controls make an experiment reproducible?

---

## Evaluation and generalization (Weeks 7, 10, 11)

### What it is

Evaluation in neural networks is multi-dimensional:

- Predictive quality: confusion matrix, precision, recall, F1, task metrics.
- Generalization behavior: train vs validation curves, overfitting signs.
- Confidence quality: calibration and reliability of predicted probabilities.
- Stability: robustness under perturbation/noise.
- Internal diagnosis: gradients, activations, weight statistics.

Calibration and uncertainty anchors:

- Entropy of class probabilities: $H(p) = -\sum_i p_i \log p_i$
- Calibration error compares predicted confidence against observed correctness frequency.

### Why it matters

- High accuracy can hide overconfidence, poor minority-class behavior, or fragile predictions.
- Reliable deployment needs correctness + confidence quality + robustness.

### When to use

- Use precision/recall-focused analysis for imbalanced or high-cost error settings.
- Use calibration checks for decision systems that rely on probability thresholds.
- Use perturbation testing before deployment in noisy real-world environments.
- Use internal diagnostics when training is unstable or unexpectedly flat.

### Common confusion and correction

- Confusion: "Confidence equals correctness."
  Correction: models can be confidently wrong; calibration must be measured.
- Confusion: "Good test score means robust model."
  Correction: clean-data performance and perturbation stability are different properties.
- Confusion: "If loss goes down, nothing is wrong internally."
  Correction: gradients/activations can still reveal hidden failure modes.

### Self-check

- Why is "accuracy alone" an incomplete statement for neural-network evaluation?
- What does a reliability diagram tell you that accuracy does not?
- Name one signal each from gradients, activations, and parameters used in debugging.

---

## Core model families (Weeks 1-13)

### 1) Feed-forward and MLP family (Weeks 1-6)

**What it is:** layered feed-forward computation with learned nonlinear transformations.
**Why it matters:** baseline architecture for tabular and many structured tasks; foundation for deeper families.
**When to use:** fixed-size input problems without strong spatial/temporal structure.
**Common confusion:** deeper is always better; correction: depth helps only with proper optimization and regularization.

Self-check:

- Why do hidden layers improve representational power beyond linear models?

### 2) Convolutional family (CNNs) (Week 8)

**What it is:** convolution + feature maps + pooling to exploit spatial locality and weight sharing.
**Why it matters:** strong inductive bias for images and grid-like signals.
**When to use:** vision and spatial pattern tasks where local structure repeats.
**Common confusion:** pooling is mandatory everywhere; correction: architecture choice depends on task and modern alternatives.

Self-check:

- Why does weight sharing reduce parameter count and improve pattern reuse?
- What changes when stride/padding is modified?

### 3) Recurrent and gated sequence family (RNN/LSTM/GRU) (Week 9)

**What it is:** sequence models that carry state over time; LSTM/GRU use gates for improved memory control.
**Why it matters:** captures order and temporal dependencies where feed-forward models fail.
**When to use:** sequence tasks with moderate context and sequential constraints.
**Common confusion:** LSTM/GRU fully solve long-range dependency and scaling limits; correction: they improve memory but still face sequential bottlenecks.

Self-check:

- Why do plain RNNs struggle with long-term dependencies?
- In practice, when might you choose GRU over LSTM?

### 4) Attention and transformer view (Weeks 9, 13)

**What it is:** sequence modeling centered on attention-based interaction instead of recurrence.
**Why it matters:** better parallelism and stronger long-range interaction at scale.
**When to use:** large-scale sequence/multimodal settings where context range and hardware throughput matter.
**Common confusion:** transformers have no notion of order; correction: positional information explicitly provides order.

Self-check:

- What is the key architectural shift from RNNs to transformers?

### 5) Explainability, fairness, and responsible AI layer (Week 13)

**What it is:** methods and metrics to understand model behavior, detect group-level harm, and mitigate risk.
**Why it matters:** high accuracy alone is insufficient in high-stakes deployment.
**When to use:** any system affecting real users, especially in sensitive decisions.
**Common confusion:** explainability automatically guarantees fairness; correction: fairness needs explicit metrics and interventions.

Self-check:

- Why is interpretability/explainability different from fairness?

---

## High-yield comparisons

### Perceptron vs Logistic neuron

- Perceptron: hard threshold output; Logistic neuron: smooth probability output.
- Perceptron updates are rule-style; logistic supports stable gradient-based learning.
- Both are linear at boundary level; difference is output behavior and optimization friendliness.

### Sigmoid/tanh vs ReLU family

- Sigmoid/tanh can saturate, causing weak gradients in deep networks.
- ReLU reduces saturation on positive side and usually trains faster.
- ReLU can die for persistently negative inputs; Leaky/PReLU mitigate this.

### MSE vs Cross-entropy (classification context)

- MSE is natural for regression.
- Cross-entropy with softmax/sigmoid usually gives stronger classification gradients.
- Wrong loss choice can slow convergence and hurt class separation.

### Adam vs SGD with momentum

- Adam: fast early convergence, robust default on noisy problems.
- SGD + momentum: often stronger final generalization after tuning.
- Common workflow: start with Adam, fine-tune with SGD.

### LSTM vs GRU

- LSTM has more gating structure and often higher capacity.
- GRU is simpler and lighter; often similar performance in many tasks.
- Choice is empirical: dataset size, latency, and parameter budget decide.

### RNN family vs Transformer family

- RNN/LSTM/GRU: sequential state propagation, harder parallelization.
- Transformer: attention-based global interaction, better scaling.
- Transformer usually wins at scale; recurrent models can still fit low-resource/low-latency cases.

---

## Exam traps (with one-line correction)

- Trap: "Backpropagation updates weights."
  Fix: optimizer updates weights; backprop only computes gradients.
- Trap: "If train accuracy is high, model is good."
  Fix: always check validation/test behavior and calibration.
- Trap: "Regularization means only dropout."
  Fix: combine weight decay, dropout, augmentation, early stopping, and proper setup.
- Trap: "Attention replaced all sequence models in every setting."
  Fix: architecture choice depends on data size, compute, latency, and context needs.
- Trap: "Explainability output is ground truth causality."
  Fix: explanation methods are diagnostic approximations, not perfect causal proof.
- Trap: "Single best run is enough evidence."
  Fix: use controlled, reproducible multi-run comparison.

---

## Final quick recap

- Neural-network learning is a chain: representation -> loss -> gradient flow -> optimization -> generalization.
- Most failures map to a small set of causes: data quality, poor setup, unstable gradients, weak regularization, or poor evaluation protocol.
- Architecture evolution follows limitation-driven design:
  - linear models -> MLP nonlinearity
  - MLP limits on images -> CNNs
  - feed-forward limits on sequences -> RNN/LSTM/GRU
  - recurrent bottlenecks -> attention/transformers
- Modern practice extends beyond accuracy to calibration, robustness, interpretability, and fairness.

---

## Last-day checklist

- [ ] I can explain neuron, layer, forward pass, backpropagation, and optimizer roles clearly.
- [ ] I can contrast perceptron, logistic neuron, MLP, CNN, RNN/LSTM/GRU, and transformer in one table from memory.
- [ ] I remember key anchors: $z = Wx + b$, $\hat{y} = \sigma(z)$, $\theta \leftarrow \theta - \eta \nabla_\theta L$.
- [ ] I can identify overfitting signs and list at least four regularization tools.
- [ ] I can explain why calibration and robustness are different from raw accuracy.
- [ ] I can describe a structured debugging workflow using gradients, activations, and parameter statistics.
- [ ] I can state reproducibility essentials: fixed seeds, fixed splits, tracked experiments, checkpointed runs.
- [ ] I can answer one responsible-AI question on explainability limits, fairness metrics, and mitigation strategy.
