# Demo: Notebook Quiz Application

## Running the POC

The notebook proof-of-concept runs with a single function call:

```python
run_quiz_app()
```

The terminal prompts for a topic, generates a quiz via Gemini, and runs the interactive question loop.

---

## Demo Walkthrough: Mathematics

```
What topic do you want to be quizzed on? mathematics
Generating a quiz on topic: mathematics

Math Master's Challenge

Q1: What is the value of the integral of ...?
Your answer: D
Wrong. The answer was A. [explanation]

Q2: If matrix A has eigenvalues 1, 2, 3, ...?
Your answer: B
Correct! [explanation]

Q3: [question text]
Your answer: [option]
Correct!

Final score: 2/3
Good job! Keep studying.
```

---

## Demo Walkthrough: Science

```
What topic do you want to be quizzed on? science

The Intermediate Science Challenge
[3 questions with answers and feedback]

Final score: 1/3
Good job! Keep studying.
```

---

## What the Demo Validates

| Capability | Evidence |
|------------|----------|
| Dynamic topic handling | Different subjects produce different quizzes |
| LLM-generated titles | "Math Master's Challenge", "Intermediate Science Challenge" |
| JSON parsing | Questions, options, and answers render correctly |
| Scoring logic | Correct/incorrect tracking with final ratio |
| Explanations | Shown after each answer |
| Real-time interaction | Input → generation → quiz → feedback in one session |

---

## Known Limitations

- **Factual accuracy not guaranteed** — LLM-generated questions may contain errors
- **Single-turn only** — no conversation memory between runs
- **CLI only** — requires Python familiarity to interact
- **No input validation** — notebook POC accepts any topic string

These limitations motivate the full-stack upgrade with validation, UI, and disclaimers.

---

## Next Steps After Demo

1. Experiment with different topics (cloud computing, NLP, history)
2. Modify prompt template (difficulty, question count)
3. Adapt the template to your own project idea
4. Proceed to full-stack Streamlit implementation

---

## Common Pitfalls / Exam Traps

- **Assuming LLM-generated answers are always correct** — verify critical content; add disclaimers in production.
- **Not testing multiple topics** — single-topic success does not prove robustness.
- **Ignoring JSON parse failures** — some topics may cause malformed output; handle gracefully.
- **Treating CLI demo as user-facing product** — full-stack UI needed for non-technical users.

---

## Quick Revision Summary

- Run `run_quiz_app()` to start the interactive CLI quiz.
- User enters topic; Gemini generates titled MCQ quiz in real time.
- Each question: display options, accept A/B/C/D, show correct/incorrect + explanation.
- Final score: X/Y with motivational message based on performance.
- Demo validates end-to-end: prompt → API → JSON → game loop → scoring.
- LLM content may be factually incorrect — treat as educational demo, not authoritative source.
