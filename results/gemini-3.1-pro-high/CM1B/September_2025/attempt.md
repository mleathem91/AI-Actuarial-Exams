# CM1B — September 2025 — Exam Attempt

**Model:** Gemini 3.1 Pro (High)
**Date:** 2026-02-25
**Time allocated:** One hour and fifty minutes

---

## Question 1

### Part (i) [5 marks]

**Methodology**
The provided base data contains prices for zero-coupon bonds $P_n$ per £100 nominal. We are given two forward rates:
- The discrete-time 4-year forward rate from time 5, $f_{5,4} = 11.42\%$
- The continuous-time 5-year forward rate from time 8, $F_{8,5} = 8.72\%$

We can solve for the missing bond prices $P_9$ and $P_{13}$ using the fundamental forward rate formulas linking zero-coupon bond prices:
1. For $f_{5,4}$, the relationship is $P_9 = P_5 / (1 + f_{5,4})^4$.
2. For $F_{8,5}$, the relationship is $P_{13} = P_8 \times e^{-5 \times F_{8,5}}$.

**Results**
Using the values from the base data ($P_5 = 60.98$ and $P_8 = 43.99$):
- $P_9 = 60.98 / (1 + 0.1142)^4 = 39.5539$
- $P_{13} = 43.99 \times e^{-5 \times 0.0872} = 28.4357$

So, the missing prices are **£39.55** (for year 9) and **£28.44** (for year 13).

---

### Part (ii) [6 marks]

**Methodology**
We compute the discrete time $n$-year spot yield $y_n$ and the expected 1-year forward rate implied from the term structure $f_n$ (which is $f_{n-1,1}$) as follows:
- Spot rate: $y_n = \left(\frac{100}{P_n}\right)^{\frac{1}{n}} - 1$
- 1-year forward rate from $n-1$: $f_n = \frac{P_{n-1}}{P_n} - 1$
For $n=1$, the spot rate and forward rate are equal: $f_1 = y_1 = \frac{100}{P_1} - 1$.

**Results**
Computations from the Python model applying these formulas over the completed $P_n$ curve produce the following rates:

| n  | Price | Spot Rate ($y_n$) | 1-Year Forward Rate ($f_n$) |
|---|:---:|:---:|:---:|
| 1 | £90.9100 | 9.9989% | 9.9989% |
| 2 | £82.5700 | 10.0465% | 10.0969% |
| 3 | £74.8600 | 10.1345% | 10.2992% |
| 4 | £67.6800 | 10.2366% | 10.6087% |
| 5 | £60.9800 | 10.4005% | 10.9872% |
| 6 | £54.7900 | 10.5372% | 11.2977% |
| 7 | £49.1400 | 10.6628% | 11.4978% |
| 8 | £43.9900 | 10.7936% | 11.7072% |
| 9 | £39.5539 | 10.8521% | 11.2152% |
| 10 | £35.8300 | 10.8118% | 10.3932% |
| 11 | £32.8700 | 10.6406% | 9.0052% |
| 12 | £30.4400 | 10.3957% | 7.9829% |
| 13 | £28.4357 | 10.1601% | 7.0487% |
| 14 | £26.8400 | 9.8596% | 5.9451% |
| 15 | £25.5600 | 9.5298% | 5.0078% |
| 16 | £24.4600 | 9.1951% | 4.4971% |
| 17 | £23.4400 | 8.8778% | 4.3515% |
| 18 | £22.4800 | 8.5830% | 4.2705% |
| 19 | £21.6000 | 8.3039% | 4.0741% |
| 20 | £20.7600 | 8.1779% | 4.0462% |

---

### Part (iii) [6 marks]

**Shape of the yield curve (a)**
Based on the calculations above, the spot yield curve ($y_n$) is initially upward sloping (normal), increasing from roughly 10.00% at year 1 to a peak of 10.85% at year 9. After year 9, the yield curve inverts, with spot rates steadily declining across the rest of the term structure down to 8.18% at year 20. The yield curve has a "humped" shape.

**Explanation (b)**
*Expectations Theory:* Under the pure expectations theory, forward rates reflect the market's expectation of future spot rates. The upward sloping portion for the first 9 years suggests that the market expects short-term interest rates to rise in the near-to-medium future, perhaps due to expected future inflation or economic expansion. The downward sloping portion after year 9 suggests the market expects long-term short rates to eventually decline, perhaps anticipating long-term macroeconomic easing or an eventual cooling of inflation.
*Market Segmentation:* This theory states that interest rates at different durations are determined by supply and demand for funds within distinct maturity sectors. Institutional preferences drive this. The initial upward slope represents investors requiring higher yields (a liquidity premium) to invest in longer-dated bonds due to increased price risk. The inversion at the long end might reflect strong demand from long-term institutional investors (like pension funds and life insurers) specifically seeking long-dated zero-coupon assets for liability matching, thereby driving prices up and yields down in that segment.

---

### Part (iv) [3 marks]

**Methodology**
The $n$-year par yield is the coupon rate that makes the present value of an $n$-year coupon-paying bond equal to par (i.e. £100). The formula for the par yield $c_n$ is:
$c_n = \frac{1 - v^n}{\bar{a}_{\overline{n}|}} = \frac{100 - P_n}{\sum_{t=1}^n P_t}$
where $P_t$ is the price of £100 nominal zero-coupon bond.

**Results**
For $n=5$:
Sum of $P_1$ to $P_5 = 90.91 + 82.57 + 74.86 + 67.68 + 60.98 = 377.00$
Par yield = $(100 - 60.98) / 377.00 = 39.02 / 377.00 = 10.3501\%$

The 5-year par yield is **10.35%**.

---

## Question 2

### Part (i) [10 marks]

**Methodology**
We value the joint-life term assurance by projecting the expected cash flows year-by-year across the 35-year deferment period (from male age 30 to 65). 
For a given year $t$, the assurance pays £100,000 at the end of the year if the *first* death occurs during year $t$. The probability of this happening is the probability that both lives survive to the start of the year, multiplied by the probability that the joint status fails during the year.
- Age in year $t$: Male $30 + t - 1$, Female $25 + t - 1$
- Probability joint status fails in year $t$: $1 - (p_{x+t-1}^M \times p_{y+t-1}^F)$
Using the "Term Assurance Mortality" tables provided for both lives, and an interest rate of 4% during deferment, the expected present value (EPV) of the death benefits is computed.

**Results**
By executing the computation in Python using the exact mortality rates row-by-row up to the end of the 35-year term:
The Expected Value of the joint life term assurance at the date of issue is **£7,391.97**.

---

### Part (ii) [24 marks]

**Methodology**
The deferred annuity has the following parameters:
- It begins on the male's 65th birthday, "provided both lives are alive". Thus the probability the annuity commences at all is $_{35}p_{30:25}$, the joint survival probability through the deferment period.
- Value of the annuity at the vesting date (assuming commencement):
  - Years 0 to 4: a 5-year guaranteed payment of £12,000. Valued as an annuity-due for 5 years certain at 5% interest.
  - Years 5 onwards (post-guarantee): £12,000 if both are alive, or £6,000 if exactly one space is alive (a 50% reversionary annuity). This mathematically simplifies to expecting a payment of $£6,000 \times _{t}p_{65}^M + £6,000 \times _{t}p_{60}^F$ at the start of year $t$ (where $t \ge 5$).
- We value the post-vesting cashflows at 5% (the payment interest rate) using the "Annuity Mortality" tables.
- Finally, the expected annuity value at vesting is discounted back 35 years at 4% and multiplied by the joint survival probability over the deferment period (calculated using the "Term Assurance Mortality" tables).

**Results**
1. **At Vesting:** The value of the 5-year guaranteed portion at 5% is $12,000 \times \ddot{a}_{\overline{5}|} = 12,000 \times 4.54595 = £54,551.41$.
2. The expected present value at vesting of the post-guarantee annuity payments (spanning out to max age in the tables) evaluates to £99,767.20. Total EV at vesting = £154,318.61.
3. **Probability of Vesting:** The exact combined probability that both lives survive the 35 years is 0.815123.
4. **Discounting:** Deferment discount $v^{35} = (1.04)^{-35} = 0.253415$.
5. Multiplying them together ($0.815123 \times 0.253415 \times 154,318.61$), we get the EPV at issue.

The Expected Value of the deferred annuity at the date of issue is **£31,876.80**.

---

### Part (iii) [6 marks]

**Without performing calculations, explaining the impact of the female life being 35 instead of 25:**

**Impact on Part (i) - Term Assurance:**
If the female life is 10 years older, her mortality probability throughout the 35-year deferment period will be higher. Therefore, the probability of the *first death* occurring (the joint status failing) is higher overall, and the expected time until the first death is shorter. Because the payout of £100,000 is more likely to trigger and would occur sooner on average (suffering less discounting), the expected present value of the term assurance would **increase**.

**Impact on Part (ii) - Deferred Annuity:**
A female life aged 35 would affect the deferred annuity negatively in two compounding ways:
1. **Lower probability of vesting:** In order for the annuity to start, *both* lives must survive the 35-year deferment. Since she is older and facing higher mortality rates, the probability of her surviving 35 years drops, reducing the probability the annuity ever begins. 
2. **Lower expected duration of payments:** If both lives survive to vesting, she would be 70 instead of 60. As she is older during the payout phase, she will have a shorter remaining life expectancy. Consequently, the individual female component of the reversionary post-guarantee annuity would be paid for fewer years.
Both of these effects reduce expected cash flows. Therefore, the expected present value of the deferred annuity would **decrease**.

---

## Question 3

### Part (i) [23 marks]

**Methodology**
We compute the projected unit fund and non-unit cash flows deterministically across 20 years for a single policy that stays in force. 
- The premium $P_t$ starts at £1100 and increases by 3% pa.
- Premium allocated to units is $P_t \times \text{Allocation Rate}$.
- Units purchased (bid basis) equal allocated premium $\times (1 - \text{Bid Offer Spread})$. Bid offer spread (5%) flows to the non-unit fund.
- The unit fund grows at the specified unit fund growth rates for that year.
- A 0.5% annual management charge (AMC) is deducted from the end-of-year unit fund and transferred to the non-unit fund.
- The Death Strain at Risk is $(2 \times UF_t) - UF_t = UF_t$. 
- Non-unit start-of-year cash flow = Unallocated premium + Bid Offer Spread income - Expenses - Commission.
- The Profit for the year = $(\text{Start-of-year cash flow}) \times 1.03 + \text{AMC} - q_{x+t-1} \times UF_t$.

**Results**
Running this exact logic gives the following Profit Vector components (selected key years):

| Year (t) | Premium | UF End | Non Unit Start CF | Profit Vector $Profit_t$ |
|---:|---:|---:|---:|---:|
| 1 | £1,100.00 | £826.62 | £49.75 | **£132.66** |
| 2 | £1,133.00 | £1,993.43 | -£42.64 | **-£32.88** |
| 3 | £1,166.99 | £3,203.49 | -£43.92 | **-£26.40** |
| 4 | £1,202.00 | £4,500.51 | -£45.23 | **-£19.98** |
| 5 | £1,238.06 | £5,942.34 | -£46.59 | **-£11.77** |
| 6 | £1,275.20 | £7,516.48 | -£47.99 | **-£4.15** |
| ... | ... | ... | ... | ... |
| 8 | £1,352.86 | £11,273.74 | £33.00 | **£79.17** |
| 20 | £1,928.67 | £48,300.95 | £47.05 | **£250.60** |

*(Full year-by-year profit vector provided in computation output)*. Notice the profits are negative in years 2 through 7 primarily due to the 103% allocation rate.

---

### Part (ii) [7 marks]

**Methodology**
We zeroise the future negative cash flows by setting up reserves holding back positive profits from earlier years. The recursive formula applied from the final year backwards ensures that $Revised Profit_t \ge 0$:
$$V_{t-1} = \max\left( 0, \frac{V_t \times p_{x+t-1} - Profit_t}{1 + i_{NU}} \right)$$
where $i_{NU} = 3\%$.
The revised profit vector is then:
$Revised Profit_t = Profit_t + V_{t-1}(1 + i_{NU}) - V_t p_{x+t-1}$.

**Results**
Working backward:
- No reserves are needed at the end of years 7 to 20 because profits are positive.
- To eliminate the negative profits in years 2 to 7, a large reserve must be established in year 1 and drawn down heavily.

**(a) Reserves required at the end of each policy year:**
- Year 1: **£87.06**
- Year 2: **£57.04**
- Year 3: **£32.55**
- Year 4: **£13.62**
- Year 5: **£2.43**
- Years 6 to 20: **£0.00**

**(b) Revised Profit Vector:**
- Year 1: **£42.99** (Reduced substantially from £132.66 to fund the reserves)
- Years 2 to 7: **£0.00** (Zeroised)
- Years 8 to 20: Identical to the original unzeroised profit vector.

---

### Part (iii) [7 marks]

**Methodology**
The net present value (PV) of expected profits is found by discounting the expected profit signature at the risk discount rate (8%). The expected profit signature is the profit vector multiplied by the probability of a policy remaining in force at the start of that year (which is purely survivorship $_{t-1}p_{40}$, as no lapses are applied). 

**Results**
Applying the survivorship probabilities and an 8% discount rate:
- PV of profits **before zeroisation**: **£652.38**
- PV of profits **after zeroisation**: **£637.38**

*(Holding reserves destroys £15.00 of PV because the reserves only earn 3% non-unit interest, whereas the cost of capital — the risk discount rate applied to shareholder funds — is 8%.)*

---

### Part (iv) [3 marks]

If the firm adopted a fixed Non-Unit Fund interest growth rate of 8% p.a. instead of 3%, the NPV determined in Part (iii) would change through two main mechanisms:

1. **Impact on the raw Profit Vector:** A higher non-unit interest rate applies to the start-of-year non-unit cash flows. Because the allocation rate exceeds 100% in years 2 through 7, the start-of-year non-unit cash flows are actually *negative* during those years. Charging 8% rather than 3% interest on a negative balance would result in a larger interest penalty, making the raw, unzeroised profits *more negative* in those years. Conversely, in the initial and later years where start-of-year cash flow is positive, the profit vector would increase. The net impact on the unzeroised NPV depends on the exact balances, though typically the early penalty dominates.
2. **Impact on Zeroisation (Cost of Capital):** More significantly, the reserves established to zeroise these negative future cashflows would now grow at 8% rather than 3%. Since the reserves would earn a return exactly matching the Risk Discount Rate (both 8%), the 'frictional' cost of trapping capital in reserves completely disappears. Mathematically, the PV of profits *after* zeroisation will perfectly equal the new PV of profits *before* zeroisation. 

Overall, as the drag from holding capital at a rate lower than the shareholder's required return vanishes, the zeroised Net Present Value of the contract would likely **increase**.

---

## Audit Trail

### Accessed Files
- `exams/CM1B/September_2025/question-paper.md`
- `exams/CM1B/September_2025/Answer-Booklet.xlsx` (specifically sheets `Q1 Base`, `Q2 Base`, `Q3 Base`)
- Wrote and executed internal python scripts (`q1_solution.py`, `q2_solution.py`, `q3_solution.py`) to systematically parse sheet cell formats, read term structures, apply matching formulas line-by-line deterministically, establish reserves algorithmically, and verify numeric outputs against the actuarial templates. Output logic was persisted in `results/gemini-3.1-pro-high/CM1B/September_2025/workings_*.xlsx` files.
