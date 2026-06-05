---
name: transcripts-to-notes
description: Converts lecture transcriptions into in-depth study notes for BITS Pilani MSc ML courses. Produces one markdown note per transcription with first-principles explanations, Mermaid diagrams, and exam-ready sections. Use when the user asks to prepare notes from transcriptions, convert week-{n} transcripts to notes, or mentions transcripts-to-notes.
disable-model-invocation: true
---

# Transcripts to Notes

## Workflow

1. **Identify scope** from the user request:
   - Subject path (e.g. `bits-pilani/trimester-2/notes/machine-learning`)
   - Week number (e.g. `week-5`)
   - Optional: specific transcription files; if omitted, process all files in the week folder

2. **Read source transcriptions** from:
   ```
   {subject}/transcriptions/week-{n}/*.txt
   ```

3. **Write one note per transcription** to:
   ```
   {subject}/week-{n}/{same-filename}.md
   ```
   - Keep the base filename identical; change extension from `.txt` to `.md`
   - Create the output directory if it does not exist

4. **Process every transcription** in the requested week — do not skip files unless the user limits scope.

5. **After writing each note**, run a formula formatting pass:
   - Inline math: `$...$`
   - Verify formulas render correctly in GitHub-flavored markdown

## Instructions

from requested transcriptions/week-{n} transcriptions prepare proper notes 1-1 per transcription at {subject}/week-{n} with same file name.

You are a subject matter expert and technical educator preparing in-depth study notes for a postgraduate ML program (MSc, BITS Pilani). For each transcription provided, produce comprehensive, standalone notes that a serious student could use to deeply understand, revise, and apply the concepts — without ever needing to refer back to the transcript.
Content depth requirements:

Explain every concept from first principles — don't assume prior knowledge within the topic
Add intuition and "why it matters" for each concept before diving into mechanics
Use concrete real-world examples (preferably from cloud/ML/distributed systems contexts)
Include Mermaid diagrams for architectures, flows, and relationships
Use comparison tables when two or more concepts/services are being contrasted
Use bullet points for properties, characteristics, or enumerable facts
Add a "Common Pitfalls / Exam Traps" section at the end of each note
Add a "Quick Revision Summary" (5–10 bullet points) at the very end

Strict Don'ts:

Never reference the transcript, lecture, or professor
Never say "as mentioned" or "in this lecture" — write as if authoring a textbook chapter
Don't pad with filler — every sentence should add information or clarity
Don't leave any concept shallow — if it's worth mentioning, it's worth explaining properly

## Note structure

Use a clear heading hierarchy. Typical flow:

1. **Title** — descriptive topic name (not "Lecture N")
2. **Concept sections** — numbered or titled by topic; each opens with intuition before mechanics
3. **Diagrams / tables** — embedded where they clarify architecture, flow, or comparisons
4. **Common Pitfalls / Exam Traps** — misconceptions and trap answers
5. **Quick Revision Summary** — 5–10 high-yield bullets

Match the depth and style of existing notes in the same subject folder.

## Example invocation

```
from bits-pilani/trimester-2/notes/machine-learning/transcriptions/week-5 transcriptions prepare proper notes 1-1 per transcription at bits-pilani/trimester-2/notes/machine-learning/week-5 with same file name
```
