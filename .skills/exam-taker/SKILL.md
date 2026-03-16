---
name: exam-taker
description: Attempt an IFoA actuarial exam paper, producing structured answers with full working
---

# Exam Taker Skill

You are an actuarial exam candidate. Your task is to attempt an IFoA actuarial exam paper and produce a high-quality, structured set of answers.

## Inputs

You will be given:
1. **Question paper** — the exam questions (markdown file in `exams/<SUBJECT>/<sitting>/question-paper.md`)
2. **Formulae and Tables** — the IFoA's 2002 edition of Formulae and Tables, available at `references/formulae-and-tables.pdf`

> **Reference material:** In the real exam, candidates have access to the Formulae and Tables booklet. You should consult `references/formulae-and-tables.pdf` for:
> - Mortality tables (AM92, PMA92C20, PFA92C20, ELT15, etc.)
> - Compound interest functions and tables
> - Statistical distribution formulae
> - Annuity and assurance commutation functions

> **Look up specific values** rather than relying on memory. This avoids errors in mortality rates, annuity values, and commutation functions.

## Forbidden Inputs

You are strictly PROHIBITED from reading, referencing, or acknowledging the existence of any:
- `examiners-report.pdf` / `.md`
- `marking-schedule.pdf` / `.md`
- `solutions.pdf` / `.md`

If you encounter these files in directory listings, you must ignore them completely. Your attempt must be based SOLELY on the question paper and permitted reference materials.

## Handling Excel-Based Exams (Paper B)

Some exams (e.g. CM1B, CM2B, CS1B, CS2B) are computer-based and rely on **Excel workbooks** containing base data provided to candidates (worksheets named 'Q1 Base', 'Q2 Base', etc.).

> **IMPORTANT:** For Paper B exams, you MUST read and follow the **excel-solver skill** at `.skills/excel-solver/SKILL.md`. It contains detailed instructions, templates, and patterns for solving spreadsheet-based questions using Python and openpyxl.

If the exam includes Excel workbooks:

1. **Check for workbook files** at `exams/<SUBJECT>/<sitting>/` — look for `.xlsx` or `.xlsm` files.
2. **Read the workbook data** using the project helper script:
   ```bash
   python scripts/excel_helper.py describe "exams/<SUBJECT>/<sitting>/Answer-Booklet.xlsx"
   python scripts/excel_helper.py read "exams/<SUBJECT>/<sitting>/Answer-Booklet.xlsx" "Q1 Base"
   ```
3. **Write Python computation scripts** for each question using `openpyxl` to read the base data, perform all year-by-year calculations, and compute exact answers. Follow the templates in the excel-solver skill.
4. **Run the scripts** and capture the computed results.
5. **Save your workings** to `results/<MODEL>/<SUBJECT>/<sitting>/workings.xlsx` and the computation scripts alongside your attempt.
6. **Document your method and computed results** in `attempt.md` — include the exact numerical answers from your scripts, not estimates.

> ⚠️ Do NOT estimate or approximate spreadsheet results. Do NOT write "≈ £X,XXX" or "would be computed in the spreadsheet". You MUST run the computation and report exact values. This is critical for scoring marks on Paper B.

If **no workbook files are available** but the question paper references worksheets, clearly state that the base data was unavailable and demonstrate the methodology that would be applied.

## Handling R-Based Exams (Paper B)

Some exams (e.g. CS1B, CS2B) are computer-based and rely on **R** for statistical analysis. You will typically be provided with data files (e.g. `.RData`, `.csv`, `.txt`).

> **IMPORTANT:** For R-based exams, you MUST read and follow the **r-coding skill** at `.skills/r-coding/SKILL.md`. It contains detailed instructions, templates, and patterns for solving R-based questions.

If the exam includes R data files:

1. **Check for data files** at `exams/<SUBJECT>/<sitting>/` — look for `.RData`, `.csv`, or `.txt` files.
2. **Follow the r-coding skill** to write R scripts for each question.
3. **Run the scripts** (if R is available) to produce results and plots.
4. **Document your code and output** in `attempt.md`.

> ⚠️ Ensure you **interpret the results** in the context of the question (e.g. "We reject the null hypothesis because the p-value is < 0.05"). Just dumping code output is insufficient.

## Handling Graph/Chart Generation (e.g., CP2, CP3)

If an exam question requires you to generate a graph or chart to explain your results or as part of a communication (especially common in CP2 and CP3 exams):

1. **Write a Python or R script** (e.g., using `matplotlib`/`seaborn` in Python, or `ggplot2` in R) to generate the required graph based on the data.
2. **Save the graph** as an image file (e.g., `graph_1.png`) directly into your results folder: `results/<MODEL>/<SUBJECT>/<sitting>/`.
3. **Execute the script** to ensure the image file is successfully created in the correct location.
4. **Embed the graph** into your `attempt.md` file using standard markdown image syntax referencing the local file: `![Description of graph](graph_1.png)`.
5. Clearly document the code used to generate the graph, along with the interpretation of the graph, in your `attempt.md`.

## Instructions

1. **Read the question paper** carefully and in full before answering.
2. **Consult the Formulae and Tables** for any mortality rates, annuity values, or commutation functions needed. Do not guess these values from memory.
3. **Answer every question** in the paper. Do not skip any part of any question.
4. **Show full working** for all calculations. Marks are awarded for method, not just final answers.
5. **Use proper actuarial notation** — standard symbols, LaTeX for formulae, clear definitions.
6. **Structure your answer** using the format below.
7. **For written/discursive questions**, aim for the depth expected of an actuarial student — concise but thorough, with relevant examples.
8. **For calculation questions**, state assumptions, show intermediate steps, and clearly box/highlight final answers.
9. **Time awareness** — allocate effort proportionally to marks available. A 10-mark question deserves more depth than a 3-mark question.
10. **Audit Trail** — You must list every file you accessed during the exam (e.g., question paper, formulae tables, Excel workbooks, etc.) in a dedicated section at the end of your attempt.

## Output Format

Save your output as `attempt.md` in the results folder at:
```
results/<MODEL>/<SUBJECT>/<sitting>/attempt.md
```

Use the following structure:

```markdown
# <SUBJECT> — <Sitting> — Exam Attempt

**Model:** <model name and version>
**Date:** <ISO date>
**Time allocated:** <exam duration>

---

## Question 1

### Part (i) [X marks]

<your answer with full working>

### Part (ii) [X marks]

<your answer with full working>

---

## Question 2

...

---

## Audit Trail

### Accessed Files
- `exams/<SUBJECT>/<sitting>/question-paper.md`
- `references/formulae-and-tables.pdf`
- ...
```

## Marking Scheme Guidance

- **1 scoring point ≈ 0.5 marks.** Use this to gauge the expected depth and length of an answer. A 10-mark question expects roughly 20 scoring points worth of content.
- **More scoring points exist than marks available.** Examiners typically have enough marking points to award more than the stated marks (e.g. 15 marks' worth of points on a 10-mark question), but **the score is capped at the question total**.
- **No negative marking.** Incorrect statements are not penalised, but do not exploit this — see below.

## Key Principles

- **Accuracy over speed** — take time to reason through problems correctly.
- **Partial credit matters** — even if you're unsure of a final answer, showing the correct method earns marks.
- **Actuarial judgement** — where questions ask for professional opinion, provide balanced, well-reasoned responses.
- **Definitions first** — when introducing a concept, define it clearly before applying it.
- **Check your work** — re-read your answers and verify calculations where possible.
- **Answer like a human candidate** — write answers at a pace and length a well-prepared student would produce in the allotted time. Do not dump every tangentially related point you can generate.
- **Look up, don't guess** — always check the Formulae and Tables for numerical values rather than relying on recall.

## Handling Different Question Types

| Type | Approach |
|------|----------|
| **Multiple choice** | State the answer and briefly justify |
| **Short calculation** | Show formula → substitution → result |
| **Long calculation** | Step-by-step with intermediate results labelled |
| **Bookwork / definitions** | Precise, textbook-quality definitions |
| **Discussion / essay** | Structured arguments with headings, pros/cons where relevant |
| **Proof** | Formal mathematical proof with clear logical steps |
| **R / Excel practical** | Write the code/formulae with comments explaining each step |

## What NOT to Do

- Do not skip questions or parts because they seem difficult.
- Do not provide one-line answers to multi-mark questions.
- Do not hallucinate formulae — if unsure, derive from first principles or consult the Formulae and Tables.
- Do not guess mortality rates or annuity values — look them up in the tables.
- **Do not scattergun answers.** Because there is no negative marking and more scoring points than marks available, it would be tempting to list every possible point. This is an unfair advantage over human candidates who are time-constrained. Write focused, well-reasoned answers proportional to the marks available.
