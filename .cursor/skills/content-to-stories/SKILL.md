---
name: content-to-stories
description: Transforms pointed-out study content (notes, transcripts, concepts, week folders) into memory-first story-based learning documents with vivid analogies, exam tips, and one-line summaries. Use when the user asks to create stories from content, story-based learning, turn notes into stories, or points to specific notes/concepts to memorialize.
disable-model-invocation: true
---

# Content to Stories

Turn technical study content into unforgettable story-based learning. Match the style of existing story docs in this repo.

## Before starting

1. **Read the source content** the user pointed to — notes, transcripts, revision sheets, or a list of concepts.
2. **Check for existing stories** in `{subject}/stories/` — extend or align with them; do not contradict established analogies.
3. **Determine output mode** (see below).
4. **Confirm output path** if the user did not specify one.

## Output modes

### Mode A — Comprehensive document (`Story-Based-Learning.md`)

Use when the user points to a full week map, course outline, or multiple concepts across a subject.

**Output path:**
```
{subject}/stories/Story-Based-Learning.md
```

**Structure:**
1. Title — `{Subject} — Story-Based Learning` plus optional subtitle (course, mental model)
2. Epigraph — one memorable line about why stories beat rote memorization
3. Parts grouped by week/module — `# PART N: {THEME} (Week N)`
4. One `##` section per concept
5. Closing `# ONE-LINE SUMMARIES — The Complete Set` — blockquoted one-liners for every concept
6. Footer — last compiled date and course identifier

### Mode B — Standalone topic story

Use when the user points to one note, one lecture, or one concept cluster.

**Output path:**
```
{subject}/stories/{Topic-Title}.md
```

**Structure:**
1. `# {Topic} — {Story Metaphor Title}`
2. Context block — source note link, topic, date
3. `## The Story` — extended narrative with subsections
4. Technical content woven into the story (formulas, tables, code)
5. Closing summary blockquote and key properties / pitfalls

## Per-concept section template

Every concept gets this shape (adapt depth to complexity):

```markdown
## {Concept Name} — {Short Metaphor Label}

**The Story:** {2–6 sentences. One vivid analogy — factory, bouncer, mountain, assembly line, etc. Map story elements to technical terms explicitly.}

{Optional: comparison table | equations | ASCII diagram | bullet list of mechanics}

**Exam Tip:** {One high-yield exam sentence — geometric insight, common trap, or definition to write verbatim. Omit if nothing exam-specific.}

> **{Concept}** = {single memorable one-liner tying story to formal term}
```

For week-level sections in Mode A, you may also use a story-to-term table:

```markdown
| Story | {Domain} term |
|-------|---------------|
| {analogy fragment} | **{formal term}** |
```

## Story-writing rules

### Do

- **One analogy per concept** — commit to it; do not mix metaphors mid-section.
- **Map explicitly** — name which story element equals which technical term (e.g. "bouncer = neuron", "guest list = weights").
- **Lead with intuition** — story first, then equations and mechanics.
- **Use concrete domains** — restaurants, factories, mountains, sports, driving, clubs, elections. Prefer everyday over abstract.
- **Carry analogies across related concepts** — if Layer 1 is an assembly line, backprop is the quality-control team tracing complaints backward.
- **Include exam tips** where the source material has traps, definitions, or classic MCQ angles.
- **End each concept** with a blockquoted one-liner when it aids recall.
- **Cross-reference** other parts when a story continues elsewhere ("see Part 6 — the blind hiker").

### Don't

- Never add emojis.
- Never reference the lecture, professor, or transcript — write as standalone study material.
- Never use generic AI filler ("imagine a world where learning is fun").
- Never leave a concept as story-only — always anchor back to formal terms, equations, or properties.
- Never shallow-list concepts without a story — if it appears, it gets a metaphor.

## Analogy patterns (reuse and adapt)

| Pattern | Good for |
|---------|----------|
| Nested rooms / circles | Hierarchies (AI ⊃ ML ⊃ DL) |
| Assembly line / factory | Feed-forward, layers, pipelines |
| Bouncer / guest list | Neurons, weights as templates |
| Mountain / blind hiker | Gradient descent, loss landscape |
| Telephone game | Vanishing/exploding gradients |
| Volume knob / light switch | Activation functions |
| Wedding planner / seating | Decision trees, purity, splits |
| Magnifying glass sliding | Convolution, pattern detection |
| Referee / penalty | Regularization (L1, L2) |
| Ghost colleagues / dropout | Dropout, co-adaptation |

Pick the analogy that makes the **mechanism** obvious, not just the name.

## Technical content integration

After the story, add what the student must know for exams:

- **Equations** — inline `$...$` or fenced code blocks for multi-line formulas
- **Tables** — biological↔artificial mappings, comparison of variants (sigmoid vs ReLU)
- **ASCII diagrams** — data flow, architecture pipelines
- **Bullet lists** — step-by-step algorithms, properties, when-to-use rules

Run a formula formatting pass after writing:
- Inline math: `$...$`
- Display math only where necessary

## ONE-LINE SUMMARIES section (Mode A only)

Collect every concept's blockquote one-liner into a final section:

```markdown
# ONE-LINE SUMMARIES — The Complete Set

> **{Term}** = {one line}
> **{Term}** = {one line}
...
```

Order matches the document. Include every `##` concept — this section is the last-page cram sheet.

## Workflow checklist

```
- [ ] Read all pointed-out source content
- [ ] Check existing stories/ for established analogies
- [ ] Choose Mode A or Mode B
- [ ] Draft stories — one analogy per concept, explicit mapping
- [ ] Add technical anchors (equations, tables, diagrams)
- [ ] Add Exam Tips where high-yield
- [ ] Add blockquote one-liners per concept
- [ ] Mode A: compile ONE-LINE SUMMARIES section
- [ ] Formula formatting pass ($...$)
- [ ] No emojis; no lecture/transcript references
```

## Example invocations

**Full course story doc:**
```
Turn bits-pilani/trimester-2/notes/neural-networks/week-* notes into Story-Based-Learning.md in stories/
```

**Single concept:**
```
Create a story from bits-pilani/trimester-2/notes/machine-learning/week-4/2-Finding the Best Split.md
```

**From a concept list:**
```
Story-based learning for: entropy, information gain, Gini index — decision tree splitting
```

## Reference examples

Read these before writing to match tone and depth:

- Comprehensive: `bits-pilani/trimester-2/notes/neural-networks/stories/Story-Based-Learning.md`
- Week-organized (table style): `bits-pilani/trimester-2/notes/machine-learning/stories/Story-Based-Learning.md`
- Standalone topic: `bits-pilani/trimester-2/notes/machine-learning/stories/Finding the Best Split.md`

For annotated excerpts and a filled section example, see [examples.md](examples.md).
