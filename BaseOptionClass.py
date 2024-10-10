import numpy as np
from abc import ABC, abstractmethod

class BaseOptionPricing(ABC):
    def __init__(self, S0, K, T, r, sigma, M, N):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.M = M
        self.N = N
        self.dt = T / M

    @abstractmethod
    def generate_asset_paths(self):
        pass

    def discount_payoff(self, payoff):
        return np.exp(-self.r * self.T) * payoff

    def calculate_option_price(self, payoff):
        return np.mean(self.discount_payoff(payoff))

    @abstractmethod
    def option_payoff(self, S):
        pass

    @abstractmethod
    def price_option(self):
        pass
