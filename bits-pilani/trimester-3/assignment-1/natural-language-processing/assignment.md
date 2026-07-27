# Take Home Assignment

## The Evolution of NLP — Comparing Three Eras of Sentiment Analysis

| Field | Detail |
| --- | --- |
| **Course** | Natural Language Processing |
| **Topic** | Text Preprocessing, Sentiment Analysis using Traditional ML, Deep Learning (RNN/LSTM), and Pretrained NLP Models |
| **Total Marks** | 20 |

---

## Objective

The objective of this assignment is to understand how NLP systems process human language by comparing three vastly different paradigms of AI architecture:

1. **Traditional Machine Learning** — statistical patterns
2. **Deep Learning** — sequential memory networks
3. **Pretrained "Off-the-Shelf" Models** — zero-shot inference

---

## About the Assignment

An AI consultancy firm wants to build an automated text analysis tool to process unstructured movie reviews. The engineering team needs to decide whether to:

- build a lightweight statistical model,
- invest compute power into a deep learning model, or
- simply use an existing pretrained open-source model.

To achieve this, you will implement all three pipelines on the exact same dataset and write a technical recommendation based on your findings.

---

## The Dataset

You must use the **NLTK Movie Reviews Dataset** (`nltk.corpus.movie_reviews`). This dataset contains 2,000 movie reviews categorized as either positive or negative.

---

## Pipeline Stages

You will simulate the following architectural flow:

```
NLTK Movie Reviews Data
        ↓
Text Preprocessing & Train/Test Split
        ↓
    ┌───┴───┬───────────────────┐
    ↓       ↓                   ↓
Branch 1  Branch 2            Branch 3
TF-IDF +  PyTorch LSTM/RNN    Pretrained model
Classifier                    (VADER, TextBlob, etc.)
    └───┬───┴───────────────────┘
        ↓
Data Consumption & Evaluation
(Compare accuracy and training times on the Test Set)
```

**Branches:**

- **Branch 1:** Train a Traditional ML Model (TF-IDF + Classifier)
- **Branch 2:** Train a Deep Learning Model (PyTorch LSTM/RNN)
- **Branch 3:** Inference using a Pretrained Model (e.g., NLTK VADER, TextBlob, or any other model of your choice)

---

## Task 1: Data Sourcing & Preprocessing (3 Marks)

Load the NLTK Movie Reviews dataset and prepare it for modeling.

1. Write a text-cleaning and preprocessing function (e.g., lowercasing, noise removal, stop-words removal, removing punctuation/numbers, etc.).
2. Split the data into an **80% Training set** and a **20% Test set**.

> Ensure all pipelines are evaluated on the exact same 20% Test set for a fair comparison.

---

## Task 2: Pipeline 1 — Traditional Machine Learning (4 Marks)

Train a traditional statistical model from scratch.

| Step | Requirement |
| --- | --- |
| **Vectorization** | Convert the text to numbers using Bag-of-Words, TF-IDF, or any other approach of your choice |
| **Modeling** | Train a classifier (e.g., Logistic Regression, Naive Bayes) |
| **Output** | Report accuracy and one more evaluation metric of your choice on the Test set |

---

## Task 3: Pipeline 2 — Deep Learning Approach (5 Marks)

Train a modern sequential deep learning model from scratch.

| Step | Requirement |
| --- | --- |
| **Embeddings** | Map the text to dense vectors using a PyTorch `nn.Embedding` layer |
| **Modeling** | Build and train a PyTorch architecture using an RNN or LSTM layer |
| **Output** | Report accuracy and one more evaluation metric of your choice on the Test set |

---

## Task 4: Pipeline 3 — The Pretrained Model (3 Marks)

Implement sentiment analysis using an existing, pretrained model.

| Step | Requirement |
| --- | --- |
| **Modeling** | Choose a pretrained model such as NLTK VADER (`SentimentIntensityAnalyzer`), TextBlob, a Hugging Face pipeline, or any other model of your choice |
| **Execution** | Do **not** train this model. Pass the Test set reviews through it and convert polarity scores into binary labels (Positive/Negative) |
| **Output** | Report accuracy and one more evaluation metric of your choice on the Test set |

---

## Task 5: Final Analysis (5 Marks)

Present the results as a technical business insight report for the consultancy firm.

### Questions to be answered

1. Compare the evaluation metrics and training times of all three pipelines. Which performed best?
2. Why do you think the Pretrained Model performed the way it did compared to the models you trained from scratch?

   > **Hint:** Think about domain adaptation — what was the pretrained model originally trained on versus what you tested it on?

3. Which evaluation metrics did you select for this task and why?
4. Based on your results, what recommendation would you give the consultancy firm regarding which model to deploy in production?

   > **Hint:** Consider factors such as balancing accuracy and other evaluation metrics, compute cost, training data, development time, performance on out-of-sample data, and others.

---

## Submission Requirements

Submit the following as your solution:

1. A **Jupyter Notebook** (`.ipynb`) containing cleanly commented code for all first four tasks.
2. A **presentation** with your insights and recommendations for the client, ending with answers to the Task 5 questions.

Marks will be awarded for creativity and clarity in your solution.

> **Tip:** Always keep the client in mind while preparing the deliverables.
