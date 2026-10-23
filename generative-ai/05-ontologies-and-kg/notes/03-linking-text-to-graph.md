# Linking text to graph

Unstructured text becomes useful with the graph when mentions map to **canonical entities**.

## Pipeline

1. **Mention detection** — spans in text that might be entities.
2. **Entity linking** — resolve each mention to a node ID (disambiguation: "Apple" company vs fruit).
3. **Relation extraction** — optional; predict edges with schema constraints.

## LLM-assisted extraction

Models can propose triples from passages. Always:

- Constrain to your schema (closed predicate set).
- Run consistency checks (types, cardinality).
- Sample human audit on new relation types.

## Storage pattern

Keep raw chunks in a vector index **and** attach `entity_ids[]` metadata for filtered retrieval — a bridge to GraphRAG in the next module.
