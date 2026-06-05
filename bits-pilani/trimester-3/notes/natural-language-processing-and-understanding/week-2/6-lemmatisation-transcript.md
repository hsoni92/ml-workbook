# Lemmatisation: Dictionary-Based Morphological Normalisation

## What Is Lemmatisation?

Lemmatisation reduces a word to its **lemma** — the canonical dictionary form — using vocabulary and morphological rules. Unlike stemming, lemmatisation produces **valid words** and can respect grammatical role.

Examples:
- *running* (verb) → **run**
- *better* → **good**
- *studies* → **study**

Lemmatisation prioritises **semantic correctness** over surface-pattern matching.

---

## Why Lemmatisation Is More Accurate Than Stemming

Stemming blindly strips suffixes. Lemmatisation asks: *What part of speech is this word, and what is its base form?*

| Word | Context | Lemma |
|------|---------|-------|
| *playing* | verb ("They are playing") | run → **play** |
| *playing* | noun ("The playing was excellent") | unchanged → **playing** |

This POS sensitivity makes lemmatisation valuable for text classification, information extraction, question answering, and semantic analysis.

---

## NLTK: WordNet Lemmatizer

```python
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize('running')   # 'running' (default POS = noun)
lemmatizer.lemmatize('running', pos='v')  # 'run'
lemmatizer.lemmatize('studies')   # 'study'
lemmatizer.lemmatize('better', pos='a')   # 'good'
```

### POS Tags for WordNet

| Code | Part of Speech |
|------|----------------|
| `n` | Noun (default) |
| `v` | Verb |
| `a` | Adjective |
| `r` | Adverb |

**POS-aware lemmatisation** dramatically improves results — always specify POS when available.

---

## spaCy Lemmatisation

spaCy performs tokenisation, POS tagging, and lemmatisation in one pipeline:

```python
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("The children were playing happily.")
for token in doc:
    print(token.text, token.lemma_)
# The the | children child | were be | playing play | happily happily
```

spaCy does **not offer stemming** — it treats lemmatisation as the production-grade approach.

---

## When to Use Stemming vs Lemmatisation

| Choose Stemming | Choose Lemmatisation |
|-----------------|---------------------|
| Speed is critical | Word meaning matters |
| Exploratory analysis | Clean, interpretable tokens needed |
| Slight errors acceptable | Production-grade NLP systems |
| Search/indexing at scale | Classification, NER, QA |

There is no universal best choice — match the method to task constraints.

---

## Common Pitfalls / Exam Traps

- Calling `lemmatize('running')` without POS — defaults to noun, returns *running* not *run*
- Expecting lemmatisation to be **as fast as stemming** — dictionary lookup is slower
- Using stemming in **production NER pipelines** where valid tokens matter
- Forgetting to download **wordnet** and **omw-1.4** for NLTK lemmatizer

---

## Quick Revision Summary

- Lemmatisation → valid dictionary lemma using vocabulary + POS
- More accurate than stemming; handles *better* → *good*, verb *playing* → *play*
- NLTK: `WordNetLemmatizer` with POS codes n/v/a/r
- spaCy: integrated pipeline; no separate stemming option
- Use lemmatisation for production and semantic tasks; stemming for speed-critical IR
