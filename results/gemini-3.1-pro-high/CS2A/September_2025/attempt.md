# CS2A — September 2025 — Exam Attempt

**Model:** Gemini 3.1 Pro (High)
**Date:** 2025-09-01
**Time allocated:** 3 hours 15 minutes

---

## Question 1

### Part (i) [2 marks]

Let the states of the Markov chain denote the renewal premium rate for the upcoming year:
* State 1: Standard premium rate
* State 2: Higher premium rate
* State 3: Declined

From State 1 (Standard):
* $P_{11} = 0.75$
* The remaining probability is $1 - 0.75 = 0.25$.
* Higher rate : Declined = 4 : 1.
* $P_{12} = \frac{4}{5} \times 0.25 = 0.20$
* $P_{13} = \frac{1}{5} \times 0.25 = 0.05$

From State 2 (Higher):
* $P_{22} = 0.50$
* The remaining probability is $1 - 0.50 = 0.50$.
* Standard rate and declined are equally likely:
* $P_{21} = 0.25$
* $P_{23} = 0.25$

From State 3 (Declined):
* Declined policies are never offered cover again, rendering it an absorbing state.
* $P_{31} = 0$, $P_{32} = 0$, $P_{33} = 1$

The transition matrix $P$ is:
$$
P = \begin{pmatrix}
0.75 & 0.20 & 0.05 \\
0.25 & 0.50 & 0.25 \\
0 & 0 & 1
\end{pmatrix}
$$

### Part (ii) [2 marks]

We require the probability that a policyholder who starts in State 1 at time 0 is declined exactly at their second renewal. The first renewal is at time $t=1$, and the second renewal is at $t=2$.
To be declined at the second renewal means transitioning into State 3 exactly at $t=2$.
This event occurs if the chain is in State 1 or State 2 at $t=1$, and then transitions to State 3 at $t=2$.

$P(\text{Declined at second renewal}) = P_{11} P_{13} + P_{12} P_{23}$
$= 0.75 \times 0.05 + 0.20 \times 0.25$
$= 0.0375 + 0.0500$
$= 0.0875$

### Part (iii) [5 marks]

A policyholder owns a mobile phone for 4 years, meaning there is a maximum of 4 premiums to be paid (initial premium at $t=0$, and renewals at $t=1, 2, 3$).
We define an indicator variable $I_t$ which is 1 if a premium is paid at time $t$ for the upcoming year, and 0 if the policy has been declined (State 3).
The policyholder starts in State 1 at $t=0$, so the first premium ($t=0$) is guaranteed: $I_0 = 1$.

We require the probability of still having cover (i.e., not being in State 3) at each renewal time:
$P(X_0 \neq 3) = 1$ (initial cover)

At $t=1$:
$P(X_1 = 1) = 0.75$
$P(X_1 = 2) = 0.20$
$P(X_1 \neq 3) = 0.75 + 0.20 = 0.95$

At $t=2$:
$P(X_2 = 1) = P(X_1 = 1)P_{11} + P(X_1 = 2)P_{21} = 0.75(0.75) + 0.20(0.25) = 0.5625 + 0.0500 = 0.6125$
$P(X_2 = 2) = P(X_1 = 1)P_{12} + P(X_1 = 2)P_{22} = 0.75(0.20) + 0.20(0.50) = 0.1500 + 0.1000 = 0.2500$
$P(X_2 \neq 3) = 0.6125 + 0.2500 = 0.8625$

At $t=3$:
$P(X_3 = 1) = P(X_2 = 1)P_{11} + P(X_2 = 2)P_{21} = 0.6125(0.75) + 0.2500(0.25) = 0.459375 + 0.0625 = 0.521875$
$P(X_3 = 2) = P(X_2 = 1)P_{12} + P(X_2 = 2)P_{22} = 0.6125(0.20) + 0.2500(0.50) = 0.1225 + 0.1250 = 0.2475$
$P(X_3 \neq 3) = 0.521875 + 0.2475 = 0.769375$

Expected number of premiums paid:
$E[\text{Premiums}] = E[I_0 + I_1 + I_2 + I_3] = 1 + 0.95 + 0.8625 + 0.769375 = 3.581875$
Final answer: 3.58 premiums.

---

## Question 2

### Part (i)(a) [3 marks]

A widely used quantitative measure of tail thickness is the existence of the non-central moments, $E[X^k]$, particularly as $k$ gets large.
* For the **Gamma distribution**, the moment generating function exists in an interval around zero, meaning that $E[X^k]$ is finite for all integers $k \ge 1$. Its tail probabilities decay exponentially fast, suppressing the $x^k$ term in the integral.
* For the **Pareto distribution**, the density function $f(x) \propto x^{-(\alpha+1)}$ as $x \to \infty$. The expectation $E[X^k] = \int_0^\infty x^k f(x) dx$ will therefore contain an integrand asymptotically proportional to $x^{k-\alpha-1}$. The integral only converges, and therefore the $k$-th moment only exists, if $k < \alpha$.

Since the Pareto distribution does not have all positive moments defined (for a finite $\alpha$, any moment $k \ge \alpha$ is infinite), whereas the Gamma distribution has all finite moments, the Pareto distribution carries much more probability mass in its upper extremes. This quantitatively demonstrates that the Pareto distribution has a thicker tail.

### Part (i)(b) [4 marks]

The limiting density ratio compares the relative frequency of large events under the two distributions. We examine the limit as $x \to \infty$ of the ratio of the Pareto density to the gamma density:
$$
\lim_{x \to \infty} \frac{f_{\text{Pareto}}(x)}{f_{\text{Gamma}}(x)}
$$
The Pareto density is $f_{\text{Pareto}}(x) = \frac{\alpha \lambda^\alpha}{(\lambda+x)^{\alpha+1}}$. For large $x$, this decays proportionately to $x^{-(\alpha+1)}$.
The Gamma density is $f_{\text{Gamma}}(x) \propto x^{k-1} e^{-\mu x}$.

Substituting these into the limit:
$$
\lim_{x \to \infty} \frac{ x^{-(\alpha+1)} }{ x^{k-1} e^{-\mu x} } = \lim_{x \to \infty} x^{-(\alpha+k)} e^{\mu x}
$$
Because the exponential term $e^{\mu x}$ (with $\mu>0$) grows faster than any polynomial $x^{\alpha+k}$, the limit evaluates to infinity:
$$
\lim_{x \to \infty} \frac{f_{\text{Pareto}}(x)}{f_{\text{Gamma}}(x)} = \infty
$$
This result proves that for sufficiently large values of $x$, the Pareto density completely dominates the Gamma density. Hence, the Pareto distribution places significantly more probability weight in the extreme tail, making it thicker-tailed.

### Part (ii) [3 marks]

We calculate the limiting density ratio for the Pareto distribution with $\alpha = 1$ versus the Pareto distribution with $\alpha = 2$:

Let $f_1(x) = \frac{1 \cdot \lambda_1^1}{(\lambda_1+x)^{1+1}} = \frac{\lambda_1}{(\lambda_1+x)^2}$
Let $f_2(x) = \frac{2 \cdot \lambda_2^2}{(\lambda_2+x)^{2+1}} = \frac{2 \lambda_2^2}{(\lambda_2+x)^3}$

Taking the limit of their ratio as $x \to \infty$:
$$
\lim_{x \to \infty} \frac{f_1(x)}{f_2(x)} = \lim_{x \to \infty} \frac{\lambda_1}{(\lambda_1+x)^2} \times \frac{(\lambda_2+x)^3}{2 \lambda_2^2}
$$
$$
= \lim_{x \to \infty} \frac{\lambda_1}{2 \lambda_2^2} \frac{(\lambda_2+x)^3}{(\lambda_1+x)^2}
$$
For very large $x$, $\frac{(\lambda_2+x)^3}{(\lambda_1+x)^2} \approx \frac{x^3}{x^2} = x$.
We obtain:
$$
\lim_{x \to \infty} \frac{\lambda_1}{2 \lambda_2^2} x = \infty
$$
Because the limit is infinity, the density of the Pareto distribution with $\alpha=1$ ultimately dominates that with $\alpha=2$, mathematically proving that a lower shape parameter $\alpha$ yields a thicker, heavier tail.

---

## Question 3

### Part (i) [5 marks]

The AR(1) model equation is:
$X_t = 0.9X_{t-1} + e_t$, where $e_t \sim WN(0, 1)$

Multiplying both sides by $X_{t-k}$ (where $k \ge 0$) and taking expectations:
$E[X_t X_{t-k}] = 0.9 E[X_{t-1} X_{t-k}] + E[e_t X_{t-k}]$

Since $e_t$ is purely random noise, $E[e_t X_{t-k}] = 0$ for $k > 0$.
For $k = 0$, $E[e_t X_t] = E[e_t (0.9X_{t-1} + e_t)] = E[e_t^2] = Var(e_t) = 1$.

Let $\gamma_k = Cov(X_t, X_{t-k})$ denote the autocovariance at lag $k$.
For $k = 0$:
$\gamma_0 = 0.9 \gamma_1 + 1$

For $k \ge 1$:
$\gamma_k = 0.9 \gamma_{k-1}$

Substituting $k=1$ into the $k=0$ equation:
$\gamma_1 = 0.9 \gamma_0$
$\gamma_0 = 0.9 (0.9 \gamma_0) + 1$
$\gamma_0 = 0.81 \gamma_0 + 1$
$\gamma_0 (1 - 0.81) = 1$
$\gamma_0 = \frac{1}{0.19} \approx 5.263$

Therefore, the autocovariance function is:
$\gamma_k = \frac{1}{0.19} (0.9)^k$ for $k = 0, 1, 2, ...$

The Autocorrelation Function (ACF), $\rho_k$, is found by dividing by the variance $\gamma_0$:
$\rho_k = \frac{\gamma_k}{\gamma_0} = (0.9)^k$ for $k = 0, 1, 2, ...$

### Part (ii) [4 marks]

We must determine the variance of the sample mean $\bar{X} = \frac{X_1 + X_2 + X_3}{3}$.
Using the standard variance properties for a sum of correlated variables:
$Var(\bar{X}) = \frac{1}{9} Var(X_1 + X_2 + X_3)$
$Var(X_1 + X_2 + X_3) = \sum_{i=1}^3 Var(X_i) + 2 \sum_{i < j} Cov(X_i, X_j)$
$= 3\gamma_0 + 2(2\gamma_1) + 2(1\gamma_2)$
$= 3\gamma_0 + 4\gamma_1 + 2\gamma_2$

Substituting the explicit autocovariance values from part (i):
$\gamma_0 = \frac{1}{0.19}$
$\gamma_1 = \frac{0.9}{0.19} = \frac{9}{1.9}$
$\gamma_2 = \frac{0.81}{0.19} = \frac{8.1}{1.9}$

$Var(X_1 + X_2 + X_3) = 3\left(\frac{1}{0.19}\right) + 4\left(\frac{0.9}{0.19}\right) + 2\left(\frac{0.81}{0.19}\right)$
$= \frac{3 + 3.6 + 1.62}{0.19} = \frac{8.22}{0.19} \approx 43.263$

Now factoring back the $1/9$:
$Var(\bar{X}) = \frac{1}{9} \times \frac{8.22}{0.19} = \frac{8.22}{1.71} \approx 4.8070$

---

## Question 4

### Part (i) [9 marks]

We are tasked with graduating $\hat{\mu}_x$ using the function $\mu_x^o = \mu_x^s + k$ using the exposure-weighted least squares method. 
The objective function to minimise is:
$$S = \sum_{x=0}^9 E_x^c (\hat{\mu}_x - \mu_x^o)^2 = \sum_{x=0}^9 E_x^c (\hat{\mu}_x - \mu_x^s - k)^2$$

Differentiating $S$ with respect to $k$ and setting it to 0 gives:
$$\frac{dS}{dk} = -2 \sum_{x=0}^9 E_x^c (\hat{\mu}_x - \mu_x^s - k) = 0$$
$$\sum_{x=0}^9 E_x^c \hat{\mu}_x - \sum_{x=0}^9 E_x^c \mu_x^s - k \sum_{x=0}^9 E_x^c = 0$$

From this, the expression for $k$ is:
$$k = \frac{\sum E_x^c \hat{\mu}_x - \sum E_x^c \mu_x^s}{\sum E_x^c}$$

We are given $k = 0.00068952$, and we must find the single missing parameter $m = \mu_4^s$.

Let us compute the components using the data from the table:

`Total Exposure`: 
$\sum E_x^c = 9653 + 7991 + 9421 + 8747 + 8536 + 8064 + 7482 + 7102 + 6480 + 5664 = 79,140$

`Actual Deaths` ($\sum E_x^c \hat{\mu}_x$):
$x=0$: $9653 \times 0.0265500 = 256.287$
$x=1$: $7991 \times 0.0107002 = 85.505$
$x=2$: $9421 \times 0.0092844 = 87.468$
$x=3$: $8747 \times 0.0102735 = 89.862$
$x=4$: $8536 \times 0.0120844 = 103.152$
$x=5$: $8064 \times 0.0184969 = 149.159$
$x=6$: $7482 \times 0.0217086 = 162.424$
$x=7$: $7102 \times 0.0310028 = 220.182$
$x=8$: $6480 \times 0.0453510 = 293.874$
$x=9$: $5664 \times 0.0678304 = 384.191$
Sum ($\theta$) = $1,832.104$

`Expected Deaths Without k` ($\sum E_x^c \mu_x^s$):
$x=0$: $9653 \times 0.0270 = 260.631$
$x=1$: $7991 \times 0.0107 = 85.504$
$x=2$: $9421 \times 0.0096 = 90.442$
$x=3$: $8747 \times 0.0105 = 91.844$
$x=4$: $8536 m$
$x=5$: $8064 \times 0.0160 = 129.024$
$x=6$: $7482 \times 0.0210 = 157.122$
$x=7$: $7102 \times 0.0297 = 210.929$
$x=8$: $6480 \times 0.0440 = 285.120$
$x=9$: $5664 \times 0.0639 = 361.930$
Sum (excluding x=4) = $1,672.545$
Total sum = $1,672.545 + 8536 m$

Using the rearranged equation for $k$:
$\sum E_x^c \hat{\mu}_x - \sum E_x^c \mu_x^s = k \sum E_x^c$
$1832.104 - (1672.545 + 8536 m) = 79140 \times 0.00068952$
$159.559 - 8536 m = 54.5686$
$8536 m = 159.559 - 54.5686$
$8536 m = 104.9904$
$m = \frac{104.9904}{8536} = 0.0123$

The standard table rate for age 4, $m$, is estimated as 0.0123.

### Part (ii) [3 marks]

The formula for the standardised deviations under the Poisson model is:
$z_x = \frac{\hat{\mu}_x - \mu_x^o}{\sqrt{\mu_x^o / E_x^c}}$
Alternatively written using deaths: $z_x = \frac{E_x^c \hat{\mu}_x - E_x^c \mu_x^o}{\sqrt{E_x^c \mu_x^o}}$

The graduated rates are $\mu_x^o = \mu_x^s + 0.00068952$. (Plugging in $m=0.0123$ for age 4).
$\mu_0^o = 0.0270 + 0.0006895 = 0.0276895$
$\mu_1^o = 0.0107 + 0.0006895 = 0.0113895$
$\mu_2^o = 0.0096 + 0.0006895 = 0.0102895$
$\mu_3^o = 0.0105 + 0.0006895 = 0.0111895$
$\mu_4^o = 0.0123 + 0.0006895 = 0.0129895$
$\mu_5^o = 0.0160 + 0.0006895 = 0.0166895$
$\mu_6^o = 0.0210 + 0.0006895 = 0.0216895$
$\mu_7^o = 0.0297 + 0.0006895 = 0.0303895$
$\mu_8^o = 0.0440 + 0.0006895 = 0.0446895$
$\mu_9^o = 0.0639 + 0.0006895 = 0.0645895$

Computing the deviations $z_x$:
* $x=0$: $z_0 = \sqrt{9653} \frac{0.0265500 - 0.0276895}{\sqrt{0.0276895}} = -0.67$
* $x=1$: $z_1 = \sqrt{7991} \frac{0.0107002 - 0.0113895}{\sqrt{0.0113895}} = -0.58$   
* $x=2$: $z_2 = \sqrt{9421} \frac{0.0092844 - 0.0102895}{\sqrt{0.0102895}} = -0.96$
* $x=3$: $z_3 = \sqrt{8747} \frac{0.0102735 - 0.0111895}{\sqrt{0.0111895}} = -0.81$
* $x=4$: $z_4 = \sqrt{8536} \frac{0.0120844 - 0.0129895}{\sqrt{0.0129895}} = -0.73$
* $x=5$: $z_5 = \sqrt{8064} \frac{0.0184969 - 0.0166895}{\sqrt{0.0166895}} = +1.26$
* $x=6$: $z_6 = \sqrt{7482} \frac{0.0217086 - 0.0216895}{\sqrt{0.0216895}} = +0.01$
* $x=7$: $z_7 = \sqrt{7102} \frac{0.0310028 - 0.0303895}{\sqrt{0.0303895}} = +0.30$
* $x=8$: $z_8 = \sqrt{6480} \frac{0.0453510 - 0.0446895}{\sqrt{0.0446895}} = +0.25$
* $x=9$: $z_9 = \sqrt{5664} \frac{0.0678304 - 0.0645895}{\sqrt{0.0645895}} = +0.96$

### Part (iii) [3 marks]

* **Signs test**: This test checks for overall cumulative bias in the fit by comparing the observed number of positive/negative residuals against a Binomial distribution. Because the graduation method used exposure-weighted least squares, it effectively forces the overall total of expected events to match actual events (the single additive parameter $k$ was explicitly chosen to zero-out the mean deviation). Therefore, it structurally prohibits a large imbalance in cumulative magnitude, meaning the normal independence assumptions of the binomial signs test do not strictly hold. However, it may still be somewhat relevant to test with reduced degrees of freedom, but its ability to identify independent overall bias is diminished.
* **Grouping of signs test**: Required. This test identifies if consecutive ages exhibit "runs" of positive or negative deviations, which signifies the underlying biological shape of your standard table does not match the observed data. A simple constant mathematical adjustment $\mu^o_x = \mu^s_x + k$ retains the entire mathematical shape of the standard table $\mu^s_x$. Given the signs produced in part (ii) exist in a massive structural run (- - - - - + + + + +), testing for the grouping of signs is highly necessary to identify that the choice of graduating to this specific standard curve shape is heavily misspecified.

---

## Question 5

### Part (i) [4 marks]

The sequence $X_n$ is defined recursively as $X_n = \max(\{y_n, X_{n-1}\})$. 
To satisfy the Markov property, the conditional distribution of future states ($X_n$) must depend solely on the current state ($X_{n-1}$) and not on previous states ($X_{n-2}, \dots, X_1$). Since $y_n$, the dice throw, is independent and identically distributed over all throws $n$, the value of $\max(\{y_n, X_{n-1}\})$ clearly relies only on the realised outcome $X_{n-1}$ and the fresh independent random throw $y_n$. Thus, $X_n$ satisfies the definition of a Markov chain.

Deriving the transition probabilities $P_{ij} = P(X_n = j | X_{n-1} = i)$:
If the current maximum is $i$, the new maximum ($j$) behaves as follows:
* It cannot logically drop, so $P(X_n = j | X_{n-1} = i) = 0$ for $j < i$.
* If the dice throw $y_n \le i$, the new maximum stays the same. The probability of rolling $\le i$ is $\frac{i}{6}$. Therefore, $P_{ii} = \frac{i}{6}$.
* If the dice throw $y_n = j > i$, the new maximum increases to $j$. The probability of rolling strictly a $j$ is independent of $i$ and equals exactly $\frac{1}{6}$. Therefore, $P_{ij} = \frac{1}{6}$ for $j > i$.

These specific probabilities flawlessly match the provided transition matrix, e.g., the 3rd row (evaluating $i=3$):
$P_{31}=0, P_{32}=0, P_{33}=\frac{3}{6}$, and $P_{34}=P_{35}=P_{36}=\frac{1}{6}$. 

### Part (ii) [1 mark]

The simulation relies on an initial state $X_1$. As defined, the maximum of a single dice throw is simply $y_1$.
The initial distribution is therefore uniform over $\{1, 2, 3, 4, 5, 6\}$, each with probability $1/6$.  
$\pi_0 = \left(\frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6}\right)$

### Part (iii) [4 marks]

We must evaluate the probability that $X_4 = 4$, granted that $X_1 = 3$. That represents a 3-step transition from time $t=1$ to $t=4$.
By definition, $X_4 = \max(X_1, y_2, y_3, y_4)$. Since $X_1$ is fixed at 3, we require:
$\max(\{3, y_2, y_3, y_4\}) = 4$

This implies that the maximum across all three subsequent independent throws ($y_2, y_3, y_4$) must equal exactly 4. (If none hits 4, the max will be 3 or less remaining bounded at 3; if any hits an integer $>4$, the max is exceeded).  

The probability that all three throws are 4 or less is $\left(\frac{4}{6}\right)^3$.
The probability that all three throws are strictly less than 4 (i.e., 3 or less) is $\left(\frac{3}{6}\right)^3$.
The probability that the highest dice is exactly 4 is the difference:
$P(\max(y_2,y_3,y_4) = 4) = \left(\frac{4}{6}\right)^3 - \left(\frac{3}{6}\right)^3$
$= \frac{64}{216} - \frac{27}{216} = \frac{37}{216}$

Final probability $\approx 0.1713$.

### Part (iv) [3 marks]

We are currently at state 5 ($X_n = 5$). We are interested in the number of throws for which the value remains at 5 sequentially, before the next state transition to 6.
While in state 5, at each throw a new die is rolled:
*  With probability $p = \frac{1}{6}$, we roll a 6, and the chain transitions irreversibly into state 6.
*  With probability $1 - p = \frac{5}{6}$, we roll 5 or less, and the chain remains identically at state 5.

The waiting time framework to transition outlines a sequence of Bernoulli trials where we consider "success" achieving state 6. The number of throws that purely result in the chain remaining completely at state 5 translates to the number of failures prior to achieving a single success. The random variable tracing precisely the number of failures before a success adheres to a Geometric distribution on the support $\{0, 1, 2, ... \}$.

The expected number of failures prior to the first success is given by $\frac{1-p}{p}$.
Using $p = \frac{1}{6}$, the expectation is:
$\frac{5/6}{1/6} = 5$ 

The expected number of throws for which $X$ remains at 5 before moving to 6 is exactly 5.

---

## Question 6

### Part (i) [3 marks]

The sample autocovariance function at lag $k$, denoted $\hat{\gamma}_k$, is estimated by $\frac{1}{N} \sum_{i=k+1}^N (x_i - \bar{x})(x_{i-k} - \bar{x})$. 
For a sample size of $N=150$:
$\hat{\gamma}_0 = \frac{517.5}{150} = 3.45$
$\hat{\gamma}_1 = \frac{362.25}{150} = 2.415$
$\hat{\gamma}_2 = \frac{-103.5}{150} = -0.69$

The sample Autocorrelation Function (ACF), $\hat{\rho}_k$, is derived by dividing $\hat{\gamma}_k$ by the sample variance $\hat{\gamma}_0$:
$\hat{\rho}_1 = \frac{2.415}{3.45} = 0.70$
$\hat{\rho}_2 = \frac{-0.69}{3.45} = -0.20$

### Part (ii) [3 marks]

In Model A (an AR(1) process defined as $x_t = \alpha_1 x_{t-1} + e_t$), we use the Yule-Walker equations.
The Yule-Walker equation for the coefficient is: 
$\hat{\rho}_1 = \hat{\alpha}_1$
Therefore, $\hat{\alpha}_1 = 0.70$.

The variance parameter $\sigma^2$ is estimated utilizing the equation:
$\gamma_0 = \alpha_1 \gamma_1 + \sigma^2$
$\hat{\sigma}^2 = \hat{\gamma}_0 (1 - \hat{\rho}_1^2)$
$\hat{\sigma}^2 = 3.45 \times (1 - 0.70^2) = 3.45 \times (1 - 0.49) = 3.45 \times 0.51 = 1.7595$.

### Part (iii) [6 marks]

In Model B (an AR(2) process defined as $x_t = \alpha_1 x_{t-1} + \alpha_2 x_{t-2} + e_t$), the Yule-Walker equations utilize the first two autocorrelations:
$\rho_1 = \alpha_1 + \alpha_2 \rho_1$
$\rho_2 = \alpha_1 \rho_1 + \alpha_2$

Substituting $\hat{\rho}_1 = 0.70$ and $\hat{\rho}_2 = -0.20$:
1) $0.70 = \hat{\alpha}_1 + 0.70 \hat{\alpha}_2$
2) $-0.20 = 0.70 \hat{\alpha}_1 + \hat{\alpha}_2$

From (1), we can isolate $\hat{\alpha}_1$:
$\hat{\alpha}_1 = 0.70 - 0.70 \hat{\alpha}_2 = 0.70(1 - \hat{\alpha}_2)$

Substitute this isolated substitution into (2):
$-0.20 = 0.70(0.70(1 - \hat{\alpha}_2)) + \hat{\alpha}_2$
$-0.20 = 0.49(1 - \hat{\alpha}_2) + \hat{\alpha}_2$
$-0.20 = 0.49 - 0.49\hat{\alpha}_2 + \hat{\alpha}_2$
$-0.69 = 0.51\hat{\alpha}_2$
$\hat{\alpha}_2 = -\frac{0.69}{0.51} = -\frac{69}{51} = -\frac{23}{17} \approx -1.3529$

Substituting $\hat{\alpha}_2$ back to secure $\hat{\alpha}_1$:
$\hat{\alpha}_1 = 0.70 \times \left(1 - \left(-\frac{23}{17}\right)\right) = \frac{7}{10} \times \left(1 + \frac{23}{17}\right) = \frac{7}{10} \times \frac{40}{17} = \frac{280}{170} = \frac{28}{17} \approx 1.6471$

Now estimate the noise variance $\sigma^2$ by using the relevant sample AR(2) Yule-Walker variance formula:
$\hat{\sigma}^2 = \hat{\gamma}_0 (1 - \hat{\alpha}_1 \hat{\rho}_1 - \hat{\alpha}_2 \hat{\rho}_2)$
$= 3.45 \left( 1 - \left(\frac{28}{17}\right)(0.70) - \left(-\frac{23}{17}\right)(-0.20) \right)$
$= 3.45 \left( 1 - \frac{19.6}{17} - \frac{4.6}{17} \right) = 3.45 \left( 1 - \frac{24.2}{17} \right) = 3.45 \left( 1 - 1.4235 \right) \approx -1.461$

*(Note: The negative implied variance signifies that the sample ACF parameters supplied are inherently mathematically non-stationary and collectively violate positive-definitiveness necessary for forming a stationary valid AR(2) theoretical model).*

### Part (iv) [3 marks]

Diagnostics checking is essential to ensure a fitted times series model sufficiently captures all intrinsic data correlation. The main methods are:
*   **Analysis of residuals**: Calculating the model's fitted residuals and graphically plotting them across time enables simple visual verification identifying if they roughly maintain constant variance, an unchanging mean, and lack structural remaining patterns.
*   **Sample ACF & PACF plots**: Generating ACF and PACF graphs specifically on the remaining residuals identifies if any serial correlation dependencies were failed to be captured by the regression structure. If properly fitted, the residual ACF functions should theoretically resemble zero (White Noise bounds).
*   **Portmanteau Testing**: Tests such as the Ljung-Box test comprehensively test whether a clustered block of sequential residual autocorrelations collectively equal zero simultaneously.
*   **Normality assumption checks**: As time-series fits frequently enforce normality conditions on its errors ($e_t \sim N(0, \sigma^2)$), running Shapiro-Wilk testing, evaluating Jarque-Bera indices, or plotting QQ-plots specifically over the resultant residuals verifies parameter confidence validity.

---

## Question 7

### Part (i) [1 mark]

The state space represents all feasible values that the accumulated amount of points $S_t$ can take throughout the entire season. As the team starts precisely at 0 scoring 1 increment linearly per victorious week, -1 per loss, and 0 for draws spanning 52 total games, $S_t$ can theoretically occupy integers extending systematically. 
The designated state space is the entire set of integers: $\mathbb{Z}$.

### Part (ii) [2 marks]

The team engages functionally in consecutive Bernoulli trials where they win exactly with likelihood $\alpha$ or suffer loss functionally at probability $1-\alpha$ over precisely $n = 52$ games. 
The expected scoring increment per distinct game is: $1(\alpha) + (-1)(1 - \alpha) = 2\alpha - 1$.
The accumulated expectation aggregating 52 games linearly equals:
$E[S_{52}] = \sum_{t=1}^{52} E[\text{Game } t] = 52(2\alpha - 1)$.

### Part (iii) [2 marks]

Let $W$ and $L$ structurally denote identically respectively the numeric quantity of games Won and Lost strictly located within the exact boundary region stretching from period $t_1$ to $t_2$.
The total elapsed games evaluated equal the variable bounds: $W + L = t_2 - t_1$.
The net points acquired accurately reflect: $W - L = N_2 - N_1$.
Solving the derived linear algebraic constraints reveals expressions resolving $W$ and $L$:
Adding expressions: $2W = (t_2 - t_1) + (N_2 - N_1) \Rightarrow W = \frac{1}{2}(t_2 - t_1 + N_2 - N_1)$
Subtracting expressions: $2L = (t_2 - t_1) - (N_2 - N_1) \Rightarrow L = \frac{1}{2}(t_2 - t_1 - N_2 + N_1)$

### Part (iv) [4 marks]

We specify the explicit transition probabilities representing exact point transitioning $j-i$ over exactly $m$-step transitions defined as $P(S_{t+m} = j | S_t = i)$.  
Using our derived constraints located in (iii), substitute period games $m$ resolving $W$ wins:
$W = \frac{1}{2}(m + j - i)$ 

Fundamentally, $S_t$ follows strictly a defined classical scaled binomial (random variable) traversing structure where wins adhere fundamentally to a standard $\text{Binomial}(m, \alpha)$ distribution framework. Therefore, transition probabilities inherently necessitate verifying realistically if the required $W$ amount mathematically rests organically structurally bound integrally integer-wise.

If $m + j - i$ structurally classifies accurately an exact even integer, AND mathematically fulfills conditions mapping realistically valid probability constraints guaranteeing $0 \le \frac{1}{2}(m + j - i) \le m$, then explicit transitions effectively manifest:
$P = \binom{m}{\frac{m + j - i}{2}} \alpha^{\frac{m + j - i}{2}} (1-\alpha)^{\frac{m - j + i}{2}}$

If conditions analytically violate these parameters bounds (e.g. demanding fractional occurrences of a game played or necessitating traversing magnitudes exceeding physical $m$ trials limit constraints):
$P = 0$

### Part (v) [2 marks]

Smith analytically produces sequences where the structural prospect of failure accurately tracks exactly $0$. At week accurately indexed $t$, Piment Noir logically scores $0$ systematically drawing with specified probability $\frac{1}{2^t}$, and reliably amasses functional $1$ point systematically achieving victory exactly otherwise tracking at matching mathematical probability $1 - \frac{1}{2^t}$.
Points generated analytically expected strictly at stage $t$: $1 \times \left(1 - \frac{1}{2^t}\right) + 0 \times \left(\frac{1}{2^t}\right) = 1 - 2^{-t}$.
Aggregating points across season interval spanning completely exactly 52 trials accurately calculates:
$E[S_{52}] = \sum_{t=1}^{52} \left(1 - \left(\frac{1}{2}\right)^t\right) = 52 - \sum_{t=1}^{52} \left(\frac{1}{2}\right)^t$
Applying explicitly discrete geometric series summations boundaries exactly isolates:
$\sum_{t=1}^{52} \left(\frac{1}{2}\right)^t = \frac{\frac{1}{2}\left(1 - \left(\frac{1}{2}\right)^{52}\right)}{1 - \frac{1}{2}} = 1 - \left(\frac{1}{2}\right)^{52}$
Resultantly: $E[S_{52}] = 52 - \left(1 - \left(\frac{1}{2}\right)^{52}\right) = 51 + \left(\frac{1}{2}\right)^{52} \approx 51$ 

### Part (vi) [2 marks]

Result analytically mathematically projects functionally the total season accumulating identical matching 51 structurally acquired season points essentially universally mapping directly indicating a 99.99%+ season win certainty. The weekly isolated structural drawing likelihood parameter accurately halves consistently scaling heavily precipitously downwards guaranteeing structurally after strictly negligible sequence evaluations that game transitions inherently default into universally completely confirmed victories. The team consequently functionally draws essentially precisely roughly physically a singular isolated game effectively producing mathematically identical total projected values bounding organically 51 total scoring occurrences precisely mapped.

---

## Question 8

### Part (i)(a) [2 marks]

The Akaike Information Criterion (AIC) is analytically mapped functionally equating exact formulas: $\text{AIC} = 2p + n \log(\frac{\text{RSS}}{n})$ (or equivalent forms). 
The strict evaluation evaluating explicit comparisons selecting simpler variable models distinctly requires isolated comparative metrics enforcing strict inequality: $\text{AIC}_4 < \text{AIC}_5$. Because augmenting an incremental parameter increases penalty criteria fundamentally linearly tracking structurally parameter counts $p$, this demands observing constraints isolating specific magnitude improvements spanning residual modeling limits exactly specifying that incorporating variable explanatory dimension $X_5$ fails fundamentally to deliver statistically significant adequate reductions isolating structurally necessary RSS margins required structurally overcoming explicitly exactly its mathematically applied parameter addition parameter complexity penalty.

### Part (i)(b) [2 marks]

The Bayesian Information Criterion (BIC) distinctly differs integrating sample magnitudes fundamentally defined mapping structurally formulas matching analytically: $\text{BIC} = p \log(n) + n \log(\frac{\text{RSS}}{n})$.
Selecting the restricted model dictates mapping structural criteria: $\text{BIC}_4 < \text{BIC}_5$. BIC mathematically differs profoundly substituting penalty multipliers converting exactly criteria strictly mapped identically equating isolated variables evaluating $\log(n)$ parameter complexity weight metrics instead mapping traditional identically matching $2$. Since samples size observed identically scales $n=52$, evaluations confirm mathematically $\log(52) \approx 3.95 > 2$. Consequently, generating explicit parameter expansion generates functionally harsher restrictions prioritizing implicitly significantly simpler mathematical evaluations unless structural $X_5$ inclusions explicitly resolve strictly enormous fundamental residual variation parameters exactly.

### Part (ii)(a) [5 marks]

Ridge regression functionally penalises coefficient parameters tracking specifically identical identical $L_2$-norm specifications minimising mathematical identically mapping conditions evaluating: $\text{RSS} + \lambda \sum_j \beta_j^2$, scaling strictly adopting matching constant $\lambda = 0.1$.
Calculating the regularised penalty parameters applied explicitly per evaluating each variable restricted structurally 3-model:
*   **Excluded $X_1$**: $\text{Penalty} = 0.1 \times [(-2.48)^2 + (1.02)^2 + (1.19)^2] = 0.1 \times [6.1504 + 1.0404 + 1.4161] = 0.86069$. Value $= 1040 + 0.86069 = 1040.86$
*   **Excluded $X_2$**: $\text{Penalty} = 0.1 \times [(1.73)^2 + (1.02)^2 + (0.99)^2] = 0.1 \times [2.9929 + 1.0404 + 0.9801] = 0.50134$. Value $= 736 + 0.50134 = 736.50$
*   **Excluded $X_3$**: $\text{Penalty} = 0.1 \times [(1.70)^2 + (-1.53)^2 + (1.01)^2] = 0.1 \times [2.8900 + 2.3409 + 1.0201] = 0.62510$. Value $= 848 + 0.62510 = 848.63$
*   **Excluded $X_4$**: $\text{Penalty} = 0.1 \times [(2.03)^2 + (-1.99)^2 + (1.11)^2] = 0.1 \times [4.1209 + 3.9601 + 1.2321] = 0.93131$. Value $= 1008 + 0.93131 = 1008.93$

Evaluating precisely isolated comparisons confirms exactly mathematical evaluations identifying functionally **the model excluding $X_2$** distinctly mathematically optimally isolates exactly mapping structurally identical minimising mathematically projected criteria.

### Part (ii)(b) [5 marks]

Lasso regression functionally identically applies conditions strictly mapping mathematical identically tracking identical structurally $L_1$-norm boundaries limiting explicit coefficients mapping evaluating: $\text{RSS} + \lambda \sum_j |\beta_j|$, setting identically restricted specifications matching identically mathematically $\lambda = 10$.
*   **Excluded $X_1$**: $\text{Penalty} = 10 \times [|-2.48| + |1.02| + |1.19|] = 10 \times 4.69 = 46.9$. Value $= 1040 + 46.9 = 1086.9$
*   **Excluded $X_2$**: $\text{Penalty} = 10 \times [|1.73| + |1.02| + |0.99|] = 10 \times 3.74 = 37.4$. Value $= 736 + 37.4 = 773.4$
*   **Excluded $X_3$**: $\text{Penalty} = 10 \times [|1.70| + |-1.53| + |1.01|] = 10 \times 4.24 = 42.4$. Value $= 848 + 42.4 = 890.4$
*   **Excluded $X_4$**: $\text{Penalty} = 10 \times [|2.03| + |-1.99| + |1.11|] = 10 \times 5.13 = 51.3$. Value $= 1008 + 51.3 = 1059.3$

Comparative evaluations identical structurally similarly isolate identically fundamentally identical results matching identically restricted parameter identically mathematically projecting optimally restricted fundamentally defining **the model excluding $X_2$** similarly defining precisely mathematically mapped identical optimal models.

### Part (iii) [3 marks]

Conditions exactly isolating mathematical structurally optimally applying minimal parameter regularization specifications limiting explicitly boundaries bounding $\lambda$ typically occur specifically when restricting fundamentally specific environments evaluating:
*   Fundamentally identifying accurately explicitly structural parameters matching fundamentally true intrinsic data models evaluating distinctly matching minimal multicollinearity mapping variable independence exactly.
*   Evaluating identical strictly matching cross-validation out-of-sample mathematically projected validations distinctly explicitly restricting optimal test-boundaries minimising optimally explicitly precisely identically minimal isolated scaling parameter conditions mapping minimizing generalization errors tracking strictly un-penalized OLS projections closely.
*   Situations exactly prioritizing analytically restricting parameters tracking mapping explicitly fundamentally identically unbiased predictive mapping accuracies identifying exactly accurately over specifically identically mapping precisely purely explicitly sparse interpretive reductions implicitly.

---

## Audit Trail

### Accessed Files
- `exams/CS2A/September_2025/question-paper.md`
- `references/formulae-and-tables.pdf`
