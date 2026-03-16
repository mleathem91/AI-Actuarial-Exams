---
name: excel-solver
description: Solve Excel-based actuarial exam questions using Python and openpyxl
---

# Excel Solver Skill

You are solving an Excel-based actuarial exam paper (e.g. CM1B, CM2B, CS1B, CS2B). These papers provide base data in Excel workbooks and expect candidates to build spreadsheet solutions. Since you cannot interactively use Excel, you will use **Python with openpyxl** to read the base data, perform all calculations, and write the results to an output workbook.

## Overview

Your workflow is:
1. **Read the base data** using the helper script
2. **Write Python computation scripts** for each question
3. **Run the scripts** to produce numerical answers
4. **Save workings** to an output Excel file
5. **Document your method and results** in `attempt.md`

## Step 1 — Read Base Data

Use the project helper script to inspect and extract data from the exam workbook:

```bash
python scripts/excel_helper.py describe "exams/<SUBJECT>/<SITTING>/Answer-Booklet.xlsx"
```

This prints all sheet names and their dimensions. Then read specific sheets:

```bash
python scripts/excel_helper.py read "exams/<SUBJECT>/<SITTING>/Answer-Booklet.xlsx" "Q1 Base"
```

This outputs the sheet contents as a formatted table. Use this to understand the base data before writing your solution.

> **Tip:** Redirect output to a file if the sheet is large:
> ```bash
> python scripts/excel_helper.py read "path/to/file.xlsx" "Q1 Base" > q1_data.txt
> ```

## Step 2 — Write Computation Scripts

For each question, write a **standalone Python script** that:
1. Reads the base data from the workbook using `openpyxl`
2. Performs all year-by-year / row-by-row calculations
3. Prints key intermediate and final results
4. Optionally writes results to an output workbook

### Template for a computation script

```python
from openpyxl import load_workbook, Workbook
import math

# ── Read base data ──────────────────────────────────────────────
SOURCE = "exams/<SUBJECT>/<SITTING>/Answer-Booklet.xlsx"
wb = load_workbook(SOURCE, data_only=True)
ws = wb["Q1 Base"]

# Extract values into Python data structures
# Example: read a column of mortality rates
data = {}
for row in ws.iter_rows(min_row=2, values_only=True):
    if row[0] is not None:
        data[row[0]] = row[1]

# ── Perform calculations ───────────────────────────────────────
# Year-by-year loop example:
results = []
for t in range(1, 21):
    # ... compute unit fund, non-unit fund, profit vector, etc.
    value = 0  # replace with actual calculation
    results.append({"year": t, "value": value})

# ── Print results ──────────────────────────────────────────────
print("=== Question 1 Results ===")
for r in results:
    print(f"Year {r['year']:2d}: {r['value']:.4f}")

# ── Write to output workbook ───────────────────────────────────
OUTPUT = "results/<MODEL>/<SUBJECT>/<SITTING>/workings.xlsx"
out_wb = Workbook()
out_ws = out_wb.active
out_ws.title = "Q1 Solution"
out_ws.append(["Year", "Value"])
for r in results:
    out_ws.append([r["year"], r["value"]])
out_wb.save(OUTPUT)
print(f"\nResults saved to {OUTPUT}")
```

### Key Patterns for Actuarial Calculations

#### Unit Fund Projection (Unit-Linked Policies)
```python
unit_fund = 0.0
for t in range(1, n_years + 1):
    premium = initial_premium * (1 + escalation) ** (t - 1)
    alloc_rate = allocation_rates[t]
    allocated = premium * alloc_rate
    bid_value_new = allocated * (1 - bid_offer_spread)
    
    unit_fund = (unit_fund + bid_value_new) * (1 + growth_rate[t])
    mgmt_charge = unit_fund * amc_rate
    unit_fund -= mgmt_charge
```

#### Non-Unit Fund / Profit Vector
```python
for t in range(1, n_years + 1):
    premium = premiums[t]
    allocated = premium * alloc_rate[t]
    unallocated = premium - allocated
    bos_income = allocated * bid_offer_spread
    
    start_cf = unallocated + bos_income - expenses[t] - commission[t]
    interest = start_cf * non_unit_interest
    
    death_cost = q[age + t - 1] * max(0, death_benefit[t] - unit_fund_end[t])
    
    profit[t] = start_cf + interest + mgmt_charge[t] - death_cost
```

#### Survival Probabilities and Profit Signature
```python
prob_in_force = [1.0]
for t in range(1, n_years + 1):
    p_survive = 1 - q[age + t - 1]
    p_lapse = lapse_rate[t] if t < n_years else 0
    prob_in_force.append(prob_in_force[-1] * p_survive * (1 - p_lapse))

profit_signature = [profit[t] * prob_in_force[t - 1] for t in range(1, n_years + 1)]
npv = sum(ps / (1 + rdr) ** t for t, ps in enumerate(profit_signature, 1))
```

#### Zeroisation (Eliminating Negative Cashflows)
```python
# Work backwards from the last year
reserve = [0.0] * (n_years + 1)
revised_profit = list(profit)  # copy

for t in range(n_years, 0, -1):
    if revised_profit[t] < 0:
        # Set up reserve at end of previous year
        reserve[t - 1] = -revised_profit[t] / ((1 + non_unit_interest) * (1 - q[age + t - 1]))
        revised_profit[t] = 0.0
    
    # Adjust previous year's profit for reserve cost
    if t > 1:
        revised_profit[t - 1] -= reserve[t - 1]
        revised_profit[t - 1] += reserve[t - 2] * (1 + non_unit_interest) * (1 - q[age + t - 2]) if t > 1 else 0
```

#### Joint Life Probabilities
```python
def joint_survival(qx_male, qx_female, term):
    """Compute year-by-year joint survival probabilities."""
    p_male = [1.0]
    p_female = [1.0]
    for t in range(term):
        p_male.append(p_male[-1] * (1 - qx_male[t]))
        p_female.append(p_female[-1] * (1 - qx_female[t]))
    
    p_joint = [p_male[t] * p_female[t] for t in range(term + 1)]
    p_at_least_one = [p_male[t] + p_female[t] - p_joint[t] for t in range(term + 1)]
    return p_male, p_female, p_joint, p_at_least_one
```

#### Annuity Valuation (Year-by-Year)
```python
def annuity_due(qx, interest, max_age=120):
    """Value annuity-due by summing v^t * t_p_x."""
    v = 1 / (1 + interest)
    result = 0.0
    t_px = 1.0
    for t in range(max_age):
        result += (v ** t) * t_px
        if t < len(qx):
            t_px *= (1 - qx[t])
        else:
            break
    return result
```

## Step 3 — Run Scripts

Run each computation script and capture the output:

```bash
python results/<MODEL>/<SUBJECT>/<SITTING>/q1_solution.py
```

Review the output carefully. If results look wrong, debug and re-run.

## Step 4 — Save Workings

All computation scripts should write their results to:
```
results/<MODEL>/<SUBJECT>/<SITTING>/workings.xlsx
```

If multiple questions produce output, write to different sheets within the same workbook, or create separate workbooks (e.g. `workings_q1.xlsx`, `workings_q2.xlsx`).

## Step 5 — Document in attempt.md

In `attempt.md`, for each question:
1. **State the methodology** — explain your approach
2. **Show the computational setup** — key formulae and data used
3. **Present the results** — include the final numerical answers from your Python scripts
4. **Embed key intermediate values** — show enough numbers that a marker can verify your method

> **CRITICAL:** Do not estimate or approximate. Run the computation and report the actual computed values. The whole point of this skill is to replace "≈ £8,557" with exact computed answers.

## File Organisation

```
results/<MODEL>/<SUBJECT>/<SITTING>/
├── attempt.md              # Written answers with full working and computed results
├── workings.xlsx            # Excel output with computed values
├── q1_solution.py           # Python script for Question 1
├── q2_solution.py           # Python script for Question 2
├── q3_solution.py           # Python script for Question 3
└── ...
```

## Prerequisites

The `openpyxl` package must be installed:
```bash
pip install openpyxl
```

## Common Pitfalls

- **Don't forget the bid-offer spread** — units are purchased at offer price, fund tracked at bid price
- **Select vs ultimate mortality** — check whether the question specifies select or ultimate rates
- **Interest rate timing** — deferment and in-payment rates are often different
- **Management charges** — deducted from the unit fund but credited to the non-unit fund
- **Death benefit excess** — only the excess of death benefit over unit fund is charged to non-unit fund
- **Zeroisation direction** — always work backwards from the last year
- **Probability in force** — includes both mortality and lapse decrements
- **Maturity year** — typically has no lapse decrement (all remaining policies mature)
