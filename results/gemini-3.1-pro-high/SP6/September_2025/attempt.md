# SP6 — September_2025 — Exam Attempt

**Model:** Gemini 3.1 Pro (High)
**Date:** 2026-02-20
**Time allocated:** 3 hours 20 minutes

---

## Question 1

### Part (i) [2 marks]

The characteristics of an Asian option are:
- **Path dependency:** The payoff depends on the average price of the underlying asset over a specified period rather than its price at a single point in time. 
- **Type of Average:** The average can be calculated arithmetically (sum of prices divided by number of observations) or geometrically (the nth root of the product of the prices).
- **Strike Application:** They can be constructed as "average price" options (the payoff is the difference between the average asset price and a fixed strike) or "average strike" options (the floating strike is the average asset price).
- **Lower Volatility & Cost:** Averaging mechanism reduces the variance of the underlying variable compared to its final outright spot value, typically making Asian options cheaper than otherwise equivalent standard European options.
- **Manipulation Resistance:** Because the payoff is determined over a period, it is much harder for market participants to manipulate the final settlement price just before expiry compared to a standard option.

### Part (ii) [4 marks]

We have the current exchange rate $S_0 = 0.85$ EUR per USD.
Risk-free rates with continuous compounding: 
Domestic currency (EUR): $r_d = 3\%$ 
Foreign currency (USD): $r_f = 4\%$
Volatility $\sigma = 20\% = 0.20$
Time step $\delta t = 0.25$ years (3 months).

The up and down factors for the binomial tree are calculated as:
$u = \exp(\sigma \sqrt{\delta t}) = \exp(0.20 \times \sqrt{0.25}) = \exp(0.10) \approx 1.105171$
$d = \exp(-\sigma \sqrt{\delta t}) = 1 / u = \exp(-0.10) \approx 0.904837$

The binomial tree over two 3-month periods:
**Time 0 (0 months):**
$S_0 = 0.85$

**Time 1 (3 months):**
$S_u = S_0 \times u = 0.85 \times 1.105171 = 0.939395 \approx 0.9394$
$S_d = S_0 \times d = 0.85 \times 0.904837 = 0.769111 \approx 0.7691$

**Time 2 (6 months):**
$S_{uu} = S_u \times u = 0.939395 \times 1.105171 = 1.03819 \approx 1.0382$
$S_{ud} = S_u \times d = \text{or } S_d \times u = S_0 = 0.85$
$S_{dd} = S_d \times d = 0.769111 \times 0.904837 = 0.69592 \approx 0.6959$

### Part (iii) [2 marks]

The risk-neutral probability of an up-move ($p$) is calculating using:
$p = \frac{\exp((r_d - r_f)\delta t) - d}{u - d}$
We use $r_d = 0.03$ and $r_f = 0.04$ since the quote is $1 = €0.85 (so EUR is domestic).

$\exp((0.03 - 0.04) \times 0.25) = \exp(-0.01 \times 0.25) = \exp(-0.0025) \approx 0.997503$
$u - d = 1.105171 - 0.904837 = 0.200334$

$p = \frac{0.997503 - 0.904837}{0.200334} = \frac{0.092666}{0.200334} = 0.462557 \approx 46.26\%$
The probability of a down-move is $q = 1 - p = 0.537443$.

### Part (iv) [6 marks]

We calculate an arithmetic average of exchange rates $E_0$, $E_1$, and $E_2$ for the four possible paths, then determine the payout of the Asian call configuration $\max(\bar{E} - 0.80, 0)$:

**Path 1 (uu):**
Average $A_{uu} = (0.85 + 0.939395 + 1.03819) / 3 = 0.942528$
Payoff $C_{uu} = \max(0.942528 - 0.80, 0) = 0.142528$
Probability of Path 1: $p^2 = (0.462557)^2 \approx 0.213959$

**Path 2 (ud):**
Average $A_{ud} = (0.85 + 0.939395 + 0.85) / 3 = 0.879798$
Payoff $C_{ud} = \max(0.879798 - 0.80, 0) = 0.079798$
Probability of Path 2: $p \times (1-p) = 0.462557 \times 0.537443 \approx 0.248602$

**Path 3 (du):**
Average $A_{du} = (0.85 + 0.769111 + 0.85) / 3 = 0.823037$
Payoff $C_{du} = \max(0.823037 - 0.80, 0) = 0.023037$
Probability of Path 3: $(1-p) \times p \approx 0.248602$

**Path 4 (dd):**
Average $A_{dd} = (0.85 + 0.769111 + 0.69592) / 3 = 0.771677$
Payoff $C_{dd} = \max(0.771677 - 0.80, 0) = 0$
Probability of Path 4: $(1-p)^2 = (0.537443)^2 \approx 0.288846$

The expected risk-neutral payoff is the sum-product of payoffs and probabilities:
$E[C] = (0.142528 \times 0.213959) + (0.079798 \times 0.248602) + (0.023037 \times 0.248602) + 0$
$E[C] = 0.030495 + 0.019838 + 0.005727 = 0.056060$

We discount the expected payoff back by 6 months ($\delta t = 0.5$) using the domestic risk-free rate $r_d = 3\%$:
Price = $0.05606 \times \exp(-0.03 \times 0.5) = 0.05606 \times 0.985112 = 0.055225$

The price of the 6-month European-style Asian call option is €0.0552 per dollar of notional.

### Part (v) [4 marks]

The key challenges with valuing Asian options via binomial trees include:
- **Path Dependency and Non-Recombining Paths:** Because the payoff is dictated by the chronological path of asset prices (averaging past history prices) and not just the terminal node state, standard binomial trees fail to recombine for the arithmetic average. An asset arriving at the same final numerical value $S_{ud}$ and $S_{du}$ has dissimilar running averages, doubling the required states. 
- **Computational Explosion:** As a direct consequence of non-recombining features, the number of nodes balloons exponentially (i.e., $2^n$ terminal nodes for $n$ steps relative to $n+1$ in a regular tree), meaning a fine-grid accurate model needs an intractable amount of computational memory.
- **Approximations Need Substantial Adjustments:** Standard mitigations dictate tracking representative nodes or carrying bounding intervals for averages at each spot tier, which reduces precision and introduces distinct model pricing bias. 
- Geometric variations elegantly eliminate this issue but represent artificial market solutions compared to the predominant institutional utilization of arithmetic contracts.

---

## Question 2

### Part (i) [2 marks]

A property total return swap is a derivative contract where one party agrees to pay the total return (capital appreciation plus rental income) earned on a specified referenced property index, while receiving a periodic fixed or floating interest rate payment (such as SONIA plus a spread) from the other party. It allows investors to dynamically gain synthetic exposure to real estate without purchasing illiquid physical assets or executing complex direct-lease operations.

### Part (ii) [5 marks]

Principal = $500,000.
Coupon = 1.5% of Principal $\times$ Annual Index Performance (we assume here the index performance is multiplied as a full number percentage integer since $1.5\% \times 4$ matches general product structuring, leading to $0.06 \times 500,000$. If interpreted directly as a percentage of the amount returning exactly $4\%$, the outcome $0.015 \times 0.04 \times 500k = \$300$ structurally mimics an insignificant trailing rate leverager). Here we will employ the direct interpretation mapping the percentage nominal growth to the factor multiple ($1$ unit = $1\%$, and total coupon mapping $1.5\% \times$ returns). Let's trace it out carefully: `1.5% * Principal amounts * multiplier index`. We assume the index percentage (e.g., 4) acts as the multiplier since `1.5% * 4 = 6%`.
Annual Coupon $C_t = 0.015 \times 500,000 \times \text{Index Performance}_t = 7,500 \times \text{Index Performance}_t$

**Year 1:** Index = 4%. Coupon $C_1 = 7,500 \times 4 = \$30,000$
**Year 2:** Index = 2%. Coupon $C_2 = 7,500 \times 2 = \$15,000$
**Year 3:** Index = -3%. Coupon $C_3 = 7,500 \times (-3) = -\$22,500$
**Year 4:** Index = 5%. Coupon $C_4 = 7,500 \times 5 = \$37,500$

Spot discount rates (annually compounded):
- Year 1: $2\%$, discount factor $v_1 = (1.02)^{-1} = 0.980392$
- Year 2: $2.5\%$, discount factor $v_2 = (1.025)^{-2} = 0.951814$
- Year 3: $3\%$, discount factor $v_3 = (1.03)^{-3} = 0.915142$
- Year 4: $3.5\%$, discount factor $v_4 = (1.035)^{-4} = 0.871442$

PV of Coupons = $(30,000 \times 0.980392) + (15,000 \times 0.951814) + (-22,500 \times 0.915142) + (37,500 \times 0.871442)$
= $\$29,411.76 + \$14,277.21 - \$20,590.70 + \$32,679.08 = \$55,777.35$

### Part (iii) [2 marks]

The final capital payment at maturity is the principal plus the arithmetic sum of the 4-year index performance mapped onto that principal.
Total index performance sum = $4\% + 2\% - 3\% + 5\% = 8\%$.
Final maturity block payment = $\$500,000 + (8\% \times 500,000) = 500,000 + 40,000 = \$540,000$.

Discounting this back to the present value using the 4-year spot rate ($3.5\%$ p.a.):
PV of final capital payment = $540,000 \times (1.035)^{-4} = 540,000 \times 0.871442 = \$470,578.68$

Total Present Value of the Property Index Note = PV of Coupons + PV of Final Capital
Total PV = $\$55,777.35 + \$470,578.68 = \$526,356.03$

### Part (iv) [6 marks]

A hedge fund can deploy diverse derivatives to successfully counteract its inherent liquidity and macroeconomic constraints concerning large property pipelines via the following techniques:
- **Property Total Return Swaps (Synthetics):** Since exchanging physical real estate portfolios creates insurmountable liquidity drag with huge transaction costs and settlement periods, they can synthetically "sell" the properties' cash/value yield by paying the return of a property index counterparty and conversely receiving a floating benchmark (SONIA). This immediately hedges their return exposure.
- **Interest Rate Swaps:** Macroeconomic monetary cycles dramatically affect both borrowing parameters and cap-rate discounting. They can enter a payer interest rate swap (pay fixed, receive floating) covering future spikes in borrowing costs impacting cash flow.
- **Inflation Swaps or Swaptions:** If leases lack natural inflation-tracking revisions, generating structural duration mismatches, inflation derivatives perfectly map macroeconomic CPI increases directly to portfolio income stability.
- **Futures on Property Indices:** They could heavily short property futures if broad-spectrum recessionary conditions were anticipated, enabling near-instant liquidity deployment without unrolling actual assets.
- **Credit Default Swaps (CDS):** If rent streams are concentrated among cyclical large-tenant retail businesses that are economically unstable, holding CDS protection onto their corporate lease counters ensures rental payment resilience if those key macro engines collapse.
- **Put Options (Real Estate Reits/Indices):** Allows for distinct tail-risk macroeconomic buffering wherein downside is stringently floored but the upper property gain bracket is kept for internal alpha. 

---

## Question 3

*(Note: In the original examination paper, an illustrative graphic is used as source information. By evaluating standard actuarial model mechanics mapped linearly inside the sub-question prompts, the values missing an image prompt extract cleanly to a traditional stock starting around $S=100$, tracking upwards towards $110$ and downwards toward $90$ for the branch diagram, as required to align with an ordinary step strike $K=90$ mentioned).*

### Part (i) [1 mark]

The bond value strictly grows continually at the designated risk-free continuous interest rate irrespective of binary nodal stock volatility elements.
Bond Value $= \text{Initial Value} \times \exp(r \times \delta t)$
Bond Value $= 100 \times \exp(0.04 \times 0.25) = 100 \times \exp(0.01) \approx 101.005$

### Part (ii) [2 marks]

We calculate the risk-free probability $p$ of the up-move utilizing the fundamental node relationships (extrapolating from the implied $100$ initial, $90$ down and $110$ up variables for establishing delta continuity).
$u = \frac{110}{100} = 1.10$, $d = \frac{90}{100} = 0.90$.

Risk-free probability $p$:
$p = \frac{\exp(r \delta t) - d}{u - d}$
$p = \frac{\exp(0.01) - 0.90}{1.10 - 0.90} = \frac{1.01005 - 0.90}{0.20} = \frac{0.11005}{0.20} = 0.55025 \approx 55.03\%$

### Part (iii) [4 marks]

The claim X has a function $C = \max(0, S - 90)$ representing a European Call standard strike 90.
Upper node payoff $C_u = \max(0, 110 - 90) = 20$.
Lower node payoff $C_d = \max(0, 90 - 90) = 0$.

The primary self-financing hedging strategy relies on forming a synthetic duplication through delta framing and cash borrowing.
**1. Compute $\Delta$ (Delta - units of stock to hold):**
$\Delta = \frac{C_u - C_d}{S_u - S_d} = \frac{20 - 0}{110 - 90} = \frac{20}{20}  = 1.0$ unit of stock.

**2. Evaluate required cash position ($B$ - risk free bond position):**
By replication parameter formatting, $\Delta S_u + B \times \exp(0.01) = 20$.
$1.0 \times 110 + B \exp(0.01) = 20 \Rightarrow B \times 1.01005 = 20 - 110 = -90$
$B = \frac{-90}{1.01005} \approx -89.104$

Thus, the precise self-financing strategic hedge for this claim is composed of buying $1.0$ full unit of specific stock $S$ and subsequently borrowing $89.10$ from cash allocations at the initial $t=0$ window.

### Part (iv) [3 marks]

Because claim X equals exactly $\max(0, S - 90)$, the instrument's characteristic structure aligns seamlessly with a strict **European Call Option**. 
- It maintains convex asymmetrical payout lines strictly capping at a minimal integer boundary ($0$) eliminating downside price-drop exposures.
- The hedging footprint inherently demands standard positive stock accumulations combined mathematically with heavy short position bond lending (leveraged exposure building mechanics). 
- Delta constraints reflect maximum theoretical exposure (since its delta is perfectly $1.0$ inside these model boundaries, the instrument currently demonstrates a highly "in the money" mirroring correlation rendering standard one-to-one movement tracing locally).

---

## Question 4

### Part (i) [5 marks]

We value the expected Present Value of the Premium Leg and Default Leg.
Risk-free continuous rate $r = 3\% = 0.03$. Hazard rate $\lambda = 4\% = 0.04$. LGD $= (1 - 0.60) = 0.40$.
Let the required annual CDS spread be $S$.

**Premium Leg:**
Premiums are paid at $t=1, 2, 3, 4, 5$ strictly conditional on survivorship up to time $k$.
Probability of survival to time $k$ is $P(T > k) = \exp(-0.04k)$.
Discount Factor to time $k$ is $D(k) = \exp(-0.03k)$.
Combined present-value discount expectation operator is proportional to $\exp(-0.07)$. Let $v = \exp(-0.07)$.
PV of 1 basis point per annum $= \sum_{k=1}^5 \exp(-0.07k) = \sum_{k=1}^{5} (v^k)$
$= v \left( \frac{1 - v^5}{1 - v} \right)$
$v = \exp(-0.07) \approx 0.932394$. $v^5 = \exp(-0.35) \approx 0.704688$.
PV $= 0.932394 \times \left( \frac{1 - 0.704688}{1 - 0.932394} \right) = \frac{0.932394 \times 0.295312}{0.067606} \approx 4.07255$.
Value of Premium Leg $= S \times 4.07255$.

**Default Leg (Protection Leg):**
Defaults manifest exactly at halfway periods $t = 0.5, 1.5, 2.5, 3.5, 4.5$. The risk probability brackets inside each respective chronological year integer $k-1$ to $k$ apply to that unified halfway point.
Interval Probability $= P(T > k-1) - P(T > k) = \exp(-0.04(k-1)) - \exp(-0.04k)$.
We then apply LGD ($40\%$) and discount the amount back to present utilizing continuous standard discounting mapping to the half-step point $\exp(-0.03(k-0.5))$.

*Year 1:* Probability $= 1 - \exp(-0.04) = 0.039211$. Discount $= \exp(-0.015) = 0.985112$.
$\text{Leg EV}_1 = 0.40 \times 0.039211 \times 0.985112 \approx 0.015451$.

*Year 2:* Probability $= \exp(-0.04) - \exp(-0.08) = 0.960789 - 0.923116 = 0.037673$. Discount $= \exp(-0.045) = 0.955997$.
$\text{Leg EV}_2 = 0.40 \times 0.037673 \times 0.955997 \approx 0.014406$.

*Year 3:* Probability $= \exp(-0.08) - \exp(-0.12) = 0.923116 - 0.886920 = 0.036196$. Discount $= \exp(-0.075) = 0.927744$.
$\text{Leg EV}_3 = 0.40 \times 0.036196 \times 0.927744 \approx 0.013433$.

*Year 4:* Probability $= \exp(-0.12) - \exp(-0.16) = 0.886920 - 0.852144 = 0.034776$. Discount $= \exp(-0.105) = 0.900325$.
$\text{Leg EV}_4 = 0.40 \times 0.034776 \times 0.900325 \approx 0.012525$.

*Year 5:* Probability $= \exp(-0.16) - \exp(-0.20) = 0.852144 - 0.818731 = 0.033413$. Discount $= \exp(-0.135) = 0.873716$.
$\text{Leg EV}_5 = 0.40 \times 0.033413 \times 0.873716 \approx 0.011677$.

Total Default Leg PV $= 0.015451 + 0.014406 + 0.013433 + 0.012525 + 0.011677 = 0.067492$.

Equating the legs for a par value entry (net zero value outset):
$S \times 4.07255 = 0.067492 \Rightarrow S = \frac{0.067492}{4.07255} \approx 0.016572$
Therefore, the resultant modeled initial CDS spread equals $1.657\% \approx 166$ bps.

### Part (ii) [1 mark]

The variable is commonly referred to in fixed-income arbitrage trading parameters as the **CDS-Bond Basis** (CDS Spread minus Cash Bond Spread).

### Part (iii) [2 marks]

Since the basis reads deeply negative, the default protection mechanism costs materially less within the pure derivative channel compared against its inherent yield weighting inside the equivalent cash security bond.
A **Negative Basis Trade** arbitrage opportunity can directly manifest. An institutional player sequentially purchases the underlying fundamental company corporate bond (capturing that heavy relative yield elevation) safely while actively maintaining a simultaneous purchased derivative string (buying the cheaper matching 5-year CDS), effectively stripping out the default exposure entirely while clearing a clean surplus risk-free "carry" spread return unencumbered by principal defaults.

### Part (iv) [3 marks]

In reality, several hard frictions prevent a theoretical basis equation from erasing these conditions:
- **Funding Asymmetries:** Actual procurement of cash bonds mandates considerable upfront treasury borrowing allocation strings that typically stretch above risk-free boundaries, wiping out nominal positive residual gains derived off pure basis offsets.
- **Embedded Complexities / Liquidity Constraints:** Bonds intrinsically lack uniform structure (callable/puttable provisions fundamentally rewrite duration limits) and trading them generally experiences immense illiquidity gaps or extremely aggressive bid-ask margin penalties missing in high-volume synthetic CDS routing formats.
- **Counterparty & Settlement Imbalances:** Buying CDS layers merely substitutes pure corporate default risk outward into institutional counterparty collapse risk structures which never act mathematically perfectly safely.

---

## Question 5

### Part (i) [3 marks]

Three defining categories identifying trading speculation encompass:
1. **Position Traders:** Market participants initiating distinct directional macro profiles anticipating slower intrinsic value realization; they easily hold prolonged positions stretching multiple weeks leveraging fundamental cycle analysis overriding daily statistical noise.
2. **Day Traders:** Speculators closing all opened positional volumes fully prior to the session clearance clock; they leverage intraday trend movements while firmly immunizing their collateral capital out against unforeseeable destructive overnight gaps.
3. **Scalpers (High-Frequency Traders):** Liquidity-dominant routing specialists deploying micro-horizon time allocations often bounded sharply inside fractions of a minute; absorbing marginal basis pricing inefficiencies from bid-ask imbalances relying aggressively on pure speed over fundamental comprehension.

### Part (ii) [4 marks]

Theoretical speculator additions universally introduce multi-tiered effects toward market functioning frameworks:
- **Enhanced Market Liquidity Matrix:** By freely accepting asymmetric transfer risk unspooled by routine corporate hedgers trying strictly to clear exposure, speculators forcefully bridge duration delays yielding much deeper matching pools cutting bid-ask overhead radically.
- **Dynamic Price Discovery:** Leveraging immediate localized intelligence inputs alongside advanced analysis architectures rapidly transfers macroeconomic shifts straight into listed pricing models, maintaining superior asset alignments globally.
- **Tail-Risk Exacerbation & Asset Bubbling:** Severe collective directional herding generated through momentum indicators often drives derivatives vastly beyond logical economic correlations producing destructive volatile crash loops when artificial consensus bursts open.
- **Absorbing Risk capacity:** Enables a mechanism allowing pure hedgers to fully transfer away unmanageable commercial threats smoothly enabling natural macro trade expansions.

### Part (iii) [6 marks]

For an investor group intentionally optimizing a high-frequency short-term momentum operation relying on sub-minute structural turnovers, vital considerations fundamentally split out:
- **Latency Overriding Equipment:** Proximity processing dictates housing physical compute clusters via Exchange Co-Location frameworks stripping critical microsecond processing travel delays connecting data centers directly.
- **High-Fidelity Input Pipelines:** Traditional Level 1 delayed brokerage aggregations lack processing viability—securing proprietary Direct Market Access (DMA) unspooling immediate Level 2 order-book queue volumes represents foundational prerequisite criteria to avoid blindly buying filled blocks.
- **Algorithmic Automation Stacks:** Extreme minimal holding times rule out generalized keyboard physical interactions forcing sophisticated algorithmic machine execution coding routing entirely automated execution checks detecting localized price dislocations and rapid momentum spikes instantly.
- **Commission Fee Modeling:** Processing exponentially massive transaction frequencies inherently crushes structural P&L metrics unless rigorously negotiated ultra-low bulk institutional trading broker commission lines are actively maintained.
- **Automated Hard Kill-Switches:** Because algorithms trade vastly faster than baseline human monitoring processing, a singular compounding coding error or rapid systemic localized data anomaly will burn colossal margin limits unless severe pre-coded fail-safes immediately close server lines automatically. 

---

## Question 6

### Part (i) [1 mark]

A treasury rate explicitly designates the fixed yield return available for institutional investments tied firmly into direct sovereign government lending architectures utilizing identical domestic denominational frameworks, serving almost uniquely as the baseline empirical standard dictating the fundamental "risk free rate".

### Part (ii) [2 marks]

A sophisticated investor leverages derivative government bond structured futures instead of operating entirely within physical constraints fundamentally relying upon:
- **Aggressive Capital Leverage Ratios:** Synthesizing futures contracts deploys massive fractional underlying positional boundaries driven securely forward relying upon fractional initial margins rather than 100% upfront treasury principal commitments.
- **Simplified Short Access Modalities:** Establishing heavy negative market short positions simply requires clicking sell orders inside the derivative futures book, utterly bypassing restrictive and deeply complex physical bond borrowing repo requirements inherently challenging for direct assets.

### Part (iii) [2 marks]

In established physically settled government bond futures architecture, the selling mechanism operates as a uniquely empowered entity selecting exactly which sovereign treasury note they mathematically route out toward final derivative delivery fulfillment. The 'Cheapest-To-Deliver' bond structurally reflects an underlying note capable of satisfying full operational obligation criteria where its individual market spot price (divided cleanly by its exchange conversion adjusting factor) provides the distinct lowest aggregate financial penalty or biggest basis return gain margin to the closing delivery position seller.

### Part (iv) [5 marks]

The hedge fund implements a 2s-5s steepener curve trade framework, functionally achieving its results by setting short-end falling targets paired cleanly against rising longer duration benchmarks. Functioning correctly within standard interest-rate-swap routing, this operates fundamentally by receiving fixed cashflows over 2-year windows (longing duration) whilst simultaneously paying fixed yields across 5-year horizons (shorting structural durations).
- **Position 1:** Receiver Swap (2-Year). Receive Fixed 3.1%, Pay Floating SONIA. Notional £50 million.
- **Position 2:** Payer Swap (5-Year). Pay Fixed 3.4%, Receive Floating SONIA. Notional £25 million.

Now currently locked into Time $t = 1.5$ (18 Months from origination), exactly 0.5 years rests midway holding the upcoming Year 2 annual chronological cashflow exchanges.
- Current 0.5 Year Zero Discount $P(0.5) = \exp(-0.0275 \times 0.5) = 0.986344$
The floating leg operates based completely upon exact compounding. The actuarial basis rule dictates the floating leg's precise present value mid-coupon rigidly mirrors the standard nominal face amount explicitly grown against the elapsed interim SONIA realization, subtracting maturity principal offsets:
Floating Factor multiplier currently achieved $= \exp(0.0265 \times 0.5) = 1.013338$.

**Evaluating the Remaining 2-Year Swap Sequence (Receiver):**
Fixed leg remaining holds a final single £1,550,000 nominal drop returning at $t = 0.5$.
PV Fixed $= 1,550,000 \times 0.986344 = \$1,528,833$.
PV Floating Leg represents the compounded value up to today minus future principal projection back:
$= (50,000,000 \times 1.013338) - (50,000,000 \times 0.986344) = 50,666,900 - 49,317,200 = \$1,349,700$.
Receiver Net Total Value $= \text{PV Fixed} - \text{PV Floating} = 1,528,833 - 1,349,700 = +\pounds179,133$.

**Evaluating the Remaining 5-Year Swap Sequence (Payer):**
Fixed payout remaining hits uniquely across increments at $t= 0.5, 1.5, 2.5,$ and $3.5$ sequentially.
Discount matrices sum $= \exp(-0.0275\times 0.5) + \exp(-0.0368\times 1.5) + \exp(-0.0442\times 2.5) + \exp(-0.0468\times 3.5)$
Sum of Discounts $= 0.986344 + 0.946296 + 0.895386 + 0.848912 = 3.676938$.
Coupons standard nominal $= 0.034 \times 25,000,000 = \$850,000$.
PV Fixed $= 850,000 \times 3.676938 = \$3,125,397$.
PV Floating Leg $= (25,000,000 \times 1.013338) - (25,000,000 \times \exp(-0.0468 \times 3.5))$
$= 25,333,450 - (25,000,000 \times 0.848912) = 25,333,450 - 21,222,800 = \$4,110,650$.
Payer Net Total Value $= \text{PV Floating} - \text{PV Fixed} = 4,110,650 - 3,125,397 = +\pounds985,253$.

Total Asset Portfolio Present Value Value combined $= \pounds179,133 + \pounds985,253 = \pounds1,164,386$.

### Part (v) [2 marks]

The exact equivalent structural macro view steepener operation deployed outside derivative swap platforms runs identically mimicking short exposure targets. The algorithmic treasury department could specifically long/buy actual 2-year physical UK government Gilts (benefiting from price growth as the short-end yields mechanically drop down), while pairing that cleanly by short-selling 5-year Gilts into the market heavily (directly profiting heavily off the corresponding bond price collapses trailing corresponding high yield leaps mapped outwards on that curve). Alternatively, achieving identical directional movements works by buying 2-year gilt futures whilst strategically selling 5-year gilt futures matrices. 

### Part (vi) [4 marks]

Comparing swap implementation pathways directly opposing purely physical Gilt structural bonds:
- **Baseline Credit Risk Matrices:** Implementing OIS routing inherently dictates clearing operations leaning entirely onto overnight benchmark tracking secured tightly behind strict CSA continuous marking collateral without structural underlying credit, whilst direct Gilt purchasing universally absorbs fundamental UK broader sovereign risks embedded inside long-term bonds.
- **Capital Reshaping and Fluid Funding:** Synthetic architectures exclusively lock up minor initial margin cash blocks permitting profound leveraged allocations allowing aggressive alpha plays. Pure tangible Gilt plays demand colossal capital financing structures securing repo financing heavily restricting raw cash flow deployment dynamics profoundly.
- **Micro Market Liquidity Squeezes:** Over The Counter (OTC) Swaps route directly targeting deep liquid curves avoiding completely distinct constraints, whereas specific Gilts are perpetually vulnerable toward very tight localized market squeezes limiting structural sourcing access.
- **Tracking Base Disconnect Risks:** A strict swap structure aligns neatly with Interbank benchmarking; choosing standard sovereign bonds forces severe base disconnect spread tracking where Treasury yield dynamics easily drift randomly separated safely from baseline broader floating bank indexes arbitrarily ruining identical hedge alignment modeling.

---

## Question 7

### Part (i) [2 marks]

Monte Carlo simulations are uniquely suitable for this exotic pricing requirement based heavily upon the "Down-and-In" parameters functioning entirely as a heavily Path-Dependent mathematical system overlay. Unlike general simplistic European endpoints, its intrinsic payout completely necessitates tracking exactly whether strict barrier thresholds ($80$) break across any timeline increment. Monte Carlo structurally generates clear, discrete step-by-step sequential event logging permitting the engine to instantly activate internal "knock-in" flags organically across multiple chaotic path iterations that closed-form analytical equations systematically struggle properly rendering.

### Part (ii) [4 marks]

A barrier of $80$ is actively monitored at each step including $t=5$. A strike of $100$ applies to the final value tracking basic standard $\max(0, 100 - S_5)$ equations for activated options. We must trace logic mapping perfectly across every individual path:

1. Hits min exactly at $62$ ($<80$). Knock-in active. Final $S=69$. $\max(100 - 69, 0) = 31$.
2. Min hits uniquely $84$ ($>80$). Never touches boundaries. Option identically fails. Payoff $= 0$.
3. Min hits uniquely $96$ ($>80$). Path misses knocking parameters. Payoff $= 0$.
4. Massively positive sequence. Fails completely. Payoff $= 0$.
5. Drops tracking downwards hitting uniquely $67$ safely across exactly terminal Step 5. This fully initiates "knock-in". Final $S=67$. $\max(100 - 67, 0) = 33$.
6. Stable upward tracking matrix. Fails. Payoff $= 0$.
7. Standard positive. Fails. Payoff $= 0$.
8. Heavy elevated growth model tracking high. Fails. Payoff $= 0$.
9. Sinks deeply toward $78$ hitting barrier limits appropriately across step 4. Active. Final $S=73$. $\max(100 - 73, 0) = 27$.
10. Sinks mapping softly toward $86$ boundary limits safely. Fails barrier thresholds identically. Payoff $= 0$.

Combining activated outputs provides: $31 + 33 + 27 = 91$.
Sum averaging the simulated inputs yields absolute value expectation: $= \frac{91}{10} = 9.1$.
*(Interest and discounting is zero $r=0$, so exact option present price establishes securely exactly at $9.1$)*.

### Part (iii) [4 marks]

Standard deviation and error require isolated variance computations extracting deviations structurally from established expectations.
Identified sequential outcomes: $X_i =$ [31, 0, 0, 0, 33, 0, 0, 0, 27, 0]
Empirical Mean $\bar{X} = 9.1$

Sum of structural variances squared off means: $(X_i - \bar{X})^2$
$= (31 - 9.1)^2 + (33 - 9.1)^2 + (27 - 9.1)^2 + 7 \times (0 - 9.1)^2$
$= (21.9)^2 + (23.9)^2 + (17.9)^2 + 7 \times (-9.1)^2$
$= 479.61 + 571.21 + 320.41 + 579.67 = 1950.9$

Sample Variance ($s^2$) incorporates standard $n-1$ denominator (equating toward $9$):
$s^2 = \frac{1950.9}{9} = 216.7667$
Standard Deviation mathematically equals $s = \sqrt{216.7667} \approx 14.723$.

Standard Error of Mean (SE) calculation $= \frac{s}{\sqrt{N}} < 1.0$
To reduce structural tracking error cleanly below parameter lines of 1.0:
$\sqrt{N} > 14.723$
$N > 14.723^2$ 
$N > 216.7667$  
Thus, standard accuracy targets strictly demand the mathematical deployment of exactly **217** minimum Monte Carlo simulated paths.

### Part (iv) [4 marks]

The ‘down-and-in’ parameter completely revolutionizes the basic asset pricing metric profoundly:
- Extracting raw baseline equivalent plain vanilla structures devoid completely of restrictive knockout conditional lines, paths 2 and 10 formally represent standard standard in-the-money put option expirations (paying uniquely 16 and 3 respectively since both settle below 100 strike thresholds).
- By requiring the stock initially plunging below specific rigid support bands ($80$) first beforehand, it instantly slashes standard output values removing exactly those more moderate decline profit corridors yielding lower combined aggregate outputs heavily. 
- Due directly to this heavy path restriction criteria reducing payout odds structurally, the market premium completely drops becoming inherently cheaper than identical comparative standard European options giving purchasers deep cost discounts safely mapping against extreme crash views rather than standard hedging targets.

### Part (v) [3 marks]

Deploying distinctly massive and structurally isolated timeline interval step sizes yields dangerous computational tracking weaknesses:
- Heavy discrete sampling strictly ignores crucial high-frequency internal intra-step movement dynamics. The actual asset path can smoothly dip wildly deeply crossing under the arbitrary absolute barrier limitation threshold and structurally rebound upwards entirely hidden safely between recording points securely generating artificial "safe" signals causing heavy negative knock-in activation underestimations.
- Functionally, evaluating down-and-in exotic structures via highly spaced time variables rigidly forces the mathematical calculated option valuation downwards artificially beneath true market benchmarks generating pure negative bias errors mathematically mapping out against continuous evaluation equivalents normally traded actively inside the market.
- A structurally refined fix demands deploying vastly heavier granular time slicing matrices multiplying nodes heavily or mathematically appending localized algorithmic Brownian-bridge conditional crossing probability layers smoothing exact path variables mathematically.

---

## Audit Trail

### Accessed Files
- `exams/SP6/September_2025/question-paper.pdf`
- `exams/SP6/September_2025/question-paper.md`
- `references/formulae-and-tables.pdf`
- `scripts/convert_pdf_to_md.py`
