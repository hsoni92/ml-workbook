---
name: university-assignment-submission
description: Implements university coursework and project submissions with authentic student voice. Covers notebooks, reports, essays, and code deliverables for MSc/BITS-style assignments. Use when implementing any assignment submission, coursework, lab report, progress report, or when the user asks to avoid AI slop in academic work.
disable-model-invocation: true
---

# University Assignment Submission

Implement university assignments as real student work — clear, correct, and submitted on time — not as polished AI output.

## Before starting

1. **Find the brief** — faculty note, rubric, portal instructions, email, or attached PDF. Read it fully before writing anything.
2. **Find prior work** — earlier weeks, outline, template, or sample submission in the same course folder. Match structure and tone.
3. **Confirm deliverables** — file types, naming, section list, word limits, deadline, upload rules (e.g. no zip).
4. **Confirm environment** — required tools, data paths, `uv`/`pip`, run commands from the project README or makefile.

If anything is unclear in the brief, ask the user once. Do not guess file names or required sections.

## General workflow

Copy and track against the actual brief:

```
- [ ] Read assignment brief + rubric
- [ ] Read prior submissions / template in same course
- [ ] List required sections and deliverables
- [ ] Implement core work (code, analysis, writing)
- [ ] Write explanations tied to actual outputs
- [ ] Cross-check all deliverables against brief
- [ ] Run / execute code; fix errors
- [ ] Final pass: student voice, no AI slop, no emojis
```

Adapt the middle steps to the assignment type — do not force an ML pipeline onto a non-ML task.

## By deliverable type

### Jupyter notebook (`.ipynb`)

- Title cell: course, assignment week/title, your name and roll number, date.
- Follow the section order from the brief or template exactly.
- Alternate code and short markdown — explain what you did and what you saw, not tutorial narration.
- Show outputs: tables, plots, metrics. Evaluators need evidence.
- Use a fixed random seed when reproducibility matters.
- Execute the full notebook before handoff; fix broken cells.

### Word / PDF report (`.docx`, `.pdf`)

- Use the faculty template if one was shared.
- Mirror the notebook or code work — same facts, same numbers. Do not write a separate generic essay.
- Pull values from executed outputs, not from memory.
- Section headings should match the brief, not invented blog-style titles.
- Respect word limits if stated.

### Code-only or script submissions

- Match existing project layout and conventions.
- README or inline comments only where a grader needs context.
- Include how to run (`make`, `uv run`, etc.) if not obvious.

### Written answers (markdown, LaTeX, plain text)

- Answer the question asked — direct first, then supporting detail.
- Use `$...$` for inline math where formulas appear.
- Cite sources in the style the course expects (APA, IEEE, or as stated).

## Student voice (critical)

Faculty can spot generic AI text. This matters more than perfect prose.

### Write like this

- First person where appropriate: "I tried…", "I kept X because…"
- Cite **your actual results**: specific numbers, figure references, metric values
- Mix short and longer sentences; sections do not need equal length
- Note real trade-offs: "I only had time to tune two values", "This did not improve validation F1"
- Tie observations to your work: "see the histogram above", "Table 2 shows…"
- State honest limitations and planned next steps when the brief asks for them
- Match the tone of your earlier submissions in the same course

### Never write like this (AI slop)

Avoid entirely:

- Emojis and decorative symbols
- Openers: "Certainly!", "Great question!", "I'd be happy to help"
- Filler: "delve into", "leverage", "robust", "comprehensive", "it's worth noting", "in today's world", "holistic", "cutting-edge", "game-changer", "dive deep", "landscape", "unlock", "empower", "tapestry", "multifaceted"
- Fake enthusiasm: "I'm excited to explore…", "This fascinating topic…"
- Section openers: "In this section, we will…" on every section
- Generic claims without numbers or evidence
- Perfect parallel bullets with identical grammar in every line
- Passive voice for everything: "It was observed that…"
- Blog headers: "Key Takeaways", "Wrapping Up", "Final Thoughts"
- Empty summaries that repeat the heading
- Superlatives without proof: "thoroughly optimized", "state-of-the-art", "highly accurate"

### Code style

- Practical names; comments only where non-obvious
- No tutorial print statements ("Step 1 complete!")
- Not every cell needs to be production-grade — iterative work is fine
- Follow the language and patterns already used in the course folder

## Quality checks before handoff

1. Every required section and file from the brief is present.
2. File names match the brief exactly.
3. Numbers in reports match notebook or code outputs.
4. Code runs without errors.
5. Formulas use `$...$` inline math where needed.
6. No emojis anywhere.
7. Read-aloud test: rewrite anything that sounds like marketing copy or a chatbot.

## Examples

Good vs bad writing samples and a course-specific ML example: [examples.md](examples.md)

Submission discovery checklist (brief, naming, upload rules): [reference.md](reference.md)
