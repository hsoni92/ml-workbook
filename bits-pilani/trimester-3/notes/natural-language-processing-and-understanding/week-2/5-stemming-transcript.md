# Stemming: Rule-Based Morphological Reduction

## What Is Stemming?

Stemming reduces inflected or derived word forms to a common **stem** — a crude base form obtained by stripping suffixes. The goal is vocabulary normalisation: treat related surface forms as one token.

Examples:
- connect, connected, connecting, connection → **connect**
- play, playing, played → **play**

Stemming is **rule-based** — it does not consider word meaning or grammatical context.

---

## Why Stemming Matters

When exact word form is unimportant, stemming:

- Groups morphological variants together
- Reduces vocabulary size
- Speeds preprocessing and retrieval

| Use Case | Why stemming helps |
|----------|-------------------|
| Search engines | Query "running" matches documents with "run", "runs" |
| Information retrieval | Higher recall across word variants |
| Topic modelling | Fewer sparse dimensions from inflectional forms |
| Early NLP pipelines | Fast, lightweight normalisation |

---

## NLTK Stemmers

NLTK provides two main algorithms:

| Stemmer | Basis | Notes |
|---------|-------|-------|
| **Porter Stemmer** | Original Porter rules (1980) | Most widely used; English-focused |
| **Snowball Stemmer** | Porter2 / improved rules | Supports multiple languages |

```python
from nltk.stem import PorterStemmer

ps = PorterStemmer()
ps.stem('running')      # 'run'
ps.stem('studies')      # 'studi'  (over-stemming)
ps.stem('better')       # 'better' (under-stemming)
```

---

## Limitations

| Problem | Example |
|---------|---------|
| **Non-words produced** | *studies* → *studi* (not a valid English word) |
| **Over-stemming** | *organisation* and *organ* merged despite different meanings |
| **Under-stemming** | *better* not reduced to *good* |
| **No context awareness** | Same suffix stripped regardless of POS |

Because of these trade-offs, stemming sacrifices accuracy for speed.

---

## Stemming vs Lemmatisation (Preview)

| Aspect | Stemming | Lemmatisation |
|--------|----------|---------------|
| Output | May be non-word | Valid dictionary form |
| Method | Rule-based suffix stripping | Dictionary + POS lookup |
| Speed | Faster | Slower |
| Context | Ignored | POS-aware variants exist |

---

## Common Pitfalls / Exam Traps

- Expecting stems to be **valid English words** — Porter often produces fragments like *studi*
- Using stemming when **word meaning matters** (e.g., *organ* vs *organisation*)
- Confusing **stem** with **lemma** — stem is heuristic; lemma is dictionary-correct
- Assuming one stemmer works for **all languages** — Porter is English-centric; use Snowball for others

---

## Quick Revision Summary

- Stemming = rule-based reduction to a common stem, ignoring context
- Reduces vocabulary, groups inflections, speeds IR and topic modelling
- NLTK: `PorterStemmer()` and `SnowballStemmer()`
- Produces non-words; over/under-stemming are known failure modes
- Prefer stemming when speed matters and slight inaccuracies are acceptable
