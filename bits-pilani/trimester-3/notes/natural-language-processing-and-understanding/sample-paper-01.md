# Sample Question Paper

## BITS Digital Comprehensive Test

| Field | Value |
|-------|-------|
| Course No. | |
| Course Title | Natural Language Processing (NLP) |
| Nature of Exam | Closed Book (No Internet) |
| Weightage | 40% |
| Duration | 2.5 Hours |
| Date of Exam | |

### Note to Students

1. Please follow all the Instructions to Candidates given on the cover page of the answer book.
2. Read each question carefully and write to-the-point answer.
3. All parts of a question should be answered consecutively. Each answer should start from a fresh page.
4. Assumptions made if any, should be stated clearly at the beginning of your answer.
5. Show all the calculations/derivations in fair and box/highlight the final answer.

---

## Q.1

### Q.1.1 — N-grams and the Bag-of-Words Limitation (6 Marks)

Explain the concept of $N$-grams (specifically unigrams and bigrams) in text vectorization. Consider the sentence: *"The food was not good."* Demonstrate how a standard unigram Bag-of-Words model fails to capture the true sentiment of this sentence, and explain how upgrading to a bigram model solves this specific issue.

#### Answer

**N-grams as a vectorization unit.** An $N$-gram is a contiguous sequence of $N$ tokens extracted from a document. **Unigrams** are single tokens (the vocabulary of a standard Bag-of-Words model), while **bigrams** are pairs of *consecutive* words, e.g. `the food`, `food was`, `was not`, `not good`. Upgrading the feature space from `ngram_range=(1,1)` to `(1,2)` adds these ordered pairs as dimensions, which recovers a small amount of local word order that plain BoW throws away.

**Why unigram BoW fails here.** BoW treats a document as a multiset of words — grammar and word order are discarded entirely. For *"The food was not good."*, the unigram vector contains the words `the`, `food`, `was`, `not`, `good`. The word *good* is present, so a sentiment classifier sees a strong positive signal, while the negation *not* floats as an independent feature with no link to *good*. The model effectively sees *"good"* without the *"not"* — the sentence could be scored as positive even though it expresses negative sentiment. This is the classic negation trap: *"not good"* and *"good"* produce almost identical unigram vectors.

**How bigrams fix it.** Adding bigrams introduces the ordered feature `not good` (and, with a slightly larger window, `was not`). Now the negation is bound to the word it modifies: the vector carries an explicit negative-evidence feature *"not_good"* alongside *"good"*. A classifier can learn that high weight on `not good` flips the sentiment, which a unigram-only model cannot represent. This is the same reason TF-IDF notes recommend `ngram_range` for negation — word order matters whenever semantics depend on it.

**Pro tip:** Negation questions are the most common BoW trap. Always phrase it as: *unigrams keep the words but lose the relationship; bigrams recover local order so the negator and the negated word become one feature.* If the sentence were *"The dog bit the man"* vs *"the man bit the dog"*, quote the identical-vector result and show bigrams distinguish them. Keep the answer to mechanism → failure → fix.

---

### Q.1.2 — When Stop-Word Removal Hurts (4 Marks)

Removing "Stop Words" (like *is, the, at, which*) is a standard preprocessing step to reduce vocabulary size. However, identify and explain one specific NLP task (e.g., sentiment analysis, machine translation, or keyword extraction) where aggressive stop-word removal could actually harm the model's performance.

#### Answer

**Task: sentiment analysis.** Stopword removal is usually safe for *content-bearing* function words (`the`, `at`, `which`) that carry little standalone meaning. It is destructive when the "stopword" list includes **negation words** such as *not*, *no*, *never*, *isn't*, or *wasn't*. These are exactly the tokens that **flip polarity**: *"This movie is not good"* becomes *"This movie good"* after removal, inverting the sentiment entirely. The classifier then sees a positive phrase because the single most informative word was stripped out.

**Why it harms performance.** The model's decision surface is built on which words are present. Removing *not* removes the primary negative signal; the remaining content words (`bad`, `boring`) may still hint at polarity, but the sentence *"not bad"* (mildly positive) is reduced to *"bad"* (negative) — the opposite meaning. The standard practice for sentiment pipelines is therefore to **discard negation words from the stopword list** (e.g. `stop_words.discard("not")`) or to keep them and rely on n-grams so negation stays attached to its target.

**One-liner to include:** Stopwords are not a mandatory removal rule — it is a *design decision*. Remove them where they add no discriminative power; preserve them where they carry grammatical or semantic weight (negation, question structure, grammar for language modelling).

**Pro tip:** Any "aggressive stopword removal hurts" question is best answered with **sentiment analysis + negation**, because it has a crisp failure mechanism: polarity flip. The marks come from (a) naming the task, (b) naming the specific word class that gets wrongly removed (negation words), and (c) showing the before/after meaning change. Mention the fix (`discard("not")`) to show you understand the remedy, not just the problem.

---

## Q.2

### Q.2.1 — TF-IDF and Document Length (5 Marks)

A search engine uses the TF-IDF (Term Frequency - Inverse Document Frequency) algorithm to rank documents for the search query "alien".

- Document A is a short 50-word summary of a sci-fi movie, containing the word "alien" 3 times.
- Document B is a massive 5,000-word Wikipedia article about extraterrestrial life, also containing the word "alien" 3 times.

Logically and mathematically explain which document will yield a higher TF-IDF score for this query, and why this algorithmic behavior is desirable for a search engine.

#### Answer

**Assumption (state it in the exam):** TF is normalised by document length so documents of very different sizes are comparable — i.e. $\text{TF}(x,d) = \text{count of } x \text{ in } d \div \text{total words in } d$. IDF is corpus-wide and identical for both documents, so it cancels out of the comparison.

**Mathematical comparison.**

$$\text{TF-IDF}(x,d) = \text{TF}(x,d) \times \log\frac{N}{\text{DF}(x)}$$

| Quantity | Document A (50 words) | Document B (5,000 words) |
|----------|----------------------|--------------------------|
| Raw count of "alien" | 3 | 3 |
| Normalised TF | $3/50 = 0.06$ | $3/5000 = 0.0006$ |
| IDF | same value $c$ | same value $c$ |
| TF-IDF | $0.06 \times c$ | $0.0006 \times c$ |

Document A's TF-IDF score is **100× higher** — the word "alien" makes up 6% of A's content but only 0.06% of B's. Even though both documents contain the word three times, A is *about* "alien" in a way B is not.

**Why this is desirable for search.** Without length normalisation, long documents would dominate ranking simply by having more chances to repeat a query term — a 5,000-word article would outrank a focused 50-word summary even when the query is the summary's entire subject. TF-IDF's length-normalised behaviour promotes **topical relevance**: documents where the term is concentrated and distinctive rank higher than documents where it is diluted. It rewards the document whose dominant theme matches the query, which is exactly what a user wants when searching for "alien".

**Pro tip:** This is the "TF is raw count, so both have 3 — how can scores differ?" trap. The escape is to *state the normalisation assumption explicitly* (the paper itself tells you to state assumptions) and then show the $3/50$ vs $3/5000$ ratio. Then connect to the search rationale: length normalisation stops long documents from winning by volume, so the ranking reflects topical density. Mention that IDF is a common factor and cancels — examiners like seeing you notice that.

---

### Q.2.2 — Out-of-Vocabulary and Sub-Word Tokenization (5 Marks)

Traditional word embeddings like Word2Vec map entire words to fixed vectors. Explain the "Out-of-Vocabulary (OOV)" problem that occurs when Word2Vec encounters a completely unseen word in production. How do modern sub-word tokenization strategies (like Byte-Pair Encoding or FastText) fundamentally solve this OOV issue?

#### Answer

**The OOV problem in Word2Vec.** Word2Vec learns one **fixed vector per whole word**, stored in a lookup table of size equal to the training vocabulary. A word absent from that vocabulary has no row in the table, so at inference time the model can only (a) crash or error, (b) fall back to a random or zero vector, or (c) silently ignore the token. Any of these corrupts the representation for that input. In production this hits constantly: new product names, typos, proper nouns, domain jargon, and morphological variants (`click` vs `clicking` vs `clicked`) that never appeared during training. The vocabulary is a **closed set**, so the model cannot generalise to anything it has not seen.

**How sub-word tokenisation solves it.** Instead of storing whole-word vectors, sub-word methods represent words **compositionally from smaller pieces**:

- **Byte-Pair Encoding (BPE)** — starts with characters and iteratively merges the most frequent adjacent pairs into new sub-word units. Any word, seen or unseen, can be decomposed into a sequence of sub-word tokens that *are* in the vocabulary (e.g. `unhappiness` → `un`, `happi`, `ness`; an unknown word is split into character-level pieces at worst). The embedding for the word is built from its sub-word tokens, so **every word gets a representation — OOV ceases to exist** in principle.
- **FastText** — goes further: a word's vector is the **sum of its character n-gram vectors**. Even a word never seen during training can be embedded purely from the character n-grams it shares with known words, which is especially strong for morphologically rich languages and rare/compound words.

The key shift: **whole-word lookup → compositional representation**. Robustness to unseen words comes from exploiting *morphology* — the word-internal structure — so new spellings, inflections, and rare forms are no longer atomic unknowns.

**Pro tip:** Structure the answer as *closed vocabulary → what breaks → the sub-word fix*. Name the decomposition explicitly (`unhappiness` → `un`+`happi`+`ness`) — a concrete example is worth more than prose. Contrast the *mechanism*: BPE merges frequent character pairs into a vocabulary of sub-word units; FastText sums character n-grams. One sentence on "BPE splits rare words into frequent morpheme-like pieces" (the morphology note phrasing) signals you connect tokenisation to morphology.

---

## Q.3

### Q.3.2 — Bidirectional LSTM for Tagging (6 Marks)

You are building a Named Entity Recognition (NER) system or a Part-of-Speech (POS) tagger. Consider the sentence: "The bear leaves the dark cave."

Explain why a Bidirectional LSTM (BiLSTM) architecture will yield significantly higher accuracy when attempting to tag the word "leaves" compared to a standard, unidirectional LSTM.

#### Answer

**The ambiguity in "leaves".** In *"The bear leaves the dark cave"*, the token *leaves* is genuinely ambiguous:

- **Left context** (`The bear __`): a determiner + noun before it suggests *leaves* is likely a **verb** ("the bear departs"), but "bear" could also be a verb ("bear leaves" as in "the tree bears leaves") — the left side alone is not conclusive.
- **Right context** (`__ the dark cave`): a full noun phrase (`the dark cave`) directly after it strongly signals **verb + object** — the bear *leaves* (departs) the cave. The noun sense (foliage) would not be followed by "the dark cave".

The correct POS tag depends primarily on information that appears **after** the target word.

**Why unidirectional LSTM struggles.** A standard LSTM reads strictly left-to-right. When it reaches *leaves*, its hidden state $H_t$ encodes only the past context — *The bear* — and cannot see *the dark cave* yet. Its decision about *leaves* is made from incomplete evidence, so it guesses between verb/noun on the left context alone, which is insufficient here.

**Why BiLSTM fixes it.** A BiLSTM runs **two parallel LSTMs**:

- a **forward** pass reading left-to-right, capturing past context (`The bear`), and
- a **backward** pass reading right-to-left, capturing future context (`the dark cave`).

The hidden states from both passes are **concatenated** at each position, so the representation of *leaves* contains information from **both sides simultaneously**. The model can now use the noun phrase that follows to resolve the ambiguity confidently.

The same reasoning applies to NER: *"book"* is a verb in *"book the flight"* but a noun in *"read the book"* — the deciding evidence sits on the right. Sequence-labelling tasks (POS, NER, chunking) have **symmetric dependencies**: tags often depend on words that come after, so a bidirectional model is the standard architecture.

**Pro tip:** Tagging questions are about *symmetric context*. The winning structure: (1) show the word is ambiguous, (2) show the decisive evidence is on the **right** (for "leaves" it is `the dark cave`), (3) explain forward pass only has the left context, (4) explain concatenated forward+backward states give both. If asked about a *different* ambiguous word, the answer template is identical — just switch the example. Avoid saying "BiLSTM has more memory" — the point is **direction**, not capacity.

---

### Q.3.3 — The Information Bottleneck in Seq2Seq (4 Marks)

> **Note:** The original paper labels this question as Q.3.2 as well — likely a typo for Q.3.3.

Even with advanced memory gates, sequence-to-sequence RNN models (like early translation models) suffer from an "Information Bottleneck" when processing very long documents. Describe this bottleneck phenomenon and explain why packing an entire paragraph into a single hidden state vector is problematic.

#### Answer

**The phenomenon.** In a classic Seq2Seq model, the encoder reads the source sequence one token at a time and **compresses everything into a single fixed-size context vector** (the encoder's final hidden state). The decoder then generates the output starting from that one vector. This is the bottleneck: a *fixed-capacity* vector must carry *variable-length* information — grammar, facts, entities, tone, and relationships from an arbitrarily long paragraph.

**Why it is problematic.**

- **Fixed capacity vs unbounded input.** A 10-word sentence and a 500-word paragraph both collapse into the same-dimensional vector. Early information must compete with everything that follows for the same limited space, so details from the beginning are squeezed out. The encoder *forgets the start by the time it reaches the end* — the same long-context amnesia seen in the vanishing-gradient problem, but now compounded by the compression step.
- **One vector, many roles.** The decoder must reconstruct the whole meaning from a single summary. The summary is lossy by construction: tone, subtle entities, and long-range dependencies that do not fit are discarded silently.
- **No selective access.** During decoding, the model has no way to "look back" at the individual encoder states — it only has the compressed vector. Anything it needs that was not stored is simply gone.

**The course framing:** it is like reading an entire book and forming one mental summary, then being asked to write the book back in another language — the summary loses too much. This is precisely the limitation that **attention mechanisms** solve: instead of one compressed vector, the decoder attends over *all* encoder hidden states and selects what is relevant at each output step.

**Pro tip:** The answer is a *capacity mismatch* argument: fixed-size vector vs variable-length input. Use the book-summary analogy (it is the course's own). Always end by naming **attention** as the fix — examiners often ask "what solves the bottleneck?" as a follow-up. Keep it tight: phenomenon → why compression loses information → why the decoder can't recover it → attention as the remedy.

---

## Q.4

### Q.4.1 — Self-Attention and Coreference (6 Marks)

The Transformer architecture relies heavily on the "Self-Attention" mechanism. Using the sentence *"The bank of the river was muddy, so he could not sit by it"*, explain in plain language how the Self-Attention mechanism helps the neural network figure out whether the word *"it"* refers to the bank, the river, or the mud.

#### Answer

**What self-attention does.** In a Transformer, each token is processed alongside every other token, and self-attention computes a **relevance score** for every pair. Each word is transformed into a **Query** ("what am I looking for?"), a **Key** ("what do I contain?"), and a **Value** ("what information do I pass?"). For a given word, the attention weights decide how much of every other word's representation is blended into its own. The **softmax over the scaled dot products** turns raw scores into weights that sum to 1, so the output at each position is a weighted combination of the whole sentence.

**How "it" is resolved.** For the pronoun *it*, its Query asks roughly "what could I refer to?" It is compared against every candidate antecedent — *bank*, *river*, *mud* (and the rest) — via their Keys. The mechanism can weigh:

- **Collocation / world knowledge:** *sit by* most naturally takes a **river** as its object ("sit by the river"), so the pair *(it, river)* receives a high attention weight.
- **Semantic plausibility:** one sits *by* a body of water; one does not typically "sit by" mud or a bank. This plausibility is reflected in higher relevance scores for *river*.
- **Structural cues:** *the bank of the river* is a possessive/`of`-construction, which the syntactic information encoded in attention can help untangle, keeping *bank* and *river* distinct candidates.

Because the representation of *it* becomes a **weighted blend dominated by the highest-scoring candidate**, the model's embedding for *it* is pushed strongly toward *river*. The final hidden state of *it* thus "means" river in this context, and the model resolves the coreference correctly — without any hand-written rules.

**Why this is special.** This is the course's canonical attention example: *"The animal did not cross the street because **it** was too tired"* — *it* scores high against *animal*, low against *street*. Encoder self-attention is **fully bidirectional** (every token sees every other token), and multi-head attention lets different heads specialise — one head may learn coreference, another syntax, another semantic similarity. So for our sentence, the coreference head can focus on the pronoun–antecedent links while others capture the `of`-structure and the `sit by` collocation.

**Pro tip:** Coreference questions are graded on *mechanism in plain language*. The template: (1) every token attends to every other token, (2) *it* is compared to each candidate, (3) high weight → strong influence on *it*'s representation, (4) the winner shapes what *it* "means". Use the textbook animal/street example as reinforcement and mention bidirectional encoder attention + multi-head specialisation for the final mark. Keep it plain-language as asked — save the formula (`softmax(QK^T/√d_k)`) for when the question asks for the math.

---

### Q.4.2 — Zero-Shot vs. Fine-Tuning for Specialized Domains (4 Marks)

A legal consultancy wants to use a Pre-trained Large Language Model (LLM) to classify highly specialized contract clauses. Briefly contrast the "Zero-Shot Inference" approach with the "Fine-Tuning" approach in terms of training data requirements and expected accuracy for this highly specialized domain.

#### Answer

| Aspect | Zero-Shot Inference | Fine-Tuning |
|--------|--------------------|-------------|
| **Training data required** | None — just a prompt/instructions describing the labels | A **labelled dataset** of the specialized clauses (hundreds to thousands of examples) plus training compute |
| **Setup cost** | Minimal — fastest to deploy; works immediately | Higher — data curation, training run, evaluation, versioned deployment |
| **Expected accuracy (specialized domain)** | Lower and inconsistent — the model guesses with generic world knowledge; format and label boundaries may drift from the firm's taxonomy | Higher and more reliable — weights adapt to legal vocabulary, clause patterns, and the firm's exact label set |
| **When it fits** | Prototyping, low-volume, or when labels are unavailable | Production classification of domain-critical contract clauses |

**Why the gap widens in this domain.** "Highly specialized contract clauses" live far from the LLM's generic pre-training distribution: legal language, firm-specific clause types, and a bespoke label taxonomy. Zero-shot relies on the model's general knowledge, which may map a clause to the wrong category or produce inconsistent outputs across documents. Fine-tuning starts from the pre-trained weights and **adapts them to the domain** — much less data than training from scratch, but far better alignment than zero-shot. Domain pre-tuned checkpoints (e.g. Legal-BERT) amplify this further when available.

**Recommendation.** For a legal consultancy where misclassification is costly, use **zero-shot to prototype quickly**, then **fine-tune on curated labelled clauses for production accuracy**. Few-shot prompting (a few labelled examples in the prompt) is a middle option when fine-tuning data is scarce.

**Pro tip:** Contrast questions want a *two-axis table*: data requirements on one side, expected accuracy on the other — then a verdict. The phrase "highly specialized domain" is the tell: the answer must explain *why* zero-shot degrades there (distribution gap between pre-training and the domain). Always end with the pragmatic hybrid: zero-shot to start, fine-tune (or few-shot) for production. Never claim zero-shot "guarantees" anything — the course explicitly warns that few/few-shot improves format consistency, not correctness.
