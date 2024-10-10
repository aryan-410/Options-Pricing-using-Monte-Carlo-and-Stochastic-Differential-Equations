from BaseOptionClass import BaseOptionPricing
import numpy as np

class EuropeanOption(BaseOptionPricing):
    def generate_asset_paths(self):
        S = np.zeros((self.N, self.M + 1))
        S[:, 0] = self.S0
        for t in range(1, self.M + 1):
            Z = np.random.standard_normal(self.N)
            S[:, t] = S[:, t - 1] * np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt + self.sigma * np.sqrt(self.dt) * Z)
        return S

    def option_payoff(self, S):
        return np.maximum(S[:, -1] - self.K, 0)

    def price_option(self):
        S = self.generate_asset_paths()
        payoff = self.option_payoff(S)
        return self.calculate_option_price(payoff)

class AmericanOption(BaseOptionPricing):
    def generate_asset_paths(self):
        S = np.zeros((self.N, self.M + 1))
        S[:, 0] = self.S0
        for t in range(1, self.M + 1):
            Z = np.random.standard_normal(self.N)
            S[:, t] = S[:, t - 1] * np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt + self.sigma * np.sqrt(self.dt) * Z)
        return S

    def option_payoff(self, S):
        payoff = np.maximum(S[:, -1] - self.K, 0)
        for t in range(self.M - 1, 0, -1):
            early_exercise_value = np.maximum(S[:, t] - self.K, 0)
            payoff = np.maximum(early_exercise_value, payoff * np.exp(-self.r * self.dt))
        return payoff

    def price_option(self):
        S = self.generate_asset_paths()
        payoff = self.option_payoff(S)
        return self.calculate_option_price(payoff)
