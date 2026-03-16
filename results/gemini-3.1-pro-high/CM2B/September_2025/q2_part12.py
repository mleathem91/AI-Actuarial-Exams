import math

kappa = 0.7
theta = 0.03
sigma = 0.09
r0 = 0.03

def B(t, T, k):
    return (1 - math.exp(-k * (T - t))) / k

def A(t, T, k, th, s):
    B_val = B(t, T, k)
    term1 = (th - (s**2)/(2 * k**2)) * (B_val - (T - t))
    term2 = (s**2 * B_val**2) / (4 * k)
    return math.exp(term1 - term2)

def P(t, T, r, k, th, s):
    return A(t, T, k, th, s) * math.exp(-B(t, T, k) * r)

P_0_1 = P(0, 1, r0, kappa, theta, sigma)
price_X = 100 * P_0_1
spot_1 = -math.log(P_0_1) / 1

print(f"Price of Bond X (T=1): {price_X}")
print(f"1-year spot rate: {spot_1}")

# (ii) The fair price of Bond Y at t=0 is $92. Bond Y matures at T=3.
# We need to find the market price of risk maybe? No, parameters are the same?
# Wait, "Assume that the Vasicek model holds", then we are given sigma=9%, etc. under martingale measure?
# "where W_t is a Weiner process under the martingale measure".
# So the given parameters ARE the risk-neutral parameters!
# But wait, P(0, 3) under these parameters:
P_0_3 = P(0, 3, r0, kappa, theta, sigma)
price_Y_theoretical = 100 * P_0_3
print(f"Theoretical price of Y: {price_Y_theoretical}")
