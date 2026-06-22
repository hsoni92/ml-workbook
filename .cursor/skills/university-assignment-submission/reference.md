# Assignment Submission — Reference

## Finding requirements

Look in this order:

1. Faculty note or instruction file in the assignment folder (`note-from-faculty.txt`, `README.md`, rubric PDF)
2. Course portal / LMS text the user pastes or links
3. Template from an earlier week in the same course
4. Prior submission by the same student in the repo (match tone and structure)

Extract and confirm:

- Deliverable file types (`.ipynb`, `.docx`, `.pdf`, `.py`, etc.)
- Exact file naming pattern
- Required sections or questions
- Upload rules (individual files vs zip, deadline)
- Word or page limits
- Citation style if specified

## Common BITS / MSc patterns

These vary by course — always follow the specific brief over these defaults.

| Pattern | Typical rule |
| --- | --- |
| File naming | `RollNumber_Name_Week{N}_Report.docx`, `RollNumber_Name_Week{N}_Notebook.ipynb` |
| Upload | Individual files; do not zip unless explicitly allowed |
| Notebook + report | Same content at different depth — report summarizes notebook with matching numbers |
| Weekly progress | Implementation plus "planned improvements" or remaining work section |

## Cross-deliverable consistency

When both notebook and report are required:

- Same section order as the brief
- Same metric values and figure interpretations
- Report is shorter; notebook has code and full outputs
- Do not introduce new claims in the report that are not supported in the notebook

## Execution

Before handoff, run whatever the project uses:

```bash
# Examples — use what the project README or makefile defines
uv sync
make
jupyter nbconvert --execute --inplace notebook.ipynb
python -m pytest
```

Fix all errors. Do not submit notebooks with failed cells unless the brief allows it.

## Formula formatting

- Inline math: `$...$`
- Use display math only where the renderer supports it consistently
- Run a quick pass on any markdown or notebook text with formulas
