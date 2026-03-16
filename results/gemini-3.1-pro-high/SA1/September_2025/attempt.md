# SA1 — September_2025 — Exam Attempt

**Model:** gemini-3.1-pro-high
**Date:** 2026-02-20
**Time allocated:** 3 hours 20 minutes

---

## Question 1

### Part (i) [10 marks]

**(a) Advantages and disadvantages for Company B**

*Advantages:*
*   **Improved morbidity experience:** Encouraging a healthier lifestyle could reduce the incidence and duration of PMI claims, directly improving underwriting profitability.
*   **Early intervention:** The annual health check may detect conditions like high blood pressure or early-stage diabetes before they become acute. Treating these early is typically much cheaper than treating advanced disease.
*   **Valuable data acquisition:** Company B will accumulate a massive, longitudinal dataset of granular health metrics (heart rate, step counts, weight) linked to claims data. This is incredibly valuable for future pricing, reserving, and targeted product design.
*   **Positive selection:** The product will be highly attractive to health-conscious individuals who already lead a good lifestyle and want a discount. These lives will naturally have lower expected claims costs.
*   **Increased policyholder engagement and retention:** Policyholders interacting daily with a wearable device provided by the insurer creates "stickiness". The inertia of accumulated data and the wearable creates a barrier to switching, improving persistency (lapse rates).
*   **Brand and reputational benefits:** The company pivots its image from a passive claims-payer to an active "health partner" assisting policyholders.
*   **Cross-selling opportunities:** Increased touchpoints provide more avenues to market other health and life insurance products.

*Disadvantages:*
*   **High direct costs:** The cost of an annual 30-minute in-person appointment with a medical professional is very high. It may outweigh the financial benefit of reduced claims.
*   **Data infrastructure and processing costs:** Significant capital expenditure is required to securely store, process, and analyze the huge volume of data flowing in daily from thousands of wearables.
*   **Initial claims spike:** The annual health check will invariably uncover existing but asymptomatic conditions (e.g., discovering high cholesterol requiring prescription medication, or referring a suspicious mole). This will lead to an immediate spike in PMI claims.
*   **Reduced premium income:** The premium discount offered upfront directly reduces immediate revenue, worsening short-term cash flows before health improvements can materialise.
*   **Regulatory and compliance risks:** Handling continuous, highly sensitive biometric data creates massive GDPR (or local equivalent) compliance burdens. A data breach would be catastrophic for the company's reputation and could result in severe fines.
*   **Anti-selection:** Some individuals who suspect they have a health issue might take the option simply to get a free, fast-tracked medical examination.

**(b) Advantages and disadvantages for policyholders**

*Advantages:*
*   **Financial savings:** They receive a discount on their PMI premiums, and a subsidized wearable device.
*   **Free holistic health assessment:** A 30-minute dedicated consultation with a healthcare professional has significant intrinsic value, providing reassurance and personalized advice.
*   **Improved health and longevity:** The combination of check-ups and the daily nudge from the wearable might motivate positive, life-changing habits (more exercise, better diet).
*   **Early warning system:** Identifying potential health issues early allows for prompt, less invasive treatment and better long-term prognoses.

*Disadvantages:*
*   **Loss of privacy:** Transmitting detailed daily movements, sleep patterns, and heart rates to a massive corporation is highly intrusive.
*   **"Over-medicalisation" and anxiety:** Constantly monitoring metrics and attending extensive health checks can cause severe anxiety over minor, normal fluctuations in health data.
*   **Upfront costs:** Although described as "small", the upfront charge for the wearable is still an out-of-pocket expense.
*   **Time and inconvenience:** Attending a 30-minute in-person appointment every single year requires time off work or leisure.
*   **Fear of future penalization:** Despite guarantees that their premium won't be *directly* affected immediately, policyholders may fear that poor health data could eventually be used against them at renewal or if they apply for other products (e.g., life insurance).

### Part (ii) [10 marks]

Under Solvency II, the Best Estimate Liabilities (BEL) represent the expected present value of future cash flows, using best estimate assumptions without margins for prudence. Introducing the annual health check will require material updates across numerous BEL assumptions:

*   **Claim Frequency (Morbidity Incidence):**
    *   *Short-term:* The assumption must be increased. The annual health checks will lead to earlier detection of conditions and subsequent referrals, bringing forward claims that might have otherwise occurred later or not at all (if minor).
    *   *Long-term:* The assumption may be decreased, reflecting the expected improvement in underlying health from lifestyle changes driven by the wearables.
*   **Claim Severity (Average Claim Cost):** Early detection often leads to cheaper, preventative treatments (e.g., medication rather than surgery). However, some preventative scans/interventions themselves can be expensive. The overall severity assumption needs to be carefully modelled to reflect this shift in the *mix* of claims.
*   **Premium Income:** The projection of future premium income in the cash flows must be reduced to explicitly model the premium discount applied to policyholders who take up the option.
*   **Maintenance Expenses:** The per-policy renewal expense assumption must be increased substantially. It now must cover:
    *   The direct cost paid to the healthcare provider for the 30-minute appointment.
    *   The ongoing IT and administrative costs of collecting, storing, and monitoring the continuous stream of wearable data.
*   **Initial Expenses:** The upfront cost of subsidizing the wearable device must be allowed for in new business projections.
*   **Persistency / Lapse Rates:** The lapse rate assumption should generally be decreased. The "sunk cost" of the wearable, the continuous engagement, and the premium discount will likely lead to higher policyholder retention. 
*   **Expense Inflation:** Medical inflation often outpaces general price inflation. The cost of the 30-minute health check will be subject to this higher medical inflation rate, which must be incorporated into the long-term expense projection.
*   **Selection Base:** The company must establish whether the risk pool will segment. If healthier lives preferentially opt into the health check, the BEL assumptions might need to be split into two cohorts: an opted-in cohort with lighter long-term morbidity and a non-opted-in cohort with heavier-than-average morbidity.
*   **Discount Rate:** Under Solvency II, the discount rate is the risk-free curve prescribed by EIOPA (or the local regulator), so the curve itself doesn't change. However, the *timing* of the cashflows changes (higher expenses upfront, potential shift in claims timing), which interacts with the discount curve to alter the present value.

### Part (iii) [10 marks]

In deciding whether to outsource the health assessments and data collection to the third-party company, Company B must evaluate:

*   **Quality and Clinical Governance:** Does the third-party employ suitably qualified medical professionals in Country Y? As they represent Company B to the policyholder, any poor clinical advice or bad bedside manner directly damages Company B’s reputation.
*   **Data Security and Privacy:** This is paramount. Can the third-party guarantee the secure collection, transmission, and storage of highly sensitive medical and tracking data? Company B must audit their IT security infrastructure and ensure total compliance with Country Y's data protection legislation. 
*   **Cost and Commercial Terms:** Is their fee structure (e.g., fixed fee per health check vs. a flat retainer + variable costs) more cost-effective than Company B building an in-house capability or using its current claims network? What are the penalties for failing to meet Service Level Agreements (SLAs)?
*   **Geographical Reach and Convenience:** The third-party is "currently setting up" centres. Company B must ensure these centres are geographically distributed to match Company B's policyholder footprint. If policyholders have to travel long distances, take-up will be low and complaints high.
*   **Operational Capacity and Scalability:** Can the third party handle the expected volume? If PMI policies typically renew on 1st January, can the medical centres handle a massive spike in health check appointments at that time without waiting lists blowing out?
*   **IT Integration:** The third party needs to seamlessly transmit the wearable data and the outcome of the health checks into Company B’s pricing and claims administration systems. The technical feasibility and cost of building these API interfaces must be assessed.
*   **Experience in Country Y:** While they have experience abroad, the medical culture, regulations, and customer expectations in Country Y might be vastly different. Their lack of local track record is a risk.
*   **Financial Stability of the Third Party:** Company B must conduct strict due diligence on the third party's balance sheet. If the third party goes bankrupt, the headline feature of Company B's PMI product collapses overnight, requiring an expensive emergency replacement.
*   **Exit Strategy / Transition Risk:** What happens at the end of the contract, or if the contract is breached? Company B must ensure it retains ultimate ownership of the policyholder data and has a contingency plan to transition the service to another provider if necessary.
*   **Regulatory Approval:** Does outsourcing a critical customer-facing medical and data-collection function require formal approval or notification to Country Y's financial or healthcare regulators?

### Part (iv) [8 marks]

**Discussion on the Finance Director's proposal to introduce an annual charge**

The proposal aims to generate immediate revenue to offset the substantial costs of the health checks and wearables, thereby improving new business profitability. However, introducing an annual charge is a high-risk strategy with severe ramifications:

*   **Destruction of the Value Proposition:** The product was marketed on the premise that participating and sharing data earns the policyholder a discount and a free check. Removing the "free" element destroys this core USP.
*   **Collapse in New Business Volumes:** A primary reason for the high sales volume was the perceived high value of a "free" health check. Introducing a charge will likely drastically reduce new business sales, reversing the recent growth the management was pleased with.
*   **Catastrophic Impact on Existing Business:** Applying a retroactive charge to existing policyholders who signed up under the expectation of a free annual check will feel like a "bait and switch". This will lead to massive customer outrage, terrible PR, a spike in complaints to the financial ombudsman, and a wave of lapsations. It may also constitute a breach of contract depending on the original policy terms and conditions.
*   **Severe Anti-selection Risk:** If a charge is introduced, healthy individuals—who feel they don't *need* a doctor—will opt out. The only people who will pay the charge are those who suspect they have a looming health issue and want a comprehensive test. This leads to a concentration of poor risks in the scheme, exacerbating claims costs.
*   **Data Strategy Failure:** A key advantage of the original proposal was the mass gathering of population health data. A charge will dramatically reduce participation, starving Company B of the critical mass of data needed for significant actuarial insights.
*   **Timing Mismatch:** The Finance Director is focused on short-term new business profitability. However, a product designed to change lifestyle behaviors takes many years to demonstrably reduce morbidity. The first three years are dominated by the upfront costs and the "early detection" claims spike. It is arguably too early to judge the long-term profitability of the initiative; the FD is panicking over timing differences.
*   **Alternative Actions:** Before introducing a destructive charge, management should explore alternatives:
    *   Increase the base PMI premium slightly across the board to cross-subsidize the option.
    *   Reduce the level of premium discount given.
    *   Renegotiate fees with the third-party provider now that volumes are established.
    *   Reduce the frequency of the check (e.g., bi-annually) for healthy lives.

---

## Question 2

### Part (i) [4 marks]

**Main product features of pre-funded LTC insurance:**

*   **Purchase Timing & Premium Structure:** The policy is usually purchased well in advance of the need for care (often in middle age). Premiums are regular (monthly/annually) and payable while the policyholder is relatively healthy, building up a reserve.
*   **Benefit Triggers:** Benefits become payable when the policyholder fails a predefined number (e.g., 2 or 3 out of 6) of Activities of Daily Living (ADLs) such as washing, dressing, mobility, feeding, transferring, and toileting; or upon severe cognitive impairment (e.g., advanced dementia).
*   **Deferred Period:** Once the claim trigger is met, there is typically a deferred period (e.g., 3 to 6 months) during which no benefit is paid. This prevents claims for short-term temporary disablement.
*   **Nature of Benefit:** Benefits are usually paid as a regular income stream (annuity) to cover ongoing care costs. This can be an agreed fixed sum, or an indemnity benefit that reimburses actual receipted care costs up to a maximum limit.
*   **Term:** Cover is usually Whole of Life, as the risk is concentrated in advanced old age.

### Part (ii) [3 marks]

**Contrasting immediate needs LTC insurance to pre-funded:**

*   **Timing and Need:** Immediate needs policies are purchased *at the exact point in time* when care is required and the individual is already entering a care home, whereas pre-funded is bought years in advance purely as a precaution.
*   **Premium Payment:** Immediate needs requires a single, large upfront premium payment (often funded by the sale of the policyholder's home), rather than a long series of regular premiums.
*   **Underwriting Approach:** Immediate needs utilizes *substandard* life underwriting. Because the product effectively pays an annuity for life to cover care costs, those with *shorter* life expectancies are charged a *lower* single premium. Pre-funded uses standard medical underwriting where healthier lives are preferred and charged less.
*   **Payment Timing:** Immediate needs begins paying out the annuity immediately with no deferred period, directly to the care provider.

### Part (iii) [10 marks]

**Reasons why the LTC insurance market may be more developed in Country B than Country A:**

*   **The "Crowding Out" Effect of Public Health:** Country A has a publicly funded health system. Citizens often blur the line between healthcare (treating illness) and social care (assistance with ADLs). Even though Country A's LTC is means-tested, the mere existence of a public health system creates a psychological safety net, suppressing the perceived need for private insurance. In contrast, Country B has no public provision at all, forcing individuals to rely entirely on private insurance and fostering a strong cultural norm of self-insuring.
*   **Moral Hazard of Means-Testing:** The means-tested nature of Country A's public LTC provision creates a disincentive to save or insure. Citizens may logically decide against paying high premiums for an LTC policy because receiving private benefits would disqualify them from state support—meaning their premiums effectively just subsidize the government.
*   **Cultural Differences and Market Maturity:** Country B's market is "well established", having launched 15 years ago. A herd mentality or social proof occurs when 75% of peers hold a product. Country A's market has been "slow to develop," suggesting a lack of market momentum, lower consumer awareness of the staggering costs of care, or a cultural expectation that families will provide care.
*   **Product Accessibility and Distribution:** Country B may possess a strong network of specialized financial advisors equipped to sell complex, expensive products like LTC. Selling LTC requires highly emotional, long-term financial planning. Country A might lack this distribution infrastructure.
*   **Supply-Side Innovation and Product Design:** Insurers in Country B (like Company XYZ) may have designed more attractive products—for example, combining LTC with Whole of Life policies to guarantee a payout either on death or upon needing care, thereby removing the "use it or lose it" objection. Country A insurers may have offered poorly designed, overly expensive, or rigidly defined products.
*   **Economic Factors:** Citizens in Country B might have higher disposable incomes or higher personal wealth, allowing them to easily afford regular LTC premiums. Alternatively, the absolute cost of long-term care relative to average wealth might be much more terrifying in Country B, driving the need for insurance over self-funding. 
*   **Tax Incentives:** The government in Country B might offer generous tax relief on LTC premiums or tax-free benefit payouts to actively encourage self-provision, a lever not yet pulled strongly in Country A.
*   **Trust in Financial Institutions:** LTC requires policyholders to pay premiums for decades, trusting the insurer will be solvent and fair when adjudicating ADL claims 30 years later. Country B may have a stronger regulatory environment fostering higher trust in insurers compared to Country A.

### Part (iv) [6 marks]

**Possible reasons why Company XYZ should start selling pre-funded LTC business in Country A:**

*   **First-Mover Advantage in an Untapped Market:** With 75% of Country A's population self-funding their care and an aging demographic, the potential market size is vast. Entering now allows Company XYZ to capture significant market share before local competitors develop viable products.
*   **Government Support and Favourable Environment:** The Country A government explicitly *asked* foreign companies to enter. Company XYZ can leverage this invitation to negotiate favourable regulatory conditions, request public-private data sharing, or lobby for tax incentives that the government may implement to ensure the initiative succeeds.
*   **Leveraging Core Competencies and Scale:** Company XYZ is the market leader in Country B. They have 15 years of hard-earned intellectual property: robust pricing models, sophisticated claims management protocols, and proven administration systems. They can export this expertise to Country A at a low marginal cost, giving them a massive competitive edge over local novices.
*   **Risk Diversification:** Operating exclusively in Country B exposes the company to concentrated regulatory, economic, and demographic risks. Expanding into Country A diversifies their geographic risk profile.
*   **Strategic Growth:** If the Country B market is saturated (having reached 75% penetration), Company XYZ needs to find new geographic markets to maintain corporate growth targets and satisfy shareholders.
*   **Cross-border Synergies:** Establishing a brand presence in Country A through LTC might open doors to eventually cross-sell other health and care products if Country A's market continues to liberalise.

### Part (v) [12 marks]

It would be exceptionally dangerous for Company XYZ to simply lift and drop its Country B pricing basis into Country A. They must consider numerous divergent factors:

*   **Morbidity (ADL Incidence) and Mortality Rates:** 
    *   Baseline mortality: Country A has public healthcare which typically results in different long-term survival rates.
    *   Healthy life expectancy: Cultural factors, diet, and occupational history differ heavily by country, impacting the rate at which citizens fail ADLs in old age. 
    *   The Country A pricing must reflect Country A's specific demographic life tables.
*   **Cost of Care (Claim Severity):** XYZ's product provides *indemnity* benefits. Therefore, the pricing is highly geared to the actual cost of nursing homes and domestic carers. Country A’s real estate costs, minimum wage laws for care workers, and the standard level of residential facilities will dictate claims severity, which likely differs drastically from Country B.
*   **Target Market Selection:** In Country B, with 75% penetration, the risk pool reflects the general population average. In Country A, initially, the product will only attract a small sliver of the population. This early-adopter cohort might exhibit different socio-economic characteristics (perhaps wealthier, healthier lives, or conversely, those with strong family histories of dementia), leading to skewed morbidity experience compared to Country B.
*   **Interaction with State Systems:** Because Country A has public healthcare and means-tested social care, the boundary between health and care is blurred. Some services deemed "social care" in Country B might be provided free as "healthcare" in Country A's hospitals, significantly altering the expected claim sizes and durations.
*   **Economic Assumptions:** 
    *   *Discount rates:* The yield curve on government bonds and investable assets in Country A will differ, altering the discount rate used to value the long-term premium streams and reserves.
    *   *Inflation:* Medical and wage inflation in Country A will dictate the projected escalation of care costs.
*   **Expense Variations:** 
    *   Initial setup costs: Entering a new country involves heavy strategic, legal, and IT setup costs that must be amortized.
    *   Distribution: Commissions paid to brokers in Country A may be different to secure distribution channels.
    *   Claims handling: XYZ does not have an established claims assessment network in Country A, so third-party medical assessments will cost more.
*   **Parameter Risk and Prudence Margins:** Company XYZ has 15 years of detailed *own experience* data for Country B, allowing for razor-sharp pricing with minimal margins. For Country A, they have almost zero relevant experience data. The pricing basis must include a massive margin for parameter risk to protect against catastrophic mispricing in a new territory.
*   **Regulatory Capital and Taxation:** Country A's financial regulator will dictate the reserving methodology and capital solvency requirements. These cost-of-capital charges must be priced into the premium. Similarly, the tax treatment of the insurer's profits and investment returns in Country A alters the required gross margin.
*   **Legal Interpretations:** How courts in Country A strictly interpret policy definitions, such as the exact definition of "failing to wash oneself," dictates claims payout ratios.

---

## Question 3

### Part (i) [2 marks]

**Asset share** is a retrospective calculation representing the accumulated value of a policy or group of policies. It is calculated by taking the premiums paid by the policyholder, deducting expenses, commission, tax, the cost of providing the life cover/claims, and the cost of any guarantees or capital provided by the shareholders, and accumulating the balance at the *actual* investment return earned on the underlying assets.

### Part (ii) [8 marks]

**Why asset share may be greater than expected on longer duration policies:**

The asset share exceeds expectations because the real-world experience over the last 10+ years has been significantly more favourable than the conservative assumptions baked into the original pricing basis a decade ago:

*   **Investment Outperformance:** The most likely driver is that the actual investment returns earned on the assets backing the CI reserves have heavily outperformed the prudent long-term investment yield assumption used in pricing 10 years ago. (e.g., a strong decade for equities or higher-than-expected bond yields).
*   **Favourable Morbidity Experience:** Medical advances or public health improvements (e.g., a drastic drop in smoking rates leading to fewer heart attacks) may mean the actual incidence rate of critical illnesses has been lower than expected. Fewer claims mean more money remains in the asset share pool.
*   **Tighter Claims Management:** Over 10 years, Company A may have refined its claims assessment processes, more strictly enforcing precise CI definitions, leading to a decline in the proportion of borderline claims paid.
*   **Favourable Mortality (if standalone CI):** If the CI product pays out on illness *or* death, lighter mortality experience leaves more in the asset pool.
*   **Expense Efficiencies:** The company may have achieved economies of scale or implemented new IT systems that reduced per-policy maintenance expenses below the inflatad assumptions modelled a decade ago. 
*   **Cross-subsidy from Lapses:** Guaranteed CI policies typically offer a zero surrender value. If policyholders lapse their policies after having paid premiums for a few years, their accumulated asset share is forfeited to the insurer and falls into the general pool. If lapse rates were higher than expected, the surviving policies benefit from this surrender surplus cross-subsidy.
*   **Excessive Initial Pricing Margins:** Guaranteed premium products are priced with enormous margins for prudence because the insurer locks in the price for decades against highly uncertain medical trends. If the feared adverse scenarios (e.g., a massive spike in cancer rates) simply didn't materialize, those massive prudence margins manifest as surplus asset share.

### Part (iii) [5 marks]

**Why insurance companies adopted reviewable premiums for new CI business in Country Z:**

*   **Consumer Affordability in a Recession:** Following 5 years of recession, consumer disposable incomes are squeezed. Sales of expensive guaranteed CI would plummet. Reviewable premiums allow insurers to remove the massive long-term prudence margins from the initial price, offering a significantly cheaper starting premium to cash-strapped consumers to maintain market share.
*   **Managing Long-Term Parameter Risk:** CI is a volatile, long-tail class of business heavily impacted by medical advances (e.g., new screening methods detecting cancers much earlier, driving a massive spike in valid claims). Insurers use reviewable premiums to pass the risk of unexpected worsening in medical trends onto the policyholder, rather than bearing it themselves.
*   **Economic Pressures (Low Yields):** Recessions are typically characterized by prolonged low central bank interest rates. Earning low yields on reserves makes long-term guaranteed products incredibly expensive to fund. Reviewable premiums allow insurers to adjust pricing dynamically if the low-yield environment persists.
*   **Capital Efficiency:** Under risk-based capital regimes, writing 30-year guaranteed premium morbidity risk requires holding a massive amount of statutory capital. Reviewable premium business severely truncates the risk horizon (as the insurer can re-price), freeing up massive amounts of capital. In a deep recession, capital is scarce and expensive, making capital-light products highly attractive.
*   **Market Dynamics:** Once one major competitor moves to cheaper reviewable products, adverse selection occurs if Company A continues selling expensive guaranteed products. They would only attract those who *know* their risks are worsening. They are forced to adopt reviewable premiums simply to remain competitive in the market.

### Part (iv) [5 marks]

**Justification for Company A updating its investment strategy:**

*   **Change in Liability Duration:** The liability profile of Company A is fundamentally shifting. Reviewable premium business has effectively shorter durations than guaranteed business because the pricing can be reset if economic conditions change. Therefore, the backing assets no longer need to be locked into ultra-long duration bonds to perfectly match long-term guaranteed cashflows.
*   **Change in Risk Appetite from Policyholder to Insurer:** For the old guaranteed business, the insurer bore all the investment risk. For the new reviewable business, significant poor investment returns can theoretically be passed partly to the policyholder via premium reviews. This allows the insurer to adopt a slightly looser or higher-yielding asset allocation.
*   **Economic Imperative of the Recession:** 5 years of recession have likely warped the yield curve, increased corporate default rates, and depressed certain equity sectors. The old investment strategy, set in a pre-recession environment, is no longer fit for purpose and must be actively realigned to current macroeconomic realities to secure adequate returns without excessive credit risk.
*   **Exploiting the Surplus:** As established in part (ii), the existing guaranteed business has built up unexpectedly large asset shares. This robust capital buffer provides the company with the financial strength and risk tolerance to potentially invest those specific backing reserves into higher-yielding, slightly riskier assets to generate higher shareholder returns, as the liabilities are more than comfortably covered. 
*   **Liquidity Needs:** A prolonged recession may lead to spikes in lapsation across the book as policyholders struggle financially. The investment strategy must be updated to hold sufficient liquid assets to meet these sudden cash outflows without forcing fire-sales of illiquid assets.

### Part (v) [7 marks]

**Tasks Company A needs to undertake to implement the updated investment strategy:**

1.  **Define and Approve Strategy:** The Board of Directors and the Assets & Liabilities Committee (ALCO) must formally document, challenge, and approve the new strategic asset allocation (SAA) benchmarks, expected return targets, and revised risk appetite limits.
2.  **Detailed ALM Modeling:** Actuaries must run extensive Asset Liability Modeling (ALM) cashflow projections using the new mix of reviewable/guaranteed liabilities against the proposed new asset classes to ensure the portfolio behaves predictably under severe economic stress tests.
3.  **Draft Implementation Mandates:** The Chief Investment Officer must translate the high-level strategy into precise, legally binding investment mandates for internal fund managers or external asset managers, detailing exact tracking errors, duration limits, and permitted asset classes.
4.  **Transition Management Plan:** Develop a meticulous trading plan to liquidate old assets and purchase new ones. This plan must seek to minimize market impact, bid-ask spread costs, and out-of-market risks during the transition phase.
5.  **Update Risk and Solvency Models:** Actuaries must update the firm's Internal Model or Solvency II standard formula calculations to reflect the new market, credit, and ALM risk profiles. The new strategy must not accidentally breach regulatory capital limits.
6.  **IT and Operational Systems Upgrade:** Ensure back-office settlement systems, pricing feeds, and risk management software can properly ingest, model, and report on any *new* asset classes (e.g., infrastructure debt or derivatives) introduced in the new strategy.
7.  **Resource Allocation:** Fulfill the CIO’s request by hiring specialist portfolio managers or quantitative analysts skilled in the newly introduced asset classes, or sourcing appropriate external managers. 

---

## Audit Trail

### Accessed Files
- `exams/SA1/September_2025/question-paper.md`
- `references/formulae-and-tables.pdf`
