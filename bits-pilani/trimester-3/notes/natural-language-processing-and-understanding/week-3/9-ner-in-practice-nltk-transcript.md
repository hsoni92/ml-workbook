# Named Entity Recognition with NLTK

## NLTK's Chunk-Based NER Pipeline

NLTK implements NER through a **multi-step classical pipeline** — fundamentally different from spaCy's integrated neural approach:

1. Tokenise text
2. Apply POS tagging
3. Chunk named entities with `ne_chunk()`

This modular design exposes each stage for learning, but produces lower accuracy than modern neural taggers.

---

## Setup

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
```

---

## Implementation

```python
text = "Apple is looking at buying a UK startup for $1 billion. Elon Musk said in December 2026."
tokens = word_tokenize(text)
tagged = pos_tag(tokens)
ne_tree = ne_chunk(tagged)
```

`ne_chunk()` returns a nested **Tree** structure where entity subtrees are labelled (e.g., `GPE`, `PERSON`, `ORG`).

Extract named entities programmatically:

```python
for chunk in ne_tree:
    if hasattr(chunk, 'label'):
        print(chunk.label(), chunk.leaves())
```

---

## NLTK Entity Types

NLTK's `maxent_ne_chunker` supports a **limited set** of entity types:

| Tag | Meaning |
|-----|---------|
| PERSON | People |
| ORG | Organisations |
| GPE | Geopolitical entities |
| LOCATION | Non-GPE locations |
| FACILITY | Buildings, airports, highways |

---

## Accuracy Limitations

On the same benchmark text, NLTK typically detects **fewer entities** than spaCy:

| Span | spaCy | NLTK (typical) |
|------|-------|----------------|
| Apple | ORG | GPE (misclassified) |
| UK | GPE | Often missed |
| $1 billion | MONEY | Missed |
| Elon Musk | PERSON | Partial (*Musk* only) |
| December 2026 | DATE | Missed |

NLTK merges or misses multi-token entities and lacks MONEY/DATE categories in the default chunker.

---

## When NLTK NER Still Matters

- **Educational contexts** — understanding chunking and POS-dependent NER
- **Legacy systems** — maintaining older rule-based pipelines
- **Fallback** — when neural models unavailable (resource-constrained environments)

For production NER, spaCy or Flair is strongly preferred.

---

## Common Pitfalls / Exam Traps

- Forgetting **`maxent_ne_chunker`** and **`words`** downloads
- Expecting **MONEY and DATE** entities — NLTK default chunker lacks these
- Not checking `hasattr(chunk, 'label')` when iterating — non-entity chunks are plain tuples
- Assuming NLTK NER **matches spaCy output** — significant accuracy gap

---

## Quick Revision Summary

- NLTK NER: tokenise → `pos_tag()` → `ne_chunk()`
- Download maxent_ne_chunker + words + tagger resources
- Limited entity types: PERSON, ORG, GPE, LOCATION, FACILITY
- Lower accuracy than spaCy — misses dates, money, multi-token spans
- Useful for learning pipeline mechanics; not recommended for production
