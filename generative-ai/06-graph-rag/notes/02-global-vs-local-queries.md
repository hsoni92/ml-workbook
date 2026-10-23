# Global vs local queries

**Local**: "What did module 3 say about KV cache?" — vector search over chunks is often enough.

**Global**: "What are the main themes across the entire curriculum?" — naive top-$k$ chunks miss the big picture; **community summaries** act as a map.

## Query routing

Classify or heuristically route:

- Local → chunk vector index (+ optional entity filter).
- Global → select relevant community summaries, maybe expand to member entities.
- Mixed → retrieve summaries **and** supporting chunks; synthesize with citations.

## Answer synthesis

Prompt the LLM with:

1. Selected community summaries (broad context).
2. Fine-grained chunks (evidence).
3. Instruction to cite summary IDs and chunk IDs.
