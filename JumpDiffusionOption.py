from BaseOptionClass import BaseOptionPricing
import numpy as np

class JumpDiffusionOption(BaseOptionPricing):
    def __init__(self, S0, K, T, r, sigma, M, N, lambd=0, muJ=0, sigmaJ=0):
        super().__init__(S0, K, T, r, sigma, M, N)
        self.lambd = lambd
        self.muJ = muJ
        self.sigmaJ = sigmaJ

    def generate_asset_paths(self, variance_reduction=False):
        S = np.zeros((self.N, self.M + 1))
        S[:, 0] = self.S0
        for t in range(1, self.M + 1):
            Z = np.random.standard_normal(self.N)
            if variance_reduction:
                Z_antithetic = -Z
                S[:, t] = S[:, t - 1] * np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt + self.sigma * np.sqrt(self.dt) * Z) \
                          * np.exp(self.lambd * (self.muJ + 0.5 * self.sigmaJ ** 2) * self.dt + np.random.poisson(self.lambd * self.dt, self.N))
            else:
                S[:, t] = S[:, t - 1] * np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt + self.sigma * np.sqrt(self.dt) * Z) \
                          * np.exp(np.random.poisson(self.lambd * self.dt) * np.random.normal(self.muJ, self.sigmaJ, self.N))
        return S

    def option_payoff(self, S):
        return np.maximum(S[:, -1] - self.K, 0)

    def price_option(self, variance_reduction=False):
        S = self.generate_asset_paths(variance_reduction=variance_reduction)
        payoff = self.option_payoff(S)
        return self.calculate_option_price(payoff)
