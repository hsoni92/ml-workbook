# Neural Networks: Connect the Dots (Weeks 1-13)

This is the full course in one view: build a function approximator, train it with stable optimization, make it generalize, pick the right architecture for data structure, evaluate honestly, debug systematically, run reproducible experiments, and deploy responsibly.

---

## The 13-week spine (one connected story)

### Week 1 - What a neural network is
- Core: AI vs ML vs DL, neuron, weights, bias, layers, feed-forward flow.
- Why it matters: defines the model as stacked computations, not magic.
- Enables next: Week 2 gives the math language to train this object.
- Hub: [week-1/8-Module Summary - Artificial Neural Networks.md](week-1/8-Module Summary - Artificial Neural Networks.md)

### Week 2 - Math language for learning
- Core: vectors/matrices/tensors, derivatives, chain rule, numerical stability.
- Why it matters: backprop is chain rule applied over composed functions.
- Enables next: Week 3 uses this to analyze perceptron and logistic models.
- Hub: [week-2/8-Module Summary - Artificial Neural Networks.md](week-2/8-Module Summary - Artificial Neural Networks.md)

### Week 3 - First models and first limitation
- Core: perceptron, logistic neuron, linear separability, XOR failure.
- Why it matters: one linear boundary is not enough for many tasks.
- Enables next: hidden layers and nonlinear activations become necessary (Week 4).
- Hub: [week-3/9-Module Summary - Artificial Neural Networks.md](week-3/9-Module Summary - Artificial Neural Networks.md)

### Week 4 - MLP representation power
- Core: multilayer perceptron, forward pass, hidden representation, activations (sigmoid/tanh/ReLU/softmax).
- Why it matters: nonlinear depth creates expressive feature hierarchies.
- Enables next: Week 5 shows how to assign blame to every parameter.
- Hub: [week-4/11-Module Summary - Artificial Neural Networks.md](week-4/11-Module Summary - Artificial Neural Networks.md)

### Week 5 - Backprop, loss, and gradient health
- Core: computational graph, backprop, initialization, loss choice, vanishing/exploding gradients.
- Why it matters: training quality depends on gradient signal quality.
- Enables next: Week 6 decides how updates are actually taken.
- Hub: [week-5/12-Module Summary - Artificial Neural Networks.md](week-5/12-Module Summary - Artificial Neural Networks.md)

### Week 6 - Optimization mechanics
- Core: GD/SGD/mini-batch, momentum, RMSProp, Adam, schedules, clipping.
- Why it matters: gradients give direction; optimizer controls trajectory.
- Enables next: Week 7 asks if learned behavior survives unseen data.
- Hub: [week-6/15-Module Summary - Artificial Neural Networks.md](week-6/15-Module Summary - Artificial Neural Networks.md)

### Week 7 - Generalization and regularization
- Core: underfit/overfit, bias-variance, L1/L2, dropout, batch norm, early stopping, augmentation.
- Why it matters: low training loss without generalization is failure.
- Enables next: architecture choice now matters as an inductive bias.
- Hub: [week-7/1-Regularization and Generalization.md](week-7/1-Regularization and Generalization.md)

### Week 8 - CNNs for spatial structure
- Core: convolution, local receptive fields, weight sharing, feature maps, pooling, CNN blocks.
- Why it matters: image priors should be baked into architecture.
- Enables next: Week 9 handles ordered/time-dependent data.
- Hub: [week-8/17-Module Summary - Artificial Neural Networks.md](week-8/17-Module Summary - Artificial Neural Networks.md)

### Week 9 - Sequence models and modern shift
- Core: sequence modeling, RNN state, LSTM/GRU gating, transformer-level attention view.
- Why it matters: temporal/context structure needs memory or attention.
- Enables next: Week 10 checks whether performance claims are real.
- Hub: [week-9/1-Module Introduction - Artificial Neural Networks.md](week-9/1-Module Introduction - Artificial Neural Networks.md)

### Week 10 - Evaluation beyond headline accuracy
- Core: task-appropriate metrics, threshold behavior, calibration, robustness, uncertainty.
- Why it matters: the wrong metric hides deployment risk.
- Enables next: Week 11 diagnoses internal causes when metrics degrade.
- Hub: [week-10/12-Module Summary - Artificial Neural Networks.md](week-10/12-Module Summary - Artificial Neural Networks.md)

### Week 11 - Internal diagnostics
- Core: inspect gradients, activations, parameter statistics; detect dead/saturated/frozen behavior.
- Why it matters: many failures are internal dynamics, not dataset bugs.
- Enables next: Week 12 replaces ad-hoc tuning with disciplined experimentation.
- Hub: [week-11/16-Module Summary - Artificial Neural Networks.md](week-11/16-Module Summary - Artificial Neural Networks.md)

### Week 12 - Reproducible experimentation
- Core: hyperparameters that matter, search strategy, split discipline, seeding, logging, checkpointing.
- Why it matters: comparisons are valid only if protocol is controlled.
- Enables next: Week 13 extends from performance to accountability.
- Hub: [week-12/8-Module Summary - Artificial Neural Networks.md](week-12/8-Module Summary - Artificial Neural Networks.md)

### Week 13 - Explainability, fairness, and future direction
- Core: interpretability vs explainability, saliency/perturbation/model-specific methods, fairness metrics, mitigation, efficiency/scaling/multimodality trends.
- Why it matters: reliable systems need transparency and governance, not just score gains.
- Enables next: practical, responsible model development beyond coursework.
- Hub: [week-13/14-Module Summary - Artificial Neural Networks.md](week-13/14-Module Summary - Artificial Neural Networks.md)

---

## Cross-week threads you should see instantly

- **Gradient flow thread:** Week 2 (chain rule) -> Week 5 (backprop signal) -> Week 6 (optimization control) -> Week 9 (long-range sequence difficulty) -> Week 11 (diagnostics).
- **Generalization thread:** Week 4-6 increase capacity and fitting power; Week 7 controls overfitting; Week 10 validates real behavior; Week 12 ensures claims are reproducible.
- **Architecture thread:** MLP for generic mapping (Week 4), CNN for spatial priors (Week 8), RNN/LSTM/GRU/attention for sequence context (Week 9).
- **Trust thread:** evaluate correctly (Week 10), inspect internals (Week 11), compare rigorously (Week 12), deploy responsibly (Week 13).

---

## End-to-end good-model checklist

1. **Objective alignment:** loss and output semantics match the task.
2. **Optimization stability:** gradients are healthy; learning rate and optimizer are appropriate.
3. **Generalization control:** train/validation behavior is consistent; regularization is intentional.
4. **Architecture fit:** model inductive bias matches data structure (tabular/image/sequence).
5. **Evaluation validity:** metrics, calibration, robustness, and uncertainty match deployment risk.
6. **Debuggability:** internal signals are monitored, not guessed.
7. **Experimental rigor:** one final test, reproducible runs, tracked configs.
8. **Responsible deployment:** explainability, fairness checks, and mitigation are in place.

---

## 13 one-line hinges (rapid revision)

| Week | Hinge |
|------|-------|
| 1 | A network is stacked weighted computation, not a black box. |
| 2 | Chain rule is the engine behind learning in deep models. |
| 3 | XOR shows why hidden nonlinear layers are necessary. |
| 4 | Depth plus nonlinearity gives representational power. |
| 5 | Backprop quality depends on loss, initialization, and gradient health. |
| 6 | Optimizers decide how gradients become parameter movement. |
| 7 | Generalization, not training loss, is the real objective. |
| 8 | CNNs encode spatial priors through locality and sharing. |
| 9 | Sequence tasks require memory/attention, not static mapping. |
| 10 | Metrics must reflect risk; accuracy alone is insufficient. |
| 11 | Diagnose internals before changing knobs blindly. |
| 12 | Without controlled experiments, model comparisons are unreliable. |
| 13 | High-performing AI still needs explainability and fairness discipline. |

---

Read this note as a map. Use week notes for depth; use this page for the full connection logic.
