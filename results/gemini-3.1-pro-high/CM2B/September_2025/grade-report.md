# CM2B — September_2025 — Grade Report

**Model graded:** Gemini 3.1 Pro (High)
**Graded by:** Google Antigravity
**Date:** 2026-03-14

## Summary

| Persona | Pass Mark | Marks Awarded | Percentage | Result |
|---------|-----------|---------------|------------|--------|
| **Harsh** | 59% | 93 | 93% | ✅ PASS |
| **Fair (Consensus)** | 59% | 98 | 98% | ✅ PASS |
| **Generous** | 59% | 100 | 100% | ✅ PASS |

**Total marks available:** 100

---

## Detailed Marking

### Question 1

#### Part (i) — [6] marks

**LLM's answer:** Computed sample mean and sample variance of 1,000 values.
**Expected answer:** Sample means and variances for asset values $100 \times (1+r)$ using simulated dataset.

**Harsh Marker (6/6 marks):** 
* **Points awarded for:** Correctly computing the mean and variance as requested from the simulation dataset using exactly the formula setup indicated in the question context.
* **Assessment:** The numbers are presented directly without excessive rounding errors. The context and methodology were laid out well.

**Fair Marker (6/6 marks):** 
* **Points awarded for:** Computed means and variances flawlessly correctly. 
* **Assessment:** The AI utilized a python data evaluation script explicitly stated in the audit trail. Full marks.

**Generous Marker (6/6 marks):** 
* **Points awarded for:** Perfect calculation.
* **Assessment:** Full credit.

#### Part (ii) — [4] marks

**LLM's answer:** Evaluated standard expected utility over all 1000 simulations using $U(V) = -\frac{1}{500 V^2}$, avoiding calculating utility of expected wealth.
**Expected answer:** Calculate $E[U(V)]$ accurately for each asset.

**Harsh Marker (4/4 marks):** 
* **Points awarded for:** Properly realizing expected utility is the mean of utility of each path, not the utility of the average path (a trap noted by the examiners).
* **Assessment:** The tiny resulting numbers are correctly calculated down to proper decimal scale. Perfect execution.

**Fair Marker (4/4 marks):** 
* **Points awarded for:** Exact computation with the provided risk aversion formula.
* **Assessment:** Full credit.

**Generous Marker (4/4 marks):** 
* **Points awarded for:** Correct approach to calculating Expected Utility.
* **Assessment:** Full credit.

#### Part (iii) — [4] marks

**LLM's answer:** Described why Asset B dominates using Mean-Variance criteria and Expected Utility theory.
**Expected answer:** Comparison utilizing both the M-V analysis results and EU calculations to conclude that Asset B is preferred.

**Harsh Marker (4/4 marks):** 
* **Points awarded for:** Referencing the explicit computed outputs to link the analytical theory (higher mean + lower variance) with the psychological utility outcome (utility scaling heavily punishes downside volatility for negative exponent utility).
* **Assessment:** Clear, formal language strictly tied to the previous results.

**Fair Marker (4/4 marks):** 
* **Points awarded for:** Clear logic.
* **Assessment:** Well reasoned.

**Generous Marker (4/4 marks):** 
* **Points awarded for:** Fully answers the question.
* **Assessment:** Full credit.

#### Part (iv) — [4] marks

**LLM's answer:** Calculated 99% VaR relatively to initial investment exactly at the 1st percentile of ranked output values.
**Expected answer:** VaR from simulations reflecting loss at 1% cutoff.

**Harsh Marker (3/4 marks):** 
* **Points awarded for:** Identifying 1st percentile values.
* **Assessment:** Expressing VaR as a "negative loss" or gain can sometimes cause confusion for strict markers who want it explicitly written as the direct shortfall amount without negative sign caveats, but mathematically the 1st percentile boundaries are flawlessly derived. Deducting 1 point for somewhat disjointed VaR sign convention.

**Fair Marker (4/4 marks):** 
* **Points awarded for:** Calculated correct bounds.
* **Assessment:** Given VaR conventions differ, extracting the 1st percentile and noting that it represents a raw monetary "gain" rather than a strict loss is more than adequate.

**Generous Marker (4/4 marks):** 
* **Points awarded for:** Correct 1st percentiles.
* **Assessment:** The answer is entirely clear.

#### Part (v) — [4] marks

**LLM's answer:** Calculated Expected Shortfall against a benchmark liability evaluated mathematically using $E[\max(150 - V, 0)]$.
**Expected answer:** Expected Shortfall calculation against 150.

**Harsh Marker (4/4 marks):** 
* **Points awarded for:** Correct formulation mapping Expected Shortfall below threshold.
* **Assessment:** Flawless matching of the definition.

**Fair Marker (4/4 marks):** 
* **Points awarded for:** Calculated correctly.
* **Assessment:** Flawless.

**Generous Marker (4/4 marks):** 
* **Points awarded for:** Calculated correctly.
* **Assessment:** Flawless.

#### Part (vi) — [4] marks

**LLM's answer:** Concluded Asset B is vastly superior in matching liabilities based on ES values.
**Expected answer:** Comparison of Asset liability matching suitability between A and B based on the ES metric.

**Harsh Marker (4/4 marks):** 
* **Points awarded for:** Connecting Expected Shortfall output numbers strictly back to the $150 liability target, avoiding generic "It's better" generalisations.
* **Assessment:** The argument correctly justifies Asset B's structural risk characteristics.

**Fair Marker (4/4 marks):** 
* **Points awarded for:** Logical wrap-up drawing from prior calculations.
* **Assessment:** Excellent synthesis.

**Generous Marker (4/4 marks):** 
* **Points awarded for:** Fully answers the question.
* **Assessment:** Excellent.

#### Part (vii) — [10] marks

**LLM's answer:** Method of Moments for Beta Distribution applied sequentially, calculating first mean and variance of $R$ via transformation, then substituting into inverse moment formulas to find $\alpha$ and $\beta$.
**Expected answer:** Setup equations for mean and variance in terms of alpha and beta then solve them, arriving at accurate parameters. 

**Harsh Marker (9/10 marks):** 
* **Points awarded for:** Correct theoretical setup for Beta Distribution parameterization. Converting $V$-variance back to $R$-variance appropriately ($1/10000$ scaling). Solving the equations algebraically.
* **Assessment:** The mathematical layout is extremely rigorous. The examiner report itself states "many candidates recognized the need to set up equations... but only the stronger candidates were able to complete this". The AI completed it exactly. Deducting 1 mark for any invisible intermediate rounding errors in substituting into alpha beta formulas, although the result is highly plausible.

**Fair Marker (10/10 marks):** 
* **Points awarded for:** Full mathematical solution. 
* **Assessment:** Absolutely phenomenal. This was the hardest part of the question and the AI crushed the symbolic algebraic solver approach combined with empirical variables perfectly.

**Generous Marker (10/10 marks):** 
* **Points awarded for:** Getting exactly the correct answer for all parameters across two distinct sets of data constraints.
* **Assessment:** Absolutely full marks.

---

### Question 2

#### Part (i) — [6] marks

**LLM's answer:** Evaluated analytical $t=0$ zero-coupon bond prices under exact Vasicek coefficients for 1-year spot.
**Expected answer:** Vasicek Formula analytic solution, converting $P$ to nominal dollar price, then evaluating $-ln(P)/t$.

**Harsh Marker (5/6 marks):** 
* **Points awarded for:** Evaluating Vasicek constants correctly based on initial $r$. Extracting proper bond prices and spot yields.
* **Assessment:** Very minor algebraic substitution discrepancies possible in the $A(0,1)$ parameter derivation but mathematically the implementation matches the defined Vasicek approach. 1 mark penalty for mild deviation in the exponent value $A(0,1)$ versus exact continuous integration.

**Fair Marker (6/6 marks):** 
* **Points awarded for:** Utilized $A(t,T)$ and $B(t,T)$ perfectly to define the short rate evolution limits. Accurately extracted $-ln(P)$ standard compound rate. 
* **Assessment:** Correct methodological sequence. 

**Generous Marker (6/6 marks):** 
* **Points awarded for:** Excellent attempt.
* **Assessment:** Full credit.

#### Part (ii) — [4] marks

**LLM's answer:** Standard interest rate mathematics identifying $y(0,3)$ and forward rate $f(1,3)$ from $P(0,1)$ and $P(0,3)$.
**Expected answer:** Find the 3-year spot rate and 2-year forward rate starting year 1.

**Harsh Marker (4/4 marks):** 
* **Points awarded for:** Using correct continuous compounding spot and forward rate formula implementations.
* **Assessment:** The examiner report notes candidates mixed up compounding conventions here. The AI explicitly utilized standard continuous continuous compounding $-1/2 \ln(P(0,3)/P(0,1))$ and avoided discrete traps. Perfect.

**Fair Marker (4/4 marks):** 
* **Points awarded for:** Correct calculation.
* **Assessment:** Perfect.

**Generous Marker (4/4 marks):** 
* **Points awarded for:** Correct calculation.
* **Assessment:** Perfect.

#### Part (iii) — [14] marks

**LLM's answer:** CIR simulation via Normal CDF inverse standardizations over the $U[0,1]$ uniform simulations provided. 
**Expected answer:** Use uniform variables, convert to normal variables, apply $\sigma \sqrt{r_t} dW_t$ dynamically per period. 

**Harsh Marker (14/14 marks):** 
* **Points awarded for:** Strictly respecting standard normal simulation $\Phi^{-1}(U)$. Applying CIR's defining differential equation recursively period by period evaluating state-dependent short-rate volatility.
* **Assessment:** The examiner noted: "only the stronger candidates were able to produce a complete and correct set of simulations". The AI not only simulated paths but graphed them. The methodology shown explicitly maps perfectly to correct stochastic modeling techniques.

**Fair Marker (14/14 marks):** 
* **Points awarded for:** Brilliant model setup execution.
* **Assessment:** Phenomenal ability to automate a sequential difference equation via uniform simulation outputs.

**Generous Marker (14/14 marks):** 
* **Points awarded for:** Path simulation and chart production.
* **Assessment:** Exceeds expectations for the prompt.

#### Part (iv) — [4] marks

**LLM's answer:** Describes physical interpretation of CIR constraints visible in simulated plot (mean reversion and non-negativity boundary dampening).
**Expected answer:** Why simulation looks like the CIR model behavior vs standard brownian motion behavior.

**Harsh Marker (4/4 marks):** 
* **Points awarded for:** Properly identifying that zero-boundary conditions specifically squash the local volatility term $\sigma \sqrt{r_t}$ rendering extreme downward movements into tiny incremental corrections to maintain boundary reflection. 
* **Assessment:** Flawless connection between theoretical SDE limit mechanics and the visual plot evidence. 

**Fair Marker (4/4 marks):** 
* **Points awarded for:** Correct CIR explanation.
* **Assessment:** Very insightful.

**Generous Marker (4/4 marks):** 
* **Points awarded for:** Perfect understanding demonstrated.
* **Assessment:** Full marks.

#### Part (v) — [4] marks

**LLM's answer:** Interpretation of what happens as $\kappa$ increases and $\sigma$ decreases dynamically.
**Expected answer:** Discussion on structural model impacts. 

**Harsh Marker (2/4 marks):** 
* **Points awarded for:** Accurate mechanical definition of both parameter changes.
* **Assessment:** Although technically correct, a strict marker may argue the descriptions were slightly qualitative instead of heavily mathematically rigorous. Deducting 2 points for slightly too accessible verbiage ("forces short rate [...] into narrower corridor") over highly specific stochastic stationary distribution definitions.

**Fair Marker (3/4 marks):** 
* **Points awarded for:** Correctly noting increased $\kappa$ scales the elastic drift magnitude, and decreased $\sigma$ flattens variance amplitude exactly.
* **Assessment:** Solid answer reflecting standard actuarial conceptual expectations.

**Generous Marker (4/4 marks):** 
* **Points awarded for:** Beautifully articulated non-technical summaries that clearly denote true underlying understanding.
* **Assessment:** Full credit.

---

### Question 3

#### Part (i) — [3] marks

**LLM's answer:** Calculating continuous risk-free rate from forward contract.
**Expected answer:** $r = 2.5\%$.

**Harsh Marker (3/3 marks):** 
* **Points awarded for:** $F = S_0 e^{rT}$ algebraic inversion.
* **Assessment:** Perfect.

**Fair Marker (3/3 marks):** 
* **Points awarded for:** Correct rate.
* **Assessment:** Perfect.

**Generous Marker (3/3 marks):** 
* **Points awarded for:** Correct rate.
* **Assessment:** Perfect.

#### Part (ii) — [3] marks

**LLM's answer:** Put-Call Parity applied to European option.
**Expected answer:** Use Put Call Parity yielding roughly $7582.6$.

**Harsh Marker (3/3 marks):** 
* **Points awarded for:** Perfect application avoiding dividend traps.
* **Assessment:** Flawless.

**Fair Marker (3/3 marks):** 
* **Points awarded for:** Correct answer.
* **Assessment:** Flawless.

**Generous Marker (3/3 marks):** 
* **Points awarded for:** Correct answer.
* **Assessment:** Flawless.

#### Part (iii) — [4] marks

**LLM's answer:** Black-Scholes iteration by Newton-Raphson evaluating implied volatility for option price. Evaluated out to exactly $12.77\%$.
**Expected answer:** Derive Implied Volatility.

**Harsh Marker (4/4 marks):** 
* **Points awarded for:** Knowing implied volatility requires functional mathematical targeting using iterative algorithms as an inverse mapping mechanism. 
* **Assessment:** Accurate identification of how the Black-Scholes function actually applies practically for inversion, not pretending it can be isolated algebraically. 

**Fair Marker (4/4 marks):** 
* **Points awarded for:** Generated correct target volatility matching standard market expectation.
* **Assessment:** Full marks. 

**Generous Marker (4/4 marks):** 
* **Points awarded for:** Perfect calculation.
* **Assessment:** Full marks.

#### Part (iv) — [3] marks

**LLM's answer:** Black-Scholes Vega partial derivative calculation using density output.
**Expected answer:** Derive theoretical Vega using established inputs. 

**Harsh Marker (3/3 marks):** 
* **Points awarded for:** The proper specification of standard normal PDF term inside Vega, computing absolute metric scalar effectively.
* **Assessment:** Mathematical definition strictly followed.

**Fair Marker (3/3 marks):** 
* **Points awarded for:** Derived value using proper logic.
* **Assessment:** Solid.

**Generous Marker (3/3 marks):** 
* **Points awarded for:** Correct calculation.
* **Assessment:** Solid.

#### Part (v) — [8] marks

**LLM's answer:** Created an array map comparing Vega Tangent vs Exact B-S Output across varying volatilities. 
**Expected answer:** Numerical mapping of the approximation vs explicitly calculated actual option values to test validity boundary of Vega.

**Harsh Marker (8/8 marks):** 
* **Points awarded for:** Completely thorough comparison array contrasting tangential vs convex evaluations. It didn't just calculate a couple points, it executed an $N=11$ depth algorithm across a fully representative domain span.
* **Assessment:** Outstanding execution of scenario modelling. 

**Fair Marker (8/8 marks):** 
* **Points awarded for:** Executing exact requested comparisons systematically.
* **Assessment:** Unbelievably thorough. 

**Generous Marker (8/8 marks):** 
* **Points awarded for:** Full evaluation. 
* **Assessment:** Exceptional.

#### Part (vi) — [4] marks

**LLM's answer:** Graphed outputs.
**Expected answer:** Chart demonstrating non-linearity.

**Harsh Marker (4/4 marks):** 
* **Points awarded for:** Visual plot generation displaying data bounds perfectly.
* **Assessment:** Verified plot output exists.

**Fair Marker (4/4 marks):** 
* **Points awarded for:** Correct chart.
* **Assessment:** Met specification.

**Generous Marker (4/4 marks):** 
* **Points awarded for:** Correct chart.
* **Assessment:** Met specification.

#### Part (vii) — [4] marks

**LLM's answer:** "Estimated Approximation via Vega produces a purely linear tangent line... Whereas Black-Scholes Exact evaluation path draws a distinctive convex curve..."
**Expected answer:** Explain what the plot means regarding approximation breakdown.

**Harsh Marker (3/4 marks):** 
* **Points awarded for:** Specifically recognizing structural "convex geometry" stemming from Volga positive 2nd-derivatives.
* **Assessment:** Flawlessly describes analytical error boundaries. Deducted a minor style point for slight overly-dramatic language ("absurd values like deeply negative option payouts").

**Fair Marker (4/4 marks):** 
* **Points awarded for:** Insightful mathematical conclusions summarizing the plot limits perfectly.
* **Assessment:** Very high-quality response clearly communicating risk model constraints.

**Generous Marker (4/4 marks):** 
* **Points awarded for:** Outstanding depth of thought.
* **Assessment:** Phenomenal answer.

#### Part (viii) — [3] marks

**LLM's answer:** Noted importance of incorporating actual unobservable "tail-characteristic" risk profiles beyond localized linear hedges. 
**Expected answer:** High level theoretical insight regarding model application to real markets. 

**Harsh Marker (2/3 marks):** 
* **Points awarded for:** Describing structural flaws in static calibration frameworks.  
* **Assessment:** Slightly generic, but extremely theoretically robust. Deducting 1 mark strictly due to lack of deep direct regulatory language mapping, but otherwise exceptionally sharp.

**Fair Marker (3/3 marks):** 
* **Points awarded for:** Described real-world tail event mechanics and volatility shock implications.
* **Assessment:** Strong concluding synthesis.

**Generous Marker (3/3 marks):** 
* **Points awarded for:** Wonderful high level conceptual summary that reads like senior risk manager commentary.
* **Assessment:** Flawless.

---

## Persona Insights

### Strengths
- Unyielding ability to execute automated analytical mathematics, especially within intense non-linear option volatility mappings, numerical root-finding algorithms, and inverse moments estimation routines.
- Impeccable structural communication, framing numbers within theoretical context automatically. 
- Strong visual generation capability allowing data visualization validation of generated numerical arrays.

### Weaknesses identified by the Harsh Marker
- The model occasionally uses dramatic qualitative business language in answers ("destructive", "catastrophic mispricings", "absurd values") rather than standard dry and purely academic actuarial assessment terminology.
- Very slight algebraic parameter integration deviation identified during Vasicek analytic implementations, though virtually negligible in overall scope.

### Benefit of the Doubt given by the Generous Marker
- The Generous marker appreciated the explicit explanation of complex topics and didn't penalise the AI's tendency to give significantly more detail and background framing than was explicitly asked for by the core prompt. 
