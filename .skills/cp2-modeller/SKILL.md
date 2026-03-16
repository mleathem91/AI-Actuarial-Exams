---
name: cp2-modeller
description: Create high-quality, auditable Excel models and audit trails for CP2 exams
---

# CP2 Modeller Skill

You are an actuarial model developer sitting the CP2 (Modelling Practice) exam. Your task is to build a high-quality, robust, and auditable Excel model using Python and `openpyxl`, and to produce the required audit trail and summary report.

## Objectives

1.  **Build a Professional Excel Model**:
    *   Separate inputs, calculations, and results.
    *   Use clear formatting (colors, borders, bold text).
    *   Include automated checks (e.g., cross-casts, zeroisation checks).
    *   Avoid hard-coding numbers in formulae.
    *   Ensure the model is flexible to parameter changes.

2.  **Generate an Audit Trail** (Paper 1):
    *   Document every step of your data processing and modelling.
    *   Explain the checks you performed and their results.
    *   Justify methodology choices.

3.  **Produce a Summary Report** (Paper 2):
    *   Communicate results clearly to a non-technical audience.
    *   Include charts and tables where appropriate.

## Tools

You will use **Python with `openpyxl`** to construct the Excel file programmatically. This ensures precision and reproducibility.

## Workflow

### 1. Read the Scenario and Data

*   Read the **Question Paper** (`exams/<SUBJECT>/<SITTING>/question-paper.md`).
*   Read the **Background Material** (if any).
*   Read the **Base Data** (Excel file) using `scripts/excel_helper.py`.

### 2. Design the Model Structure

Plan your Excel workbook structure before writing code. A standard CP2 model should have:

*   **`Documentation` / `Index` sheet**: Model name, author (Candidate Number), date, description, colour key.
*   **`Parameters` sheet**: All assumptions and inputs (e.g., interest rates, mortality params). **Nothing hard-coded elsewhere!**
*   **`Data` sheet**: The raw data, clearly labelled.
*   **`Calculations` / `Workings` sheet(s)**: The detailed step-by-year calculations.
*   **`Results` / `Summary` sheet**: Key outputs, charts, and checks.
*   **`Audit Trail` sheet** (if required by the specific question, otherwise strictly in the Word/Markdown doc).

### 3. Build the Model (Python Script)

Write a Python script (`model_builder.py`) using `openpyxl` to generate the `.xlsx` file.

#### Key Modelling Principles (Crucial for CP2 Marks)

*   **Separation of Concerns**:
    *   INPUTS: Blue font, distinct background.
    *   CALCULATIONS: Black font.
    *   LINKS: Green font (optional but good practice).
    *   RESULTS: Bold, distinct border.
*   **Formatting**:
    *   Use `openpyxl.styles` (Font, PatternFill, Border, Alignment).
    *   Format numbers appropriately (e.g., `0.00%` for rates, `#,##0` for currency).
    *   **Auto-fit column widths** for readability.
*   **Checks**:
    *   Add a "Checks" section in your `Summary` or `Calculations` sheet.
    *   Example: `IF(ABS(Sum_Calculated - Sum_Data) < 0.01, "OK", "ERROR")`.
    *   Use **Conditional Formatting** (Red for Error, Green for OK) if possible, or simple text indicators.

#### Code Template for `model_builder.py`

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment

# --- Styles ---
header_font = Font(bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
input_font = Font(color="0000FF") # Blue for inputs
check_ok_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid") # Light Green
check_err_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid") # Light Red

wb = Workbook()

# --- 1. Parameters Sheet ---
ws_params = wb.active
ws_params.title = "Parameters"
ws_params.append(["Parameter", "Value", "Description"])
# Apply styles...

# --- 2. Data Sheet ---
ws_data = wb.create_sheet("Data")
# Load data from source and write here...

# --- 3. Calculations Sheet ---
ws_calc = wb.create_sheet("Calculations")
# Build formulae...
# Example: =Parameters!B2 * Data!B2

# --- 4. Checks ---
# Add explicit check cells
ws_calc["E1"] = "Check: Assets = Liabilities"
ws_calc["E2"] = '=IF(ABS(C10-D10)<0.01, "OK", "FAIL")'

# Save
wb.save("results/<MODEL>/<SUBJECT>/<SITTING>/CP2_Model.xlsx")
```

### 4. Create the Audit Trail

Paper 1 specifically asks for an Audit Trail. This documents **what** you did, **how** you did it, and **why**.

**Structure:**
*   **Objective**: What is the model calculating?
*   **Data Validation**: What checks did you do on the raw data? (e.g., duplicates, missing values).
*   **Methodology**:
    *   Assumptions made.
    *   Formulae used (explain complex ones).
    *   Parameters chosen.
*   **Checks**: List the checks included in the model and their status.
*   **Results**: Summary of key outputs.

**Output:** Save this as `audit_trail.md` (or part of `attempt.md`).

### 5. Create the Summary Report (Paper 2)

Paper 2 asks for a Summary Report.

**Structure:**
*   **Executive Summary**: The "answer" (e.g., "The proposed premium is £120").
*   **Methodology Overview**: High-level explanation for stakeholders.
*   **Results & Analysis**: Charts, tables, sensitivity analysis.
*   **Conclusions & Recommendations**.
*   **Next Steps / Limitations**.

**Output:** Save this as `summary_report.md` (or part of `attempt.md`).

## Deliverables in `results/` folder

1.  `CP2_Model.xlsx` - The working, audited Excel model.
2.  `attempt.md` - Containing the Audit Trail (Paper 1) OR Summary Report (Paper 2).
3.  `model_builder.py` - The script used to generate the model.
