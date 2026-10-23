# Chain-of-thought and search

**Chain-of-thought (CoT)** prompts or trains the model to emit intermediate steps before the final answer. It increases tokens but can unlock multi-step reasoning.

## Self-consistency

Sample multiple reasoning paths; aggregate answers (majority vote). Simple System 2 baseline without explicit search trees.

## Search over thoughts

- **Beam search**: keep top partial hypotheses — classic in seq2seq, less common in chat LMs but conceptually similar.
- **Tree search (MCTS-style)**: expand promising partial solutions, prune weak branches — used in research systems with verifiers.

Cost grows with branching factor and depth; cap budgets in production.

## When CoT hurts

Verbose reasoning on easy tasks wastes latency and can introduce hallucinated steps. Use routing or classifiers to decide when to "think longer."
