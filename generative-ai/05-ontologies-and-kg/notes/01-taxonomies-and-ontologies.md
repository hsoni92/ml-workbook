# Taxonomies and ontologies

A **taxonomy** is a hierarchy of terms (broader/narrower). An **ontology** adds typed relations, domains, and constraints — machines can reason over it, not only humans browse it.

## Representations

| Style | Example | Good for |
| :--- | :--- | :--- |
| RDF triples | `(subject, predicate, object)` | Interop, reasoning, SPARQL |
| OWL | Classes, restrictions | Formal semantics |
| Property graph | Nodes + labeled edges | Analytics, Cypher/Gremlin |

Vectors capture similarity; graphs capture **asserted facts** and **typed structure**.

## When structure wins

- Compliance rules ("only `Instructor` can approve `Syllabus`").
- Multi-hop questions ("Which courses share a prerequisite chain?").
- Entity-centric analytics (degree, centrality, community).

## When vectors win

- Paraphrase and fuzzy match over unstructured prose.
- Cold start with no schema yet.

Hybrid systems are common: graph for canonical entities, vectors for document text.
