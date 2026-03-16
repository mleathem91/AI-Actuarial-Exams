# CS1A — September 2025 — Exam Attempt

**Model:** Gemini 3.1 Pro (High)
**Date:** 2026-02-25
**Time allocated:** 3 hours 20 minutes

---

## Question 1

### Part (i) [2 marks]

The marginal distribution of $Y$ is Geometric(p) with probability function $P(Y=y) = p(1-p)^{y-1}$ for $y=1,2,3,\ldots$ and $p=0.5$.
Hence $P(Y=y) = 0.5 \times 0.5^{y-1} = 0.5^y = \frac{1}{2^y}$.

The conditional probability function of $X$ given $Y=y$ is:
$$ P(X=x \mid Y=y) = \frac{P(X=x, Y=y)}{P(Y=y)} = \frac{\frac{e^{-y} y^x}{2^y x!}}{\frac{1}{2^y}} = \frac{e^{-y} y^x}{x!} $$

This matches Option A.

**Answer:** A

### Part (ii) [1 mark]

From the conditional probability function derived in Part (i), $P(X=x | Y=y) = \frac{e^{-y} y^x}{x!}$, which is the probability mass function of a Poisson distribution.

Distribution: Poisson distribution  
Parameter: $\lambda = y$

### Part (iii) [2 marks]

Using the law of total expectation:
$E[X] = E[E[X \mid Y]]$

Since $X \mid Y \sim Poisson(Y)$, we know $E[X \mid Y] = Y$.
Thus, $E[X] = E[Y]$.

$Y$ follows a Geometric distribution with parameter $p=0.5$ (defined on $1, 2, 3, \ldots$).  
The expected value of this Geometric distribution is $E[Y] = \frac{1}{p} = \frac{1}{0.5} = 2$.

Therefore, $E[X] = 2$.

---

## Question 2

### Part (i) [2 marks]

Yes, the sample mean $\bar{X}$ is an unbiased estimator for the population mean $\mu$. 
By definition of an unbiased estimator, $E[\bar{X}] = \mu$.

Proof: Let $X_1, X_2, \ldots, X_{50}$ be the random sample.
$E[\bar{X}] = E\left[\frac{1}{n}\sum_{i=1}^n X_i\right] = \frac{1}{n}\sum_{i=1}^n E[X_i] = \frac{1}{n} \times n\mu = \mu$.

### Part (ii) [2 marks]

The variance of the sample mean is given by the variance of the population divided by the sample size:
$Var(\bar{X}) = \frac{\sigma^2}{n}$

Given $\sigma^2 = 16$ and $n = 50$:
$Var(\bar{X}) = \frac{16}{50} = 0.32$.

### Part (iii) [1 mark]

The mean square error (MSE) of an estimator is the sum of its variance and the square of its bias:
$MSE(\bar{X}) = Var(\bar{X}) + Bias(\bar{X})^2$

Since $\bar{X}$ is an unbiased estimator, its bias is $0$.
Hence, $MSE(\bar{X}) = 0.32 + 0^2 = 0.32$.

---

## Question 3

### Part (i) [2 marks]

The cumulant generating function $C_X(t)$ is the natural logarithm of the moment generating function $M_X(t)$.
Assuming the intended expression of the MGF is $M_X(t) = (1 - at)^{-1}$:
$C_X(t) = \ln M_X(t) = \ln((1 - at)^{-1}) = -\ln(1 - at)$.

### Part (ii) [3 marks]

The cumulants of $X$ can be found by evaluating the derivatives of $C_X(t)$ at $t=0$, or by expanding the Maclaurin series for $-\ln(1-at)$:
$C_X(t) = -\ln(1-at) = at + \frac{(at)^2}{2} + \frac{(at)^3}{3} + \ldots$

The $k$-th cumulant $\kappa_k$ is the coefficient of $\frac{t^k}{k!}$ in the expansion.
$C_X(t) = at + a^2 \frac{t^2}{2!} + 2a^3 \frac{t^3}{3!} + \dots$

The mean is the first cumulant:
$E[X] = \kappa_1 = a$.

The variance is the second cumulant:
$Var(X) = \kappa_2 = a^2$.

---

## Question 4

### Part (i) [4 marks]

We have the following sample statistics:
Sample A: $n_A = 25$, $s_A^2 = 25$  
Sample B: $n_B = 13$, $s_B^2 = 15$

We know that the ratio $\frac{s_A^2 / \sigma_A^2}{s_B^2 / \sigma_B^2}$ follows an F-distribution with degrees of freedom $(n_A - 1, n_B - 1) = (24, 12)$.
A $90\%$ confidence interval for the variance ratio $\frac{\sigma_A^2}{\sigma_B^2}$ is given by:

$\left[ \frac{s_A^2}{s_B^2} \frac{1}{F_{24, 12}(0.95_{upper})}, \frac{s_A^2}{s_B^2} \frac{1}{F_{24, 12}(0.05_{upper})} \right]$

From the statistical tables:
- $F_{24, 12}(0.05_{upper}) = 2.505$
- $F_{24, 12}(0.95_{upper}) = \frac{1}{F_{12, 24}(0.05_{upper})} = \frac{1}{2.183} \approx 0.458$

Substituting our values:
- Lower limit = $\frac{25}{15} \times \frac{1}{2.505} = 1.6667 \times 0.3992 = 0.665$
- Upper limit = $\frac{25}{15} \times 2.183 = 1.6667 \times 2.183 = 3.638$

The 90% confidence interval for $\frac{\sigma_A^2}{\sigma_B^2}$ is $[0.665, 3.638]$.

### Part (ii) [2 marks]

We are testing the null hypothesis $H_0: \frac{\sigma_A^2}{\sigma_B^2} = 1$ against the alternative hypothesis $H_1: \frac{\sigma_A^2}{\sigma_B^2} \neq 1$ at the $10\%$ significance level.

The value $1$ represents equality of the population variances.
Since $1$ lies within our $90\%$ confidence interval $[0.665, 3.638]$ calculated in part (i), we have insufficient evidence to reject the null hypothesis at the $10\%$ level of significance. We conclude there is no significant difference between the variances of the claim amounts in the two portfolios.

### Part (iii) [1 mark]

The two required assumptions are:
1. The claim amounts in both underlying population portfolios follow normal distributions.
2. The samples taken from Portfolio A and Portfolio B are independent random samples.

---

## Question 5

### Part (i) [2 marks]

The normal/normal Bayesian model assumes the data (aggregate claims cost) follows a normal distribution.
A key feature of the normal distribution is that it has a domain of $(-\infty, \infty)$, which implies a positive probability of generating negative values.
Aggregate claims represent costs which theoretically cannot be negative. Therefore, strict suitability is low.
However, it can still serve as a reasonable and computationally convenient approximation if the expected aggregate claims are large relative to their standard deviation (such that the probability of negative values is negligible).

### Part (ii) [2 marks]

Using the law of total variance:
$Var(X_i) = Var(E[X_i \mid \theta]) + E[Var(X_i \mid \theta)]$

From the question statement, the conditional distribution of $X_i \mid \theta$ has mean $\theta$ and variance $\sigma_1^2$.
The prior distribution of $\theta$ has variance $\sigma_2^2$.

Substituting these components:
- $E[X_i \mid \theta] = \theta \implies Var(E[X_i \mid \theta]) = Var(\theta) = \sigma_2^2$
- $Var(X_i \mid \theta) = \sigma_1^2 \implies E[Var(X_i \mid \theta)] = E[\sigma_1^2] = \sigma_1^2$ (as $\sigma_1^2$ is fixed).

Summing those results gives:
$Var(X_i) = \sigma_2^2 + \sigma_1^2 = \sigma_1^2 + \sigma_2^2$.

### Part (iii) [3 marks]

We first find the unconditional covariance between $X_i$ and $X_j$:
$Cov(X_i, X_j) = E[Cov(X_i, X_j \mid \theta)] + Cov(E[X_i \mid \theta], E[X_j \mid \theta])$

Since $X_i, X_j$ are conditionally independent given $\theta$:
$Cov(X_i, X_j \mid \theta) = 0 \implies E[Cov(X_i, X_j \mid \theta)] = 0$

Then:
$Cov(X_i, X_j) = 0 + Cov(\theta, \theta) = Var(\theta) = \sigma_2^2$

The correlation coefficient is:
$\rho_{i,j} = \frac{Cov(X_i, X_j)}{\sqrt{Var(X_i)Var(X_j)}} = \frac{\sigma_2^2}{\sqrt{(\sigma_1^2 + \sigma_2^2)(\sigma_1^2 + \sigma_2^2)}} = \frac{\sigma_2^2}{\sigma_1^2 + \sigma_2^2}$

This matches Option B.

**Answer:** B

### Part (iv) [4 marks]

**(a) $\sigma_1^2 = 0$**
If $\sigma_1^2 = 0$, then $\rho_{i,j} = \frac{\sigma_2^2}{0 + \sigma_2^2} = 1$.
**Validity:** A conditional variance of $0$ means that there is no random fluctuation in $X_i$ once $\theta$ is known ($X_i = \theta$ with certainty). Since all $X_i$ are identical constants for any given $\theta$, any two years will be perfectly correlated unconditionally. The correlation is therefore exactly $1$.

**(b) $\sigma_2^2 = 0$**
If $\sigma_2^2 = 0$, then $\rho_{i,j} = \frac{0}{\sigma_1^2 + 0} = 0$.
**Validity:** A prior variance of $0$ implies there is no uncertainty in the risk parameter $\theta$, meaning the true parameter is fixed and known. The $X_i$ are generated independently from identical populations whose parameters are fixed. Therefore, there is no unconditional correlation between years (correlation is $0$).

---

## Question 6

### Part (i) [5 marks]

Let $X$ be the number of policyholders making a claim. $X \mid p \sim Binomial(100, p)$.
We observe a sample where $x = 15$ claims out of $n = 100$ policyholders.

The likelihood equation is:
$L(p \mid x) \propto p^{15} (1-p)^{100-15} = p^{15} (1-p)^{85}$

The prior distribution for $p$ is $Beta(a, b)$:
$f(p) \propto p^{a-1} (1-p)^{b-1}$

By Bayes' theorem, the posterior distribution is proportional to the product of the likelihood and prior:
$f(p \mid x) \propto L(p \mid x) f(p)$
$f(p \mid x) \propto p^{15} (1-p)^{85} \times p^{a-1} (1-p)^{b-1}$
$f(p \mid x) \propto p^{15+a-1} (1-p)^{85+b-1}$

This expression maps exactly to the kernel of a $Beta$ distribution.
Thus, the posterior distribution of $p$ is $Beta(a + 15, b + 85)$.

### Part (ii) [1 mark]

The posterior distribution is in the same mathematical family ($Beta$) as the prior distribution. This means that the $Beta$ distribution is the conjugate prior for binomial likelihoods.

### Part (iii) [3 marks]

Under all-or-nothing (0-1) loss, the Bayesian estimate is the mode of the posterior distribution (i.e. maximum a posteriori estimate).
For a $Beta(\alpha, \beta)$ distribution, the mode is given by:
$Mode = \frac{\alpha - 1}{\alpha + \beta - 2}$

Substituting the parameters of our posterior $Beta(a + 15, b + 85)$:
$\hat{p} = \frac{(a + 15) - 1}{(a + 15) + (b + 85) - 2}$
$\hat{p} = \frac{a + 14}{a + b + 100 - 2}$
$\hat{p} = \frac{a + 14}{a + b + 98}$

### Part (iv) [1 mark]

Given a $Beta(1, 1)$ prior, $a = 1$ and $b = 1$. Substituting into the estimate from part (iii):
$p' = \frac{1 + 14}{1 + 1 + 98} = \frac{15}{100} = 0.15$.

### Part (v) [2 marks]

The Bayesian estimate derived from a $Beta(1,1)$ prior under 0-1 loss is identical to the Maximum Likelihood Estimate (MLE) of $0.15$.
This is because a $Beta(1,1)$ prior corresponds to a Uniform(0,1) distribution, meaning the prior is "flat" and contains no informative beliefs. When the prior is flat, the mode of the posterior is purely governed by the maximum of the likelihood function.

---

## Question 7

### Part (i) [1 mark]

To model $X$ as a Binomial distribution $Bin(5, p)$, two main assumptions are required:
1. The probability $p$ that any specific sampled customer suffers food poisoning is constant across all customers in a given restaurant.
2. Whether one sampled customer suffers food poisoning is completely independent of the outcome of other sampled customers.

### Part (ii) [3 marks]

Total number of tests (customers surveyed) $n_{total} = 100 \times 5 = 500$
Total number of customers with food poisoning:
$k_{total} = (0 \times 40) + (1 \times 35) + (2 \times 19) + (3 \times 4) + (4 \times 1) + (5 \times 1) = 0 + 35 + 38 + 12 + 4 + 5 = 94$
Total customers without food poisoning = $500 - 94 = 406$.

The overall likelihood of experiencing exactly these sample counts across all observations is proportional to:
$L(p) \propto p^{94}(1 - p)^{406}$

This matches Option A.

**Answer:** A

### Part (iii) [4 marks]

The likelihood function is $L(p) = c p^{94}(1-p)^{406}$.
The log-likelihood is:
$l(p) = \ln(c) + 94 \ln(p) + 406 \ln(1-p)$

To find the turning point, we take the derivative with respect to $p$ and set it to $0$:
$\frac{\mathrm{d} l(p)}{\mathrm{d} p} = \frac{94}{p} - \frac{406}{1-p} = 0$
$\frac{94}{p} = \frac{406}{1-p}$
$94(1-p) = 406p$
$94 - 94p = 406p$
$500p = 94$
$\hat{p} = \frac{94}{500} = 0.188$

To verify it is a maximum, we look at the second derivative:
$\frac{\mathrm{d}^2 l(p)}{\mathrm{d} p^2} = -\frac{94}{p^2} - \frac{406}{(1-p)^2}$
Since $p \in [0,1]$, both terms are strictly negative, hence $\frac{\mathrm{d}^2 l(p)}{\mathrm{d} p^2} < 0$. This confirms the point $\hat{p} = 0.188$ is indeed a maximum.

### Part (iv) [3 marks]

Using the binomial probability formula and assuming $\hat{p} = 0.188$, we calculate expected counts.
Expected freq($x$) = $100 \times \binom{5}{x} p^x (1-p)^{5-x}$:

- $x = 0$: $100 \times 1 \times (0.188)^0 \times (0.812)^5 = 100 \times 0.3529 = 35.29$
- $x = 1$: $100 \times 5 \times (0.188)^1 \times (0.812)^4 = 100 \times 0.4086 = 40.86$
- $x = 2$: $100 \times 10 \times (0.188)^2 \times (0.812)^3 = 100 \times 0.1892 = 18.92$
- $x = 3$: $100 \times 10 \times (0.188)^3 \times (0.812)^2 = 100 \times 0.0438 = 4.38$
- $x = 4$: $100 \times 5 \times (0.188)^4 \times (0.812)^1 = 100 \times 0.0051 = 0.51$
- $x = 5$: $100 \times 1 \times (0.188)^5 \times (0.812)^0 = 100 \times 0.0002 = 0.02$

### Part (v) [5 marks]

For measuring the true mean $\mu$ cost per incident:
$n = 30$,   $\sum y_i = 975$,   $\sum y_i^2 = 34062$

Sample mean:
$\bar{y} = \frac{975}{30} = 32.5$

Sample variance is:
$s^2 = \frac{1}{n-1} \left( \sum y_i^2 - n\bar{y}^2 \right) = \frac{1}{29} \left( 34062 - 30(32.5)^2 \right) = \frac{1}{29} (34062 - 31687.5) = \frac{2374.5}{29} = 81.8793$
Sample standard deviation $s = \sqrt{81.8793} = 9.0487$.

**Assumptions**: Since the sample size ($n=30$) is large enough, by the Central Limit Theorem we assume the sample mean follows a Normal distribution, allowing use of normal or $t$-distributed confidence intervals. We calculate the $95\%$ confidence interval using the Student's $t$-distribution with $29$ degrees of freedom to be precise ($t_{29, 0.025} = 2.045$).

Limit evaluation:
$\bar{y} \pm t_{29, 0.025} \frac{s}{\sqrt{n}}$
$= 32.5 \pm 2.045 \times \frac{9.0487}{\sqrt{30}}$
$= 32.5 \pm 2.045 \times 1.6521$
$= 32.5 \pm 3.378$

$95\%$ Confidence Interval $= (29.12, 35.88)$.

*(Note: Utilizing standard normal quantiles ($1.96$) instead would yield $(29.26, 35.74)$).*

---

## Question 8

### Part (i) [2 marks]

For a Geometric distribution defined where $X$ is the trial number on which the first success occurs, the expected value is $E[X] = \frac{1}{p}$.
Given $p = 0.07$, the expected value is:
$E[X] = \frac{1}{0.07} = 14.286$

### Part (ii) [2 marks]

The event "inspector does not find a defective component in the first four checks" is exactly $P(X > 4)$.
Since components are independent events:
$P(X > 4) = (1 - p)^4 = (1 - 0.07)^4 = 0.93^4 = 0.7481$.

### Part (iii) [2 marks]

The 'memoryless' property of the geometric distribution states that the probability of waiting additionally for a success after having already waited for $n$ trials with no success is exactly the same as the initial probability distribution from the start. Mathematically, it implies that $P(X > y+x \mid X > y) = P(X > x)$. Past failures have no effect or "memory" on predicting the number of subsequent future trials.

### Part (iv) [2 marks]

By simply applying the memoryless property proven in part (iii), the probability we need evaluates to identically $P(X > 6)$.
$P(X > 10 \mid X > 4) = P(X > 6) = (0.93)^6 = 0.6470$.

### Part (v) [3 marks]

Let $A$ be the event of Scanner A passing a component, and $B$ passing a component.
$P(A \mid Defective) = 1 - 0.75 = 0.25$
$P(B \mid Defective) = 1 - 0.85 = 0.15$
$P(A \mid Non-Defective) = 0.95$
$P(B \mid Non-Defective) = 0.90$

Since the scanners act independently:
**(a) Defective components:**
$P(Accepted \mid Defective) = P(A \mid Defective) \times P(B \mid Defective) = 0.25 \times 0.15 = 0.0375$.

**(b) Non-defective components:**
$P(Accepted \mid Non-Defective) = P(A \mid Non-Defective) \times P(B \mid Non-Defective) = 0.95 \times 0.90 = 0.855$.

### Part (vi) [3 marks]

By Bayes' theorem, we find the overall unconditional probabilities:
$P(Defective) = 0.07$  
$P(Non-Defective) = 0.93$

$P(Accepted) = P(Accepted \mid Defective)P(Defective) + P(Accepted \mid Non-Defective)P(Non-Defective)$
$P(Accepted) = (0.0375 \times 0.07) + (0.855 \times 0.93) = 0.002625 + 0.79515 = 0.797775$.

The needed reverse conditional probability is:
$P(Defective \mid Accepted) = \frac{P(Accepted \mid Defective)P(Defective)}{P(Accepted)} = \frac{0.002625}{0.797775} = 0.0032904 = 0.329\%$

**Answer:** B

### Part (vii) [1 mark]

Number of components accepted is $4,512$. 
The expected number of defective choices amongst those accepted is $= 4512 \times 0.0032904 = 14.846$.
Thus the expected cost $= 14.846 \times \$200 = \$2,969.25$.

### Part (viii) [4 marks]

Let $W$ be the number of components incorrectly accepted (defective but passed). $W \sim Binomial(n = 4512, p \approx 0.0032904)$.
Given $n$ is very large and $p$ very small, we can strongly approximate $W$ using either Normal or Poisson distributions.

Using normal approximation: 
$n \times p = \mu = 14.846$
Variance $= np(1-p) = 14.846(1 - 0.0032904) \approx 14.797$
Standard deviation $= \sqrt{14.797} = 3.847$

The liability cost limit matches when $y \ge \frac{5000}{200} = 25$ critical failed parts.
Using a continuity correction for $P(W \ge 25)$, $x = 24.5$. However, strict exceeds implies $> 5000$, which indicates $\ge 26$, hence using $x=25.5$:
$Z \approx \frac{25.5 - 14.846}{3.847} = \frac{10.654}{3.847} = 2.769$

From continuous standard normal parameter tables, $P(Z > 2.769) = 1 - 0.9972 = 0.0028$.

The probability is approximately $0.28\%$.

---

## Question 9

### Part (i) [4 marks]

For a linear predictor built structurally acting as categorical effects, the degrees of parameter mapping is established per independent base variable and possible combinations against the overarching intersect. Total degrees are computed directly:

- **Model 1 (NWL + SMK)** uses an intercept $(1)$ parameter, a main variable with $4$ parameters for $NWL$ ($5 - 1$), and a feature with $1$ parameter for SMK ($2 - 1$).
  Total: $1 + 4 + 1 = 6$ parameters.
  
- **Model 2 (NWL + SMK + CRR)** builds directly from Model 1 and additionally includes one extra independent effect $CRR$ parameter ($2 - 1$).
  Total: $6 + 1 = 7$ parameters.

- **Model 3 (NWL + SMK + NWL:SMK + CRR)** builds from Model 2 and features one multiplicative interaction between all discrete dimensions of $NWL$ ($4$ relative shifts) against $SMK$ ($1$ relative shift): $4 \times 1 = 4$ combined components.
  Total: $7 + 4 = 11$ parameters.
  
- **Model 4 (NWL\*SMK\*CRR)** represents a fully saturated $5\times2\times2$ matrix mapped combination array mapping every combination distinctively.
  Total parameters mapping $5\times2\times2$ categories: $20$ parameters.

### Part (ii) [3 marks]

- **Model 1:** Is overly simplistic and ignores geographic variances completely (CRR). Exclusions cause model biases if main residency carries statistical significance for assessing critical illness incidence structures, so it is likely underfitting the claims structure.
- **Model 2:** Integrates all basic measurable dimension characteristics independently mapping proportional responses sequentially. This is reliable, interpretable, and captures base rates well, preventing parameter overfitting that harms practical usability.
- **Model 4:** Overly saturated structure. While exact, the variance for standard modeling calculations blows out unconstrained as samples spread very thin over exact $20$ unique combination combinations. Highly susceptible to overfitting leading to poor model generalisation on testing parameters.

### Part (iii) [2 marks]

The saturated model structure for parameters yields $20$ mapping cells in its complete table structure which corresponds to $0$ residual degrees of mapping for degrees of freedom ($20-20=0$). Thus, using base observations count of $20$, we subtract to find available parameters constraint mappings:

- Model 1 Degrees of freedom = $20 - 6 = 14$
- Model 2 Degrees of freedom = $20 - 7 = 13$ 

### Part (iv) [9 marks]

We proceed sequentially selecting models if subtracting deviance drops exceed $\chi^2$ value tables for associated sequential lost degrees mappings parameters shifts at the $5\%$ boundary limits level. 

**Model 1 vs Model 0**
Change in Deviance ($\Delta D$) $= 86.5 - 68.6 = 17.9$
Change in DF ($\Delta df$) $= 19 - 14 = 5$ 
Value of $\chi^2_5(5\%) = 11.07$. Since $17.9 > 11.07$, Model 1 improves significantly on the constant Model 0.

**Model 2 vs Model 1**
$\Delta D = 68.6 - 45.7 = 22.9$
$\Delta df = 14 - 13 = 1$
Value of $\chi^2_1(5\%) = 3.841$. Since $22.9 > 3.841$, Model 2 significantly improves fit on 1 over geographic base incorporation.

**Model 3 vs Model 2**
$\Delta D = 45.7 - 11.3 = 34.4$
$\Delta df = 13 - 9 = 4$
Value of $\chi^2_4(5\%) = 9.488$. Since $34.4 > 9.488$, integrating wealth versus smoker interaction gives strongly substantial fit improvements. Choose Model 3.

**Model 4 vs Model 3**
$\Delta D = 11.3 - 0 = 11.3$
$\Delta df = 9 - 0 = 9$
Value of $\chi^2_9(5\%) = 16.919$. Since $11.3 < 16.919$, further parameter exhaustion yields no significant structural gains over random noise limits.

**Conclusion:** We firmly choose to utilize **Model 3** to establish claims baselines.

### Part (v) [2 marks]

Extra considerations for the actuary:
1. Plot and review standard modeling residuals (deviance residuals mapping against predictors) to make certain there's no unaccounted structural variances or heavy outlier distortion patterns across bounds.
2. Review absolute standard error limits evaluated across the individual parameters computed on Model 3 to observe statistical stability limitations on small dataset subdivisions.
3. Compare models utilizing complementary Information criteria factors measuring penalised limits like AIC and BIC limits scaling parameters vs observations depth more effectively as an alternative to simple sequenced deviance tests.

---

## Audit Trail

### Accessed Files
- `exams/CS1A/September_2025/question-paper.md`
- `references/formulae-and-tables.pdf`
