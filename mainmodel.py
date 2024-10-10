from EuropeanAndAmericanOption import EuropeanOption, AmericanOption
from JumpDiffusionOption import JumpDiffusionOption
from GreekCalculation import OptionGreeks

# Parameters
S0 = 100
K = 100
T = 1.0
r = 0.05
sigma = 0.2
M = 365
N = 10000

# European Option
european_option = EuropeanOption(S0, K, T, r, sigma, M, N)
price_european = european_option.price_option()
print(f"European Option Price: {price_european:.2f}")

# American Option
american_option = AmericanOption(S0, K, T, r, sigma, M, N)
price_american = american_option.price_option()
print(f"American Option Price: {price_american:.2f}")

# Jump Diffusion Option
jump_option = JumpDiffusionOption(S0, K, T, r, sigma, M, N, lambd=0.1, muJ=0.02, sigmaJ=0.1)
price_jump_diffusion = jump_option.price_option(variance_reduction=True)
print(f"Jump Diffusion Option Price: {price_jump_diffusion:.2f}")

# Option Greeks
# European Option Greek Calculation
option_greeks = OptionGreeks(european_option)
delta = option_greeks.calculate_delta()
gamma = option_greeks.calculate_gamma()
vega = option_greeks.calculate_vega()
theta = option_greeks.calculate_theta()
rho = option_greeks.calculate_rho()

print(f"Delta: {delta:.4f}, Gamma: {gamma:.4f}, Vega: {vega:.4f}, Theta: {theta:.4f}, Rho: {rho:.4f}")

