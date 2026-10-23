# Hybrid retrieval

GraphRAG at serving time is usually **hybrid**:

| Signal | Retrieves |
| :--- | :--- |
| Vector on chunks | Evidence passages |
| Vector on summaries | Thematic context |
| Graph traversal | Neighbors of seed entities |
| Metadata | Course, week, ACL |

## Example pattern

1. Embed user query.
2. Top communities by summary similarity.
3. Expand 1–2 hops on entities mentioned in those communities.
4. Pull chunks linked to those entities.
5. Rerank merged candidates; pass to LLM.

Tune hop depth and community count — each adds tokens and latency.

## Relation to module 04

Standard RAG optimizes passage retrieval. GraphRAG adds **structure** for questions that need aggregation or multi-document themes. Many products implement a subset (entity tags + hybrid search) before full community summarization.
