# CM2A — September 2025 — Exam Attempt

**Model:** Gemini 3.1 Pro (High)
**Date:** 2026-02-25
**Time allocated:** 3 hours 20 minutes

---

## Question 1

### Part (i) [7 marks]

To calculate the total reserve using the Bornhuetter–Ferguson (BF) method, we first determine the development factors from the given cumulative claims triangle.

**Development factors:**
$$f_{0,1} = \frac{84 + 89 + 180}{67 + 70 + 133} = \frac{353}{270} = 1.3074$$
$$f_{1,2} = \frac{101 + 120}{84 + 89} = \frac{221}{173} = 1.2775$$
$$f_{2,3} = \frac{113}{101} = 1.1188$$

**Proportion of claims developed ($z_j$):**
Using $z_3 = 1.0$ (claims fully developed by year 3):
$$z_2 = \frac{1}{f_{2,3}} = \frac{1}{1.1188} = 0.8938$$
$$z_1 = \frac{z_2}{f_{1,2}} = \frac{0.8938}{1.2775} = 0.6997$$
$$z_0 = \frac{z_1}{f_{0,1}} = \frac{0.6997}{1.3074} = 0.5352$$

**Expected Ultimate Loss Ratio (ULR):**
The 2021 accident year has earned premium of 128 and ultimate claims (year 3) of 113.
$$ULR = \frac{113}{128} = 0.8828$$

**Bornhuetter-Ferguson Reserves:**
The reserve required is given by $\text{Earned Premium} \times ULR \times (1 - z_j)$.

- 2022: $145 \times 0.8828 \times (1 - 0.8938) = 13.59$
- 2023: $216 \times 0.8828 \times (1 - 0.6997) = 57.27$
- 2024: $468 \times 0.8828 \times (1 - 0.5352) = 192.05$

**Total Reserve Required:**
$13.59 + 57.27 + 192.05 = \mathbf{262.91}$

### Part (ii) [2 marks]

An insurance regulator may prefer the Bornhuetter-Ferguson method because it incorporates a prior expected ultimate loss ratio, making it more stable and less sensitive to early claim fluctuations. The basic chain ladder method relies solely on historical run-off patterns, so purely anomalous random changes in the earliest development years can significantly distort the projected ultimate claims for recent accident years. The BF method provides a smoother, expectation-anchored estimate which supports solvency stability.

---

## Question 2

### Part (i) [2 marks]

**Lundberg's inequality** states that the probability of ultimate ruin, $\psi(u)$, for an insurer with an initial capital $u$ satisfies the following upper bound:
$$\psi(u) \le e^{-Ru}$$
Where $u$ is the initial wealth and $R$ is the adjustment coefficient, which is defined as the unique positive root of the equation $\lambda M_X(R) - \lambda - c R = 0$, where $\lambda$ is the Poisson claim arrival rate, $M_X(R)$ is the moment generating function of the claim severity distribution, and $c$ is the continuous premium income rate.

### Part (ii) [4 marks]

We have $\lambda = 1$, claim amounts $X \sim Exp(\text{mean } 1000)$, and premium loading factor $\theta = 0.25$.
Premium condition: $c = (1 + \theta)\lambda E[X] = (1.25)(1)(1000) = 1250$.
The moment generating function for an exponential distribution with mean $\mu = 1000$ is given by $M_X(R) = \frac{1}{1 - 1000R}$ for $1000R < 1$.

Lundberg's equation:
$$\lambda M_X(R) - \lambda - cR = 0$$
$$\frac{1}{1 - 1000R} - 1 - 1250R = 0$$

Multiply both sides by $(1 - 1000R)$:
$$1 - (1 - 1000R) - 1250R(1 - 1000R) = 0$$
$$1000R - 1250R + 1250000R^2 = 0$$
$$1250000R^2 - 250R = 0$$
Since $R > 0$, we can divide by $250R$:
$$5000R - 1 = 0 \implies R = \frac{1}{5000} = \mathbf{0.0002}$$

### Part (iii) [1 mark]

Using Lundberg's inequality for initial wealth $u = 5000$:
$$\text{Upper bound} = e^{-0.0002 \times 5000} = e^{-1} = \mathbf{0.3679}$$

### Part (iv) [2 marks]

If the insurer pays a fixed lump sum of \$1,000 for each claim, the new claim distribution becomes degenerate at \$1,000 with zero variance. The mean claim size remains \$1,000, meaning the premium income rate ($c = 1250$) stays intact.
Because the variance of claims decreases drastically (from $1000^2$ to $0$) while retaining the same mean and premium, the adjustment coefficient $R$ will increase. A larger adjustment coefficient $R$ strictly decreases the upper bound $e^{-Ru}$. Thus, the impact of the proposal drops the uncertainty strictly mitigating tail risk, lowering the overall probability of ultimate ruin.

---

## Question 3

### Part (i) [4 marks]

For the single-period multifactor model:
$$R_i = a_i + \sum_{j=1}^K b_{ij} I_j + e_i$$
We aim to find $C_{ij} = \text{Cov}(R_i, R_m)$ (here we use $m$ to denote the second security to prevent index clash).
Since the security specific random components $e_i$ and $e_m$ are cross-sectionally independent, $\text{Cov}(e_i, e_m) = 0$ for $i \neq m$. The components $e_i$ are also independent of the factors $I_j$, so $\text{Cov}(e_i, I_j) = 0$.
Additionally, the factors $I_j$ are cross-sectionally independent, leading to $\text{Cov}(I_k, I_l) = 0$ for $k \neq l$.
$$\text{Cov}(R_i, R_m) = \text{Cov}\left(a_i + \sum_{j=1}^K b_{ij} I_j + e_i, a_m + \sum_{j=1}^K b_{mj} I_j + e_m\right)$$
$$\text{Cov}(R_i, R_m) = \sum_{j=1}^K b_{ij} b_{mj} \text{Var}(I_j)$$

### Part (ii) [3 marks]

For an equally-weighted portfolio of $N$ securities, the portfolio weight is $w = \frac{1}{N}$.
The variance of the portfolio is:
$$\text{Var}(R_P) = \sum_{i=1}^N \frac{1}{N^2} \text{Var}(R_i) + \sum_{i \neq l} \frac{1}{N^2} \text{Cov}(R_i, R_l)$$
As the number of securities $N \to \infty$, the first term (security-specific risk) diminishes to zero ($\frac{N}{N^2} \to 0$). The second term remains and reflects the average covariance between the securities caused by shared factor exposures. This implies that specific, idiosyncratic risk is diversified away, whereas the systematic risk, governed by the factors $I_j$ and the corresponding sensitivities ($b_{ij}$), persists in the portfolio's variance.

### Part (iii) [4 marks]

In the single index model: $R_i = \alpha_i + \beta_i R_M + e_i$
Given: $\text{Cov}(R_X, R_Y) = -0.000075$, $\beta_X = 1.5$, $\text{Var}(R_M) = (1.0\%)^2 = 0.0001$.
$$\text{Cov}(R_X, R_Y) = \beta_X \beta_Y \text{Var}(R_M)$$
$$-0.000075 = 1.5 \times \beta_Y \times 0.0001$$
$-0.000075 = 0.00015 \beta_Y \implies \beta_Y = \mathbf{-0.5}$

Next, for security X, using $E[R_M] = 7.5\%$:
$$E[R_X] = \alpha_X + \beta_X E[R_M]$$
$$0.123 = \alpha_X + 1.5 \times 0.075$$
$$0.123 = \alpha_X + 0.1125 \implies \alpha_X = \mathbf{0.0105} \text{ (or } 1.05\%)$$

### Part (iv) [4 marks]

Because the covariance between the returns on securities X and Y is strictly negative (-0.000075), combining them into a portfolio produces significant diversification benefits. Their responses to movements in the market index ($R_M$) are opposite directionally ($\beta_X = 1.5$ and $\beta_Y = -0.5$).
An investor could construct a portfolio with appropriately balanced long combinations (e.g., allocating proportional funds strictly $X:Y$ at $1:3$ ratio, weights 0.25 and 0.75 respectively) which nets the aggregate market Beta to zero (($0.25 \times 1.5) + (0.75 \times -0.5) = 0$). By completely hedging out market systematic risk ($R_M$), the resulting portfolio operates purely on stock-specific parameters isolating absolute returns while removing directional market variance. 

---

## Question 4

### Part (i) [2 marks]

Four assumptions underlying the Black-Scholes option pricing model:
1. The underlying asset price follows a geometric Brownian motion with constant drift and volatility ($\sigma$).
2. The risk-free rate of interest ($r$) is constant and applies to all maturities.
3. The underlying asset pays no dividends during the life of the option.
4. There are no transaction costs or taxes, and trading is continuous.

### Part (ii) [3 marks]

We have $S = 75$, $K = 60$, $T = 3$, $r = 0.04$, $\sigma = 0.15$.
$$d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma \sqrt{T}} = \frac{\ln(75/60) + (0.04 + 0.5 \times 0.15^2) \times 3}{0.15 \sqrt{3}}$$
$$d_1 = \frac{0.22314 + (0.04 + 0.01125) \times 3}{0.25981} = \frac{0.22314 + 0.15375}{0.25981} = \frac{0.37689}{0.25981} = 1.4507$$
$$d_2 = d_1 - \sigma \sqrt{T} = 1.4507 - 0.25981 = 1.1909$$

Using normal CDF probabilities:
$\Phi(d_1) = 0.9266$
$\Phi(d_2) = 0.8831$

$$c = S \Phi(d_1) - K e^{-rT} \Phi(d_2)$$
$$c = 75 \times 0.9266 - 60 \times e^{-0.12} \times 0.8831$$
$$c = 69.495 - (53.215) \times 0.8831 = 69.495 - 46.994 = \mathbf{22.50}$$

### Part (iii) [2 marks]

Delta ($\Delta_c$) acts as the first derivative of the option price with respect to the share price indicating expected change:
$$\Delta_c \approx \frac{\Delta c}{\Delta S}$$
$$\Delta_c \approx \frac{27.21 - 22.50}{80 - 75} = \frac{4.71}{5} = \mathbf{0.942}$$
*(Note: Exceedingly close to explicit numerical solution $\Phi(d_1) = 0.926$ plus convex gamma effect for finite movements)*

### Part (iv) [3 marks]

Put-call parity for European options holds:
$$c - p = S - K e^{-rT}$$
Taking the first derivative with respect to the underlying stock price $S$:
$$\frac{\partial c}{\partial S} - \frac{\partial p}{\partial S} = \frac{\partial S}{\partial S} - 0$$
$$\Delta_c - \Delta_p = 1$$

### Part (v) [2 marks]

The portfolio combines long one call, short one put, and short the underlying share.
$\text{Portfolio Value}_{T} = c - p - S$.
According to put-call parity ($c - p - S = -K e^{-rT}$), this portfolio has a completely deterministic, risk-less payoff regardless of the eventual share price path. The investor would create this synthetic position to exploit short-term violations of put-call parity for spatial arbitrage (risk-free profit) or to borrow money implicitly at the risk-free rate structurally bypassing standard lending markets.

### Part (vi) [2 marks]

As the share price increases, the European call option moves deeper into-the-money. The probability of the option expiring exercised strictly approaches 1. Therefore $\Delta_c$, which essentially correlates dynamically to $\Phi(d_1)$, asymptotically rises towards 1.0. The sensitivity speed driving this correlation change refers to the positive Gamma ($\Gamma$) function intrinsic to continuous option positions.

---

## Question 5

### Part (i) [6 marks]

The maturity payoff $X$ distribution takes values $\{0, 1, 2, 3, 4, 5\}$ with conditional probability $1/6$ if default occurs (prob = $0.2$). Otherwise, payload returns strict $\$6$ (prob = $0.8$).
Expected value $\mu = E[X] = 0.8(6) + 0.2 \left( \frac{0+1+2+3+4+5}{6} \right) = 4.8 + 0.5 = 5.3$.

**(a) Downside semi-variance**
Calculated using the expected value ($\mu = 5.3$) as the default threshold parameter. Note, considering the only instances failing below thresholds are purely embedded within default branches:
$$\text{Semivariance} = E[\max(0, \mu - X)^2]$$
$$= 0.8 \times \max(0, 5.3 - 6)^2 + 0.2 \sum_{x=0}^5 \frac{1}{6} \max(0, 5.3 - x)^2$$
Since $5.3 - 6 < 0$, the $0.8$ term contributes natively $0$.
$$= \frac{0.2}{6} \left[ 5.3^2 + 4.3^2 + 3.3^2 + 2.3^2 + 1.3^2 + 0.3^2 \right]$$
$$= 0.03333 \times [28.09 + 18.49 + 10.89 + 5.29 + 1.69 + 0.09]$$
$$= 0.03333 \times 64.54 = \mathbf{2.151}$$

**(b) Shortfall probability below \$4**
The outcomes strictly below \$4 are values $0, 1, 2,$ and $3$. All stem definitively from the default state.
$$P(X < 4) = 0.2 \times \frac{4}{6} = \frac{0.8}{6} = \mathbf{0.1333}$$

**(c) Expected shortfall below \$4**
$$E[\max(0, 4 - X)] = 0.2 \sum_{x=0}^3 \frac{1}{6} (4 - x) = \frac{0.2}{6} ((4-0) + (4-1) + (4-2) + (4-3))$$
$$= 0.03333 \times (4 + 3 + 2 + 1) = 0.03333 \times 10 = \mathbf{0.3333}$$

### Part (ii) [1 mark]

If the default probability elevates to 30%, downside structural risks uniformly broaden. The downside semi-variance will logically increase. Both shortfall probability and expected shortfall calculations scale uniformly upward because the weighting assigned to the compromised default branch actively expands.

---

## Question 6

### Part (i) [2 marks]

The four axioms used to derive the expected utility theorem are:
1. **Completeness (Comparability):** An individual has strong determinable preferences ensuring any two lotteries can be explicitly ranked, e.g. either $A \succ B$, $B \succ A$, or $A \sim B$.
2. **Transitivity:** A logical consistency of preferences; if $A \succ B$ and $B \succ C$, then $A \succ C$.
3. **Independence:** If $A \succ B$, then a mixture of $A$ identically holds superior weighting against a matching mixture mapping of $B$. ($pA + (1-p)C \succ pB + (1-p)C$).
4. **Continuity (Certainty Equivalence):** If $A \succ B \succ C$, there rigidly implies a distinct valid probability $p$ such that the individual functionally maintains indifference mapping $B \sim pA + (1-p)C$.

### Part (ii) [2 marks]

Utility function: $U(w) = w - \frac{w^2}{2d}$
First derivative: $U'(w) = 1 - \frac{w}{d}$
Second derivative: $U''(w) = -\frac{1}{d}$

**(a) Non-satiation:** $U'(w) > 0 \implies 1 - \frac{w}{d} > 0 \implies \mathbf{d > w}$
**(b) Diminishing marginal utility:** $U''(w) < 0 \implies -\frac{1}{d} < 0 \implies \mathbf{d > 0}$

### Part (iii) [1 mark]

Current wealth $w = 100,000$ and $U(100,000) = 75,000$.
$$75,000 = 100,000 - \frac{100,000^2}{2d}$$
$$-25,000 = -\frac{10,000,000,000}{2d}$$
$$2d = 400,000 \implies \mathbf{d = 200,000}$$

### Part (iv) [3 marks]

Initial wealth before wedding = \$100,000. Core wedding fee universally spent: \$15,000.
We consider the four outcome wealths (and associated probabilities):
- $O_1$: No issue. Wealth $w_1 = 100,000 - 15,000 = 85,000$ ($p = 0.70$)
- $O_2$: Damages \$2k. Wealth $w_2 = 100,000 - 15,000 - 2,000 = 83,000$ ($p = 0.15$)
- $O_3$: Cancellations. No additional cost, no refund. Wealth $w_3 = 100,000 - 15,000 = 85,000$ ($p = 0.05$)
- $O_4$: Venue \$5k loss. Wealth $w_4 = 100,000 - 15,000 - 5,000 = 80,000$ ($p = 0.10$)

Substitute to Utility $U(w) = w - \frac{w^2}{400,000}$:
- $U(85,000) = 85,000 - 18,062.5 = 66,937.5$
- $U(83,000) = 83,000 - 17,222.5 = 65,777.5$
- $U(80,000) = 80,000 - 16,000.0 = 64,000.0$

Expected Utility:
$$EU = 0.70(66937.5) + 0.15(65777.5) + 0.05(66937.5) + 0.10(64000)$$
$$EU = 46856.25 + 9866.625 + 3346.875 + 6400 = \mathbf{66469.75}$$

### Part (v) [3 marks]

We calculate the projected wealth states provided full insurance indemnity (less the unknown absolute premium $P$):
- $O_1$: Coverage $\$0$. Final wealth $= 85,000 - P$
- $O_2$: Damages covered $\$2,000$ (limits under $\$10k$). Final wealth $= 85,000 - P$
- $O_3$: Cancellation pays $\frac{15,000}{2} = 7,500$. Final wealth $= 85,000 + 7,500 - P = 92,500 - P$
- $O_4$: Venue substitution covered $\$5,000$. Final wealth $= 85,000 - P$

Grouping strictly identical probabilities:
$P(W_{ins} = 85,000 - P) = 0.70 + 0.15 + 0.10 = 0.95$
$P(W_{ins} = 92,500 - P) = 0.05$

Set explicitly Equal Utility criteria to determine Maximum Premium mapping target $EU_{no\_insurance}$:
$$0.95 \times U(85000 - P) + 0.05 \times U(92500 - P) = 66469.75$$
Solving iteratively (via derived model / bounds): Maximum permitted target limits equalisation at approximately $\mathbf{\$1,174}$. The individual secures utility surplus mapping safely assuming any quoted cost lies below this absolute figure.

---

## Question 7

### Part (i) [1 mark]

For $N=1$, each round implies a simple random walk step of $+\$1$ or $-\$1$ for the casino's wealth. Starting from $\$5$, the possible wealth figures after 2 rounds are $\$3$, $\$5$, or $\$7$.
Since the wealth cannot drop to zero within exactly two steps maximally bounding $-\$2$, the probability of bankruptcy is $\mathbf{0}$.

### Part (ii) [2 marks]

Starting from $\$5$, ruin at precisely the 5th round requires the casino to strictly lose linearly 5 recurring rounds in succession (dropping $\$1$ every single round uninterrupted). 
$$P(\text{Ruin after 5}) = (0.5)^5 = \frac{1}{32} = \mathbf{0.03125}$$

### Part (iii) [5 marks]

**(a) Target wealth distributions tracking cumulative iterations directly mapped from $N=5$ bets per round:**
Number of winning customers conditionally behaves precisely as a Binomial Distribution ($n=5, p=0.5$).
Casino functionally collects $5$ inputs, expending selectively out $2$ per winning tier constraint $k$. Profit structurally isolates to $= 5 - 2k$.

Probabilities of per-round profits natively calculate matching $Bin(5, 0.5)$:
| $k$ | Profit | Probability | End Round 1 Wealth |
|---|---|---|---|
| 0 | +\$5 | 1/32 (0.03125) | \$10 |
| 1 | +\$3 | 5/32 (0.15625) | \$8 |
| 2 | +\$1 | 10/32 (0.31250) | \$6 |
| 3 | -\$1 | 10/32 (0.31250) | \$4 |
| 4 | -\$3 | 5/32 (0.15625) | \$2 |
| 5 | -\$5 | 1/32 (0.03125) | \$0 (RUIN) |

To map Round 2 possibilities we must multiply Round 1 continuing surviving branches natively against repeating iteration metrics. As Round 1 outputs limit to values $\{10,8,6,4,2,0\}$, any repeating chain resulting $\le 0$ constitutes cumulative ruin boundaries.

**(b) Probability of bankruptcy explicitly restricted through the *first two rounds*:**
The probability of entering ruins purely inside Round 1 directly equals the $-\$5$ extreme condition: $P(ruin_1) = 1/32 \approx 0.03125$.
If Round 1 survives actively, Round 2 absorbs risk limits specifically when existing Wealth structures face critical limits dynamically:
- If $W_1 = 4$ (Prob 10/32), needs profit $-\$5$ (Prob 1/32) $\to \frac{10}{1024}$
- If $W_1 = 2$ (Prob 5/32), needs profit $-\$3$ or $-\$5$ (Prob 6/32) $\to \frac{30}{1024}$

Consolidating total sequence metrics mathematically dictates:
$P(\text{Ruin entirely}) = \frac{32}{1024} + \frac{10}{1024} + \frac{30}{1024} = \frac{72}{1024} \approx \mathbf{0.0703}$

### Part (iv) [2 marks]

Because the structural $N=5$ environment expands concurrent transactional throughput fivefold per round without uniformly boosting baseline operational capacity scales organically, cumulative variance heavily distorts extreme movements directly. Higher aggregated volume significantly stretches distributional boundaries granting faster, exponentially denser opportunities breaching capital limits in condensed timeframes than sequential, smoothed constraints artificially imposed inside the $N=1$ limit. 

### Part (v) [2 marks]

This casino acts organically paralleling discrete ruin theory assumptions mapping an early-stage insurance underwriter aggregating homogenous identical-scale premiums while facing volatile binary claims distribution constraints. Just as insurers operate natively tracking probability-of-ruin models reflecting starting surplus against portfolio width dimensions, the casino risks insolvency tracking matching mathematical limits showing explicitly that unless underwriting reserves linearly pace increased transactional exposure ($N$), ultimate structural failure rates expand exponentially regardless of zero-mean fair-game advantages over unbounded timelines.

---

## Question 8

### Part (i) [3 marks]

- **(a) Weak form:** Asserts that historical price and trading volume data are already fully reflected inside current asset prices, rendering technical analysis entirely useless for generating persistent abnormal returns.
- **(b) Semi-strong form:** Maintains that all publicly available information (inclusive of historical limits natively alongside structural financial statements and market news) immediately consolidates into the asset price rendering fundamental analysis powerless producing excess returns.
- **(c) Strong form:** Defines strict perfection mapping where absolute information matrices—incorporating totally sequestered, exclusive internal corporate secrets/insider knowledge—absorb effortlessly inside prices completely eliminating all structural abnormal returns regardless of privilege levels. 

### Part (ii) [6 marks]

**1. Unexpected positive earnings stock price rise**
This behaviour explicitly reacts absorbing entirely brand new systemic inputs harmonising inherently with the **semi-strong form**. By structurally adjusting exclusively upon externalising the news event dynamically, it successfully maps both semi-strong and absolute strong form principles verifying organic market tracking mechanics.

**2. Board member prevented capitalising on pending approvals**
Because the strictly private constraints and sequestered privileged drug approvals were inherently baked heavily inside existing price definitions nullifying leverage capacity, this instance fully supports the **strong form** definitions. Crucially, it directly violates the semi-strong form limits naturally because strictly unpublished insider details managed functionally leaking organic absorptions internally prior broadly cascading into wider generic distributions legally reflecting absolute maximum integration. 

**3. Investor effectively identifies undervalued stocks via fundamental analysis**
Consistently generating abnormal advantages actively via deep structural external investigation contradicts firmly both bounds inherently defining the specific **semi-strong form** and strictly wider reaching **strong form**. Under functional semi-strong properties entirely assumed, such granular report readings should guarantee distinctly zero operational leverage as identical variables intrinsically match native baseline evaluations. Consequently, this scenario completely negates the hypothesis bounds targeted universally maintaining limits isolated purely restricting inside minimal Weak boundaries solely.

---

## Question 9

### Part (i) [4 marks]

The Tower Property declares: $E(Y_2|F_0) = E[E(Y_2|F_1)|F_0]$. 
Based mathematically reflecting upsteps $U=1.2 (75\%)$ and downsteps $D=0.9 (25\%)$.

Conditional Expectation of subsequent period logically tracking prior anchor limits dynamically translates natively:
$$E(Y_{t+1}|F_t) = 0.75 \times 1.2 Y_t + 0.25 \times 0.9 Y_t$$
$$E(Y_{t+1}|F_t) = Y_t(0.90 + 0.225) = 1.125 Y_t$$

Using this identity backwards sequentially validating conditional properties internally guarantees:
$$E(Y_2|F_1) = 1.125 Y_1$$
Taking expectations again unconditionally rooted reflecting start targets identically completes standard nested substitutions intrinsically:
$$E[E(Y_2|F_1)|F_0] = E[1.125 Y_1 |F_0] = 1.125 \times E[Y_1|F_0]$$
Since $E[Y_1|F_0] = 1.125 Y_0$, we definitively generate recursively $1.125 \times 1.125 Y_0 = \mathbf{1.2656 Y_0}$.

Verifying bounds manually evaluating all discrete nodes explicitly calculating raw branches yields:
- $UU: 1.44 Y_0 \times (0.75 \times 0.75 = 0.5625)$
- $UD/DU: 1.08 Y_0 \times (0.75 \times 0.25 \times 2 = 0.375)$
- $DD: 0.81 Y_0 \times (0.25 \times 0.25 = 0.0625)$

Total raw expected value definitively aggregates purely mapping exactly absolute validation paths comprehensively:
$E[Y_2|F_0] = 1.44(0.5625) + 1.08(0.375) + 0.81(0.0625) = 0.81 + 0.405 + 0.0506 = \mathbf{1.2656 Y_0}$. The definitions strictly match mapping proof successfully. 

### Part (ii) [1 mark]

The property establishes backward induction recursively ensuring complex multi-step derivatives cleanly isolate calculating expected final-node payloads scaling backwards conditionally stage-by-stage sequentially mitigating systemic calculation burdens naturally without disrupting absolute martingale bounds.

---

## Question 10

### Part (i) [6 marks]

Given Asset S weight volume 500 mapping $1.5\%$ regular limits daily ($\sigma_S \approx \$7.5$) and Asset T weight volume 700 mapping $1.3\%$ absolute limits similarly ($\sigma_T \approx \$9.1$). Correlation strictly defined scaling limits $\rho = 0.5$.

Assuming universally an arbitrary baseline parameter dynamically anchoring confidence measurements globally against 95% standard limits mathematically targeting single-sided continuous boundaries native evaluating ($z \approx 1.64485$).

**(a)**
Daily discrete Value at Risk natively bounds sequentially:
- $\text{VaR}_S (\text{Daily}) = 7.5 \times z$
- $\text{VaR}_T (\text{Daily}) = 9.1 \times z$

Mapping generic uniform constraints tracking square root time variables $n=9$ specifically calculating targeted horizon expansions globally evaluates: 
- 9-day $\text{VaR}_S = 7.5 \times \sqrt{9} \times 1.64485 \approx 22.5 \times 1.64485 = \mathbf{\$37.01}$
- 9-day $\text{VaR}_T = 9.1 \times \sqrt{9} \times 1.64485 \approx 27.3 \times 1.64485 = \mathbf{\$44.91}$

**(b)**
Evaluating portfolio aggregate native correlations strictly:
$\sigma_{Daily\_P} = \sqrt{\sigma_S^2 + \sigma_T^2 + 2\rho(\sigma_S)(\sigma_T)} = \sqrt{7.5^2 + 9.1^2 + 2(0.5)(7.5)(9.1)}$
$\sigma_{Daily\_P} = \sqrt{56.25 + 82.81 + 68.25} = \sqrt{207.31} = \$14.398$

Re-mapping 9-day aggregate limits tracking horizon scaling internally limits VaR structures entirely conditionally:
- 9-day $\text{VaR}_{P} = 14.398 \times \sqrt{9} \times 1.64485 \approx 43.194 \times 1.64485 = \mathbf{\$71.05}$

*(Note: Exact values scale naturally adjusting corresponding limits natively reflecting any absolute specific z-value internally selected tracking Solvency parameters)*

### Part (ii) [3 marks]

Because the aggregate combined VaR metric mapped reflecting consolidated holdings intrinsically calculates (\$71.05) definitively positioned far beneath the mathematical ceiling naturally representing individual isolated VaR boundaries actively paired functionally (\$37.01 + $44.91 = $81.92), it systematically illustrates organic portfolio diversification benefits natively tracking less-than-perfect asset correlations internally. Such structural mitigations highlight effectively reducing systemic variance risk exposures simply reflecting non-unitary aggregate variable movements entirely independent tracking market swings.

---

## Audit Trail

### Accessed Files
- `exams/CM2A/September_2025/question-paper.md`
- `references/formulae-and-tables.pdf` (Referenced structural limit definitions)
- Python computational scratchpad file `run_calc2.py`
