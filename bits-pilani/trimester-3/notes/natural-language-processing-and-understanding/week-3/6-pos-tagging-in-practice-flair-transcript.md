# POS Tagging with Flair

## What Is Flair?

Flair is a PyTorch-based NLP framework offering **pre-trained neural sequence taggers** for POS tagging, NER, sentiment analysis, and more. Models use contextual embeddings (biLSTM-CRF architectures) to achieve high accuracy at the cost of slower inference compared to spaCy.

---

## Installation and Usage

```python
from flair.data import Sentence
from flair.models import SequenceTagger

tagger = SequenceTagger.load('pos')
sentence = Sentence("Flair is a great library for natural language processing.")
tagger.predict(sentence)
print(sentence.to_tagged_string())
```

Output assigns Penn-style tags: *Flair/NNP*, *is/VBZ*, *a/DT*, etc.

---

## How Flair Differs

| Aspect | Flair | NLTK | spaCy |
|--------|-------|------|-------|
| Architecture | BiLSTM-CRF + contextual embeddings | Averaged perceptron | Transition-based NN |
| API | Load model → predict | Tokenise → tag | `nlp(text)` |
| Preprocessing | Built into `Sentence` | Manual | Built into pipeline |
| Speed | Moderate | Slowest | Fastest |
| Accuracy | High on benchmarks | Lower | High; slight trade-off for speed |

Flair tag definitions are documented on Hugging Face (Flair POS tag set reference).

---

## Multilingual Support

Flair provides language-specific POS models (e.g., `pos-fast`, German POS taggers). Tag sets may align with Universal Dependencies or language-specific conventions.

---

## When to Prefer Flair for POS

- **Maximum accuracy** on specialised or ambiguous text
- **Research benchmarks** where F1 score matters more than latency
- **Domain text** (legal, medical) where contextual embeddings help disambiguation

For most production POS needs at scale, spaCy remains the default choice.

---

## Common Pitfalls / Exam Traps

- Forgetting **`tagger.predict(sentence)`** — model load alone does not tag
- Passing a **string instead of `Sentence` object** — wrap text in `Sentence(text)`
- Expecting **spaCy-level speed** on millions of documents
- Confusing Flair **POS models** with **NER models** — different `SequenceTagger.load()` checkpoints

---

## Quick Revision Summary

- Flair: PyTorch sequence taggers with contextual embeddings
- `SequenceTagger.load('pos')` → `tagger.predict(sentence)` → `to_tagged_string()`
- Higher accuracy, moderate speed; multilingual models available
- Simple API: create Sentence, load model, predict
- Compare same text across NLTK, spaCy, and Flair to observe tag differences
