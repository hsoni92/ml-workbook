# POS Tagging with NLTK

## NLTK's Modular Approach

NLTK implements POS tagging as an explicit multi-step pipeline: tokenise first, then tag. This transparency helps learners understand each stage — unlike spaCy's single-call abstraction.

---

## Setup and Resources

Required NLTK downloads:

```python
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets_json')
```

The **averaged perceptron tagger** is a classical ML tagger — a lightweight neural precursor useful for understanding non-transformer tagging.

---

## Implementation

```python
text = "NLTK is a powerful library for natural language processing."
tokens = word_tokenize(text)
tagged = nltk.pos_tag(tokens)
# [('NLTK', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('powerful', 'JJ'), ...]
```

`nltk.pos_tag()` returns a list of `(token, tag)` tuples using the **Penn Treebank tag set**.

---

## Understanding Penn Treebank Tags

Look up any tag programmatically:

```python
nltk.help.upenn_tagset('VBZ')
# verb, present tense, 3rd person singular
```

### Common Penn Tags

| Tag | Meaning | Example |
|-----|---------|---------|
| NN | Noun, singular | language |
| NNP | Proper noun, singular | NLTK |
| VBZ | Verb, present 3sg | is |
| DT | Determiner | a |
| JJ | Adjective | powerful |
| IN | Preposition | for |

Full reference: `nltk.help.upenn_tagset()` without arguments lists all tags.

---

## NLTK vs spaCy for POS

| Aspect | NLTK | spaCy |
|--------|------|-------|
| Pipeline | Manual: tokenise → tag | Automatic in `nlp()` |
| Tagger | Averaged perceptron | Transition-based NN |
| Speed | Slower | Faster |
| Best for | Learning fundamentals | Production |

---

## Common Pitfalls / Exam Traps

- Forgetting **`averaged_perceptron_tagger`** download — tagging fails silently or errors
- Confusing **NN** (common noun) with **NNP** (proper noun)
- Not knowing how to look up tags — `nltk.help.upenn_tagset('TAG')`
- Expecting NLTK output to include **dependency relations** — POS only unless using additional parsers

---

## Quick Revision Summary

- NLTK POS: `word_tokenize()` → `nltk.pos_tag()` → Penn Treebank tags
- Download punkt + averaged_perceptron_tagger + tagsets_json
- Common tags: NN, NNP, VBZ, DT, JJ, IN
- Lookup: `nltk.help.upenn_tagset('VBZ')`
- Modular pipeline ideal for learning; spaCy preferred for production speed
