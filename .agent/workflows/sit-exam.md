---
description: Sit an IFoA actuarial exam for a given subject and sitting
---

# Sit Exam Workflow

This workflow runs the exam-taker skill to produce an exam attempt.

## Prerequisites

- The exam paper must exist at `exams/<SUBJECT>/<SITTING>/question-paper.md`
- The Formulae and Tables book must exist at `references/formulae-and-tables.pdf`
- For Paper B (Excel-based) exams, any workbook files should be at `exams/<SUBJECT>/<SITTING>/*.xlsx`
- For Paper B (R-based) exams, any data files should be at `exams/<SUBJECT>/<SITTING>/*.RData` or `*.csv`

## Steps

1. **Identify the exam** — Confirm the `<SUBJECT>` (e.g. CS1, CM1A, CM1B) and `<SITTING>` (e.g. September_2025) to attempt.

2. **Read the skill instructions** — Read `.skills/exam-taker/SKILL.md` to understand the exam-taking approach.

3. **Check for reference materials:**
   - Verify `references/formulae-and-tables.pdf` exists
   - For Excel-based exams, check for workbooks in `exams/<SUBJECT>/<SITTING>/`
   - For R-based exams, check for data files in `exams/<SUBJECT>/<SITTING>/`
   - If workbooks exist, use the Excel MCP tools to read the base data
   - If data files exist, use the r-coding skill to process them

4. **Attempt the exam** — Follow the appropriate skill instructions:
   - **CRITICAL:** You are strictly PROHIBITED from reading or referencing any `examiners-report`, marking schemes, or solution files during the attempt. If you see such files in the directory, you must ignore them completely.
   - **For standard exams:**
     - Follow .skills/exam-taker/SKILL.md
     - Read the question paper from `exams/<SUBJECT>/<SITTING>/question-paper.md`
     - Consult `references/formulae-and-tables.pdf`
     - Produce the attempt and save to `results/<MODEL>/<SUBJECT>/<SITTING>/attempt.md`
   - **For CP2 (Modelling) exams:**
     - **Follow .skills/cp2-modeller/SKILL.md** — This is CRITICAL.
     - Use Python to build a high-quality, formatted Excel model.
     - Save the model to `results/<MODEL>/<SUBJECT>/<SITTING>/CP2_Model.xlsx`.
     - Save the Audit Trail / Summary Report to `results/<MODEL>/<SUBJECT>/<SITTING>/attempt.md`.

5. **Report to user** — Confirm the attempt has been saved and summarise any questions that felt uncertain.
