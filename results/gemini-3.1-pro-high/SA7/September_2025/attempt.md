# SA7 — September_2025 — Exam Attempt

**Model:** Gemini 3.1 Pro (High)
**Date:** 2026-02-20
**Time allocated:** 3 hours 20 minutes

---

## Question 1

### Part (i) [9 marks]

**Assumptions and Working:**
- The couple's combined annual earnings are £84,000 (£42,000 each) and it is assumed these grow in line with inflation (so they remain £84,000 in real terms).
- The total contribution rate to the AE scheme is 14% (6% employee, 6% employer, 2% state). Real annual contributions are £11,760.
- Assumed contributions are paid evenly over the year, but for simplicity, the calculation uses annual payments in advance at a time-weighted average rate of return.
- **Investment assumptions (real terms, net of charges):**
  - **Equities net real return** = 5% (real equity return) - 0.5% (charges) = 4.5% p.a.
  - **Bonds net real return** = 1% (real bond return) - 0.5% (charges) = 0.5% p.a.
- **Lifestyle strategy timeline (age 25 to 65 = 40 years):**
  - **Years 1 to 30 (Age 25 to 55):** Fixed allocation of 80% equities, 20% bonds.
    - Portfolio Return = (0.8 * 4.5%) + (0.2 * 0.5%) = 3.6% + 0.1% = 3.7% p.a.
  - **Years 31 to 40 (Age 55 to 65):** The equity allocation reduces linearly from 80% to 0%, over 10 years, increasing bond allocations from 20% to 100%. Returns decline linearly each year.

**(a) The couple’s combined pension fund at age 65 in real terms**
Tracking the accumulated fund for 40 years sequentially:
- At the end of year 30 (age 55), the fund has accumulated from 30 annual contributions of £11,760 at 3.7% return:
  - Fund at Year 30 = £650,675
- Over the subsequent 10 years (Years 31 to 40), the portfolio return falls gradually from 3.38% (Year 31) to 0.5% (Year 40). Continuing to add the £11,760 annual contribution and compounding with the shifting blended return yields the accumulated fund at age 65.
- Carrying out the exact year-by-year recursion, we obtain:
  - **Final combined pension fund at age 65 = £915,771 (in real terms)**

**(b) The pension that the combined fund would produce in real terms**
- At age 65, the assets are converted into an inflation-linked annuity with a real yield of 1% p.a.
- The pension is assumed to be paid annually in advance for exactly 30 years (to age 95).
- Annuity factor at 1%: a_advance_30_at_1% = 26.0658
- Annual Pension = Fund / Annuity Factor = £915,771 / 26.0658 = **£35,133 p.a. (in real terms)**
*(Note: If paid in arrears, it would be £35,484 p.a.)*

### Part (ii) [9 marks]

**Comparing the relative benefit over the first 10 years: AE scheme vs Savings for a home**

**Option 1: AE Scheme (Contributions for 10 years only)**
- Total contribution rate = 14% (£11,760 p.a.).
- Accumulated fund at year 10 (at 3.7% p.a.) = £139,837
- This fund is then left invested for a further 30 years with no further contributions.
- From Year 11 to 30, it grows at 3.7% p.a.
- From Year 31 to 40, it grows at the de-risking lifestyle blended rates.
- Using the exact year-by-year recursion, the accumulated value at age 65 is:
  - **AE Scheme Value at age 65 = £361,741 (real terms)**

**Option 2: Saving for a Deposit on a Home (over 10 years)**
- The couple can save only the 6% employee contribution, as employer and state components are absent without AE.
- Savings amount = 6% of £84,000 = £5,040 p.a.
- Cash deposit returns exactly neutralise inflation. So net real return = 0%.
- Accumulated deposit at year 10 = £5,040 * 10 = £50,400.
- At year 10, they buy a home worth £250,000 (real terms).
- They take out a mortgage for the balance: £250,000 - £50,400 = £199,600.
- Mortgage duration is 30 years (years 11 to 40), so the house will be owned outright by age 65.
- The property value increases at real equity returns less 1% = 5% - 1% = 4% p.a.
- Home value at age 65 = £250,000 * (1.04)^30
- **Value of Home at age 65 = £810,849 (real terms)**

**Comment:**
- Based on the expected values, **saving for a home produces a significantly larger asset at age 65 (£810,849) compared to the AE scheme (£361,741)**.
- **Leverage:** The home purchase allows the couple to achieve investment returns (4% p.a. real) on the entire £250,000 house from year 10, magnified by the use of leverage (the mortgage).
- **Return Differential:** The property asset returns 4% p.a. real, whilst the AE scheme, particularly during its 10-year de-risking glidepath towards the end, has lower expected returns.
- **Lost Contributions:** The home saver gives up the "free money" of employer and state contributions (8% combined), but the leveraged return on the property more than makes up for this in the projection.
- **Cashflows:** The scenario assumes the mortgage repayments equal renting costs, essentially making the property strategy cost-neutral compared to continuing to rent after year 10. The AE scheme strategy assumes no further pension saving after year 10, and they will own no property asset at retirement.

### Part (iii) [6 marks]

**Validity of the assumptions used in the projections:**

**Economic Assumptions:**
- **Equity Risk Premium (4% over bonds):** This is a long-term historical average but may turn out to be optimistic going forward in a low-growth environment. Over a defined 30-year span, sequence of returns risk is significant.
- **House Price Growth (Equity return minus 1% = 4% real):** This is a highly aggressive assumption. Historically, real house price growth has been closer to 1-2%, varying heavily by region. 4% real growth would mean house prices drastically outpace wage growth over 40 years, potentially causing affordability crises.
- **Mortgage = Rent:** This might be a valid starting assumption at a point in time, but long-term mortgage payments (usually fixed or variable interest but amortising) often diverge significantly from rent (which typically tracks wage or general inflation). Initially, renting might be cheaper, whilst mortgages become cheaper in real terms due to inflation eroding the debt.
- **Cash Deposit Yield (0% real):** Plausible in the modern macroeconomic environment where central banks heavily manage rates, but over long cycles, positive real risk-free rates are possible.
- **Annuity real yield (1%):** Seems plausible as a long-term real discount rate based on long-dated inflation-linked sovereign bonds, though actual pricing might incorporate higher longevity margins.

**Other Assumptions:**
- **Mortgage Debt / Affordability:** The assumption that a bank will advance a 30-year 80% LTV mortgage (£199,600) on a combined £84,000 salary is broadly realistic (about a 2.37x multiple), but depends on future lending criteria and interest rate stress tests.
- **No Tax / Charges on Property:** This is highly flawed. Buying a residential property typically involves stamp duty, legal fees, ongoing maintenance, and insurance, which would severely drag the property's real return compared to the gross appreciation projection used.
- **Fixed Earning levels:** The model assumes flat real earnings (£42,000 each) for an unbroken 40-year career. Typically, individuals experience real wage growth with career progression, but also career breaks (e.g. for dependents).
- **Life Expectancy:** Annuity assumption fixed at 30 years post-retirement ignores longevity risk and actual mortality distributions.

### Part (iv) [6 marks]

**Implications for the state’s design of the AE scheme to manage demographic change:**

- **Aimed outcome:** The demographic reality (falling worker-to-retiree ratio) necessitates higher private provision of retirement income to relieve the burden on the state. The AE scheme is the primary vehicle to achieve this.
- **Property wealth vs. Pension wealth:** The scenario highlights that property ownership, due to leverage and asset appreciation, could provide significant wealth. However, property wealth is highly illiquid. Retirees need an income stream to replace the state pension, and downsizing or equity release presents complexities. Thus, the state should not view housing outright as a perfectly fungible substitute for pension savings.
- **Integration of housing into AE policy:** Given the massive relative benefit demonstrated in saving for a home, young contributors might rationally prefer to opt out of the AE scheme to save a deposit. This defeats the aim of mass enrolment. 
- **Policy solutions:** The state could redesign the AE scheme to allow members to use part of their AE pot as a tax-free withdrawal or a loan for a first-home deposit. This would harmonise the dual objectives of home ownership and pension saving.
- **Risk profile of investments:** The relatively poor projected final value of the 10-year AE contribution compared to housing suggests the lifestyle strategy's de-risking phase may be overly conservative. If retirees are living 30 years post-retirement, switching 100% to bonds at age 65 risks severe shortfall. The state might need to design a default path with higher growth asset exposure deep into retirement.
- **Employer / State matching:** The lost "free money" from employers and the state when avoiding the AE scheme is a huge distortion. The state should consider whether state components or tax relief can be maintained even if redirected toward housing for the young, to prevent a structural disadvantage.

---

## Question 2

### Part (i) [6 marks]

**Differences between DB and DC assets in the scheme:**

- **Investment Objective:**
  - **DB Assets:** Focus primarily on meeting the defined liability cashflows of the pensioner population and ensuring long-term systemic solvency to avoid government bailouts.
  - **DC Assets:** Aim to maximise risk-adjusted returns to build individual member pots over an accumulation phase, shifting to wealth preservation strategies as members approach retirement.
- **Time Horizon:**
  - **DB Assets:** Since it relates to current and future civil service pensioners, the liability duration could be 15-30 years, though shortening over time given the scheme is closing to future DB accrual.
  - **DC Assets:** Highly diverse, ranging from very long-term (multi-decade horizons for younger civil servants) to very short-term (nearing drawdown).
- **Risk Tolerance:**
  - **DB Assets:** Risk appetite is driven by the sponsor (government) backing the scheme. Often leans towards Liability Driven Investment (LDI), fixed income, and low volatility to stabilise the funding level.
  - **DC Assets:** The investment risk is borne entirely by the individual member. While young members can bear significant equity risk, members nearing drawdown cannot absorb capital shocks.
- **Asset Allocation Strategy:**
  - **DB Assets:** Expected to feature heavily in long-duration bonds, inflation-linked assets, and perhaps defensive alternative/income assets (infrastructure, real estate, private credit) generating predictable yields to match pensioner run-offs.
  - **DC Assets:** A "lifestyle" or target-date fund design, primarily comprising global equities during the accumulation phase, transitioning to multi-asset/corporate bonds and cash nearing retirement (since members will draw down).
- **Liquidity Needs:**
  - **DB Assets:** Requires regular, predictable liquidity to meet massive ongoing monthly pensioner payrolls (bearing in mind 1/3 of the $10bn relates to pensioners). In extreme events, collateral liquidity is needed if LDI is used.
  - **DC Assets:** Needs massive periodic liquidity because $500m p.a. in new cash is continually deploying, plus members may transfer funds, switch between investment options, or commence unpredictable drawdowns at retirement.

### Part (ii) [8 marks]

**Key considerations for the fiduciary manager when responding to the ITT:**

- **Scale and Complexity ($10bn size):** Managing a mega-scheme requires proving robust operational infrastructure, scalable trading platforms, deep resources, and strong governance frameworks to handle large discrete inflows ($500m p.a.) without market impact.
- **Liability Matching / LDI Capability (DB aspect):** The response must demonstrate expertise in matching the closed DB scheme's specific run-off profile, likely involving liability-driven investment (LDI), bespoke duration matching, and hedging inflation / interest rate risks for the pensioner cohort.
- **DC Strategy Design and Implementation:** Since the manager will handle portfolio construction, they need to supply compelling default lifecycle/target-date fund designs tailored to the specific drawdown behaviour of civil servants, plus a curated self-select range. 
- **Transition Management:** Switching from a monolithic DB structure to a bifurcated DB/DC structure with individual unitisation for DC members entails severe transition risks. The pitch must outline a seamless transition plan, minimising transaction costs, out-of-market risks, and operational errors during the unitisation phasing.
- **Manager Selection and Oversight:** The manager must underscore their open-architecture approach. They must prove substantial manager research capabilities across all major asset classes, especially alternatives which the government might desire for the DB portion.
- **Liquidity Management:** Addressing how to juggle the negative cash flows of the DB pensioner run-offs versus the ongoing positive $500m p.a. cashflows scaling the new DC section.
- **Reporting and Client Servicing:** Designing bespoke reporting for two entirely different audiences: highly technical aggregate reporting for the government/trustees focusing on funding levels and sponsor covenant risk (DB), versus individual, compliant, easy-to-digest unit pricing and performance metrics for the underlying DC members and administrators.
- **Cost and Value for Money:** Given it is a civil service scheme governed by a developing nation, scrutinising fees and ensuring low total expense ratios (particularly using passive building blocks where applicable) will be a critical political and commercial differentiator.

---

## Question 3

### Part (i) [5 marks]

**Benefits of using an external vendor of ESG ratings:**

- **Cost and Resource Efficiency:** Establishing an in-house ESG research team is highly expensive, requiring data scientists, specialized analysts, and huge data-gathering infrastructure. Outsourcing provides immediate access to scale without major fixed costs.
- **Comprehensive Coverage:** External vendors have established large teams to evaluate thousands of global companies across multiple asset classes (equities, corporate bonds, sovereign debt), providing a breadth of coverage that would take years for a single insurer to replicate.
- **Objectivity and Specialisation:** Third-party providers offer an independent, objective lens. They specialize purely in ESG, employing experts in niches like carbon footprinting, biodiversity, or corporate governance, ensuring deeper insights than generalist internal analysts might achieve.
- **Standardisation and Benchmarking:** Using widely recognized external ratings allows the insurer to standardize comparisons across its entire portfolio and easily benchmark its holdings against market indices or competitor funds that use the same vendor.
- **Regulatory and Client Reporting:** Many end-investors and regulators recognize leading external ESG scores. Using an established vendor offers reputational safety and simplifies compliance reporting, whereas a proprietary internal model might face severe regulatory or client scrutiny to prove its validity.

### Part (ii) [3 marks]

**ESG Factors that could be considered:**

- **Environmental (E):** Carbon emissions (Scope 1, 2, 3), water usage and waste management, energy efficiency, biodiversity impact, and transition plans to a low-carbon economy.
- **Social (S):** Labour standards (including supply chains), employee health and safety, diversity and inclusion metrics, community relations, and customer data privacy/security.
- **Governance (G):** Board independence and diversity, executive remuneration structures, anti-bribery and corruption policies, shareholder rights, and audit quality.

### Part (iii) [4 marks]

**Reasons why ESG scores differ significantly across providers:**

- **Differing Methodologies & Weightings:** Vendors place different subjective importance on factors. For example, an extraction company might score extremely poorly with a vendor prioritizing carbon emissions, but adequately with a vendor prioritizing safe labour practices and strong board governance.
- **Data Sourcing and Imputation:** Since ESG disclosure is not universally mandated or standardized, vendors often have to plug data gaps. Different providers will use different algorithms or proxies to estimate missing data (e.g. estimating Scope 3 emissions using different industry averages).
- **Absolute vs. Relative Scoring:** Some providers measure a company's absolute impact on the world, while others score companies strictly relative to their industry peers (best-in-class approach). A "clean" oil company might score high relative to other oil companies, but low in an absolute sustainability framework.
- **Scope of Assessment:** Providers vary on whether they emphasize a company's *current operations and controversies* (backward-looking risk mitigation) versus assessing the company's *future transition strategy and products* (forward-looking opportunities).

### Part (iv) [6 marks]

**Complexities of creating internal ESG scores using external ratings:**

- **Incompatible Scales and Normalisation:** Vendors use completely different scoring regimes (e.g. 0-100 scales vs AAA-CCC letter grades vs risk quartiles). Aggregating or averaging these requires building complex normalization models which might distort the underlying, nuanced signals.
- **Methodological Clashes:** Averaging a "best-in-class" relative score with an "absolute impact" score produces a mathematically meaningless outcome. The insurer must understand exactly what philosophy they are reflecting.
- **Frequency of Updates:** Different providers update their ratings on different cycles (e.g., annually, semi-annually, or whenever a controversy breaks). Maintaining a consolidated average score runs the risk of combining stale data with fresh data.
- **Treatment of Data Gaps:** If Vendor A covers a small-cap company but Vendor B does not, how does the aggregation mechanism treat the missing data? It can bias the portfolio depending on whether missing scores are defaulted to sector averages or ignored.
- **Loss of Specific "Why" Factors:** An aggregated "average" score obscures the driver of the rating. A company might have a catastrophic environmental score but a perfect governance score, resulting in an "average" combined rating. The investment team loses the specific risk flag (the E factor).
- **Governance and Maintenance overhead:** By blending data, the insurer effectively becomes a quasi-ratings agency. They must constantly maintain the weighting algorithm and justify strictly why they chose a 50/50 blend vs a 70/30 blend, which undermines the cost-saving purpose of using external vendors.

---

## Question 4 [10 marks]

**Due Diligence Document for Directly Held Private Loans**

**1. Loan Summary & Identifiers**
- Name of the borrower / obligor entity
- Sector / Industry and geographic location
- Loan Type (e.g., senior secured, unitranche, mezzanine)
- Loan Size/Allocation amount proposed vs total facility size

**2. Financial Terms and Returns**
- Interest Rate / Margin (e.g., floating over reference rate like SOFR + spread, or fixed)
- Loan maturity date and expected duration
- Payment structure (Payment In Kind (PIK), amortising, or bullet maturity)
- Expected Internal Rate of Return (IRR) / Yield to Maturity (gross and net of fees)

**3. Credit and Risk Metrics**
- Credit Rating (Internal assessment and/or shadow credit rating)
- Leverage multiples (e.g., Debt-to-EBITDA) and Interest Coverage Ratios
- Covenants package (financial covenants such as maintenance covenants, and restrictive covenants)
- Security / Collateral details and position in the capital structure (seniority, recovery rate assumptions)

**4. Borrower Business Profile & Financials**
- Qualitative overview of the borrower’s business model and competitive advantage
- Summary historical financial performance (Revenue, EBITDA margins, cash flow generation)
- Management team overview and Sponsor (Private Equity) backing details, if applicable.

**5. Illiquidity, Prepayment & Structural Factors**
- Expected illiquidity premium relative to equivalent public corporate bonds
- Prepayment terms/penalties (e.g., make-whole provisions, call protection)
- Ongoing serving and monitoring arrangements (who acts as the facility agent?)

**6. Portfolio Fit & ESG Analysis**
- Alignment with the insurer’s fixed income strategy and ALM / duration requirements
- Concentration limits check (breach of sector, counterparty, or geography limits)
- Summary of the ESG assessment on the borrower, noting any exclusionary criteria or sustainability risks.

---

## Question 5

### Part (i) [5 marks]

**Assessing the performance of a hedge fund:**
When assessing hedge funds, simple raw returns are insufficient because hedge funds often take significant asymmetric risks, utilise leverage, and target absolute returns independent of market benchmarks.

- **Absolute Returns vs Targets:** Evaluating the annualised net-of-fees performance against a cash benchmark plus a stated margin (e.g. SONIA + 4%) to ensure it achieves absolute return goals.
- **Risk-Adjusted Metrics:**
  - **Sharpe Ratio:** Evaluates return generated per unit of total volatility.
  - **Sortino Ratio:** More suitable for hedge funds as it only penalises downside volatility (crucial since hedge funds often exhibit non-normal return distributions).
- **Drawdown Analysis:** Analysing the Maximum Drawdown (the largest peak-to-trough drop) and the "Time to Recovery" to understand capital preservation during crises.
- **Correlation to Broad Markets:** Assessing the fund's beta/correlation to major equity and bond indices to ensure the hedge fund is actually delivering diversification rather than simply taking disguised, leveraged market beta.
- **Alpha Generation:** Using regression models to isolate the manager's true 'alpha' (skill) separated from factor exposures (value, momentum, carry).

### Part (ii) [9 marks]

**Factors driving strong manager performance to investigate in due diligence:**

- **Skill vs Luck:** Due diligence must verify if performance stems from repeatable, systematic skill (alpha) or if they just took a lucky, leveraged macro punt (e.g., correctly calling a single currency crash).
- **Style Drift:** Determining if the manager abandoned their stated global macro strategy to chase returns in crowded trades (e.g. going heavily long US tech equities) which violates the mandate constraints.
- **Market Environment Tailwinds:** Global macro tends to perform very well during periods of high economic dislocation, trend establishment, and rising rate environments. Due diligence must assess whether the strong performance is simply an artefact of the recent "Significant economic and political instability" rather than enduring proprietary models.
- **Leverage Levels:** The strategy may look spectacular purely because the manager has massively scaled up leverage. Due diligence must unpick the gross and net exposure levels to ensure the fund isn't exposing investors to disastrous tail risks (liquidation risk).
- **Key Person Dependency:** In global macro especially, returns are often driven by a single star manager's intuition. If this individual was highly active, do they still have the motivation to continue, or relies heavily on an analytical team?
- **Operational Infrastructure & Risk Controls:** Determining if the return came at the expense of ignoring risk limits. Reviewing the robustness of the stop-loss mechanisms, sizing limits, and independent risk management oversight.
- **Capacity Constraints:** The manager may have achieved great returns on a small asset base, but macro strategies can suffer diminishing returns as massive inflows occur (inability to put money to work without moving markets).

### Part (iii) [14 marks]

**(a) Commodities [7 marks]**
**Pros:**
- **Inflation Hedge:** Commodities typically have strong positive correlation with unexpected inflation, providing excellent real-return protection for pension scheme liabilities linked to CPI/RPI.
- **Diversification:** Historically low correlation to traditional equities and bonds, improving the overall portfolio's risk-adjusted return (efficient frontier).
- **Crisis Alpha:** During severe geopolitical instability (wars, energy shocks, supply chain strikes—as this developing country might be experiencing), commodity prices often spike, offsetting damages in domestic equity portfolios.
**Cons:**
- **No Natural Yield:** Unlike bonds or equities, physical commodities provide no income (dividends or coupons). Returns are driven entirely by price speculation, making it a drag on cash flow for a pension scheme.
- **High Volatility:** Commodity markets are notoriously volatile, subject to extreme weather, political intervention, and massive cyclical swings.
- **Implementation Costs and Roll Yield:** Investing via physical goods is impractical (storage/insurance costs). Investing via futures incurs "roll yield" drag—if markets are in contango (futures prices higher than spot), the fund loses money consistently just rolling the derivatives forward.
- **ESG Concerns:** Significant complications regarding environmental damage (mining, oil extraction) and human rights impacts, clashing with standard responsible investment policies.

**(b) Insurance-Linked Securities (ILS) [7 marks]**
**Pros:**
- **Uncorrelated Returns:** ILS (e.g., catastrophe bonds) yields depend on whether specific natural disasters occur (e.g. hurricanes, earthquakes). This is fundamentally uncorrelated to economic instability, equity crashes, or interest rate movements, providing pure diversification.
- **High Yield/Return Potential:** They typically offer severe risk premiums, producing a highly attractive floating-rate coupon above risk-free rates, which benefits a scheme seeking absolute returns.
- **Protection from Domestic Instability:** Given the developing country is facing "economic and political instability", ILS provides access to globally diversified, purely apolitical risk phenomenons.
**Cons:**
- **Binary / Tail Event Risk:** ILS exhibit extreme negative skewness. They generally provide steady, positive returns for years but can suffer a 100% loss of principal instantly if the trigger event occurs.
- **Illiquidity:** ILS is an over-the-counter, niche market. In times of stress or if the pension scheme needs cash urgently, selling the bonds before maturity may incur huge haircuts or be impossible due to no secondary market buyers.
- **Complexity and Modelling Risk:** Pricing ILS relies heavily on sophisticated meteorological/actuarial models. The pension scheme trustees and advisor may lack the expertise to understand these "black box" models, risking severe mispricing (e.g. failing to account for climate change accelerating disaster frequency).
- **ESG/Reputational Risk:** Investing in ILS effectively means the fund is capitalising on the insurance mechanism—if disaster strikes, they lose money, but if no disaster occurs they profit. The ethics of essentially betting against natural disasters might raise stakeholder queries.

---

## Audit Trail

### Accessed Files
- `exams/SA7/September_2025/question-paper.md`
- `references/formulae-and-tables.pdf`

