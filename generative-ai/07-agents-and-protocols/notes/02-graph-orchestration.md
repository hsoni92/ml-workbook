# Graph orchestration

Complex workflows map cleanly to **graphs**: nodes are functions; edges are control flow conditioned on state.

## Why graphs over one big prompt

- **Branching** — different paths for research vs booking vs chit-chat.
- **Checkpointing** — resume long runs; human-in-the-loop interrupts.
- **Testing** — unit-test nodes with fixed state fixtures.

LangGraph (used in this repo's agent lab) models state as a typed object mutated by node functions.

## Patterns

| Pattern | Use |
| :--- | :--- |
| ReAct | Alternate reasoning and tool calls |
| Planner / executor | Plan once, worker tools carry out |
| Critic | Second pass reviews draft output |

Keep shared state small and serializable; log transitions for debugging.
