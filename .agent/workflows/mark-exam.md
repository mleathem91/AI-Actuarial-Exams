---
description: Mark an LLM exam attempt against the official examiner's report
---

# Mark Exam Workflow

This workflow runs the exam-grader skill to grade a previously completed exam attempt.

## Prerequisites

- The exam attempt must exist at `results/<MODEL>/<SUBJECT>/<SITTING>/attempt.md`
- The examiner's report must exist at `exams/<SUBJECT>/<SITTING>/examiners-report.md` (or `.pdf`)
- The question paper must exist at `exams/<SUBJECT>/<SITTING>/question-paper.md` (for reference)

## Steps

1. **Identify the attempt** — Confirm the `<MODEL>`, `<SUBJECT>`, and `<SITTING>` to grade.

2. **Read the skill instructions** — Read `.skills/exam-grader/SKILL.md` to understand the grading approach, incorporating the multi-persona grading system.

// turbo
3. **Extract PDFs if needed** — Check the exam folder at `exams/<SUBJECT>/<SITTING>/`. If `examiners-report.md` does not exist but `examiners-report.pdf` does, extract it:
   ```bash
   python scripts/extract_pdf.py exams/<SUBJECT>/<SITTING>/examiners-report.pdf exams/<SUBJECT>/<SITTING>/examiners-report.md
   ```
   Do the same for `question-paper.pdf` → `question-paper.md` if needed.
   > ⚠️ Do NOT use `read_url_content` with `file://` URIs or search the web for reports. Always use the local extraction script.

4. **Grade the attempt** — Follow the `exam-grader` skill instructions:
   - **For standard exams:**
     - Read the attempt from `results/<MODEL>/<SUBJECT>/<SITTING>/attempt.md`
     - Read the examiner's report from `exams/<SUBJECT>/<SITTING>/examiners-report.md`
     - Evaluate the exam using all THREE personas (Harsh, Fair, Generous) on a per-question basis.
     - Produce the comprehensive grade report at `results/<MODEL>/<SUBJECT>/<SITTING>/grade-report.md`
     - Produce the metadata at `results/<MODEL>/<SUBJECT>/<SITTING>/metadata.json`
   - **For CP2 (Modelling) exams:**
     - **CRITICAL:** You MUST inspect the generated Excel model at `results/<MODEL>/<SUBJECT>/<SITTING>/CP2_Model.xlsx` (or similar).
     - Use `python scripts/excel_helper.py describe ...` to check structure/sheets.
     - Look for: Separation of inputs/calcs, formatting, checks, audit trail.
     - Grade the `attempt.md` (Audit Trail / Summary Report) and model against the Examiner's Report using the three personas.
     - Award marks for "Modelling", "Audit Trail", and "Summary Report" sections explicitly across all personas.
     - Produce the grade report and metadata as usual.

5. **Update the scoreboard** — Add the result to `analysis/scoreboard.md`. Use the **Fair** assessment score as the primary metric, while noting the confidence interval [Harsh% - Generous%].

6. **Report to user** — Summarise the result including pass/fail status based on the Fair marker, the score range [Harsh% - Generous%], and key insights across the personas.
