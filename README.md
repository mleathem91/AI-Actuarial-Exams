# Can Large Language Models Pass the IFoA Actuarial Exams?

An experiment to systematically test whether modern LLMs can pass the Institute and Faculty of Actuaries (IFoA) qualification exams.

## Methodology

1. **Exam Attempt** — An agent skill reads a past exam paper and produces a structured answer document, showing full working for each question.
2. **Self-Assessment** — A separate agent skill compares the LLM's attempt against the official examiner's report, awarding marks per the published marking scheme using a three-persona grading system (Harsh, Fair, Generous) to establish a confidence interval.
3. **Analysis** — Results are aggregated across subjects and models to identify patterns in LLM performance. See `analysis/scoreboard.md` for the current results.

## Prerequisites

- **Python 3.10+** with the following packages:
  - `pypdf` — for converting exam paper PDFs to markdown
  - `openpyxl` — for Excel-based (Paper B) exams
- **R** (optional) — required for R-based exams (CS1B, CS2B)
- **Google Antigravity** — this project uses Google Antigravity agent skills and workflows (`/sit-exam` and `/mark-exam`) to orchestrate exam-taking and grading.
- **IFoA Formulae and Tables** — the 2002 edition PDF, placed at `references/formulae-and-tables.pdf`. This is provided to candidates in real exams and is available from the IFoA.
- **IFoA Past Papers** — exam question papers and examiner reports, available from the [IFoA website](https://actuaries.org.uk). These are copyright IFoA and must not be redistributed publicly.

Install Python dependencies:

```bash
pip install pypdf openpyxl
```

## Project Structure

```
├── .skills/
│   ├── exam-taker/SKILL.md       # Skill: attempt an exam paper
│   ├── exam-grader/SKILL.md      # Skill: grade an attempt
│   ├── excel-solver/SKILL.md     # Skill: solve Excel-based (Paper B) questions
│   ├── r-coding/SKILL.md         # Skill: solve R-based (Paper B) questions
│   └── cp2-modeller/SKILL.md     # Skill: build CP2 modelling exam solutions
├── .agent/workflows/
│   ├── sit-exam.md               # Workflow: end-to-end exam attempt
│   └── mark-exam.md              # Workflow: end-to-end grading
├── scripts/
│   ├── extract_pdf.py            # Convert exam PDFs to markdown
│   └── excel_helper.py           # Inspect and read Excel workbooks
├── exams/<SUBJECT>/<SITTING>/     # Exam papers & examiner reports
├── results/<MODEL>/<SUBJECT>/     # LLM attempts & grade reports
├── references/                    # Formulae and Tables PDF
└── analysis/                      # Scoreboard & write-ups
```

## IFoA Subjects Covered

| Stage | Subjects |
|-------|----------|
| **Core Principles** | CS1, CS2, CM1, CM2, CB1, CB2 |
| **Core Practices** | CP1, CP2, CP3 |
| **Specialist Principles** | SP1, SP2, SP4, SP5, SP6, SP7, SP8, SP9 |
| **Specialist Advanced** | SA1, SA2, SA3, SA4, SA7 |

## Getting Started

### 1. Obtain and prepare exam papers

Download past papers and examiner reports from the IFoA website. Place them into the appropriate folder structure:

```
exams/CS1A/September_2025/
├── question-paper.pdf        # The exam questions (PDF from IFoA)
├── question-paper.md         # Converted to markdown (see below)
├── examiners-report.pdf      # The official marking scheme (PDF from IFoA)
└── examiners-report.md       # Converted to markdown (see below)
```

Convert PDFs to markdown using the extraction script:

```bash
python scripts/extract_pdf.py exams/CS1A/September_2025/question-paper.pdf exams/CS1A/September_2025/question-paper.md
python scripts/extract_pdf.py exams/CS1A/September_2025/examiners-report.pdf exams/CS1A/September_2025/examiners-report.md
```

> **Note:** PDF extraction is imperfect, especially for mathematical notation and tables. Review and fix any garbled LaTeX formulae in the output markdown where possible.

For practical exams, also place any data files (`.xlsx`, `.RData`, `.csv`) provided to candidates in the same folder.

### 2. Run the exam-taker workflow

In Google Antigravity, run the `/sit-exam` slash command:

```text
> /sit-exam CS1A September_2025
```

This reads the question paper, consults the Formulae and Tables, and produces a structured `attempt.md` at:

```
results/<MODEL>/CS1A/September_2025/attempt.md
```

The exam-taker skill is designed to answer like a well-prepared human candidate — showing full working, using proper actuarial notation, and allocating effort proportionally to marks available.

> **Important:** The workflow enforces exam integrity — the agent is prohibited from reading the examiner's report during the attempt.

### 3. Grade the attempt

Run the `/mark-exam` slash command:

```text
> /mark-exam <MODEL> CS1A September_2025
```

This compares the attempt against the examiner's report using three marker personas:

| Persona | Description |
|---------|-------------|
| **Harsh** | Requires absolute precision. No benefit of the doubt. |
| **Fair** | Standard professional judgement. Credit for clear understanding. |
| **Generous** | Looks for reasons to award marks. Credit for implicit correctness. |

The output is a detailed `grade-report.md` and machine-readable `metadata.json`, giving a confidence interval for the score (e.g. Harsh 52% — Fair 63% — Generous 71%).

### 4. Review the scoreboard

Check `analysis/scoreboard.md` for the aggregated results table across all models and subjects.

## Replicating with a Different LLM or Platform

This project is built around [Google Antigravity](https://antigravity.google/)'s agent framework (using its slash commands, workflows, and skills), but the methodology is model-agnostic. The skills and workflows can be adapted for use with other agentic development tools like Claude Code, Cursor, or similar IDEs.

### Using Other Platforms

For any other LLM or agentic tool:

1. **Use the same exam papers** — the `exams/` folder contains the inputs.
2. **Follow the skill instructions** — the instructions in `.skills/*/SKILL.md` describe the expected approach and output format. Adapt these as system prompts for your LLM.
3. **Provide the Formulae and Tables** — attach `references/formulae-and-tables.pdf` as context.
4. **Code execution** — use an agent that has terminal access for Paper B exams which require running Python or R scripts.
5. **Grade consistently** — use the three-persona grading approach from `.skills/exam-grader/SKILL.md` to produce comparable results.
6. **Save results** under `results/<YOUR-MODEL>/` following the same directory structure.

The key requirement is an agentic LLM with a sufficient context window to read a full exam paper and produce detailed answers with working. For practical exams, the LLM also needs code execution capabilities for Python and R.

## Exam Format Notes

Some exams have two papers:
- **Paper A** — Written/theoretical
- **Paper B** — Practical (Excel or R-based), requiring code execution and data file handling

The project includes specialised skills for Paper B:
- `excel-solver` — solves Excel-based questions using Python and openpyxl
- `r-coding` — solves R-based questions using R scripts
- `cp2-modeller` — builds professional Excel models for the CP2 modelling exam

## Important Caveats

- Exam papers are **copyright IFoA** — this repository does not contain copyrighted material in public form.
- Self-grading by an LLM is inherently imperfect — the three-persona system provides a range rather than a point estimate, but human spot-checking is still recommended.
- Results reflect a point-in-time snapshot of LLM capabilities and are not an endorsement or critique of actuarial education.

## License

This is a personal research project. Exam content remains the intellectual property of the IFoA.
