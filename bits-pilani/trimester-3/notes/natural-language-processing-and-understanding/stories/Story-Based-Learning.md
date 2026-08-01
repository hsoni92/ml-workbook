# Natural Language Processing and Understanding — Story-Based Learning
## The Complete Mental Model: The Language Detective Agency

---

> *"Every messy sentence is a crime scene. Every NLP pipeline is a detective turning chaos into evidence. This is your field manual."*

---

**The Master Narrative:** You work at **The Language Detective Agency**. Raw human language arrives as unstructured crime scenes — ambiguous, context-dependent, full of red herrings. Your job: **decode language into structured evidence** machines can act on. Each week adds a new division to the agency — from opening case files, to dusting for fingerprints (preprocessing), to tagging suspects (NER), to building semantic maps (embeddings), to deploying senior detectives with memory (RNNs), to the all-seeing spotlight team (Transformers), and finally the press office (LLMs).

---

# PART 1: OPENING THE AGENCY (Week 0)

## Course Overview and Practitioner Learning — The Agency Charter

**The Story:** Before any case lands on your desk, the agency director explains the mission: turn unstructured human language into actionable intelligence. The course arc mirrors a detective's career — crime-scene basics (preprocessing), evidence tagging (POS/NER), case archives (corpora), clue weighting (TF-IDF), semantic maps (embeddings), detectives with memory (RNNs), the spotlight team (Transformers), and the press office (LLMs). Industry practitioners run this agency daily; your job is to know *why* each tool exists, not just which API to call.

**Course arc:** Foundations → Preprocessing → Sparse vectors → Dense embeddings → Sequential models → Transformers → Applications → LLM capstone.

**Tools in the toolkit:** NLTK, spaCy, Flair, Hugging Face, Gensim, Gemini/OpenAI APIs.

**Practitioner lens:** Production trade-offs — latency, cost, maintainability — matter as much as benchmark accuracy.

**Exam Tip:** NLP is not only ChatGPT; classical preprocessing and sparse methods remain examinable foundations.

> **Course Overview** = The agency charter: NLP turns unstructured language into structured, actionable signals.

---

# PART 2: THE NATURE OF THE CRIME SCENE (Week 1)

## Introduction to NLP — Opening the First Case

**The Story:** The rookie detective's first briefing: human language is the most complex evidence you'll ever handle. This module introduces the agency's core divisions — understanding (NLU), generation (NLG), morphology, and ambiguity — before any tool is deployed. Rule-based lookup without context fails on real cases; every pipeline must account for structure, meaning, and surrounding sentences.

**Core questions the module answers:** What is NLP? How do NLU and NLG differ? Why is morphology relevant? Why does ambiguity break naive systems?

**Exam Tip:** NLP is not chatbots only; NLU and NLG are distinct design concerns even when LLMs blur the boundary.

> **NLP Module Introduction** = First briefing — language is complex evidence requiring structured pipelines.

---

## What Is Natural Language Processing? — The Core Mission

**The Story:** Every day, billions of people type, speak, and message. Computers only see bits and numbers. The agency's core mission — **NLP** — is closing that gap: enabling machines to **read**, **extract**, and **respond** in human language. A crime scene (raw text) is unstructured, ambiguous, and context-dependent. No single regex solves it; you need a multi-stage pipeline.

**Formal definition:** NLP = AI branch enabling computers to (1) read and interpret text/speech, (2) extract structured information, (3) generate meaningful responses.

| Property | Detective impact |
|----------|-----------------|
| Unstructured | No fixed schema — must parse and segment |
| Ambiguous | Context needed to disambiguate |
| Context-dependent | Prior sentences change meaning |

**Exam Tip:** NLP includes understanding and extraction, not just generation. ASR converts audio to text; NLP operates on the resulting language.

> **NLP** = The agency's mission: bridge human communication and machine computation.

---

## NLP, NLU, and NLG — Three Divisions in One Building

**The Story:** The agency has three divisions under one roof. **NLP** is the whole building — any computational work on language. **NLU** (Natural Language Understanding) is the analysis wing: "What does this witness mean?" — sentiment, NER, intent. **NLG** (Natural Language Generation) is the press office: "How do we express our findings?" — summaries, chatbots, reports. LLMs blur the lines, but the design distinction still matters when you architect a system.

| Division | Core question | Direction |
|----------|---------------|-----------|
| **NLP** | Process language computationally? | Umbrella |
| **NLU** | What does input **mean**? | Input → structured meaning |
| **NLG** | How to **express** information? | Data → human-readable text |

**Exam Tip:** NLU and NLG are subsets of NLP, not disjoint fields. Design systems by asking: do I need to understand, generate, or both?

> **NLU / NLG** = Analysis wing vs press office — both inside the NLP building.

---

## NLP Applications by Domain — Case Files Across Industries

**The Story:** The agency takes cases from every industry. Search engines need query understanding and document ranking. Voice assistants chain speech recognition with language understanding. Email filters classify spam. Keyboards predict the next word. Chatbots generate fluent replies. Each case combines sub-tasks — tokenisation, classification, generation — in a single pipeline.

| Domain | Example | NLP task |
|--------|---------|----------|
| Search | Google, Bing | Query understanding, ranking |
| Voice | Siri, Alexa | ASR + NLU |
| Email | Spam filter | Text classification |
| Keyboards | Autocomplete | Language modelling |
| Generative AI | ChatGPT, Gemini | Understanding + generation |

**Exam Tip:** Link applications to underlying tasks (NER vs classification vs generation). Medical NER needs domain corpora, not general web text.

> **NLP Applications** = Every industry sends the agency a different kind of case file.

---

## Morphology — Dissecting the Evidence

**The Story:** A detective dissects words like a forensic pathologist. **Morphology** is the study of word structure from **morphemes** — the smallest meaningful units. The **root** carries core meaning (*act* in *acting*). **Affixes** attach: prefixes (*un-*), suffixes (*-ing*). The **stem** is a rough chop (*stud* from *studying*); the **lemma** is the dictionary form (*study*). Stemming is fast but crude; lemmatisation is precise but needs POS tags. Modern transformers use **subword tokenisation** — a hybrid strategy.

**Key terms:** root, stem, affix, lemma, inflection, derivation, stemming, lemmatisation.

**Exam Tip:** Stem ≠ lemma. Over-stemming merges unrelated words (*university*/*universe*). Lemmatisation requires POS (*running* verb → *run*, not *running* noun).

> **Morphology** = Forensic word dissection — roots, affixes, stems, and lemmas.

---

## Ambiguity — Polysemy and Synonymy — The Red Herrings

**The Story:** Every crime scene has red herrings. **Polysemy** is one word, multiple related meanings — *bank* (river vs financial), *run* (sprint vs operate). **Synonymy** is different words, same meaning — *buy*/*purchase*. Stemming cannot fix synonymy; static embeddings give *bank* one vector regardless of sense. **Contextual embeddings** (BERT) resolve polysemy by changing the vector per sentence. Sentence-level ambiguity (*"I saw her duck"*) needs full context.

**Definitions:**
- **Polysemy:** one word, multiple related senses
- **Synonymy:** different words, similar meaning

**Exam Tip:** Polysemy ≠ homonymy (unrelated senses). Static Word2Vec fails on polysemy; BERT handles it via context.

> **Polysemy / Synonymy** = Red herrings — one word many meanings, many words one meaning.

---

# PART 3: CRIME-SCENE PROCESSING (Week 2)

## Text Preprocessing Foundations — Cleaning the Scene

**The Story:** Raw text arrives covered in grime — HTML tags, URLs, inconsistent casing, filler words. **Cleaning** removes noise; **preprocessing** transforms text into machine-ready form. These are not the same job, and over-cleaning destroys evidence (negation in sentiment, numbers in finance). LLMs still benefit from corpus cleaning at scale. Every task needs its own pipeline — NER keeps capitalisation; topic modelling removes stopwords.

**Exam Tip:** Cleaning ≠ preprocessing. Over-cleaning loses negation and punctuation cues. Pipelines are task-specific, not universal.

> **Preprocessing** = Crime-scene cleaning — remove grime without destroying evidence.

---

## Tokenisation — Bagging the Evidence

**The Story:** Before analysis, detectives bag individual pieces of evidence. **Tokenisation** splits text into **tokens** — words, sentences, or subwords. Whitespace splitting fails on contractions (*don't*). Word tokenisation is wrong for BERT, which uses subword pieces. NLTK and spaCy offer different tokenisers; choose based on downstream model.

**Exam Tip:** Tokenise before stopword removal. BERT needs subword tokenisation, not simple word split. Download NLTK `punkt` for sentence tokenisation.

> **Tokenisation** = Bagging evidence — split text into processable units.

---

## Noise Removal with Regex — The Fine Brush

**The Story:** Some grime needs a fine brush, not a bulldozer. **Regular expressions** remove HTML tags, URLs, extra whitespace, and special characters. Pattern `\s+` collapses whitespace — but replacing with empty string destroys word boundaries. Case normalisation helps matching but loses named-entity cues. Domain matters: stripping numbers destroys financial and medical evidence.

**Key patterns:** `\s+` (whitespace), `<.*?>` (HTML tags), `https?://\S+` (URLs).

**Exam Tip:** Over-cleaning is as dangerous as under-cleaning. Never strip numbers in finance/medical domains without reason.

> **Regex cleaning** = Fine brush — precise noise removal without destroying boundaries.

---

## Stopword Removal — Filtering the Noise

**The Story:** Function words (*the*, *is*, *and*) are like footprints everyone leaves — they tell you someone was here but not who. **Stopwords** carry little discriminative power. Removing them shrinks feature space for classification and topic modelling. But for sentiment, removing *not* destroys meaning. TF-IDF partially handles stopwords automatically; explicit removal still helps.

**Exam Tip:** Never remove negation words for sentiment analysis. Tokenise before removing stopwords. Stopword lists are language- and domain-specific.

> **Stopwords** = Common footprints — filter them when they add no clue.

---

## Stemming and Lemmatisation — Normalising the Clues

**The Story:** Detectives normalise clues for comparison. **Stemming** chops suffixes with rules (Porter stemmer: *studying* → *studi*) — fast but produces invalid forms. **Lemmatisation** looks up dictionary forms (*studying* → *study*) — accurate but needs POS tags and is slower. Porter is English-centric. For short-text topic modelling (tweets), stemming helps; for NER, avoid aggressive normalisation.

| Method | Speed | Accuracy | Needs POS |
|--------|-------|----------|-----------|
| Stemming | Fast | Crude | No |
| Lemmatisation | Slower | Precise | Yes |

**Exam Tip:** *Stems* may be invalid words. Lemmatisation needs POS (*running* verb → *run*). Download NLTK `wordnet` and `omw-1.4`.

> **Stemming / Lemmatisation** = Normalise word forms — rough chop vs dictionary lookup.

---

## Preprocessing Pipeline Construction — The Standard Operating Procedure

**The Story:** Every detective follows a standard operating procedure. The canonical pipeline: **clean** (regex) → **tokenise** → **(remove stopwords)** → **(stem or lemmatise)**. Order matters: tokenise before cleaning destroys boundaries; remove stopwords before sentiment destroys negation. The same pipeline is wrong for NER (keep entities) vs topic modelling (remove stopwords).

```
Raw text → Clean → Tokenise → Stopwords → Stem/Lemmatise → Model input
```

**Exam Tip:** Pipelines are task-specific. Document your order; exam questions test sequencing errors.

> **Preprocessing pipeline** = Standard operating procedure — order matters.

---

# PART 4: EVIDENCE TAGGING (Week 3)

## Structural Text Analysis Overview — The Tagging Division

**The Story:** The Tagging Division assigns structure to raw evidence. **POS tagging** labels grammatical roles (noun, verb, adjective). **NER** identifies real-world entities (persons, organisations, locations). These are different jobs — POS tells you *what role* a word plays; NER tells you *who or what* it refers to. NLTK, spaCy, and Flair each have strengths; none is universally best.

**Exam Tip:** POS ≠ NER. POS is context-dependent (*book* as noun vs verb). Tool choice depends on speed vs accuracy trade-offs.

> **Structural analysis** = Tagging division — grammatical roles and named entities.

---

## Part-of-Speech Tagging — Grammatical Role Labels

**The Story:** Every word at a crime scene plays a role — witness, suspect, location. **POS tagging** assigns grammatical categories: noun (NN), verb (VB), adjective (JJ). Tags are **context-dependent**: *book* is a noun in "read a book" but a verb in "book a flight." Penn Treebank and Universal POS tag sets differ across libraries. POS tags are required for accurate lemmatisation.

**Exam Tip:** POS ≠ NER. Tag sets differ (NLTK Penn vs spaCy Universal). Context determines the tag for ambiguous words.

> **POS tagging** = Assign grammatical roles — noun, verb, adjective, context-dependent.

---

## POS Tagging in Practice — spaCy, NLTK, and Flair

**The Story:** Three junior detectives handle POS tagging differently. **spaCy** uses `token.pos_` (coarse) and `token.tag_` (fine-grained) — fast, production-ready. **NLTK** uses `pos_tag()` after tokenisation — modular, educational. **Flair** wraps text in `Sentence` objects and calls `SequenceTagger.load('pos')` — highest accuracy, slowest. All require loading models or downloading data first.

**Key APIs:**
- spaCy: `token.pos_`, `token.tag_`
- NLTK: `nltk.pos_tag(tokens)`
- Flair: `tagger.predict(sentence)`

**Exam Tip:** Load spaCy model before use. Download NLTK `averaged_perceptron_tagger`. Flair requires `Sentence` wrapper.

> **POS in practice** = Three detectives, three toolkits — spaCy for speed, Flair for accuracy.

---

## Visualising POS and Dependency Trees — The Evidence Board

**The Story:** Detectives pin evidence on a board to see connections. **spaCy displacy** renders POS tags and **dependency trees** — who modifies whom (*nsubj*, *dobj*, *amod*). Use `style='dep'` for syntactic trees, `style='ent'` for named entities (not POS). Dependency labels show grammatical relationships beyond simple tags.

**Exam Tip:** `'ent'` style is for NER, not POS. Dependency labels (nsubj, dobj) ≠ POS tags.

> **Dependency trees** = Evidence board — visual grammar and entity connections.

---

## Named Entity Recognition — Identifying the Suspects

**The Story:** NER is the suspect-identification unit. It finds **named entities** — real-world objects with proper names: PERSON, ORG, GPE, LOC, DATE, MONEY. Entities can span multiple tokens (*New York*). Not every noun is an entity. NER is the primary step in information extraction — pulling structured facts from unstructured text.

**Common entity types:** PERSON, ORG, GPE (geo-political), LOC, DATE, TIME, MONEY, PERCENT.

**Exam Tip:** NER ≠ POS. Tag sets differ across libraries (PER vs PERSON). Multi-token spans need special handling.

> **NER** = Suspect identification — find persons, organisations, locations in text.

---

## NER in Practice — spaCy, NLTK, and Flair

**The Story:** Three tools, three accuracy levels. **spaCy** uses `doc.ents` and `ent.label_` — industry standard, fast. **NLTK** uses chunk-based `ne_chunk` — educational, fewer entity types (no MONEY/DATE). **Flair** loads `SequenceTagger.load('ner')` — highest accuracy, slowest. All require model loading; Flair needs `predict()` call.

**Exam Tip:** spaCy uses `doc.ents`, not `doc.entities`. NLTK accuracy gap vs spaCy. Call `predict()` on Flair tagger.

> **NER in practice** = Three suspect-ID teams — spaCy for production, Flair for accuracy.

---

## Comparing NLTK, spaCy, and Flair — Choosing Your Detective

**The Story:** The agency maintains three detective ranks. **NLTK** is the trainee — slowest, lowest accuracy, best for learning linguistics. **spaCy** is the field agent — fast, good accuracy, production pipelines. **Flair** is the specialist — slowest, highest accuracy, research and critical cases. None is obsolete; choose by constraints.

| Library | Speed | Accuracy | Best for |
|---------|-------|----------|----------|
| NLTK | Slowest | Lower | Education, linguistics |
| spaCy | Fast | Good | Production pipelines |
| Flair | Slowest | Highest | Research, accuracy-critical |

**Exam Tip:** spaCy uses shallow neural nets, not BERT, for default POS/NER. Flair is slower but more accurate.

> **Tool comparison** = Trainee vs field agent vs specialist — match tool to constraints.

---

# PART 5: THE CASE ARCHIVES (Week 4)

## Text Corpora Overview — The Evidence Vault

**The Story:** Detectives don't work from single clues — they study **case archives** (corpora). A corpus is a collection of documents whose statistics shape every model trained on it. Model behaviour is a function of corpus statistics: $\text{Model behaviour} = f(\text{corpus statistics})$. Large does not mean unbiased. Always explore before modelling.

**Exam Tip:** Corpus ≠ labelled dataset. Single PDF ≠ corpus. Explore vocabulary and distribution before training.

> **Corpus linguistics** = The evidence vault — archives that shape every model.

---

## What Is a Text Corpus? — Building the Archive

**The Story:** A **text corpus** is a structured collection of documents — books, articles, tweets, clinical notes. Models trained on a corpus reproduce its statistics. TF-IDF weights depend on document frequency across the archive: $\text{TF-IDF}(t, d) \propto \text{count}(t \text{ in } d) \times \log\frac{N}{\text{df}(t)}$. Garbage in, garbage out — the archive defines what the model "knows."

**Exam Tip:** Corpus ≠ dataset (which implies labels). Models inherit corpus biases and vocabulary.

> **Text corpus** = Case archive — documents whose statistics define model behaviour.

---

## Types of Corpora — Filing the Archives

**The Story:** Archives come in different categories. **General corpora** (Gutenberg, Brown) cover broad language. **Domain-specific** corpora focus on medicine, law, finance. **Annotated corpora** (CoNLL) have human labels for training. **Task-specific** corpora target one NLP task. Training medical NER on Gutenberg fails — the vocabulary and entities differ completely.

| Type | Example | Use |
|------|---------|-----|
| General | Gutenberg, Brown | Broad language study |
| Domain | PubMed, legal filings | Specialised models |
| Annotated | CoNLL NER | Supervised training |
| Task-specific | Sentiment reviews | Single-task models |

**Exam Tip:** Don't train domain models on general literary corpora. Gutenberg is archaic literary English.

> **Corpus types** = Filing system — general, domain, annotated, task-specific archives.

---

## Bias and Representation in Corpora — Skewed Archives

**The Story:** Archives are not neutral. A corpus over-representing one demographic produces models that fail on others: $\text{Model bias} \leftarrow \text{Corpus bias}$. Scale can amplify bias — bigger archives with skewed content make worse stereotypes. Annotation bias in labels propagates to predictions. Examine training data before blaming the algorithm.

**Exam Tip:** Examine corpus composition first. Scale amplifies existing bias. Annotation choices create label bias.

> **Corpus bias** = Skewed archives — models inherit what the vault contains.

---

## Corpus Exploration — Gutenberg and Brown Analysis

**The Story:** Before opening a case, detectives survey the archive. **Types** (unique words) vs **tokens** (total word count) differ: $\text{TTR} = \frac{|\text{types}|}{|\text{tokens}|}$. Gutenberg reveals literary vocabulary and word frequency. **Brown corpus** compares genres (news, fiction, academic) — showing language varies by domain. TTR is not comparable across very different text lengths.

**Key metrics:** type-token ratio (TTR), word frequency distribution, genre comparison.

**Exam Tip:** Types ≠ tokens. TTR varies with text length. Brown corpus is 1960s American English — dated but genre-diverse.

> **Corpus exploration** = Survey the archive — types, tokens, frequency, genre.

---

# PART 6: WEIGHING THE CLUES (Week 5)

## Traditional Word Representations Overview — The Scoring Lab

**The Story:** Machines need numbers, not words. The Scoring Lab converts text to vectors. **Vectorisation** is not preprocessing — it happens after cleaning. "Embedding" broadly includes sparse methods (one-hot, BoW, TF-IDF) and dense methods (Word2Vec). Methods are not interchangeable; each makes different trade-offs.

**Exam Tip:** Vectorisation ≠ preprocessing. Sparse and dense embeddings serve different purposes. Know when each applies.

> **Word representations** = Scoring lab — turn words into numbers machines can compute.

---

## One-Hot Encoding — The Identity Badge

**The Story:** Each word gets an identity badge — a vector of zeros with a single one. Vocabulary size $|V|$ determines vector length. Document vector marks which words appear:

$$x_i = \begin{cases} 1 & \text{if word } w_i \text{ appears in } d \\ 0 & \text{otherwise} \end{cases}, \quad \mathbf{x}_d \in \{0, 1\}^{|V|}$$

Every word is orthogonal — *dog* and *puppy* have zero similarity. No word order, no frequency beyond presence.

**Exam Tip:** One-hot ≠ BoW (which counts frequency). No semantic similarity: $\text{dog} \cdot \text{puppy} = 0$.

> **One-hot encoding** = Identity badge — one slot per word, all others zero.

---

## One-Hot Encoding Implementation — Printing the Badges

**The Story:** In code, build a sorted vocabulary list, then for each word in a sentence, set the corresponding index to 1. Lookup is $O(n)$ with `list.index`. Case sensitivity matters — *The* and *the* are different badges. Sort vocabulary for deterministic output across runs.

**Exam Tip:** Case sensitivity creates duplicate vocabulary entries. Sort vocabulary for reproducibility.

> **One-hot implementation** = Print badges — vocabulary index lookup, watch case sensitivity.

---

## Advantages and Limitations of One-Hot Encoding — Badge Pros and Cons

**The Story:** Identity badges are simple and interpretable but wasteful. Sparsity ratio $\approx 1 - \frac{\text{words per sentence}}{|V|}$ — most entries are zero. High dimensionality grows with vocabulary. Orthogonality means linguistically related words appear unrelated. One-hot loses word order, frequency, and meaning.

**Exam Tip:** One-hot is not lossless — order, frequency, and semantics are all discarded. Orthogonality ≠ linguistic independence.

> **One-hot trade-offs** = Simple badges — interpretable but sparse, high-dimensional, no semantics.

---

## Bag of Words — The Evidence Count

**The Story:** Instead of just marking presence, count how many times each word appears — a **multiset** of words. BoW preserves multiplicity but discards order: *"the man bit the dog"* and *"the dog bit the man"* produce identical vectors. Case and stemming choices affect counts. Still a sparse, high-dimensional representation.

**Exam Tip:** BoW preserves count, not order. Same words different order = same vector. Case and stemming matter.

> **Bag of Words** = Evidence count — word frequencies in a multiset, order discarded.

---

## BoW Implementation with scikit-learn — Automated Counting

**The Story:** scikit-learn's `CountVectorizer` automates the counting pipeline. Fit on training data only to prevent data leakage. `binary=True` gives presence/absence, not frequency. BoW produces integer matrices; TF-IDF produces float weights — different downstream behaviour.

**Exam Tip:** Fit vectoriser on train only. `binary=True` ≠ frequency BoW. BoW = integers, TF-IDF = floats.

> **BoW implementation** = Automated counter — CountVectorizer, fit on train only.

---

## Advantages and Limitations of Bag of Words — Count Pros and Cons

**The Story:** BoW is a workhorse — simple, fast, competitive for keyword-heavy tasks like spam detection. But it fails on negation (*not good* looks like *good*), ignores word order, and treats all non-zero counts equally without rarity weighting. Still widely used as a baseline.

**Exam Tip:** BoW fails on negation. Competitive for keyword tasks but lacks semantics and order.

> **BoW trade-offs** = Workhorse counter — fast baseline, blind to order and negation.

---

## TF-IDF — Weighting Clues by Rarity

**The Story:** Not all clues are equal. **Term Frequency (TF)** asks: how often does this word appear in *this* document? **Inverse Document Frequency (IDF)** asks: how rare is it across the *entire archive*?

$$\text{TF}(x, d) = \text{count of } x \text{ in } d$$
$$\text{IDF}(x) = \log\frac{N}{\text{DF}(x)}$$
$$\text{TF-IDF}(x, d) = \text{TF}(x, d) \times \log\frac{N}{\text{DF}(x)}$$

Word in every document → IDF = 0 → downweighted. Rare domain term → high IDF → boosted.

**Exam Tip:** TF is per-document; IDF is corpus-wide. Log is required. TF-IDF does not capture semantics (*car* ≠ *automobile*).

> **TF-IDF** = Rarity-weighted clues — frequent locally, rare globally = high score.

---

## TF-IDF Implementation — The Scoring Machine

**The Story:** scikit-learn's `TfidfVectorizer` builds sparse TF-IDF matrices. Sublinear TF scaling uses $1 + \log(\text{TF})$. Smoothing parameter $k$ prevents zero division. Fit on training data only. Same word gets different scores in different documents based on local TF.

**Exam Tip:** Fit on train only. Same word, different TF-IDF per document. Sublinear scaling dampens high frequencies.

> **TF-IDF implementation** = Scoring machine — TfidfVectorizer, sparse float matrix.

---

## Advantages and Limitations of TF-IDF — Best Sparse Representation

**The Story:** TF-IDF is the best sparse representation for classification and retrieval — automatically downweighting *the*, *is*, *and* while boosting domain terms like *mitochondria*. But it remains high-dimensional, statistical (not semantic), and blind to word order. TF-IDF ≠ Word2Vec — different paradigm entirely.

**Exam Tip:** TF-IDF ≠ Word2Vec. High dimensionality remains. Statistical weighting, not semantic understanding.

> **TF-IDF trade-offs** = Best sparse scorer — auto-downweights common words, still no semantics.

---

# PART 7: SEMANTIC MAPS (Week 6)

## Dense Embeddings Overview — The Cartography Division

**The Story:** Sparse vectors tell you *which* words appear; dense embeddings tell you *what they mean*. The Cartography Division maps words into continuous space where similar meanings cluster. The famous analogy: $\mathbf{v}_{\text{king}} - \mathbf{v}_{\text{man}} + \mathbf{v}_{\text{woman}} \approx \mathbf{v}_{\text{queen}}$. Word2Vec and GloVe produce **static** embeddings — one vector per word. BERT produces **contextual** ones.

**Exam Tip:** "Embedding" includes TF-IDF broadly. Word2Vec/GloVe are static; dense ≠ always better than sparse.

> **Dense embeddings** = Semantic maps — words as points in meaning-space.

---

## Word2Vec — Predict to Compress

**The Story:** Word2Vec trains a shallow neural network on a prediction game. **CBOW** (Continuous Bag of Words): given context words, predict the center — fill in the blank. **Skip-gram**: given center word, predict context — opposite direction. To solve prediction efficiently, the network compresses meaning into hidden-layer vectors: $\mathbf{v}_w \in \mathbb{R}^{d}$, $d \in [50, 300]$.

| Architecture | Direction | Speed | Rare words |
|-------------|-----------|-------|------------|
| CBOW | Context → target | Faster | Less effective |
| Skip-gram | Target → context | Slower | Better |

**Exam Tip:** CBOW = many → one; Skip-gram = one → many. Shallow network, not deep. Learns by prediction, not co-occurrence counting (that's GloVe).

> **Word2Vec** = Prediction game — CBOW fills blanks, Skip-gram predicts neighbours.

---

## Word2Vec Implementation — Training Your Own Map

**The Story:** Gensim's `Word2Vec` takes `List[List[str]]` — pre-tokenised sentences. Lowercase for consistency. `min_count` filters rare words — on small corpora, lower it. Pretrained models like `word2vec-google-news-300` provide 3M words in 300 dimensions ready for cosine similarity.

**Exam Tip:** Input must be list of token lists. Lowercase. `min_count` on small corpora. Pretrained models avoid training from scratch.

> **Word2Vec implementation** = Train the map — Gensim, tokenised sentences, min_count tuning.

---

## GloVe — Global Co-occurrence Statistics

**The Story:** While Word2Vec learns locally from prediction windows, **GloVe** (Global Vectors) factorises a global co-occurrence matrix. $X_{ij}$ = times word $j$ appears in context of word $i$. The model learns: $\mathbf{w}_i^T \mathbf{w}_j \approx \log X_{ij}$. Matrix factorisation, not a prediction neural network. Still produces static embeddings.

**Exam Tip:** GloVe ≠ neural network — it's matrix factorisation on global statistics. Global vs Word2Vec's local windows.

> **GloVe** = Global statistics map — factorise co-occurrence matrix, not predict words.

---

## GloVe Implementation — Loading Pretrained Maps

**The Story:** Gensim loads pretrained GloVe vectors (e.g., glove-wiki-gigaword). No training from scratch in standard workflow. Out-of-vocabulary words raise KeyError — handle gracefully. Small demo models (25-dim) are for illustration only; production uses 100–300 dimensions.

**Exam Tip:** Gensim loads pretrained only. OOV → KeyError. Small models for demos, not production.

> **GloVe implementation** = Load pretrained maps — Gensim, handle OOV gracefully.

---

## Visualising Word Embeddings — Reading the Map

**The Story:** Semantic maps live in hundreds of dimensions — humans need 2D projections. **PCA** preserves global structure; **t-SNE** preserves local clusters better but distorts distances. Cosine similarity in original space is the reliable metric; 2D plots are for intuition only. Need 20+ words for meaningful visualisation. Never mix models in one plot.

**Exam Tip:** 2D distances are distorted — trust cosine similarity in original space. Don't mix embedding models.

> **Embedding visualisation** = Flatten the map — PCA/t-SNE for intuition, cosine for truth.

---

## Static vs Contextual Embeddings — Fixed vs Adaptive Maps

**The Story:** Word2Vec and GloVe assign one fixed coordinate per word — *bank* gets the same vector whether river or financial. **Contextual embeddings** (ELMo, BERT) change the vector based on surrounding words. Vector arithmetic works on static embeddings: $\mathbf{r}_{\text{gender}} = \mathbf{v}_{\text{woman}} - \mathbf{v}_{\text{man}}$. Polysemy breaks static maps; context saves them.

**Exam Tip:** Word2Vec/GloVe = static (one vector per word). BERT = contextual. Vector arithmetic demonstrated on static embeddings only.

> **Static vs contextual** = Fixed map vs GPS that recalculates per sentence.

---

# PART 8: DETECTIVES WITH MEMORY (Week 7)

## Sequential Modelling Overview — Why Order Matters

**The Story:** A bag of evidence loses sequence — who spoke first, who reacted second. Language is a **sequence**, not a bag. TF-IDF vectors have fixed size regardless of sentence length. BoW destroys word order. Sequential models read evidence one piece at a time, carrying memory forward. Two problems to solve: variable-length input and preserved order.

**Exam Tip:** TF-IDF size is fixed per vocabulary, not per sentence length. BoW loses order — two problems drive sequential models.

> **Sequential modelling** = Detectives with notebooks — language is ordered, not a bag.

---

## Sequence-to-Sequence Modelling — Translator Pairs

**The Story:** Some cases require transforming one sequence into another — translation, summarisation, dialogue. **Seq2Seq** uses an **encoder** that reads the input into a **context vector** and a **decoder** that generates output token by token. The context vector is an information bottleneck — long sequences lose detail. Attention (Part 9) solves this bottleneck.

**Exam Tip:** Encoder reads, decoder generates. Bottleneck limits long sequences. Attention addresses the bottleneck.

> **Seq2Seq** = Translator pair — encoder compresses, decoder generates.

---

## Recurrent Neural Networks — The Memory Notebook

**The Story:** An RNN detective carries a **hidden state** notebook — at each time step, read new evidence $X_t$, update memory $H_t$, produce output $Y_t$. Weights are **shared across time steps** — same detective rules at every position.

$$H_t = \tanh(W_{hh} H_{t-1} + W_{xh} X_t + b_h)$$
$$Y_t = W_{hy} H_t + b_y$$

$H_t$ = memory, $Y_t$ = output. Activation is $\tanh$, not sigmoid.

**Exam Tip:** Weights shared across time. $H_t$ is memory, $Y_t$ is output. Vanishing gradients limit long-range memory.

> **RNN** = Memory notebook — hidden state updated at each time step.

---

## RNN Architecture Patterns — Case Shapes

**The Story:** Same detective, different case shapes. **Many-to-one**: read entire sequence, one verdict (sentiment). **One-to-many**: one clue, generate sequence (image captioning). **Many-to-many**: input sequence → output sequence (translation). Sentiment is many-to-one, not one-to-many.

| Pattern | Input | Output | Example |
|---------|-------|--------|---------|
| Many-to-one | Sequence | Single label | Sentiment |
| One-to-many | Single input | Sequence | Captioning |
| Many-to-many | Sequence | Sequence | Translation |

**Exam Tip:** Sentiment = many-to-one. Translation = many-to-many (not synced step-by-step in basic form).

> **RNN patterns** = Case shapes — many-to-one, one-to-many, many-to-many.

---

## Vanishing and Exploding Gradients — The Broken Telephone

**The Story:** Training an RNN is the telephone game — gradients multiply through time steps. If each multiplier $< 1$, the signal vanishes ($0.9^{100} \approx 0$). If $> 1$, it explodes ($1.1^{100} \approx 13{,}780$). Long sequences forget early evidence.

$$\frac{\partial \mathcal{L}}{\partial H_0} = \frac{\partial \mathcal{L}}{\partial H_T} \prod_{t=1}^{T} \frac{\partial H_t}{\partial H_{t-1}}$$

**Gradient clipping** caps exploding gradients: $\mathbf{g} \leftarrow \frac{\text{threshold}}{\|\mathbf{g}\|} \cdot \mathbf{g}$ if $\|\mathbf{g}\| > \text{threshold}$. Clipping fixes exploding, not vanishing.

**Exam Tip:** Clipping fixes exploding, not vanishing. Solution for vanishing = LSTM/GRU gates.

> **Vanishing gradients** = Broken telephone — gradients fade or explode across time steps.

---

## LSTM Networks — The Gated Memory Chip

**The Story:** LSTM detectives carry two notebooks: **cell state** $C_t$ (long-term memory) and **hidden state** $H_t$ (working memory). Three gates control flow:

$$f_t = \sigma(W_f \cdot [H_{t-1}, X_t] + b_f) \quad \text{(forget gate)}$$
$$i_t = \sigma(W_i \cdot [H_{t-1}, X_t] + b_i) \quad \text{(input gate)}$$
$$\tilde{C}_t = \tanh(W_C \cdot [H_{t-1}, X_t] + b_C) \quad \text{(candidate)}$$
$$o_t = \sigma(W_o \cdot [H_{t-1}, X_t] + b_o) \quad \text{(output gate)}$$
$$H_t = o_t \odot \tanh(C_t)$$

Forget gate uses sigmoid; cell update uses tanh. Three gates: forget, input, output.

**Exam Tip:** $C_t$ = long-term, $H_t$ = short-term. Forget gate = sigmoid, not tanh. Three gates, not two.

> **LSTM** = Gated memory chip — cell state with forget, input, output gates.

---

## GRU — The Lean Memory Unit

**The Story:** GRU is LSTM's leaner sibling — no separate cell state, only two gates. **Update gate** $z_t$ decides how much past memory to keep. **Reset gate** $r_t$ decides how much past to forget when computing new candidate.

$$z_t = \sigma(W_z \cdot [H_{t-1}, X_t]) \quad \text{(update gate)}$$
$$r_t = \sigma(W_r \cdot [H_{t-1}, X_t]) \quad \text{(reset gate)}$$
$$H_t = (1 - z_t) \odot H_{t-1} + z_t \odot \tilde{H}_t$$

Fewer parameters, often comparable performance on smaller datasets.

**Exam Tip:** No separate cell state. Two gates (update, reset), not three. Often matches LSTM on smaller data.

> **GRU** = Lean memory unit — two gates, no separate cell state.

---

# PART 9: THE SPOTLIGHT TEAM (Week 8)

## From Sequential Models to Transformers — Breaking the Sequential Bottleneck

**The Story:** RNN detectives process evidence one piece at a time — slow, hard to parallelise, and LSTMs still struggle with very long sequences. The Spotlight Team processes **all tokens simultaneously** via self-attention. Parallel batching across sequences ≠ within-sequence parallelism. Positional information must still be injected explicitly.

**Exam Tip:** LSTMs don't solve all long-sequence problems. Transformers enable within-sequence parallelism. Positional encoding is mandatory.

> **Transformer motivation** = Spotlight team replaces sequential notebook — all tokens at once.

---

## Attention Is All You Need — The 2017 Breakthrough

**The Story:** Before 2017, attention was an add-on to seq2seq models. The landmark paper made attention the entire architecture — no RNN needed. GPT is a decoder-only Transformer, not an LSTM. The original Transformer has both encoder and decoder stacks. Attention existed before 2017 but was not the core.

**Exam Tip:** GPT = decoder-only Transformer. Original Transformer = encoder + decoder. Attention predates 2017 but became central in Transformers.

> **Attention paper** = 2017 breakthrough — attention replaces recurrence entirely.

---

## Transformer Architecture — The Spotlight Network

**The Story:** Every token shines a spotlight on every other token. **Self-attention** computes relevance scores; high scores dominate the final representation. Coreference (*it* → *animal*) is the canonical example. The attention equation:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

| Symbol | Role |
|--------|------|
| $Q$ (Query) | "What am I looking for?" |
| $K$ (Key) | "What do I contain?" |
| $V$ (Value) | "What information do I pass?" |

**Multi-head attention** runs parallel specialised heads (syntax, semantics, coreference). **Positional encoding** (sin/cos waves) injects word order — without it, parallel processing loses sequence information.

**Exam Tip:** Don't omit $\sqrt{d_k}$. Encoder self-attention is bidirectional; decoder uses masking. Positional encoding is mandatory.

> **Transformer** = Spotlight network — every token attends to every other token.

---

## Transformer Model Families — Three Detective Ranks

**The Story:** One architecture spawns three specialist ranks. **Encoder-only** (BERT, RoBERTa): read and understand — NLU, classification. **Decoder-only** (GPT, Gemini, Llama): generate autoregressively — NLG. **Encoder-decoder** (T5, BART): transform sequences — translation, summarisation.

| Family | Examples | Best for |
|--------|----------|----------|
| Encoder-only | BERT, RoBERTa | NLU, classification |
| Decoder-only | GPT, Gemini | NLG, chat |
| Encoder-decoder | T5, BART | Seq2seq tasks |

**Exam Tip:** GPT for NER lacks left context in generation mode. BERT cannot generate paragraphs. T5/BART need both halves.

> **Transformer families** = Three ranks — encoders read, decoders write, both transform.

---

## Hugging Face Hub — The Detective Supply Depot

**The Story:** Hugging Face is the agency's supply depot — pretrained models, datasets, tokenisers, and pipelines in one hub. Every model has a **model card** with license, bias notes, and limitations. Check commercial license before production. Not NLP-only — vision and audio models too.

**Exam Tip:** Check license for commercial use. Read bias/limitations on model cards. Hugging Face covers multiple ML domains.

> **Hugging Face** = Supply depot — models, tokenisers, pipelines, model cards.

---

## Hugging Face Token and Model Implementation — Field Deployment

**The Story:** Access tokens authenticate API calls — never hardcode `hf_` tokens in notebooks committed to git. Tokeniser must match model checkpoint exactly. `truncation=True` for 512-token BERT limit. Pipeline task must match architecture (classification pipeline on BERT, not GPT).

**Exam Tip:** Never commit tokens. Match tokeniser to checkpoint. `truncation=True` for length limits. Task must match architecture.

> **HF implementation** = Field deployment — tokens, matching tokenisers, truncation.

---

# PART 10: SENIOR DETECTIVE BERT (Week 9)

## BERT and Contextual Embeddings — The Senior Analyst

**The Story:** Junior detectives (Word2Vec) assign one identity per word. **Senior Detective BERT** re-evaluates every word in context — *bank* gets different vectors in "river bank" vs "bank account." BERT is encoder-only Transformer, not GPT. Fine-tuning starts from pretrained weights, not from scratch.

**Exam Tip:** BERT embeddings are contextual. BERT ≠ GPT (encoder vs decoder). Fine-tuning uses pretrained weights.

> **BERT introduction** = Senior analyst — contextual embeddings from encoder-only Transformer.

---

## BERT Architecture and Pre-Training — Two Training Drills

**The Story:** BERT trains on two self-supervised drills. **MLM (Masked Language Modelling):** hide ~15% of tokens, predict using bidirectional context — both left and right neighbours. **NSP (Next Sentence Prediction):** given sentences A and B, predict if B truly follows A. Input format: `[CLS] sentence_A [SEP] sentence_B [SEP]`.

| Task | What it teaches |
|------|----------------|
| MLM | Token meaning from full context |
| NSP | Sentence-pair coherence |

BERT-base = 12 layers, 768 dims. BERT-large = 24 layers. RoBERTa later removed NSP.

**Exam Tip:** MLM is bidirectional; GPT is left-to-right only. BERT-base = 12 layers, not 24. RoBERTa dropped NSP.

> **BERT pre-training** = Two drills — MLM (bidirectional fill-in) and NSP (sentence pairs).

---

## BERT Applications — Case Specialisations

**The Story:** Senior Detective BERT excels at understanding tasks: sentiment classification (using `[CLS]` token), NER (with subword merging), extractive QA (span prediction), and natural language inference. BERT is not for open-ended generation — that's the press office's job (GPT).

**Exam Tip:** BERT not for open-ended generation. Subword tokens need merging for NER spans. QA is extractive, not generative.

> **BERT applications** = Understanding specialist — sentiment, NER, QA, NLI.

---

## BERT Variants — Specialised Units

**The Story:** The agency deploys specialised BERT units. **RoBERTa:** more data, no NSP, better training recipe. **ALBERT:** parameter sharing for efficiency. **DistilBERT:** ~40% smaller, ~60% faster, ~97% of BERT performance via knowledge distillation. **Domain fine-tunes:** BioBERT, FinBERT for specialised corpora.

**Exam Tip:** RoBERTa changes training, not architecture entirely. Distillation ≠ fine-tuning. Domain models need domain data.

> **BERT variants** = Specialised units — RoBERTa, ALBERT, DistilBERT, domain fine-tunes.

---

# PART 11: MOOD ANALYSIS DIVISION (Week 10)

## Text Classification Overview — Sorting the Case Files

**The Story:** The Mood Analysis Division sorts incoming case files into categories: $y \in \{c_1, c_2, \ldots, c_k\}$ — mapping text $x$ to label $y$. Sentiment is one type of text classification. Class imbalance makes accuracy misleading; use precision, recall, F1. Topic modelling discovers themes; topic labelling assigns names — different jobs.

**Exam Tip:** Sentiment is text classification. Class imbalance distorts accuracy. Topic modelling ≠ topic labelling.

> **Text classification** = Sort case files — map text to discrete category labels.

---

## Sentiment Analysis — Reading the Room

**The Story:** Sentiment analysis reads emotional tone at three levels: **document** (whole review), **sentence** (one statement), **aspect-based** (ABSA — sentiment toward a specific feature). Labels: positive, negative, neutral. Traps abound: *"not bad"* is positive, sarcasm breaks rules, *long* is context-dependent. Subjectivity (opinion vs fact) ≠ polarity (positive vs negative).

**Exam Tip:** "Not bad" = positive. Sarcasm breaks rule-based systems. Subjectivity ≠ polarity.

> **Sentiment analysis** = Reading the room — document, sentence, or aspect-level tone.

---

## Sentiment Implementations — VADER, BERT, Flair, spaCy

**The Story:** Four mood-readers, four philosophies. **VADER**: rule/lexicon, compound score $\in [-1, 1]$, thresholds at $\pm 0.05$ — fast, explainable, social-media tuned. **BERT**: contextual deep learning via Hugging Face pipeline — accurate on complex language, 512 token limit. **Flair**: neural tagger with `Sentence` + `predict()`. **spaCy/TextBlob**: pattern-based polarity $[-1, 1]$ and subjectivity $[0, 1]$.

Contrast: *"I usually hate waiting, but this was worth it"* → VADER: neutral; BERT/Flair: positive; TextBlob: negative.

**Exam Tip:** Use VADER `compound`, not `pos` alone. BERT needs `truncation=True`. Flair requires `predict()`.

> **Sentiment tools** = Four mood-readers — VADER (rules), BERT (context), Flair (neural), TextBlob (patterns).

---

## Comparing Sentiment Approaches — Choosing the Mood Reader

**The Story:** Use **VADER** when speed, cost, and explainability matter — social media, real-time dashboards. Use **BERT** when accuracy on complex language matters — negation, contrast, domain nuance. BERT is not always better; regulated industries may require explainable VADER scores. Black-box constraints are a real production concern.

**Exam Tip:** BERT not always better. VADER is ML-adjacent, not "non-computational." Match tool to constraints.

> **Sentiment comparison** = Match mood-reader to case — speed vs accuracy vs explainability.

---

# PART 12: THEME CLUSTERING UNIT (Week 11)

## Introduction to Topic Modelling — Finding Hidden Themes

**The Story:** The Theme Clustering Unit discovers hidden themes in unsorted case archives — no labels needed. A **topic** is a probability distribution over words; a **document** is a mixture of topics. Topic modelling ≠ classification. Documents are mixtures, not single assignments. Word order is ignored (bag-of-words assumption).

**Exam Tip:** Topic modelling is unsupervised. Documents are mixtures, not single-topic. Word order ignored.

> **Topic modelling** = Theme clustering — discover hidden topics as word distributions.

---

## Latent Dirichlet Allocation — The Probabilistic Theme Finder

**The Story:** **LDA** is the classic theme finder. Two core ideas: (1) documents are **mixtures** of topics — a tech-health article might be 70% technology, 30% healthcare; (2) topics are **distributions over words** — technology weights *software*, *algorithm*; healthcare weights *patient*, *treatment*. Output is proportions like $(0.70, 0.30)$, not a single label. Number of topics $K$ must be set manually.

**Exam Tip:** LDA assigns proportions, not one topic per document. $K$ is manual. Topics are unlabelled — interpret via top words.

> **LDA** = Probabilistic theme finder — documents as topic mixtures.

---

## Key Assumptions of LDA — The Rulebook

**The Story:** LDA detectives follow strict rules: bag-of-words input (no word order), documents are mixtures of topics, topics are distributions over words, fixed $K$ topics, and **exchangeability** (word order doesn't matter). Short text (tweets) violates the mixture assumption. Unsupervised ≠ no preprocessing — stopword removal is critical.

**Exam Tip:** No context preserved. Short text violates assumptions. Unsupervised still needs preprocessing.

> **LDA assumptions** = Strict rulebook — bag-of-words, mixtures, fixed K, no word order.

---

## LDA Implementation — Running the Theme Finder

**The Story:** Gensim pipeline: preprocess (tokenise, remove stopwords) → build BoW dictionary → `LdaModel(corpus, num_topics=K)`. Inspect top words per topic for interpretation. Proportions are not classification probabilities — they are topic mixture weights.

**Exam Tip:** Set `num_topics=K` explicitly. Proportions ≠ classification probabilities. Stopword removal critical.

> **LDA implementation** = Run the theme finder — Gensim, BoW dictionary, tune K.

---

## Why Alternatives to LDA Are Needed — When Classic Fails

**The Story:** LDA hits a ceiling: no semantic understanding (*car* ≠ *automobile*), poor on short text (tweets), manual $K$ tuning, incoherent topics on sparse data. Alternatives: **GSDMM** for short text (one-topic-per-document assumption), **BERTopic** for semantic clustering.

**Exam Tip:** LDA fails on short text and lacks semantics. Know when to switch to GSDMM or BERTopic.

> **LDA limitations** = Classic theme finder hits ceiling — short text, no semantics, manual K.

---

## BERTopic — Semantic Theme Clustering

**The Story:** BERTopic is not "LDA with BERT." Pipeline: embed documents (sentence transformer) → **UMAP** dimensionality reduction → **HDBSCAN** clustering (no preset $K$) → **c-TF-IDF** for interpretable topic words → optional MMR for diversity. Embedding model choice matters significantly.

**Exam Tip:** Not "LDA with BERT." c-TF-IDF uses IDF per cluster, not global. HDBSCAN discovers topic count.

> **BERTopic** = Semantic theme clustering — embed, cluster, extract words.

---

## BERTopic Architecture — Five-Stage Pipeline

**The Story:** The full BERTopic pipeline has five stages: (1) sentence embeddings, (2) UMAP reduction (non-linear, preserves local structure), (3) HDBSCAN clustering (automatic $K$), (4) c-TF-IDF topic representation (cluster-level IDF), (5) optional MMR for diverse topic words. UMAP vs PCA: UMAP is non-linear and better for clustering.

**Exam Tip:** Five stages, not three. HDBSCAN discovers topic count automatically. UMAP is non-linear.

> **BERTopic architecture** = Five-stage pipeline — embed, UMAP, HDBSCAN, c-TF-IDF, MMR.

---

## GSDMM for Short Text — The Tweet Specialist

**The Story:** **GSDMM** (Gibbs Sampling Dirichlet Multinomial Mixture) assumes **one topic per document** — perfect for short text like tweets where LDA's mixture assumption fails. Uses Gibbs sampling with hyperparameters $\alpha$ and $\beta$. Stemming helps on short text. Choose GSDMM over LDA when documents are very short.

**Exam Tip:** GSDMM for tweets, not LDA. One-topic-per-document vs mixture is the key difference. Stemming helps.

> **GSDMM** = Tweet specialist — one topic per short document via Gibbs sampling.

---

# PART 13: THE PRESS OFFICE (Week 12)

## Why Decoder-Only Models Dominate NLG — The Press Release Machine

**The Story:** The press office writes fluent releases one word at a time: $P(t_n \mid t_1, t_2, \ldots, t_{n-1})$. **Decoder-only** models (GPT, Gemini) excel because autoregressive generation is their native training objective. BERT cannot write press releases — it reads, not writes. No planning ahead — each token conditions on all prior tokens.

**Exam Tip:** BERT not for open-ended NLG. Autoregressive = one token at a time. Decoder-only dominates generation.

> **Decoder-only NLG** = Press release machine — autoregressive, one token at a time.

---

## What Is a Large Language Model? — The Senior Press Officer

**The Story:** An **LLM** is a neural network with billions of parameters ($10^9$+) pretrained on massive text via self-supervised next-token prediction — no labels needed for pre-training. **Fine-tuning** adapts to labelled tasks afterward. No fixed parameter threshold defines "large" — scale, data, and capability matter.

**Exam Tip:** No fixed parameter cutoff for "large." Pre-training is self-supervised (no labels). Fine-tuning uses labelled data.

> **LLM** = Senior press officer — billions of parameters, pretrained on next-token prediction.

---

## Why LLMs Excel at NLG — Pattern Mastery

**The Story:** LLMs excel at NLG because they model $P(\text{token} \mid \text{context})$ over vast training data — learning grammar, style, facts, and reasoning patterns statistically. But they mimic patterns, not true reasoning. Prompt quality shapes output. Without RAG, they don't retrieve — they generate. Output is non-deterministic.

**Exam Tip:** Pattern mimicry, not guaranteed reasoning. Prompt quality matters. Fluency ≠ accuracy.

> **LLM NLG strength** = Pattern mastery — statistical fluency from massive pre-training.

---

## Natural Language Generation — From Templates to Probabilistic Writing

**The Story:** **NLG** transforms structured data into human-readable text. Two paradigms: **deterministic** (templates, mail-merge) and **probabilistic** (LLMs sampling from learned distributions). The **prompt** is the control mechanism — it steers the LLM without changing weights. Prompts must be domain-adapted; generic prompts produce generic output.

**Exam Tip:** LLMs use statistical patterns, not explicit rules. Prompts must be domain-adapted.

> **NLG** = Probabilistic writing — templates replaced by learned language generation.

---

## How LLMs Generate a Response — The Writing Process

**The Story:** Generation loop: tokenise input → embed tokens → pass through Transformer layers → softmax over vocabulary → sample next token → append and repeat until stop condition. Each token is generated, not retrieved. Single-turn has no memory of prior conversations. Knowledge cutoff limits factual currency. Fluency does not guarantee accuracy.

**Exam Tip:** Generated, not retrieved. No cross-turn memory in single-turn. Knowledge cutoff applies. Fluency ≠ accuracy.

> **LLM generation** = Writing loop — tokenise, embed, predict, sample, repeat.

---

## Controlling LLM Output — The Editor's Knobs

**The Story:** The editor controls output via decoding strategies. **Temperature** $T$ scales logits before softmax:

$$P(token_i) = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}$$

Low $T$ (0–0.3) = deterministic, factual. High $T$ (0.7–1.0) = creative, risky. **Top-K**: keep $K$ highest-probability tokens. **Top-P (nucleus)**: keep smallest set whose cumulative probability exceeds $p$ — adapts dynamically.

**Exam Tip:** Top-K ≠ Top-P. High temperature causes hallucination on factual tasks. $T > 1$ incoherent in production.

> **Decoding strategies** = Editor's knobs — temperature, Top-K, Top-P control randomness.

---

## Choosing the Right Decoding Strategy — Match Settings to Task

**The Story:** No universal best settings. Code/JSON extraction: low temperature (0–0.3), Top-P. Creative writing: medium-high temperature, Top-P. Factual Q&A: low temperature, greedy or low Top-P. High temperature breaks JSON structure. Top-P is the industrial default for flexibility.

| Task | Temperature | Strategy |
|------|-------------|----------|
| Code/JSON | 0–0.3 | Top-P |
| Creative | 0.7–1.0 | Top-P |
| Factual Q&A | Low | Greedy or low Top-P |

**Exam Tip:** No universal settings. High temperature breaks structured output. Top-P is production default.

> **Decoding selection** = Match editor settings to task — factual needs low T, creative needs high T.

---

## Prompts and Prompt Engineering — The Briefing Document

**The Story:** A **prompt** is the briefing document sent to the press officer. Core components: **role** (who you are), **instruction** (what to do), **context/input** (the evidence), **output format** (JSON, bullets, prose), **constraints** (length, tone), and **examples** (shots). Role ≠ instruction. Bigger model does not eliminate need for good prompts.

**Exam Tip:** Role ≠ instruction. Specify output format explicitly. Good prompts required even for large models.

> **Prompt engineering** = Briefing document — role, instruction, context, format, constraints, examples.

---

## Zero-Shot, One-Shot, and Few-Shot Prompting — Example Count

**The Story:** **Zero-shot**: no examples, just instruction. **One-shot**: one example in the prompt. **Few-shot**: several examples. "Shot" = example demonstrations, not conversation turns. Few-shot improves output format adherence but not guaranteed accuracy. Zero-shot weak for strict JSON schemas. Too many shots waste context window.

**Exam Tip:** Shot = examples, not turns. Few-shot helps format, not always accuracy. Zero-shot weak for strict JSON.

> **Shot prompting** = Example count — zero, one, or few demonstrations in the briefing.

---

## Practical Prompt Engineering Guidelines — The Editor's Playbook

**The Story:** Prompting is experimental — iterate, test edge cases, state constraints explicitly. Balance creativity vs constraints. Unstated constraints are ignored. One-time prompt design fails in production. Document what works and what breaks.

**Exam Tip:** Iterate and test edge cases. Unstated constraints are ignored. Prompting is experimental, not one-shot design.

> **Prompt guidelines** = Editor's playbook — iterate, constrain, test edge cases.

---

## Google AI Studio Playground — The Testing Desk

**The Story:** Google AI Studio is the testing desk for Gemini models — experiment with prompts before API integration. Watch knowledge cutoff dates. Temperature above 1.0 produces incoherent output. System instructions vs user messages serve different roles. API billing applies beyond free tier.

**Exam Tip:** Knowledge cutoff limits facts. Temperature > 1 incoherent. System vs user instruction roles differ.

> **Google AI Studio** = Testing desk — experiment with Gemini prompts before deployment.

---

## LLM API Setup — Gemini and OpenAI Keys

**The Story:** API keys authenticate calls — never commit keys to git. Use `.env` files and `.gitignore`. OpenAI keys shown once at creation — store immediately. Gemini requires `genai.Client(api_key=...)`. ChatGPT app subscription ≠ API access — separate products.

**Exam Tip:** Never commit API keys. `.env` + `.gitignore`. OpenAI key shown once. ChatGPT app ≠ API.

> **API setup** = Secure the keys — .env files, never commit, separate products.

---

# PART 14: CAPSTONE CASE — QUIZGENIUS (Week 13)

## QuizGenius Capstone Project Overview — The Final Case

**The Story:** The capstone case: build **QuizGenius AI** — a quiz generator powered by Gemini API, Python backend, Streamlit frontend, JSON quiz schema. No hardcoded keys. Parse structured JSON, not free text. LLM-generated answers may be wrong — validate. Notebook proof-of-concept ≠ production application.

**Stack:** Gemini API, Python backend, Streamlit frontend, JSON schema.

**Exam Tip:** No hardcoded keys. Parse JSON, not free text. LLM answers need validation. Notebook ≠ production.

> **QuizGenius overview** = Final case — LLM-powered quiz generator with structured JSON output.

---

## Package Installation and API Setup — Equipping the Team

**The Story:** Install dependencies from `requirements.txt`. Store API keys in Colab Secrets or `.env` — never in notebook cells. Validate key before API calls. Use Flash models for demos to control cost and latency.

**Exam Tip:** Colab Secrets, not notebook cells. Validate key first. Flash models for demos.

> **Project setup** = Equip the team — requirements, secrets, key validation.

---

## Quiz Prompt Template Design — The Quiz Briefing

**The Story:** The prompt template is the briefing for quiz generation. Requirements: raw JSON only (no markdown fences), schema with `questions`, `options`, `correct_option`, placeholders for topic. Include a schema example in the prompt. Vague option format produces inconsistent output.

**Exam Tip:** Specify JSON schema in prompt. No markdown fences. Use placeholders for dynamic topic.

> **Prompt template** = Quiz briefing — JSON schema, options format, topic placeholder.

---

## Quiz Generation Logic and Application Runner — The Engine Room

**The Story:** The engine room: `generate_quiz()` calls Gemini with `response_mime_type="application/json"`, extracts JSON via regex if needed, validates schema, checks answers case-insensitively. Handle `JSONDecodeError`. Use dynamic `len(questions)`, not hardcoded count. Key naming: `correct_option` must match schema exactly.

**Exam Tip:** Handle JSON parse errors. `correct_option` key naming matters. Dynamic question count.

> **Quiz generation logic** = Engine room — API call, JSON parse, schema validation, scoring.

---

## Application Architecture — The Agency Floor Plan

**The Story:** User flow: User → Streamlit frontend → Backend (`quiz_engine.py`) → Gemini API → JSON response → UI scoring. LLM is external — not inside the backend box. Backend mediates API to protect keys. Session state preserves data across multi-screen flow (v1 notebook → v2 full-stack).

**Exam Tip:** LLM is external service. Backend protects API keys. Session state for multi-screen apps.

> **App architecture** = Agency floor plan — frontend, backend, external LLM, session state.

---

## Project Setup and Repository Structure — Filing the Case

**The Story:** Repository structure: `app.py` (frontend), `quiz_engine.py` (backend), `.env` (secrets), `requirements.txt`, `.gitignore`. Never commit `.env`. Avoid monolithic single-file apps. Separate concerns for maintainability.

**Exam Tip:** Never commit `.env`. Include `requirements.txt`. Separate frontend and backend files.

> **Repository structure** = Filing the case — app.py, quiz_engine.py, .env, requirements.txt.

---

## Streamlit Frontend — The Client Desk

**The Story:** Streamlit builds the client-facing desk. Key APIs: `st.session_state` preserves quiz state across reruns, `st.rerun()` refreshes after submission, dynamic question rendering from JSON. Launch with `streamlit run app.py`, not `python app.py`.

**Exam Tip:** Data lost without session state. Use `streamlit run app.py`, not `python app.py`.

> **Streamlit frontend** = Client desk — session state, dynamic rendering, correct launch command.

---

## Running the Full-Stack Application — Opening for Business

**The Story:** Launch checklist: activate virtual environment, ensure `.env` with valid API key, run `streamlit run app.py`, test multiple topics. Verify JSON parsing and scoring across edge cases.

**Exam Tip:** Activate venv. `.env` required. Test multiple topics and edge cases.

> **Running the app** = Opening for business — venv, .env, streamlit run, multi-topic test.

---

## Demo Notebook Quiz Application — The Proof of Concept

**The Story:** The notebook POC validates the core loop before building the full app. Verify LLM-generated answers manually — models hallucinate. Handle JSON parse failures gracefully. CLI notebook demo ≠ user-facing product.

**Exam Tip:** Verify LLM answers manually. Handle JSON failures. POC ≠ production product.

> **Notebook demo** = Proof of concept — validate loop before full-stack build.

---

## From Notebook POC to Full-Stack Application — Leveling Up

**The Story:** Why upgrade beyond the notebook? Product wrapper matters — session state, error handling, clean UI, key protection. Streamlit is sufficient for portfolio projects vs React. The LLM capability is one layer; the application architecture is the deliverable.

**Exam Tip:** Product wrapper matters beyond LLM capability. Streamlit sufficient for portfolio. Architecture is the deliverable.

> **POC to production** = Level up — wrapper, error handling, and architecture matter.

---

## Updated Project Architecture — The Revised Floor Plan

**The Story:** Version 2 architecture adds session state, separated backend, environment-based config, and improved error handling. Update architecture diagrams after implementation changes. Include `.env` and session state in documentation — they are not optional extras.

**Exam Tip:** Update diagrams after implementation. Document `.env` and session state in architecture.

> **Updated architecture** = Revised floor plan — v2 adds session state and separated concerns.

---

## Implementation Overview and Integration — Closing the Case

**The Story:** Integration summary: prompt template → generation logic → JSON validation → Streamlit UI → scoring. Cross-cutting patterns: never hardcode keys, always validate LLM output, handle errors at every layer. Stopping at notebook POC misses the production lessons — error handling and validation are the examinable architecture skills.

**Exam Tip:** Don't stop at notebook POC. Error handling and validation at every layer. Integration patterns are examinable.

> **Integration summary** = Closing the case — prompt, generate, validate, display, score.

---

# ONE-LINE SUMMARIES — The Complete Set

> **Course Overview** = Agency charter: NLP turns unstructured language into structured signals.
> **NLP Module Introduction** = First briefing — language is complex evidence requiring structured pipelines.
> **NLP** = Core mission: bridge human communication and machine computation.
> **NLU / NLG** = Analysis wing vs press office inside the NLP building.
> **NLP Applications** = Case files across search, voice, email, keyboards, chatbots.
> **Morphology** = Forensic word dissection — roots, affixes, stems, lemmas.
> **Polysemy / Synonymy** = Red herrings — one word many meanings, many words one meaning.
> **Preprocessing** = Crime-scene cleaning without destroying evidence.
> **Tokenisation** = Bagging evidence into processable units.
> **Regex cleaning** = Fine brush for precise noise removal.
> **Stopwords** = Common footprints to filter when they add no clue.
> **Stemming / Lemmatisation** = Rough chop vs dictionary lookup for word forms.
> **Preprocessing pipeline** = Standard operating procedure — order matters.
> **Structural analysis** = Tagging division for POS and NER.
> **POS tagging** = Grammatical role labels — context-dependent.
> **POS in practice** = spaCy for speed, Flair for accuracy.
> **Dependency trees** = Evidence board for syntax and entities.
> **NER** = Suspect identification — persons, orgs, locations.
> **NER in practice** = spaCy for production, Flair for accuracy.
> **Tool comparison** = Trainee (NLTK) vs field agent (spaCy) vs specialist (Flair).
> **Corpus linguistics** = Evidence vault shaping every model.
> **Text corpus** = Case archive whose statistics define behaviour.
> **Corpus types** = General, domain, annotated, task-specific filing.
> **Corpus bias** = Skewed archives produce skewed models.
> **Corpus exploration** = Survey types, tokens, frequency, genre.
> **Word representations** = Scoring lab — words to numbers.
> **One-hot encoding** = Identity badge — one slot per word.
> **One-hot implementation** = Vocabulary index lookup, watch case sensitivity.
> **One-hot trade-offs** = Simple but sparse, high-dimensional, no semantics.
> **Bag of Words** = Evidence count — frequencies, order discarded.
> **BoW implementation** = CountVectorizer, fit on train only.
> **BoW trade-offs** = Fast baseline, blind to order and negation.
> **TF-IDF** = Rarity-weighted clues — local frequency × global rarity.
> **TF-IDF implementation** = TfidfVectorizer sparse float matrix.
> **TF-IDF trade-offs** = Best sparse scorer, still no semantics.
> **Dense embeddings** = Semantic maps in continuous space.
> **Word2Vec** = Prediction game — CBOW fills blanks, Skip-gram predicts neighbours.
> **Word2Vec implementation** = Gensim on tokenised sentences.
> **GloVe** = Global co-occurrence matrix factorisation.
> **GloVe implementation** = Load pretrained vectors, handle OOV.
> **Embedding visualisation** = PCA/t-SNE for intuition, cosine for truth.
> **Static vs contextual** = Fixed map vs GPS recalculating per sentence.
> **Sequential modelling** = Language is ordered, not a bag.
> **Seq2Seq** = Encoder compresses, decoder generates.
> **RNN** = Memory notebook updated each time step.
> **RNN patterns** = Many-to-one, one-to-many, many-to-many shapes.
> **Vanishing gradients** = Broken telephone — gradients fade or explode.
> **LSTM** = Gated memory chip with forget, input, output gates.
> **GRU** = Lean memory — two gates, no cell state.
> **Transformer motivation** = Spotlight team replaces sequential processing.
> **Attention paper** = 2017 — attention replaces recurrence.
> **Transformer** = Every token attends to every other token.
> **Transformer families** = Encoders read, decoders write, both transform.
> **Hugging Face** = Supply depot for models and pipelines.
> **HF implementation** = Tokens, matching tokenisers, truncation.
> **BERT introduction** = Senior analyst with contextual embeddings.
> **BERT pre-training** = MLM (bidirectional) + NSP (sentence pairs).
> **BERT applications** = Sentiment, NER, QA, NLI — not generation.
> **BERT variants** = RoBERTa, ALBERT, DistilBERT, domain fine-tunes.
> **Text classification** = Sort case files into category labels.
> **Sentiment analysis** = Read tone at document, sentence, or aspect level.
> **Sentiment tools** = VADER (rules), BERT (context), Flair, TextBlob.
> **Sentiment comparison** = Match tool to speed, accuracy, explainability.
> **Topic modelling** = Discover hidden themes as word distributions.
> **LDA** = Documents as topic mixtures, topics as word distributions.
> **LDA assumptions** = Bag-of-words, mixtures, fixed K, no word order.
> **LDA implementation** = Gensim pipeline with BoW dictionary.
> **LDA limitations** = No semantics, poor on short text, manual K.
> **BERTopic** = Embed, UMAP, HDBSCAN, c-TF-IDF pipeline.
> **BERTopic architecture** = Five stages with automatic topic count.
> **GSDMM** = One topic per short document via Gibbs sampling.
> **Decoder-only NLG** = Press release machine — autoregressive generation.
> **LLM** = Billions of parameters, next-token pre-training.
> **LLM NLG strength** = Statistical fluency from massive pre-training.
> **NLG** = Probabilistic writing steered by prompts.
> **LLM generation** = Tokenise, embed, predict, sample, repeat.
> **Decoding strategies** = Temperature, Top-K, Top-P control randomness.
> **Decoding selection** = Low T for facts, high T for creativity.
> **Prompt engineering** = Briefing with role, instruction, format, examples.
> **Shot prompting** = Zero, one, or few examples in the briefing.
> **Prompt guidelines** = Iterate, constrain, test edge cases.
> **Google AI Studio** = Testing desk for Gemini prompts.
> **API setup** = Secure keys in .env, never commit.
> **QuizGenius overview** = LLM quiz generator with JSON schema.
> **Project setup** = Requirements, secrets, key validation.
> **Prompt template** = JSON schema briefing for quiz generation.
> **Quiz generation logic** = API call, JSON parse, validation, scoring.
> **App architecture** = Frontend, backend, external LLM, session state.
> **Repository structure** = app.py, quiz_engine.py, .env, requirements.txt.
> **Streamlit frontend** = Session state, dynamic rendering, streamlit run.
> **Running the app** = venv, .env, multi-topic testing.
> **Notebook demo** = POC before full-stack build.
> **POC to production** = Wrapper and architecture matter beyond LLM.
> **Updated architecture** = v2 with session state and separated backend.
> **Integration summary** = Prompt, generate, validate, display, score.

---

*Last compiled: 2026-08-01 | BITS Pilani — NLP and Understanding*
