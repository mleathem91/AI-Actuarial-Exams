# SA3 — September_2025 — Exam Attempt

**Model:** Gemini 3.1 Pro (High)
**Date:** 2026-02-20
**Time allocated:** 3 hours 20 minutes

---

## Question 1

### Part (i) [2 marks]

**Exposure to risk** in the context of premium earnings refers to the measure of the extent of risk that the insurer is exposed to over the policy term. It represents the proportion of the total expected risk on a policy that has already been borne by the insurer up to a specific given point in time. It is the fundamental basis on which written premium is converted into earned premium, as premiums should ideally be earned in line with the level of exposure over the lifetime of the policy to reflect the underlying pattern of risk accurately.

### Part (ii) [3 marks]

Factors that can affect the distribution of exposure to risk throughout a policy's duration include:
- **Seasonality of risk:** e.g., weather-related risks like hurricane or freeze coverage where claims are more likely in certain months of the year.
- **Nature of the underlying subject matter:** e.g., in construction or engineering policies, the risk is typically low at first, builds steadily as the structure is built and value increases, and may taper at the testing phase.
- **Reporting delays or latent risks:** e.g., some liability policies may have exposure that extends over a long period, or exposure curves skewed based on the timing of when accidents occur vs. when they are reported/manifest.
- **Legislative or economic changes:** changes during the policy period that alter the underlying propensity or severity of claims from a certain date onwards.
- **Changing value of the insured item:** for instance in mortgage indemnity or credit insurance where the outstanding balance decreases, or motor insurance where the value depreciates, making the risk profile uneven over the year.

### Part (iii) [3 marks]

Different methods used to calculate earned premium include:
- **Daily pro-rata (or 1/365ths) method:** The most exact linear approach, assuming risk is spread evenly across each day of the year. Premium is earned exactly proportionately based on the number of days the policy has been in force.
- **24ths method (or ½ monthly method):** An approximation assuming that policies are written uniformly over a month, thus on average they are written in the middle of the month. Premium is earned in 24ths (e.g. 1/24th earned in the first month).
- **8ths method (quarterly):** Similar to the 24ths method but assuming policies are written uniformly over a quarter (so on average in the middle of the quarter). Less accurate but computationally simpler.
- **Risk-apportionment method (or non-linear earning patterns):** Premium is earned in proportion to a pre-defined exposure curve instead of time mathematically. Used when the risk profile over the year is significantly non-uniform (e.g. extended warranty, construction).

### Part (iv) [3 marks]

**Advantages of earning premium linearly:**
- It is simple and easy to understand for all stakeholders (underwriters, management, policyholders).
- It is computationally straightforward to implement in IT and accounting systems.
- For many short-tail, high-volume personal lines (like standard motor or home contents), the risk is genuinely distributed fairly evenly across the year, making this a highly appropriate and accurate method without unwarranted complexity.
- It provides a smooth, predictable unwinding of premium into the profit and loss account.

**Disadvantages of earning premium linearly:**
- It does not accurately reflect reality for lines of business where the risk does not accrue evenly over time (e.g., seasonal risks, escalating construction risks).
- This mismatch can lead to profit distortions, such as front-loading or deferring profit inappropriately at reporting periods if risk isn't matched with revenue.
- Can lead to insufficient matching of revenue and claims costs, potentially leading to inaccurate reserving (e.g., misstatement of Unearned Premium Reserves) and poor management information or inadequate pricing feedback loops.

### Part (v) [6 marks]

*(Note: The question paper references exposure to risk graphs that are visually presented. Assuming the graphs depict the standard non-linear exposure patterns typical of General Insurance exams, the following lines of businesses correspond to such profiles.)*

1. **Marine Cargo / Transit Insurance (Short spike exposure):** The exposure might show a rapid spike for a short period of time (e.g., representing a specific voyage). The risk is heavily concentrated during the transit period, with minimal or zero risk before loading and after unloading.
2. **Engineering / Contractors All Risks (CAR) (Increasing curve):** An expected graph would show a gradually rising curve across an extended multi-year x-axis. The exposure at the start is low (just raw materials) and increases steadily as the construction progresses and the value of the property at risk grows, peaking near the completion phase.
3. **Extended Warranty (Back-loaded curve):** An expected graph would show a deeply back-loaded curve. During the initial period, risk is low because the manufacturer's warranty covers defaults. Exposure ramps up significantly in subsequent years as the underlying parts age and the risk of mechanical breakdown increases.
4. **Seasonal Weather or Crop Insurance (Step-function):** A clustered exposure over a 12-month x-axis. The exposure is near zero for most of the year, with a sharp concentration of risk over a specific season (e.g., hurricane season or frost season).

### Part (vi) [9 marks]

**Potential impacts of moving from a straight-line to an exposure-based earning approach:**

**(a) Quarterly earned premium income:**
The impact will depend on the mix of business and the seasonality/shape of the exposure. For portfolios that are heavily front-loaded in exposure, earned premium will be recognised more quickly in the earlier quarters post-inception, boosting income in those periods relative to the old method. Conversely, for back-loaded profiles (like extended warranties), quarterly earned premium will fall dramatically in the early quarters and only begin to be recognised much later in the policy duration. This will introduce more volatility and non-linearity into quarterly revenue streams that were previously smoothed artificially by the straight-line method.

**(b) Quarterly earned loss ratio:**
The earned loss ratio (Incurred Claims / Earned Premium) should become much more stable and accurate under the new method. Under straight-line earning, if claims were occurring rapidly during a high-exposure period but premium was only trickling in straight-line, the loss ratio would spike incorrectly (making the business look artificially unprofitable). By aligning the earned premium with the actual risk, the denominator (earned premium) will scale up concurrently with the numerator (incurred claims). This proper matching principle will result in a truer underlying reflection of the portfolio's profitability in any given quarter, reducing spurious volatility in technical results.

**(c) Claim reserves:**
There should be no direct impact on the outstanding claims reserves (for claims that have occurred) or IBNR (for claims occurred but not reported), as these are driven by the actual underlying occurrence of claims and exposure to date, not by the accounting method of earning premium. However, the Unearned Premium Reserve (UPR) will change significantly. If the business is back-loaded, the UPR will need to be held significantly larger and longer than under a straight-line basis. Conversely, there could be an impact on the Additional Unexpired Risk Reserve (AURR). If the new UPR assessment better reflects the risk, it may reduce the situations where previously inadequate (straight-line) UPR necessitated holding an offsetting AURR.

**(d) Overall profitability:**
Over the total lifetime of the cohort of policies, the ultimate overall profitability (Total Premium - Total Claims - Expenses) is entirely unchanged by this accounting change. It is merely a timing difference as to when profit is recognised. However, the timing of profit recognition will change. Depending on whether the portfolio’s overall bias is front-loaded or back-loaded, profit release might be accelerated or deferred. In a growing book of back-loaded business, the change will defer profit recognition, depressing statutory/accounting profits in the short term. This could conceptually impact tax timing, dividend capacity, and return on equity metrics.

### Part (vii) [5 marks]

**Impact of earning a 10-year warranty policy fully over 1 year (the old method):**
- **Profit distortion (Front-loading):** Earning all the premium in Year 1 while the claims are expected to materialise over Years 1-10 massively overstates profitability and revenue in the first year. The company is recognising profit for 9 years of unexpired risk that it has yet to bear.
- **Inadequate UPR / Regulatory Breaches:** At the end of Year 1, the UPR for these policies would be zero. However, the company still has 9 years of exposure on its books. This leaves a major shortfall in the combined reserves (UPR), likely triggering the need for a massive Additional Unexpired Risk Reserve (AURR) if identified by the reserving actuary. Failure to reserve properly would be a breach of accounting and regulatory standards regarding the matching principle.
- **Capital impact:** The artificial inflation of Year 1 profits would flatter the company’s retained earnings and available capital. If this 'fake' profit was distributed to shareholders as dividends, it would severely drain the company’s capital base, potentially leaving it unable to pay the actual claims emerging in Years 2 to 10.
- **Distorted management information:** The management might mistakenly believe that these warranty policies are highly lucrative (given the low claims in Year 1 against 100% of premium). This could lead to poorly informed strategic decisions, such as cutting prices to write even more unprofitable volume, leading to catastrophic losses in the long term.

---

## Question 2

### Part (i) [3 marks]

**Advantages of reinsurance:**
- **Capacity:** Allows the insurer to write larger individual risks or a greater volume of business than its own balance sheet could sustain.
- **Volatility reduction:** Smooths financial results by capping large individual losses or aggregate portfolio losses, reducing the variability of profits and making them more predictable.
- **Capital optimization:** By transferring risk, the insurer reduces its regulatory capital requirements, potentially improving the Return on Capital and freeing up capital for growth.
- **Expertise and Support:** Reinsurers often provide valuable services such as access to new markets, pricing assistance, and underwriting expertise for complex risks.

**Disadvantages of reinsurance:**
- **Cost:** It reduces overall expected profit, as the reinsurer requires a profit margin built into the reinsurance premium.
- **Credit Risk:** The insurer remains ultimately liable to the policyholder; if the reinsurer defaults, the insurer must still pay the claim but won't recover the funds.
- **Administrative burden:** Managing the reinsurance programs, tracking recoveries, and auditing processes require resources and can be complex.
- **Loss of control:** Reinsurers may impose constraints on underwriting guidelines or claim settlements.

### Part (ii) [3 marks]

**Reasons a reinsurance company could fail:**
- **Systemic Catastrophe Losses:** An unprecedented cluster of natural disasters (e.g., multiple massive hurricanes or earthquakes globally) causing massive, correlated losses that breach the reinsurer's capital boundaries.
- **Underpricing/Poor Underwriting:** Consistently inadequate pricing in a soft market environment, perhaps driven by a desire for market share over profitability.
- **Reserve Deterioration:** Historic long-tail liabilities emerging much worse than modeled (e.g., mass torts, asbestos, social inflation), leading to massive retrospective reserve strengthening that wipes out capital.
- **Asset/Investment Losses:** Poor investment strategy, such as exposure to a market crash, toxic assets, or severe mismatches in asset-liability duration.
- **Counterparty/Retrocession Failure:** The reinsurer's own reinsurance (retrocessionaries) failing to pay, leaving the reinsurer holding the gross loss footprint unmitigated.

### Part (iii) [6 marks]

**(a) Impact on companies who bought Quota Share reinsurance:**
A quota share reinsurer takes a fixed percentage of all premiums and all losses from the ground up.
- **Immediate capital gap:** The insurer will instantly see a drop in its capital position because it can no longer rely on the failed reinsurer's capital to support the percentage of the book written.
- **Gross liability realization:** The primary insurer remains liable for 100% of the policyholder claims. Thus, for every small, regular claim that occurs, the insurer must pay the full amount without receiving the quota share recovery it was expecting. Given frequency is high in QS, this creates a major and immediate cash flow drain.
- **Unearned Premium Risk:** The primary insurer will have ceded a large block of unearned premium to Company R. It will now need to replace the cover for the unexpired portion of the risks, likely paying double for the same risk, impacting immediate profitability.

**(b) Impact on companies who bought Excess of Loss (XL) reinsurance:**
XL reinsurance only responds if individual claims (or aggregate losses) breach a very high deductible.
- **Exposure to severe volatility:** The insurer is suddenly exposed to catastrophic or large individual losses entirely on a net basis. While daily attritional claims are unaffected, a single large industrial fire or storm could now threaten the primary insurer's solvency.
- **Capital requirement spike:** Under regulatory regimes (like Solvency II), large loss / catastrophe risk modules will drastically increase the capital requirement since the risk mitigation effect of the XL treaty is gone.
- **Less immediate cash flow impact (but extreme tail risk):** Unlike the QS scenario, there may be no immediate cash flow drains if large losses haven't occurred yet, but the insurer is operating "naked" on the limits. If large losses have already occurred but recoveries are pending, the write-down of those specific large reinsurance recoverables will cause an immediate painful hit to the balance sheet.

### Part (iv) [6 marks]

**Actions Company C could take to limit its exposure to future reinsurance company failure:**
1. **Diversification of Reinsurers (Panel approach):** Instead of placing treaties with a single reinsurer, split the placement across a panel of many reinsurers (e.g., 10% shares across 10 companies) to ensure no single failure is ruinous.
2. **Strict Credit Rating Criteria:** Implement robust internal guidelines requiring reinsurers to maintain a minimum credit rating (e.g., A- or better by S&P/AM Best) and constantly monitor these ratings to downgrade exposures proactively.
3. **Collateralisation and Funds Withheld:** Require reinsurers, especially lower-rated ones or for long-tail lines, to post collateral (letters of credit, trust accounts) for the value of the reserves. Alternatively, use a "funds withheld" arrangement where the insurer holds onto the premium to pay claims, only releasing the net profit to the reinsurer.
4. **Shorter Tail / Commutations:** Vigorously pursue the commutation of old reinsurance treaties for long-tail business. By settling present value and taking the cash now, the future credit risk on those long-tail claims is eliminated.
5. **Alternative Risk Transfer (ART):** Utilize the capital markets instead of traditional reinsurers, such as issuing catastrophe bonds. Cat bonds are fully collateralised upfront, completely eliminating credit risk for the insurer.
6. **Limit overall reliance on reinsurance:** Strategy shift toward retaining more risk (higher deductibles or lower QS cessions), reliant on strengthening its own capital base, thus structurally reducing the amount of credit risk in its business model.

### Part (v) [3 marks]

**Most appropriate action for Company C:**
I recommend a combination of **Diversification of the Reinsurance Panel** combined with **Strict Credit Rating Criteria**.
*Reasoning:* These two actions form the standard bedrock of prudent reinsurance risk management for a primary insurer. While tools like fully collateralised Cat Bonds (Alternative Risk Transfer) eliminate credit risk entirely, they are very expensive to structure and usually only viable for peak catastrophe perils, not daily working excess of loss or quota share programs. Similarly, demanding full collateral or "funds withheld" from highly-rated traditional reinsurers is difficult as they may refuse to write the business or charge exorbitant premiums. Therefore, keeping the traditional reinsurance model but rigidly enforcing a highly-rated, widely diversified panel ensures that the insolvency of one reinsurer only hurts a small percentage of the recoveries, keeping the impact well within Company C's risk tolerance without significantly damaging their commercial ability to secure capacity at sensible prices.

### Part (vi) [4 marks]

**Reasons Company Y (a legacy acquirer) is willing to accept liabilities:**
1. **Claims management expertise:** Company Y specializes in running off business and believes it can manage the claims process much more efficiently, settling claims faster and for lower amounts than the primary insurer originally reserved, capturing the difference as profit.
2. **Investment returns:** Company Y will receive a large upfront portfolio transfer premium (the assets backing the reserves). It may believe it can achieve a higher investment return on these assets over the payout period than the pricing assumptions implied.
3. **Economies of scale:** A specialist run-off company does not have the overheads of writing new business (no underwriters, no marketing budgets). Combining many portfolios together allows them to aggressively spread fixed administrative costs across a huge base of run-off claims.
4. **Capital synergies / Diversification:** The acquired portfolio might provide diversification benefits against Company Y’s existing back-book of liabilities, allowing them to hold less regulatory capital against the risks than the standalone primary insurer had to.

### Part (vii) [4 marks]

**Factors affecting the transfer price in a loss portfolio transfer:**
- **Actuarial estimate of the ultimate liabilities:** The central, best estimate of the remaining unpaid claims (including IBNR). This is the foundation of the price.
- **Risk Margin / Capital requirements:** The amount of capital Company Y must hold to support the volatility of the run-off. They will charge for the cost of tying up this capital.
- **Discount rate / Investment yield:** The long-tail nature of the liabilities means they will be heavily discounted. The expected investment returns Company Y anticipates making on the assets transferred will significantly reduce the premium required.
- **Claims handling expenses:** The estimated future cost of administering the run-off and paying claims staff over many years.
- **Negotiating power / Motivation:** If the primary insurer is desperately motivated to rid themselves of the risk (e.g., to free up capital quickly), Company Y can dictate a higher transfer price.

---

## Question 3

### Part (i) [2 marks]

**Benefits of expanding sale of insurance to another country:**
- **Diversification of risk:** Combining uncorrelated geographic hazards and economic cycles reduces overall portfolio volatility and aggregate capital requirements.
- **Growth and increased revenue:** Access to new customer bases and market segments, especially valuable if the domestic market (Country A) is highly saturated or heavily regulated.

### Part (ii) [6 marks]

**Strategies Company Z can take to start selling in foreign Country B:**
1. **Greenfield Operation (Branch/Subsidiary):** Setting up a completely new entity from scratch in Country B. This provides full control over the brand, underwriting, and culture but takes a long time, requires heavy upfront capital, and lacks local market knowledge initially.
2. **Acquisition:** Buying an existing, locally licensed insurer in Country B. This grants immediate access to a customer base, local market data, regulatory licenses, and local staff expertise. However, it is expensive, carries integration/culture-clash risks, and may involve inheriting legacy reserve issues.
3. **Joint Venture / Strategic Alliance:** Partnering with a local entity (like a local bank or a non-insurance corporation in Country B). The partner provides local distribution and knowledge, while Company Z provides the insurance expertise and capital. This shares the risk and reward.
4. **Selling on a Freedom of Services / Cross-Border basis (if regulations allow):** Writing policies for Country B residents from the Country A entity without tracking a physical footprint. Very cheap and low risk to set up, but difficult to establish brand presence, handle local claims effectively, or navigate unharmonised regulations.
5. **Managing General Agent (MGA):** Delegating underwriting authority to an established local MGA in Country B. The MGA acts as the intermediary, leveraging their local networks while Z provides the paper and capital. Provides rapid market entry and utilises local skills with less friction than a full acquisition.

### Part (iii) [3 marks]

**Advantages and disadvantages of aggregator sites (for the insurer):**
*Advantages:*
- Instantly grants access to a massive volume of potential customers without needing a massive standalone advertising/brand budget.
- Lower cost of acquisition per policy compared to setting up a large direct marketing infrastructure or paying ongoing agent commission trails.

*Disadvantages:*
- Extreme price sensitivity; because customers rank merely by cheapest premium, it forces commoditization and severely damages brand loyalty and customer retention.
- "Winner's curse" risk; the insurer quoting the cheapest rate is likely to attract the worst risks (that models may have underpriced), damaging the loss ratio. High cost of aggregator fees per quote that is actually bound.

### Part (iv) [3 marks]

**Advantages and disadvantages of selling through insurance agents (for the customer):**
*Advantages:*
- **Personalised advice:** Complex needs are explained, ensuring the customer gets a policy precisely tailored to their risk profile, avoiding underinsurance or confusing policy exclusions.
- **Claims advocacy:** In the event of a loss, the agent can act as an intermediary, helping guide the customer through the claims process and advocating on their behalf against the insurer.

*Disadvantages:*
- **Higher cost:** The policies are typically more expensive as the customer is indirectly paying for the hefty commission or fee the agent extracts from the premium.
- **Conflict of interest / Bias:** Agents may not offer the whole market view. They might steer customers towards policies that offer the agent the highest commission rather than the product that is genuinely the best or cheapest for the customer.

### Part (v) [5 marks]

**Impact of distribution channels on pricing for A (online/aggregators) vs B (agents):**
- **Expense loading:** Pricing in Country B will require a significantly higher expense load to cover the persistent, heavy commission structures demanded by physical agents. Pricing in Country A primarily needs to cover fixed IT/direct marketing overhead costs, or the flat per-policy fee of an aggregator.
- **Price elasticity and margin:** Country A's aggregator environment is hyper-competitive and highly price elastic. Insurers must load incredibly thin profit margins into the price, as being even slightly off the top screen means zero sales. Conversely, the agent model in Country B relies on relationships and advice; price elasticity is lower, allowing Company Z to potentially build in slightly higher profit margins as customers are less likely to shop around purely on rate.
- **Risk segmentation and complexity:** In Country A, online pricing algorithms must be highly sophisticated, utilizing massive arrays of rating factors to avoid anti-selection. The price calculates instantly without human intervention. In Country B, pricing might be simpler or involve more discretionary underwriter adjustments, as the agent can visually inspect the risk (moral hazard checking) and provide qualitative context that algorithms cannot.
- **Conversion assumptions:** Country A pricing models will see millions of quotes but single-digit conversion rates, requiring careful treatment of IT quoting costs. Country B will see far fewer quotes but much higher conversion rates due to the agent's pre-qualification work.

### Part (vi) [6 marks]

**Impact of working with different currencies on:**

**(a) Reserving [2 marks]**
If Company Z holds consolidated reserves in Currency A but liabilities are emerging in Currency B, they are exposed to translation risk. An adverse move (strengthening) of Currency B will suddenly make the reserves held (if purely in A) inadequate to meet the localized claims, requiring constant revaluation of reserve estimates purely driven by FX movements.

**(b) Pricing [2 marks]**
Prices set in Country B must account for local claims inflation which might be highly correlated with currency devaluation. Furthermore, if Company Z's headquarters demands a required return on capital denominated in Currency A, pricing models in Country B must build in an FX margin to ensure the profit repatriated to A still hits target hurdles, making the policies more expensive to locals.

**(c) Capital modelling [2 marks]**
The capital model now needs an entirely new risk module: Foreign Exchange (FX) Risk. The model must assess the dependency/correlation between the exchange rate fluctuations, local claims inflation, and local asset returns. A mismatch between the currency of the regulatory capital held and the currency of the underlying liabilities creates severe volatility in the solvency ratio.

### Part (vii) [3 marks]

**Other areas of Company Z impacted by multiple currencies:**
- **Asset Liability Matching (ALM) / Investment Strategy:** The investment function must actively manage currency hedging. To immunise the balance sheet, they broadly need to back the Currency B liabilities with Currency B assets.
- **Accounting and Financial Reporting:** Consolidating multi-currency operations creates complex financial reports. Profit & Loss items must be converted at average rates, while balance sheets at spot rates, causing "Foreign Exchange Translation Reserves" to bounce around the equity position confusingly.
- **Reinsurance Strategy:** Z will need to decide whether to purchase reinsurance in Currency A or Currency B. If they buy excess of loss cover in Currency A for Currency B risks, the retention level effectively acts as a moving target, meaning they might accidentally retain too much risk if B weakens.

### Part (viii) [6 marks]

**Impact of sharp devaluation of Currency B relative to Currency A on Company Z:**
- **Translation of Profits:** Any profit generated in Country B, when translated back to Currency A for consolidated reporting and dividends, will be worth significantly less. This directly hurts the group RoE and hurts consolidated earnings.
- **Asset / Liability Mismatches:** If Company Z had failed to perfectly match its assets and liabilities in Currency B (e.g., funding Country B's operations with capital held in Country A), they are exposed. If they held Currency B assets against Currency A capital, the fall in B wipes out capital. Conversely, if Currency B claims were backed by Currency A assets, a devaluation of B actually creates a translation windfall gain.
- **Import Inflation on Claims:** A sharp devaluation of Currency B against A likely signals broader weakness of B against all global currencies. If insurance claims in Country B involve importing parts (e.g., motor crash repairs requiring foreign car parts, property repairs requiring foreign materials), the cost of these claims in Currency B will hyperinflate. The frequency severity model will break.
- **Pricing Adequacy:** Because of the sudden import claims inflation, the historical premiums collected in Currency B were likely drastically underpriced relative to the new severity reality. Existing policies on the books will run at a heavy loss ratio until premiums can be renegotiated/increased.
- **Reinsurance Issues:** If local Country B risks are protected by a reinsurance treaty denominated in Currency A, the local claims (which are now smaller in A terms) might fail to breach the XL attachment points, leaving Company Z to absorb far more attritional net loss than anticipated.

### Part (ix) [6 marks]

**Other potential effects of the war in Country B on Company Z:**
- **Direct War Exclusion Clashes:** War is typically a standard exclusion in property/casualty policies. However, managing the public relations of declining thousands of claims, or handling fierce legal disputes over whether an event was "war" or "riot/civil commotion" will drain legal resources and potentially incur regulatory wrath or state mandates to pay.
- **Economic Collapse and Premium Volume:** War typically devastates a country's economy. Businesses close, car sales plummet, and construction halts. Consequently, the volume of new business and renewal premium Company Z can write in Country B will collapse.
- **Operational disruption:** If Company Z has a local office, staff safety is paramount. Staff may be drafted, flee, or unable to work. Local IT infrastructure, power, and banking systems may go offline, making it impossible to collect premiums, assess claims, or pay out money safely.
- **Asset Defaults / Investment write-downs:** Any local investments held by Company Z in Country B (e.g., Country B government bonds, local corporate equities, or local property) to match local liabilities will likely suffer massive defaults or severe impairment in value, destroying the asset-side of the balance sheet.
- **Sanctions and Compliance Risk:** The geopolitical situation surrounding the war may result in International Sanctions being placed on Country B or certain entities within it. Company Z’s central compliance team in Country A will scramble to ensure no claims or premiums are transacted with blocked individuals, risking massive fines if breached.
- **Surge in specific types of claims:** While standard property might have war exclusions, other lines might be highly exposed. For example, if they write Life/Health/Workers Compensation locally, war exclusions are harder to uphold to civilians. If they write Cyber insurance, hostilities often coincide with major state-sponsored cyber attacks on businesses.

---

## Audit Trail

### Accessed Files
- `exams/SA3/September_2025/question-paper.md`
- `scripts/convert_pdf_to_md.py`
