# POS Tagging with spaCy

## Why spaCy for POS Tagging

spaCy provides an end-to-end NLP pipeline: tokenisation, POS tagging, dependency parsing, and NER in a single `nlp()` call. For production workloads, spaCy balances speed and accuracy with a streamlined API.

---

## Setup and Basic Usage

```python
import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp("I will book a ticket.")
for token in doc:
    print(f"{token.text:12} {token.pos_:5} {token.tag_}")
```

Output:

| Token | Universal POS (`pos_`) | Fine-grained (`tag_`) |
|-------|--------------------------|----------------------|
| I | PRON | PRP |
| will | AUX | MD |
| book | VERB | VB |
| a | DET | DT |
| ticket | NOUN | NN |
| . | PUNCT | . |

- `token.pos_` — Universal POS category (human-readable)
- `token.tag_` — Detailed Penn Treebank-style tag

---

## Context Disambiguation Example

```python
doc1 = nlp("I will book a ticket.")   # book → VERB
doc2 = nlp("Read this book.")        # book → NOUN
```

spaCy's transition-based parser uses word embeddings and context to resolve ambiguity automatically — no manual pipeline assembly required.

---

## Key Properties

| Property | Detail |
|----------|--------|
| Tokenisation | Automatic inside `nlp()` |
| Model | `en_core_web_sm` (small), `md`, `lg` variants |
| Speed | Optimised for production batch processing |
| Output | Token text, POS, tag, lemma, dependency in one pass |

---

## Real-World Usage

- **Document intelligence APIs** — extract noun phrases for indexing
- **Chatbot intent pipelines** — verb/noun patterns for slot filling
- **Pre-annotation** — bootstrap NER training data with POS-filtered candidates

---

## Common Pitfalls / Exam Traps

- Forgetting to **install and load** the language model (`python -m spacy download en_core_web_sm`)
- Confusing `pos_` (Universal) with `tag_` (Penn fine-grained)
- Expecting spaCy POS tags to **match NLTK Penn tags exactly** — mapping may differ slightly
- Running POS on raw text **without loading model** — `nlp` must be initialised first

---

## Quick Revision Summary

- spaCy: `nlp(text)` → tokens with `token.pos_` and `token.tag_`
- Tokenisation included; no separate step needed
- Context resolves ambiguity (*book* verb vs noun)
- Production-ready: fast, integrated pipeline
- Install `en_core_web_sm` before use; practise on varied sentences
