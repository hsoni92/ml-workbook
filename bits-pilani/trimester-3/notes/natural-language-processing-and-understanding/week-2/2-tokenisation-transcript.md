# Tokenisation: Splitting Text into Processable Units

## The Core Idea

Tokenisation is the process of breaking raw text into smaller units called **tokens**. Tokens can represent words, sentences, subwords, or individual characters. Every NLP pipeline — from simple word counting to transformer models — begins here.

If tokenisation is wrong, every downstream step inherits the error: wrong POS tags, missed entities, skewed TF-IDF weights.

---

## Granularity Levels

| Level | Unit | Typical Use |
|-------|------|-------------|
| Word | Space/punctuation-delimited tokens | Bag-of-words, classical NLP |
| Sentence | Clause/period boundaries | Summarisation, document segmentation |
| Subword | BPE/WordPiece fragments | BERT, GPT tokenizers |
| Character | Individual letters | Spell-checking, very low-resource languages |

```mermaid
flowchart TB
    P["Paragraph: NLP is fascinating. Deep learning changed AI."]
    P --> W[Word tokens: NLP | is | fascinating | . | Deep | learning | ...]
    P --> S[Sentence tokens: NLP is fascinating. | Deep learning changed AI.]
    P --> C[Character tokens: N | L | P | ...]
```

---

## Why Tokenisation Is Non-Trivial

Natural language resists naive splitting:

- **Punctuation ambiguity** — "U.S.A." vs "USA"; decimals vs sentence endings
- **Hyphenation** — "state-of-the-art" as one token or four
- **Numbers and symbols** — "$1.2B", version strings, URLs
- **Emojis and Unicode** — multi-codepoint sequences
- **Language and domain** — Chinese has no spaces; biomedical text has chemical formulae

There is **no single correct tokenisation** for all applications. The choice depends on language, domain, and downstream task.

---

## Implementation with NLTK

NLTK provides two primary functions after downloading the `punkt` resource:

**Word tokenisation** — `word_tokenize(text)` splits on word boundaries while preserving punctuation as separate tokens.

**Sentence tokenisation** — `sent_tokenize(text)` splits on sentence boundaries using a pre-trained Punkt model.

Example flow:

```python
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Natural language processing is fascinating."
word_tokenize(text)
# ['Natural', 'language', 'processing', 'is', 'fascinating', '.']

sent_tokenize("First sentence. Second sentence.")
# ['First sentence.', 'Second sentence.']
```

---

## Real-World Considerations

- **Production search** — query tokenisation must match index tokenisation exactly
- **Multilingual SaaS** — different Punkt models or spaCy pipelines per language
- **Transformer APIs** — subword tokenisation (BPE) differs from NLTK word splits; comparing counts across tokenisers is invalid

---

## Common Pitfalls / Exam Traps

- Assuming **split on whitespace** is sufficient — fails on "don't", "U.K.", URLs
- Using **word tokenisation for BERT** — transformer models require their own subword tokenisers
- Forgetting to **download punkt** before calling NLTK tokenisers
- Ignoring that **punctuation as separate tokens** affects vocabulary size and stopword lists

---

## Quick Revision Summary

- Tokenisation = breaking text into tokens (words, sentences, subwords, or characters)
- First step in virtually every NLP pipeline; errors propagate downstream
- Complexity arises from punctuation, hyphens, numbers, emojis, and language-specific rules
- NLTK: `word_tokenize()` and `sent_tokenize()` after downloading `punkt`
- No universal tokenisation strategy — match granularity to task and model
