# Running the Full-Stack Application

## Launch Command

```bash
conda activate quiz-genius
cd quiz-genius-ai
streamlit run app.py
```

Streamlit starts a local web server (typically `http://localhost:8501`) and opens the browser automatically.

---

## End-to-End Walkthrough

### Screen 1: Setup

| Element | Action |
|---------|--------|
| Topic input | Enter "science" (or any subject) |
| Question slider | Select 3 (or 1–10) |
| Difficulty dropdown | Select easy / intermediate / hard |
| Generate Quiz button | Triggers API call with spinner |

Error case: empty topic → "Please enter a topic to generate a quiz."

### Screen 2: Quiz

- Header: LLM-generated title (e.g., "The Intermediate Science Challenge")
- Caption: "3 questions — select your answers and submit"
- Per question: radio buttons for A, B, C, D
- Submit Answers (primary) | Back (secondary)

### Screen 3: Results

- Score header: "1/3" with emoji
- Percentage and tiered message
- Detailed review per question:
  - Correct: green checkmark
  - Wrong: red cross + correct answer highlighted
  - Explanation for each question
- "Take Another Quiz" → resets to Screen 1

---

## Code-to-UI Mapping

| UI Element | Source in `app.py` |
|------------|-------------------|
| "QuizGenius AI" title | `main()` → `st.title()` |
| "Configure Your Quiz" | `render_setup_form()` → `st.header()` |
| Topic text box | `st.text_input("Topic", placeholder=...)` |
| Question slider | `st.slider()` with MIN/MAX from backend |
| Difficulty dropdown | `st.selectbox()` with VALID_DIFFICULTIES |
| "Generate Quiz!" button | `st.form_submit_button()` with `use_container_width=True` |
| Quiz title (dynamic) | `quiz_data["quiz_title"]` in `render_quiz()` |
| Question text (dynamic) | `f"Q{q['id']}: {q['text']}"` |
| Radio buttons | `st.radio()` with option labels from `q["options"]` |
| Score display | `render_results()` → `st.header(f"{emoji} Score: {score}/{total}")` |

---

## Testing Multiple Topics

Run the app with different topics to verify:

- Dynamic title generation
- Variable question counts via slider
- Difficulty level affecting question complexity
- Consistent JSON parsing across topics
- Score calculation accuracy

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "GEMINI_API_KEY is missing" | Add key to `.env` file |
| Import error for `quiz_engine` | Run from project root directory |
| Streamlit not found | `pip install -r requirements.txt` in activated venv |
| JSON parse failure | Check prompt template; retry with simpler topic |
| Page does not transition | Verify `st.rerun()` called after state update |

---

## Common Pitfalls / Exam Traps

- **Running `python app.py` instead of `streamlit run app.py`** — Streamlit requires its own runner.
- **Not activating virtual environment** — wrong package versions or missing dependencies.
- **Forgetting `.env` file** — backend raises ValueError immediately.
- **Testing only one topic** — edge cases appear with unusual or very long topics.
- **Ignoring container width on buttons** — `use_container_width=True` improves visual layout.

---

## Quick Revision Summary

- Launch: `streamlit run app.py` from project root with venv activated.
- Three screens: setup (form) → quiz (radio buttons) → results (score + review).
- Empty topic shows error; valid topic triggers spinner then quiz display.
- Results show score, percentage, tiered message, and per-question explanations.
- "Take Another Quiz" resets session state to setup.
- Map UI elements to `render_setup_form`, `render_quiz`, `render_results`, and `main()`.
