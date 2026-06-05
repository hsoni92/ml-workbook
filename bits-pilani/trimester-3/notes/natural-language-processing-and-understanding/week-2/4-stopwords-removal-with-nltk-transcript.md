# Stopword Removal: Filtering Function Words

## What Are Stopwords?

Stopwords are high-frequency words that carry little standalone semantic meaning — articles, prepositions, conjunctions, and common auxiliaries. Examples: *the*, *is*, *of*, *and*, *a*.

They dominate word frequency distributions, making models overweight function words relative to content-bearing terms like *policy*, *economy*, or *diagnosis*.

---

## Why Remove Stopwords?

| Benefit | Explanation |
|---------|-------------|
| Reduced vocabulary size | Fewer dimensions in bag-of-words / TF-IDF |
| Improved efficiency | Faster training and smaller feature matrices |
| Better signal | Models focus on content words that distinguish documents |

**Example:** In topic modelling, *the* and *is* do not reveal themes; *health*, *budget*, and *regulation* do.

Stopword removal is applied **after tokenisation**: tokenise first, then filter tokens against a stopword list.

---

## NLTK Implementation

```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
tokens = word_tokenize("Natural language processing is a fascinating area of computer science.")
filtered = [w for w in tokens if w.lower() not in stop_words]
# ['Natural', 'language', 'processing', 'fascinating', 'area', 'computer', 'science']
```

NLTK ships stopword lists for multiple languages. The English list is generic — customise for domain-specific needs.

---

## When NOT to Remove Stopwords

Stopwords carry grammatical and semantic weight in several tasks:

| Task | Why stopwords matter |
|------|---------------------|
| Sentiment analysis | *not*, *no*, *never* flip polarity — "not good" ≠ "good" |
| Question answering | Function words define query structure |
| Language modelling | Next-word prediction needs full grammar |
| Dependency parsing | Syntactic structure depends on determiners and auxiliaries |

**Example:** "This movie is **not** good" — removing *not* inverts meaning entirely.

---

## Custom Stopword Lists

Domain-specific high-frequency words may add no value:

- **Product reviews** — *product*, *item* appear too often
- **News corpora** — *said*, *reported* are uninformative

Practise: add domain terms to the stopword set, or remove words like *not* from the default list for sentiment tasks.

```python
stop_words.add('said')       # news domain
stop_words.discard('not')   # sentiment task
```

---

## Common Pitfalls / Exam Traps

- Treating stopword removal as a **mandatory rule** — it is a design decision
- Removing **negation words** in sentiment pipelines
- Applying stopwords **before tokenisation** — must tokenise first
- Using the default English list for **all domains** without customisation
- Forgetting **case sensitivity** — compare with `.lower()` consistently

---

## Quick Revision Summary

- Stopwords = frequent function words with low discriminative power
- Removal reduces vocabulary, improves efficiency, highlights content words
- Apply after tokenisation using NLTK's `stopwords.words('english')`
- Keep stopwords for sentiment, QA, language modelling, and grammar-aware tasks
- Customise lists per domain — add domain noise, preserve negations
