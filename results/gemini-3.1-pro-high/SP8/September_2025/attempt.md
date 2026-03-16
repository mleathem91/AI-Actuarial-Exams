# SP8 — September 2025 — Exam Attempt

**Model:** Gemini 3.1 Pro (High)
**Date:** 2026-02-20T17:19:26Z
**Time allocated:** 3 hours 20 minutes

---

## Question 1

Let $n$ be the number of policies and $N_{full}$ be the number of policies required for full credibility under the classical (square root) approach.

Under the square root rule for partial credibility, the credibility factor $Z_{sq}$ is given by:
$$Z_{sq} = \sqrt{\frac{n}{N_{full}}}$$

We are given that full credibility is achieved when there are 100 policies, so $N_{full} = 100$.
When $n = 25$, the square root credibility factor is:
$$Z_{sq} = \sqrt{\frac{25}{100}} = \sqrt{0.25} = 0.5$$

The Bühlmann–Straub credibility factor $Z_{BS}$ is calculated using the formula:
$$Z_{BS} = \frac{n}{n + k}$$
where $k$ is the parameter representing the ratio of expected process variance (EPV) to the variance of the hypothetical means (VHM).

We are told that when $n = 25$, $Z_{BS}$ is equal to $Z_{sq}$:
$$\frac{25}{25 + k} = 0.5$$
$$25 = 0.5(25 + k)$$
$$50 = 25 + k$$
$$k = 25$$

The question asks for the Bühlmann–Straub credibility factor under the full credibility standard, which corresponds to $n = 100$ policies.
$$Z_{BS} = \frac{n}{n + k} = \frac{100}{100 + 25} = \frac{100}{125} = 0.8$$

The Bühlmann–Straub credibility factor under the full credibility standard is **0.8**.

---

## Question 2

### Part (i)

Data the AI system may collect from the photographs to provide quotations:
*   **Property Type and Size:** Whether the home is detached, semi-detached, or an apartment, as well as an estimation of the square footage, number of stories, and general footprint.
*   **Construction Materials:** The predominant building materials used for the exterior walls (e.g., brick, stone, wood siding, stucco) which affects fire risk and rebuild costs.
*   **Roof Characteristics:** The type of roof (e.g., pitched, flat), the materials used (e.g., tiles, shingles), and the apparent condition/age of the roof, indicating susceptibility to wind or water damage.
*   **External Features and Hazards:** Presence of features that increase liability or property risks, such as a swimming pool, trampoline, overhanging large trees, or proximity to bodies of water.
*   **Condition and Maintenance:** Visible signs of disrepair, such as cracked walls, peeling paint, accumulated debris in gutters, or a poorly maintained yard, indicating potential moral hazard or higher likelihood of claims.
*   **Security and Protection:** Presence of visible security measures like burglar alarms, surveillance cameras, secure window locks, or a solid perimeter fence.
*   **Interior Features and Contents:** The quality of the interior finishings (e.g., hardwood floors, custom kitchen cabinets) which drives the sum insured, and the presence of high-value items like expensive electronics, art, or antique furniture.
*   **Heating and Electrical:** If visible, the type and apparent age of heating systems (e.g., wood-burning stoves, open fireplaces) and electrical panels or wiring condition.

### Part (ii)

Challenges the insurer may face while using this AI system to quote for commercial policies:
*   **Heterogeneity of Commercial Risks:** Commercial properties are far more diverse than residential homes (e.g., a chemical manufacturing plant versus a standard office block). An AI trained on straightforward residential features will struggle to categorize and assess the wide variety of commercial operations correctly.
*   **Scale and Complexity:** Commercial buildings are often significantly larger and structurally more complex. A specified number of photographs cannot adequately capture the entirety of a large warehouse or factory, leading to severe blind spots in the risk assessment.
*   **Hidden Hazards:** Many of the most critical risks in commercial properties are internal or operational (e.g., specialized heavy machinery, storage of hazardous or flammable materials, complex industrial processes) which cannot be reliably identified from general photographs.
*   **Regulatory and Compliance Life Safety:** Commercial properties are subject to strict fire and safety regulations (e.g., sprinkler systems, fire doors, extraction systems). Verifying compliance with these standards requires specialized inspections and documentation, not just photos.
*   **Business Interruption (BI) and Liability:** Commercial pricing heavily relies on BI exposures (which depend on financial data like revenue and profit margins) and Public/Employers' Liability (which depends on payroll, footfall, and operational practices). Photographs provide zero data for these crucial pricing components.
*   **Lack of Training Data:** To build a robust AI model, the insurer needs thousands of labelled images of commercial properties linked to claims experience. Obtaining enough relevant, high-quality historical image data for diverse commercial risks is highly challenging.
*   **Dynamic Nature of Commercial Risks:** A commercial operation can change its processes, inventory levels, or layout frequently. A snapshot in time (photographs) may quickly become outdated, whereas a home's characteristics reflect a much more static risk profile.
*   **Fraud or Non-Disclosure:** A business owner could deliberately manipulate what is photographed, hiding high-risk areas or dangerous operations, which is much harder to detect in a sprawling commercial complex than in a standard home.
*   **Lack of Explainability / Intermediary Resistance:** Commercial insurance is often sold through specialized brokers who will demand transparency in how the premium was calculated. A "black box" AI generating a quote based on photos may face severe pushback if the underwriter or broker cannot explain the specific rating factors to the client.
*   **Integration with Other Rating Factors:** Assuming the AI handles only the physical property aspects, the system must be seamlessly integrated with other traditional commercial rating engines (e.g., taking standard industrial codes, claims history, financial health) to produce a coherent final quote, increasing IT complexity.

---

## Question 3

### Part (i)

Potential impact of large infrequent cyber claims on the frequency–severity pricing model:
*   **Distortion of Severity Distribution:** Large, infrequent claims will cause the empirical severity distribution to exhibit a very heavy tail. Traditional parametric severity distributions (e.g., Lognormal, Gamma) often fail to fit this extreme tail adequately, resulting in the model severely underestimating the true expected severity and extreme percentiles.
*   **Parameter Volatility and Uncertainty:** Because these claims are infrequent (a small data sample in the tail), the parameter estimates for the severity distribution will be highly volatile and heavily influenced by the inclusion or exclusion of one or two large claims. This leads to immense parameter error in the pricing model.
*   **Breakdown of Attritional vs. Large Claim Assumptions:** If the model does not explicitly separate attritional claims from large claims, fitting a single distribution will result in an overestimation of the frequency/severity of small claims to compensate for the tail, creating a poorly fitting model across all claim sizes.
*   **Contagion and Independence Assumptions:** Frequency models (like Poisson) typically assume claim events are independent. However, large cyber claims often involve systemic risks or systemic accumulation (e.g., a widespread ransomware attack exploiting a common vulnerability). The model's failure to account for this contagion will lead to a gross underestimation of the variance of the frequency distribution.
*   **Impact on Risk Premium and Volatility:** The calculated expected risk premium will become highly unstable from year to year as new large claims emerge. The overall variance of the aggregate loss distribution will be immense, drastically increasing the required risk margins and cost of capital for the portfolio.

### Part (ii)

How the insurance company may address the issues in part (i):
*   **Separate Modelling of Attritional and Large Claims:** Split the historical data into attritional claims (below a chosen threshold) and large claims. Model the attritional claims using a standard frequency-severity GLM approach, and model the large claims separately.
*   **Use Extreme Value Theory (EVT):** For the large claims component, fit an extreme value distribution, such as the Generalized Pareto Distribution (GPD), to the tail of the data above the specified threshold to better capture the heavy-tailed nature of the cyber severity risk.
*   **Scenario Testing and Stochastic Modelling:** Since historical data is sparse, the insurer should supplement the data by running specific forward-looking cyber disaster scenarios. Stochastic modelling incorporating expert judgement regarding the frequency and severity of these hypothetical catastrophic events should be used.
*   **Incorporate External Vendor Models:** Purchase access to third-party cyber catastrophe models. These models use cybersecurity threat intelligence, network topologies, and simulated attack vectors to estimate the frequency and severity of systemic, large-scale cyber events, providing a view of risk not present in the insurer's limited historical data.
*   **Reinsurance Adjustments:** The pricing model should calculate the gross premium but then be run through the company's reinsurance structure. By buying non-proportional (Excess of Loss) reinsurance to cap the large claims, the insurer can price the net realistic risk and appropriately price the cost of the reinsurance charge into the policyholder's premium.
*   **Apply Explicit Loadings for Uncertainty:** Given the immense parameter error and model error surrounding large cyber claims, the pricing actuary must apply significant, explicit risk margins or safety loadings on top of the expected risk premium to compensate for the uncertainty.
*   **Refine Rating Factors and Underwriting Rules:** Analyze the root causes of the historical large claims to identify new, predictive rating factors (e.g., lack of multi-factor authentication, specific industry sectors, use of legacy software) and incorporate these into the GLM. Simultaneously, use these insights to tighten underwriting guidelines to simply decline risks prone to large claims.

---

## Question 4

### Part (i)

Reasons for Company U wishing to launch this emissions insurance product:
*   **First Mover Advantage and Differentiation:** Emissions insurance is a highly innovative product. Launching it allows Company U to differentiate itself in a highly competitive, commoditized marine hull market, presenting itself as a market-leading, forward-thinking insurer.
*   **Cross-Selling and Client Retention:** By offering this as an extension to existing marine hull policies, it provides a powerful cross-selling opportunity. It increases stickiness, as clients are more likely to renew their main hull policies if Company U is the only provider offering this comprehensive, bundled coverage.
*   **Addressing Emerging ESG Client Needs:** Global shipping companies face immense pressure from regulators (e.g., IMO 2020/2050 targets) and stakeholders to reduce their carbon footprint. This product directly addresses the clients' growing Environmental, Social, and Governance (ESG) concerns and financial risks tied to missing emissions targets.
*   **Diversification of Risk:** While correlated with the underlying marine hull risk (e.g., a breakdown causes both a hull claim and an emissions claim), the ultimate financial payout size depends on the price of carbon credits, not repair costs. This introduces a new, diversifying risk vector into Company U's portfolio.
*   **Profitability and Margin:** Because it is a niche, novel product with little direct competition, Company U can likely charge a premium with a substantial profit margin and uncertainty loading, avoiding the severe price competition seen in standard marine lines.
*   **Strategic Data Gathering:** Offering this product requires clients to submit detailed emissions and operational data. This allows Company U to build a proprietary, highly valuable dataset on marine emissions profiles, which can be leveraged later for more accurate pricing of transition risks across its entire marine portfolio.

### Part (ii)

Limitations in using 2 years of total excess emissions and annual revenue data to price the risk premium:
*   **Insufficient Data History Length:** Two years is a very short time horizon to capture the true underlying frequency and severity of "unforeseen deviations." Major marine breakdowns or severe weather diversions (which would cause the largest excess emissions) are low-frequency events that require a much longer return period to model accurately.
*   **Revenue is a Poor Exposure Proxy:** Annual revenue has a very weak, potentially spurious correlation with the actual risk of unforeseen journey deviations. A company could have high revenue from short, safe coastal trips, or lower revenue from long, hazardous ocean crossings. A much more appropriate measure of exposure would be total distance traveled, number of journeys, or baseline fuel consumption.
*   **Changing Regulatory and Technological Baselines:** The definition of what constitutes "excess" emissions depends on heavily fluctuating environmental regulations and baseline standards. Furthermore, the marine industry is rapidly transitioning to differing fuel types (e.g., LNG, biofuels), meaning the emissions profile from two years ago may be completely irrelevant to the prospective policy period.
*   **Aggregation Obscures Frequency and Severity:** The data only provides "total" excess emissions per client over the year. This aggregation makes it impossible for the pricing actuary to separate the number of deviation events (frequency) from the size of the emissions per event (severity), severely hindering the construction of a robust frequency-severity model.
*   **Lack of Specific Rating/Risk Factors:** The data lacks the granual detail needed to differentiate risks. Factors crucial for assessing the likelihood of a deviation—such as vessel age, vessel type/class, specific voyage routes taken, seasonality, and maintenance history—are missing. This will lead to flat pricing and severe adverse selection.
*   **Ignores the Price of Carbon Credits:** The actual financial claim amount will be driven not just by the volume of excess emissions, but by the market value of the carbon credits at the time of the claim. Historical emissions data alone provides no insight into the extreme volatility of carbon market prices, which must be incorporated into the risk premium.

---

## Question 5

### Part (i)

Benefits provided under a product liability policy to a cell phone manufacturer:
*   **Legal Defence Costs:** Covers the substantial costs of instructing lawyers, gathering expert witnesses, and court fees required to defend the manufacturer against claims of injury or damage, regardless of whether the manufacturer is ultimately found liable.
*   **Compensation for Bodily Injury:** Pays damages and negotiated settlements awarded to third parties (consumers) who suffer physical harm caused by a defect in the cell phone (e.g., severe burns or lacerations caused by a lithium-ion battery overheating and exploding).
*   **Compensation for Third-Party Property Damage:** Covers settlements awarded to third parties if the defective cell phone causes damage to their property (e.g., a phone catching fire while charging and destroying the user's home or vehicle).
*   **Public Relations / Crisis Management Costs:** Provide funding to hire specialized crisis management or public relations firms to mitigate reputational damage following a high-profile product failure (e.g., managing the press surrounding exploding batteries).
*   **Product Recall Expenses (often as an extension):** Covers the logistical costs of withdrawing the defective cell phones from the market. This includes the cost of publishing recall notices, transporting the products back to the manufacturer, and disposing of or repairing the items.
*   **Regulatory Investigation Costs:** May offer protection for the legal and administrative costs involved if a government consumer safety body launches a formal investigation into the defective cell phones.

### Part (ii)

Potential concerns with using an external database of global news articles for product liability cases:
*   **Reporting Bias towards Severe/Sensational Claims:** News organizations disproportionately report on catastrophic, large-scale, or highly unusual product failures involving massive global brand names. The database will severely under-represent the high-frequency, low-severity attritional claims that are typical and highly relevant for a *small* electronics manufacturer.
*   **Lack of Actuarial Granularity and Detail:** News articles are not written for actuaries. They typically lack the critical pricing data points required, such as the exact final settlement figure (often conflating initial demands with actual payouts), the breakdown of damages versus defense costs, the number of units sold (the exposure base), or the policy limits and deductibles involved in the case.
*   **Incompleteness due to Confidentiality:** The vast majority of product liability claims are settled out of court. These settlements almost universally include strict Non-Disclosure Agreements (NDAs). Therefore, a database relying on news articles will miss a massive portion of the true claims environment.
*   **Inaccuracy and Sensationalism:** The information contained in early news reports is often inaccurate, speculative, or highly sensationalized. Relying on this data could lead the model to incorporate incorrect assumptions about the financial severity or root cause of the liability incidents.
*   **Categorization and Relevance Issues:** Generating relevant insight requires filtering the database down to "small electronics manufacturers." A news database may lump all "electronics" together (e.g., a massive flaw in an industrial power grid component grouped with a faulty cell phone charger), making it difficult to extract data highly relevant to the specific target market.
*   **Jurisdictional Inconsistency and Legal Environments:** Product liability awards are heavily dependent on the legal jurisdiction (e.g., the US tort system yields vastly higher punitive damages than European courts). A global news database may mix these diverse legal environments. If the insurer only operates in specific, less litigious regions, using global news data will result in severe overpricing.
*   **Timeliness and Settlement Lag:** There is often a multi-year lag between a product defect causing injury and the final court settlement being reported in the news. Analyzing today's news articles reflects the manufacturing landscape and safety standards of several years ago, failing to capture current or emerging risks.
*   **Duplication and Double Counting:** A major product liability case will be reported by hundreds of different news outlets globally over the lifecycle of the tort. Without incredibly sophisticated deduplication algorithms, the insurer risks counting the same event multiple times, vastly overestimating the frequency of large claims.

---

## Question 6

### Part (i)

**Method of Moments Estimation**

First, calculate the sample mean ($m_1$) and sample variance ($s^2$) of the given data. We have $n=9$ observations.

Data ($x_i$): 704.13, 469.59, 941.01, 360.37, 671.67, 715.76, 784.12, 454.46, 868.92

Sum of $x_i$:
$\sum x_i = 704.13 + 469.59 + 941.01 + 360.37 + 671.67 + 715.76 + 784.12 + 454.46 + 868.92 = 5970.03$

Sample mean ($m_1$ = First Moment):
$m_1 = \bar{x} = \frac{5970.03}{9} = \mathbf{663.3367}$

To find the variance, calculate the sum of squares ($\sum x_i^2$):
$704.13^2 = 495799.04$
$469.59^2 = 220514.77$
$941.01^2 = 885499.82$
$360.37^2 = 129866.54$
$671.67^2 = 451140.59$
$715.76^2 = 512312.38$
$784.12^2 = 614844.17$
$454.46^2 = 206533.90$
$868.92^2 = 755021.93$
Sum of $x_i^2$ = 4,271,533.14

Second sample moment ($m_2$):
$m_2 = \frac{4271533.14}{9} = 474614.793$

Sample variance using the method of moments (population variance formula):
$Var(x) = m_2 - m_1^2 = 474614.793 - (663.3367)^2 = 474614.793 - 440015.580 = \mathbf{34599.213}$

**(1) Exponential Distribution Parameters**
The Exponential distribution has parameter $\lambda$.
The theoretical mean is $E[X] = \frac{1}{\lambda}$.
Equating the theoretical mean to the sample mean:
$\frac{1}{\lambda} = 663.3367$
$\lambda = \frac{1}{663.3367} = \mathbf{0.0015075}$

**(2) Lognormal Distribution Parameters**
The Lognormal distribution has parameters $\mu$ and $\sigma^2$.
The theoretical mean is $E[X] = \exp(\mu + \frac{\sigma^2}{2})$.
The theoretical variance is $Var[X] = \exp(2\mu + \sigma^2)(\exp(\sigma^2) - 1) = (E[X])^2(\exp(\sigma^2) - 1)$.

Equating theoretical moments to sample moments:
1. $E[X] = 663.3367$
2. $Var[X] = 34599.213$

Using the variance equation:
$34599.213 = (663.3367)^2 (\exp(\sigma^2) - 1)$
$34599.213 = 440015.580 \times (\exp(\sigma^2) - 1)$
$\exp(\sigma^2) - 1 = \frac{34599.213}{440015.580} = 0.0786318$
$\exp(\sigma^2) = 1.0786318$
Take the natural logarithm of both sides:
$\sigma^2 = \ln(1.0786318) = \mathbf{0.07569}$

Now substitute $\sigma^2$ back into the mean equation:
$\exp(\mu + \frac{0.07569}{2}) = 663.3367$
$\mu + 0.037845 = \ln(663.3367)$
$\mu + 0.037845 = 6.49728$
$\mu = 6.49728 - 0.037845 = \mathbf{6.4594}$

* Exponential parameter: $\lambda = 0.001508$
* Lognormal parameters: $\mu = 6.4594$, $\sigma^2 = 0.07569$

### Part (ii)

Why the model outputs in part (i) may not be suitable for predicting the average claim size:
*   **Extremely Small Sample Size:** Fitting a distribution with only 9 data points introduces immense parameter uncertainty. The estimates for the mean, and especially the variance, will be highly unreliable and likely not representative of the true underlying population.
*   **Modelling Averages vs Individual Claims:** The student is fitting severity distributions (Lognormal, Exponential) to the *average* claim size in a year, rather than to the individual claim sizes. By the Central Limit Theorem, the distribution of the average of a large number of independent claims will tend towards a Normal distribution, regardless of the underlying individual claim size distribution. Therefore, forcing a heavy-tailed Lognormal or strictly positive right-skewed Exponential onto aggregated averages is theoretically flawed.
*   **Failure to Adjust for Claims Inflation:** The data spans 9 years (2016-2024), during which the cost of home repairs and rebuilds will have undoubtedly been impacted by claims inflation. Fitting a stationary distribution to unadjusted, raw historical data ignores this fundamental temporal trend. The model will systematically over-predict early years and under-predict future years.
*   **Heteroskedasticity and Varying Volumes:** The variance of the average claim size in a given year is inversely proportional to the number of claims that occurred in that year. A year with 10,000 claims will have a much more stable average than a year with 100 claims. The Method of Moments treats every year as an equally weighted data point, ignoring exposure/volume differences.
*   **Method of Moments Limitations:** The Method of Moments estimator is generally less robust and efficient than Maximum Likelihood Estimation (MLE). It is highly sensitive to outliers, meaning a single year with an unusually high or low average will severely skew the $\mu$ and $\sigma^2$ parameters.
*   **Lacks Predictive Covariates:** Fitting a single univariate distribution ignores the underlying drivers of the average claim size (e.g., changing mix of business, shifts in the geographical spread, changes in policy deductibles over the 9 years). A predictive model should ideally utilize a GLM framework incorporating these rating factors.

---

## Question 7

### Part (i)

**Description:**
A swing rated contract is an insurance or (more commonly) reinsurance agreement where the final premium paid is retrospectively adjusted based on the actual loss experience of the policyholder during the coverage period. 
**Purpose:**
Its primary purpose is to closely align the premium charged with the actual risk transfer. It is used when a risk is heavily exposed to moral hazard (incentivizing the insured to implement strong loss control/risk management to lower their premium) or when the expected level of losses is highly uncertain up front, allowing both parties to share in the risk and reward of the emerging experience.
**Main types:**
*   **Pure/Proportional Swing Rate:** The final premium varies continuously and proportionally with the actual losses (e.g., Premium = Losses $\times$ Load factor) subject to predefined floor (Minimum Premium) and ceiling (Maximum Premium) caps.
*   **Stepped Swing Rate:** The premium adjusts in discrete jumps based on pre-agreed loss ratio bands or thresholds, rather than continuously.

### Part (ii)

How the pricing model may be adjusted to incorporate a swing rated contract:
*   **Shift from Expected Loss to Full Distribution:** A traditional frequency-severity model often focuses heavily on determining the single point estimate of the expected risk premium (the mean loss). For a swing rated contract, the actuary must model the *entire distribution* of aggregate losses, because the premium calculation mechanism is non-linear (due to caps and minimums).
*   **Aggregate Loss Modelling:** The actuary must combine the frequency and severity distributions. This is typically done by building a stochastic pricing model using Monte Carlo simulation, or using numerical methods like Panjer recursion, to generate thousands of possible aggregate annual loss scenarios.
*   **Apply Swing Terms to Simulations:** For each individual simulated scenario, the actuary must take the aggregate simulated loss and apply the specific terms of the swing contract to calculate the theoretical charged premium.
    *   Formula applied is typically: Calculated Premium = (Simulated Aggregate Losses + Insurer Expenses) / Permissible Loss Ratio
*   **Apply Caps and Floors:** Crucially, within each simulation, the Calculated Premium must be strictly constrained. If it falls below the Minimum Premium, it is increased to the Minimum Premium constraint. If it exceeds the Maximum Premium, it is capped at the Maximum constraint.
*   **Determine Expected Swing Premium:** The final expected risk premium to be charged upfront (or targeted as the expected return) is the mathematical average of the constrained premium results across all the simulated scenarios, not just the premium calculated on the average expected loss.
*   **Pricing the Options (Caps and Corridors):** The actuary must analyze the specific cost of the upper cap (the risk transferred entirely to the insurer when losses exceed the maximum premium equivalent) and compare it against the value of the minimum premium (the guaranteed income to the insurer even if losses are zero).
*   **Incorporate Risk Margin for Volatility:** If the swing terms leave the insurer heavily exposed to large tail losses (e.g., an unusually low Maximum Premium cap), the model must incorporate a higher explicit risk margin or cost of capital compared to a standard fixed-rate policy where premium is fully known.
*   **Cash Flow and Time Value of Money Adjustments:** Swing rated contracts usually involve an upfront deposit premium, followed by adjustment premiums paid years later as claims develop. The pricing model must incorporate a discounted cash flow component to account for the time value of money, the expected timing of claim payments, and the delayed receipt of adjustment premiums.

---

## Question 8

### Part (i)

Tests and considerations to determine if a new rating factor should be included in the traditional GLM:
*   **Statistical Significance (p-values/Standard Errors):** Examine the parameter estimates for the new rating factor. If the standard errors are small relative to the parameter estimates, and the resulting p-values (using a Wald test or t-test) are below a chosen significance level (e.g., < 0.05), it indicates the factor's effect is statistically different from zero.
*   **Deviance and Log-Likelihood Tests:** Fit a base GLM (without the new factor) and a proposed GLM (with the new factor). Calculate the change in deviance or log-likelihood. Conduct a Chi-square or Analysis of Deviance test to check if the addition of the new factor significantly improves the overall fit of the model to the training data.
*   **Information Criteria (AIC / BIC):** Compare the Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) of the base and proposed models. These metrics penalize the model for adding complexity (extra parameters). The new factor should only be included if it results in a lower AIC/BIC, indicating the improvement in fit outweighs the penalty for complexity and reduces the risk of overfitting.
*   **Out-of-Sample / Validation Testing:** Train the model with the new factor on a subset of data (training set) and test its predictive power on a hold-out unseen sample (validation set). Compare predictive accuracy metrics (e.g., Root Mean Squared Error (RMSE), Gini Coefficient, or lift charts) against the base model.
*   **Check for Multicollinearity:** Calculate the correlation matrix or use Variance Inflation Factors (VIF) to ensure the new factor is not highly correlated (aliased) with existing rating factors. High multicollinearity will lead to unstable parameter estimates and redundant information.
*   **Consistency over Time:** Run the model on different historical accident or calendar years individually. The direction and magnitude of the new factor's parameters should be relatively stable over time. If they swing wildly, the factor may merely be capturing anomalous noise in a specific year.
*   **Actuarial / Business Justification:** Ensure the factor makes intuitive sense and has a plausible causal link to the risk being priced, rather than being a spurious correlation.
*   **Cost-Benefit Analysis of Implementation:** The IT and administrative costs of collecting, storing, validating, and updating the new data field on the policy administration system must be weighed against the marginal pricing advantage it provides.
*   **Regulatory and Ethical Acceptability:** Verify that the new factor is legally permissible to use for rating in the relevant jurisdiction, complies with data protection laws (like GDPR), and does not act as a discriminatory proxy for protected characteristics.

### Part (ii)

Advantages and disadvantages of adopting unsupervised machine learning techniques instead of a traditional GLM:

**Advantages:**
*   **Uncovering Hidden Feature Relationships:** Unsupervised techniques (like K-means clustering, Principal Component Analysis (PCA), or Autoencoders) excel at analyzing massive, multidimensional datasets to find complex, non-linear patterns, groupings, and interactions that human actuaries might completely overlook when manually specifying a traditional GLM structure.
*   **Handling Unstructured and Novel Data:** Unsupervised learning is perfectly suited to ingest and extract value from vast quantities of unstructured or high-dimensionality data that small insurers are beginning to access, such as free-text claims descriptions, telematics data, or granular geographical coordinates.
*   **Powerful Feature Engineering/Dimensionality Reduction:** Techniques like PCA can rapidly reduce hundreds of correlated variables into a few key, distinct components. Clustering can group highly similar policyholders together, allowing the insurer to create a single, powerful new categorical "risk cluster profile" rating factor to drastically simplify downstream pricing.
*   **Reduction of Human Bias in Discovery:** It allows the algorithm to explore the data objectively without the actuary imposing preconceived notions or historical biases regarding which rating factors "should" group together or what the risk segments look like.

**Disadvantages:**
*   **Lack of a Defined Target Variable:** This is the critical weakness for pricing. Unsupervised learning finds structure in the *input features* only; it does not map these features to a specific target outcome variable (like claim frequency or claims severity). Therefore, it cannot directly output a predictive risk premium or estimate expected losses like a GLM can. It must be paired with a supervised learning step.
*   **The "Black Box" Problem and Interpretability:** The results of unsupervised algorithms (e.g., why an algorithm placed two risks generated in the same cluster, or what a PCA component actually represents in the real world) are notoriously difficult to interpret precisely. This makes it exceedingly difficult to explain premium changes to customers, brokers, internal management, or regulators who demand transparency.
*   **Risk of Discovering Spurious / Irrelevant Patterns:** Because there is no target variable guiding the algorithm, there is a high risk it will identify and aggressively cluster based on strong correlations in the data that are purely coincidental or entirely irrelevant to insurance risk (e.g., clustering based on alphabetical policy numbers).
*   **High Complexity and Cost:** Implementing these complex models requires massive computational power, specialized data science software, and, most importantly, highly specialized data science talent. For a "small insurance company", building and supporting this infrastructure will result in enormous operational cost increases compared to running a standard GLM.
*   **Loss of Actuarial Control:** Traditional GLMs allow the pricing actuary to constrain parameters, smooth curves manually, and override empirical results with business judgement (e.g., capping the young driver loading). Unsupervised models afford much less control to impose mandatory business or underwriting rules directly into the modeling process.
*   **Regulatory Backlash and Proxy Discrimination:** Regulators strongly prefer GLMs due to their additive/multiplicative transparency. It is exceptionally difficult to prove to a regulator that complex, unsupervised groupings have not inadvertently constructed an illegal discriminatory proxy (e.g., grouping by postcodes that inadvertently maps exactly to race or religion).

---

## Question 9

### Part (i)

Factors the reinsurer should consider when deciding which option to proceed with:

*   **Cost vs Risk Transfer Efficiency (Rate on Line):** The absolute reinsurance premium cost must be considered alongside the Rate on Line (Premium / Capacity). The reinsurer must assess whether the cheaper cost of Option C (due to the high attachment point) justifies the significant reduction in net protection compared to A or B.
*   **Profile of Gross Aggregate Exposure:** The reinsurer must conduct a detailed exposure profiling of its inward marine hull portfolio. Do they frequently write individual risks with limits exposing them to losses between $10m and $40m? If the vast majority of their inward limits are, for example, $15m, then Option C ($60m xs $40m) provides almost zero effective protection for single risk losses, whereas Option A acts as an active working layer.
*   **Return Period and Attachment Probability:** Using stochastic models, the reinsurer must estimate the probability of losses exceeding the respective attachment points ($10m, $13m, and $40m). Options A and B will attach far more frequently, protecting the income statement and earnings volatility. Option C will attach rarely, acting strictly as catastrophic balance sheet protection.
*   **Required Capacity Amount:** Option C provides double the capacity ($60m vs $30m). The reinsurer must review its maximum possible gross loss (e.g., from a clash event like a major port explosion). If a modelled worst-case event is $65m, Option A leaves a net retention of $35m ($10m deductible + $25m un-reinsured above the cap). Option C leaves a net loss of $45m ($40m deductible + $5m above).
*   **Company Capital & Risk Appetite:** Does the reinsurer hold sufficient economic capital to comfortably absorb a $40m loss on a single event? If risk appetite dictates that no single event should impact earnings by more than $15m, then Option A or B is mandatory, and Option C is entirely inappropriate regardless of price.
*   **Reinstatement Provisions:** The terms regarding reinstatements are critical. How many reinstatements are offered under each option, and what is the cost (e.g., 100% additional premium)? An option providing $30m of cover with one free reinstatement is vastly superior to an option providing $30m with no reinstatements available.
*   **Counterparty Credit Risk:** Who is providing the options? The reinsurer must assess the financial strength and credit rating of the retrocessionaire offering the quotes. A slightly more expensive Option A provided by an AA-rated entity is preferable to a cheaper option from a BBB-rated entity that might default during a catastrophe.
*   **Clash and Aggregation Cover:** The basis of the limit is crucial. In marine hull, a storm or port explosion can damage multiple insured vessels simultaneously. The reinsurer must ensure the chosen option effectively covers accumulated clash losses arising from exactly one originating cause.
*   **Basis of Cover:** Do the options cover on a "Losses Occurring During" or "Risks Attaching During" basis? This must intimately match the reinsurer's inward portfolio profile to avoid dangerous gaps in coverage.

### Part (ii)

Potential data adjustments that Company X (the retrocessionaire) will have to make before pricing this excess of loss retrocession contract:

*   **As-If Premium Adjustments:** Company X must adjust the historic inward premium data provided by the reinsurer to current "as-if" rate levels. If the marine market has experienced significant rate hardening or softening over the historical period, past premiums must be rebased using rate indices so they are comparable to the prospective premium environment.
*   **Exposure / Mix of Business Adjustments:** The historical claims profile must be adjusted to reflect the reinsurer's *current* operational reality. If the reinsurer recently stopped writing highly dangerous offshore energy platforms and moved purely to safe coastal cargo, the historical claims data must be filtered to remove platform claims to accurately reflect the prospective exposure.
*   **Claims Inflation / Trending:** This is paramount for excess of loss pricing. Historical marine hull repair costs (driven by steel prices, specialized labor, and fluctuating exchange rates) must be inflated using severe trend factors up to the midpoint of the prospective policy period. A claim that historically settled for $8m might trend to $11m today, meaning it would now breach the Option A ($10m) attachment point, heavily impacting the pricing.
*   **IBNR and Development Factors (LDFs):** Marine claims, particularly involving complex salvage, collision liability, or legal disputes, have notoriously long reporting and settlement tails. Company X must apply sophisticated Loss Development Factors (triangulation) to historic claims to bring them up to their ultimate expected settlement value, ensuring the tail risk is priced.
*   **Large Loss Extraction / Smoothing:** If the historical dataset contains a massive, 1-in-100 year catastrophic loss (e.g., a major hurricane sinking an entire fleet), Company X must extract or "cap" this claim in the experience dataset and model it separately, otherwise the resulting experience-based rate will be unsustainably high and heavily skewed.
*   **Currency Conversion and Exchange Variations:** Marine insurance is inherently global, dealing with multiple currencies. Company X must meticulously convert all historical premiums and claims into a common denominator currency (e.g., USD), adjusting for significant historical exchange rate fluctuations, to ensure comparing limits and severities operates on a level monetary baseline.
*   **Deductible and Limit Adjustments:** The inward policies written by the reinsurer will have changing deductibles over time. Company X must calculate the theoretical gross claim from the ground up to ensure they are applying their retrocession excess point correctly against the true scale of the loss.

---

## Question 10

### Part (i)

Benefits that could be provided under this wedding insurance policy:
*   **Cancellation or Alternative Arrangement:** Reimburses non-refundable deposits, advanced payments, and incurred costs if the wedding must be entirely cancelled or heavily postponed due to unforeseen, unavoidable circumstances (e.g., sudden serious illness/death of the bride, groom, or close family member; severe extreme weather rendering the venue inaccessible; sudden venue bankruptcy).
*   **Failure of Suppliers/Vendors:** Covers the extra, reasonable expenses incurred to arrange last-minute alternative services if a critical booked supplier (e.g., the caterer, the photographer, the official officiant, or the transport provider) goes out of business or fails to appear on the day.
*   **Public and Personal Liability:** Provides vital legal defense and compensation cover if a guest or a member of the public sustains bodily injury, or if third-party property is damaged during the event, and the couple (or the host) is held legally liable.
*   **Damage/Loss of Attire:** Reimburses the cost to repair or replace the wedding dress, formal suits, or bridal party attire if they are lost, stolen, or accidentally severely damaged while in the couple’s possession prior to or during the event.
*   **Loss/Damage to Gifts:** Covers the value of wedding presents (usually up to a specified sub-limit) if they are stolen from the venue or damaged while in transit immediately after the reception.
*   **Loss/Damage to Rings:** Covers the cost of replacing the actual wedding rings if they are lost, stolen, or damaged during a specified window around the ceremony.
*   **Photography/Videography Rectification:** Covers the cost of re-staging the wedding photographs (hiring suits, dresses, paying the photographer again) if the original photographs/video are completely ruined due to technical failure of the photographer's equipment or loss of the underlying film/digital media.

### Part (ii)

Risks the insurer may face if it launched this new product:
*   **High Pricing Risk (Lack of Data):** As a completely new product line for the established insurer, they have precisely zero internal proprietary data regarding the actual frequency of wedding cancellations or the typical severity of supplier failure claims. Relying purely on heavily generalized external market data leads to high parameter error and mispricing.
*   **Severe Anti-Selection (Adverse Selection):** Couples who have pre-existing knowledge that their event is high-risk are far more likely to buy the policy. For example, a couple booking an outdoor wedding in an area prone to severe flooding, or a couple relying on an elderly, critically ill relative, will disproportionately purchase cover, leading to worse-than-expected loss ratios.
*   **Moral Hazard:** Once the insurance is purchased, the bridal party might become deliberately careless, assuming "insurance will pay for it." This could manifest as leaving expensive gifts unattended or engaging reckless, slightly cheaper vendors knowing they have fallback cover. In extreme cases, a couple experiencing "cold feet" might fabricate an illness or excuse to trigger a cancellation payout.
*   **Accumulation and Systemic Risk:** Weddings are highly seasonal and localized. A large-scale systemic event, such as an outbreak of an infectious disease resulting in government lockdowns, or a severe, wide-ranging weather catastrophe (e.g., a regional hurricane or widespread flooding causing transport collapse), will generate hundreds or thousands of maximum-limit cancellation claims simultaneously, devastating the insurer's balance sheet.
*   **Reputational Damage:** Weddings are highly emotive, heavily publicized, and deeply personal events. If the insurer acts strictly according to policy wordings and denies a borderline claim, the angry couple can easily generate severe negative media attention and social media backlash, severely damaging the insurer’s wider, established brand reputation across its other product lines.
*   **Increased Operational and Claims Handling Costs:** The insurer will need to build new IT infrastructure, write new policy wordings, and, crucially, train claims handlers to deal with highly stressed, highly emotional clients making complex claims involving multiple small vendors, heavily increasing operational overheads to launch the line.

### Part (iii)

How the insurer’s reinsurance needs would change if it provided coverage for this celebrity wedding:
*   **Requirement for Huge Facultative Capacity:** A multi-week, extravagant celebrity wedding will feature astronomical sums insured (covering immense cancellation costs, highly valuable bespoke attire, globally sourced vendors, massive security deposits, and exclusive venue buyouts). The Total Insured Value (TIV) of this single risk will vastly breach the limit profile of the insurer's existing, retail-focused proportional or excess of loss treaties. The insurer will absolutely require bespoke, individual Facultative (Fac) placements heavily supported by the global market to safely write the limit.
*   **Addressing Highly Bespoke Risk Perils:** The risk profile of a massive celebrity wedding is alien to standard retail policies. The insurer will face unique exposures such as targeted paparazzi intrusion causing physical/property damage, specific high-level security/terrorism threats, or cancellation required because a filming schedule for the celebrity suddenly changes. Reinsurance coverage must be dynamically rewritten from scratch to specifically include or exclude these bespoke celebrity perils to avoid massive exposure gaps.
*   **Extended Period of Exposure Aggregation:** A standard wedding policy carries heavy risk for only 1 to 2 days. This celebration lasts several weeks, massively expanding the time window (the exposure period) during which a catastrophic peril (like a major storm, a targeted incident, or an illness) could occur and trigger a claim. The reinsurance wording must be explicitly adjusted to aggregate losses appropriately over this highly extended duration.
*   **Necessity for Syndication and Spreading Credit Risk:** Because the limits are so extreme, the insurer cannot logically rely on a single facultative reinsurer. They will require multiple reinsurers forming a syndicate, each taking a proportionate share of the massive placement, requiring complex negotiation and greatly diversifying counterparty credit risk for the direct insurer.
*   **Accessing Niche Reinsurance Expertise:** Due to the insurer's total lack of experience in this specific ultra-high-net-worth niche, they will need a reinsurer that does not just provide capital, but provides deep, specialized underwriting expertise in Contingency and specialized Event Cancellation covers. The insurer will directly utilize the reinsurer's specialized knowledge to set the complex terms, conditions, and specialized pricing structure.
*   **Stringent Claims Control Clauses:** Given the severe reputational implications of a dispute over a celebrity claim (guaranteed global news coverage), the reinsurers carrying the bulk of the financial risk will likely insist on "Claims Control" or tight "Claims Co-operation" clauses. The reinsurer will demand the right to dictate or heavily influence the settlement negotiation, rather than allowing the primary insurer to settle quickly just to protect their own brand.

---

## Audit Trail

### Accessed Files
- `exams/SP8/September_2025/question-paper.md`
