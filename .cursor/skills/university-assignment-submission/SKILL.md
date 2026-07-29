---
name: university-assignment-submission
description: Implements university coursework and project submissions with authentic student voice. Follows assignment briefs, rubrics, and shared repo context (prior submissions, templates, course folders). Covers notebooks, reports, essays, and code for MSc/BITS-style assignments. Use when doing assignments, coursework, lab reports, progress reports, or when the user asks to avoid AI slop in academic work.
disable-model-invocation: true
---

# University Assignment Submission

Implement university assignments as real student work — clear, correct, and submitted on time — not as polished AI output.

## Non-negotiable rules

1. **No AI slop language** — human-like content always. Write like a student who did the work, not a chatbot or blog post.
2. **No emojis** — nowhere in notebooks, reports, code comments, or presentations.
3. **Follow the assignment carefully** — every task, rubric row, deliverable, and submission rule in the brief. Do not skip, reorder, or substitute unless the brief allows it.
4. **No markers that reveal AI authorship** — this is college coursework. Avoid chatbot phrasing, meta-commentary, placeholder text, overly polished template structure, and any pattern that reads as machine-generated rather than student-written.

## Shared context (read before writing)

Use everything available in the repo and conversation — not just the latest user message.

1. **Target instructions** — `assignment.md`, faculty note, rubric, portal text, or attached PDF in the assignment folder. Read fully before writing anything.
2. **Prior work** — earlier weeks, outline, template, or sample submission in the same course folder. Match structure, naming, and tone.
3. **Student identity** — roll number, name, file naming pattern from prior submissions (e.g. `RollNumber_Name_Week{N}_Notebook.ipynb`).
4. **Project environment** — README, makefile, `uv`/`pip` setup, data paths, required libraries.
5. **Workspace rules** — `.cursor/rules/` (e.g. formula formatting, no emojis).

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

### No AI authorship markers (college submissions)

Graders notice when work does not sound like a student wrote it. Also avoid:

- Meta-commentary: "As per the assignment requirements…", "This section addresses Task 3…", "Below is a comprehensive analysis…"
- Placeholder or scaffold text: `[Insert results here]`, `TODO`, `your name here`, lorem ipsum
- Chatbot narration in code: `# Step 1: Load the dataset as required`, `# Now we will train the model`
- Overly uniform structure — every section same length, same opener, same bullet rhythm
- Claims not backed by your actual notebook outputs or runs
- References to "we" when the brief expects individual work — use "I" where appropriate
- Disclaimers: "Note: results may vary", "This is a simplified example"
- Brand-new jargon or framing not used elsewhere in the course or your prior submissions

### Code style

- Practical names; comments only where non-obvious
- No tutorial print statements ("Step 1 complete!")
- Not every cell needs to be production-grade — iterative work is fine
- Follow the language and patterns already used in the course folder

## Quality checks before handoff

1. Every required section and file from the brief is present.
2. Every rubric criterion is addressed — cross-check the rubric table row by row.
3. File names match the brief exactly.
4. Numbers in reports match notebook or code outputs.
5. Code runs without errors.
6. Formulas use `$...$` inline math where needed.
7. No emojis anywhere.
8. Read-aloud test: rewrite anything that sounds like marketing copy or a chatbot.
9. AI-marker pass: remove meta-commentary, placeholders, and overly polished template phrasing.

## Examples

Good vs bad writing samples and a course-specific ML example: [examples.md](examples.md)

Submission discovery checklist (brief, naming, upload rules): [reference.md](reference.md)
