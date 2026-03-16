# CP2_1 — September_2025 — Exam Attempt

**Model:** gemini-3.1-pro-high
**Date:** 2026-02-20
**Time allocated:** 3 hours 20 minutes

---

## Audit Trail

### 1. Purpose of the model
The purpose of this model is to value the proposed Pooled Retirement Benefit (PRB) plan for a sample of 250 individuals. The model calculates the expected accumulated contributions at retirement (or earlier death), the projected level of pension at retirement, and the present value of both contributions and benefits. It determines the single accrual rate required for the scheme to balance given a 20% contingency margin, and further determines an annual pension increase rate that would exhaust this surplus. Finally, the model calculates Equivalent PRB level annuity factors for each individual reaching retirement.

### 2. Data and Reasonableness Checks
The data consists of 250 sample individuals with details on current age, starting contribution, expected salary increase, and expected age at death.

**Checks performed on raw data:**
- Values were checked for missing fields or negative numbers. None were found.
- The `Current age at t=0` ranges from 18 to 59 years, which is reasonable for a working population.
- The `Starting contribution amount` ranges from £1,020 to £18,040. Since contributions are exactly 10% of salary, this implies salaries between £10,200 and £180,400, which is a sensible range.
- The `Salary increase rate` ranges between 0.59% and 5.82% p.a., which aligns with typical expected long-term economic assumptions.
- The `Expected age of death` ranges from 58 to 106 years. The presence of deaths prior to retirement (age 65) confirms the necessity of modelling the pre-retirement death benefit correctly.

**Comment on patterns and charts:**
A "Summary by Age" sheet was built to aggregate the raw data into Count, Min, Max, and Average for each current age, allowing the generation of the demanded charts.
1. **Starting contribution amount vs Current Age:** We observe that average contributions (and thus average salaries) tend to increase with age reflecting career progression, flattening out towards later ages.
2. **Salary increases vs Current Age:** Salary increase rates generally appear slightly lower for older ages, indicating more rapid salary growth for younger individuals at the start of their careers.
3. **Age at death vs Current Age:** Expected death ages generally scatter, but the average age at death typically edges higher for older subsets because they have already survived to older ages.
4. **Equivalent PRB Level Annuity Factors vs Current age:** Evaluated for members reaching 65. The value for money ratio reflects accumulated contributions relative to the final pension. The shape is driven by the interaction between the lengthy accumulation phases vs salary growth.

### 3. Assumptions Used
The model employs the following parameters set out in the `Parameters` sheet:
- **Retirement Age:** 65
- **Contribution Rate:** 10% of salary
- **Expense Charge:** 3% deducted from contribution amounts.
- **Investment Return:** 7% p.a. (net of investment expenses).
- **Target Single Accrual Rate:** The model derives this as 81.92 to balance the equation of value including a 20% margin. 
- **Pension Increase Rate:** The model solves this as 2.95% to maintain a zero surplus plan.
- **Timing:** Contributions are assumed mid-year. Retirements and deaths occur on birthdays.

### 4. Methodology
The core calculations are performed row-by-row on the `Calculations` sheet.

**Term of accumulation:**
The number of years in the scheme `n` is `MIN(65 - CurrentAge, MAX(0, DeathAge - CurrentAge))`. The individual's final salary is projected using compound salary growth over `n` years.

**Present Value of Contributions:**
All contributions are assumed mid-year, growing at the member's salary increase rate `s`. A geometric series present value formula is leveraged to compute the PV of gross contributions at `t=0`. Expenses of 3% are deducted to define PV of Net Contributions. Since the accumulation to retirement is evaluated, the accumulated fund is this PV scaling forward by `(1+i)^n`. 

**Retirement Income (Base configuration / Accrual Rate setup):**
A "dummy" accrual rate of 90 is used initially. 
- The dummy pension at retirement is calculated as `(Years x Final Salary) / 90`. If death occurs prior to 65, the pension is 0. 
- The PV of the dummy pension is computed assuming a level annuity in arrears for `DeathAge - 65` years, discounted back to `t=0`.
- The death benefit (paid if death occurs between 66 and 69) is 5x the dummy pension at retirement, discounted to `t=0`.
- For deaths occurring on or before 65, the retirement income is solely the accumulated fund (calculated previously), which is independent of the accrual rate.

**Equation of Value and Single Accrual Rate:**
To solve for the overall target accrual rate `A`, we use the fact that the actual pension is strictly proportional to `90 / A`. We separate the PV of retirement incomes into Accrual-independent elements (funds paid on early death) and Accrual-dependent elements (pensions and subsequent fixed death lump sums). 
The Equation of Value requires: `Total Expected Retirement Income PV = 80% * Total PV of Net Contributions`.
The model sums across all individuals and exactly backs out `A = 81.92`.

**Surplus and Increasing Pension Rate:**
To find the annual pension increase rate `b` that exhausts the surplus (reducing the Equation of Value margin exactly to zero), we replace the level annuity PV with an increasing annuity PV factor: `(1 - ((1+b)/(1+i))^p) / ((1+i)/(1+b) - 1)`. The lump sum death benefits (if death 66-69) correspond to 5 times the *starting* pension at retirement and so do not incorporate the post-retirement trajectory `b`. The Python component solves `b = 2.95%` iteratively, ensuring the exact value is embedded into the `Parameters` sheet.

**Equivalent PRB Level Annuity Factor:**
For each individual, calculated as `Accumulated Fund at 65 / Target Level Pension`. Values are tabulated and summarized by age on the "Summary by Age" sheet using `AVERAGEIFS/MINIFS/MAXIFS` to drive the required chart.

### 5. Further Checks Performed
- **Equation of Value Check:** Within the `Checks and Equations` sheet, we explicitly verify that `80% * SUM(PV Net Contributions)` matches exactly the `SUM(Total Target PV)` after the application of the derived actual accrual rate. The check confirms a `0.00` difference resulting in a green "OK" status.
- **Term Sanity Checks:** The derived formula for term `n` intrinsically averts negative durations and enforces that no active contributions are modelled past age 65 or after an individual's expected death, validated by visual spot checking extreme cases (e.g., Member 41 deceased prior to 65).
- **Geometric Series Check:** A conditional trap was inserted into the PV of contribution calculations handling the edge case where salary growth exactly equals the discount rate (`1+s` equals `1+i`), avoiding division-by-zero errors.

---

## Audit Trail
### Accessed Files
- `exams/CP2_1/September_2025/question-paper.md`
- `exams/CP2_1/September_2025/CP2_P1_data for candidate.xlsx`
- `references/formulae-and-tables.pdf`
- `.skills/cp2-modeller/SKILL.md`
- `.skills/exam-taker/SKILL.md`
