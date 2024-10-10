class OptionGreeks:
    def __init__(self, option_pricing_model):
        """
        option_pricing_model: An instance of a pricing model (e.g., EuropeanOption, AmericanOption)
        """
        self.option_pricing_model = option_pricing_model

    def calculate_delta(self):
        """Calculate the Delta of the option (sensitivity to asset price)."""
        dS = 1e-4 * self.option_pricing_model.S0
        option_price = self.option_pricing_model.price_option()
        option_price_up = self.option_pricing_model.__class__(
            self.option_pricing_model.S0 + dS, self.option_pricing_model.K, 
            self.option_pricing_model.T, self.option_pricing_model.r, 
            self.option_pricing_model.sigma, self.option_pricing_model.M, 
            self.option_pricing_model.N
        ).price_option()
        delta = (option_price_up - option_price) / dS
        return delta

    def calculate_gamma(self):
        """Calculate the Gamma of the option (sensitivity of Delta to asset price)."""
        dS = 1e-4 * self.option_pricing_model.S0
        delta_up = self.__class__(self.option_pricing_model.__class__(
            self.option_pricing_model.S0 + dS, self.option_pricing_model.K, 
            self.option_pricing_model.T, self.option_pricing_model.r, 
            self.option_pricing_model.sigma, self.option_pricing_model.M, 
            self.option_pricing_model.N
        )).calculate_delta()

        delta_down = self.__class__(self.option_pricing_model.__class__(
            self.option_pricing_model.S0 - dS, self.option_pricing_model.K, 
            self.option_pricing_model.T, self.option_pricing_model.r, 
            self.option_pricing_model.sigma, self.option_pricing_model.M, 
            self.option_pricing_model.N
        )).calculate_delta()

        gamma = (delta_up - delta_down) / (2 * dS)
        return gamma

    def calculate_vega(self):
        """Calculate the Vega of the option (sensitivity to volatility)."""
        dsigma = 1e-4
        option_price = self.option_pricing_model.price_option()
        option_price_up = self.option_pricing_model.__class__(
            self.option_pricing_model.S0, self.option_pricing_model.K, 
            self.option_pricing_model.T, self.option_pricing_model.r, 
            self.option_pricing_model.sigma + dsigma, self.option_pricing_model.M, 
            self.option_pricing_model.N
        ).price_option()
        vega = (option_price_up - option_price) / dsigma
        return vega

    def calculate_theta(self):
        """Calculate the Theta of the option (sensitivity to time decay)."""
        dT = 1 / 365  # 1 day time decay
        option_price = self.option_pricing_model.price_option()
        option_price_later = self.option_pricing_model.__class__(
            self.option_pricing_model.S0, self.option_pricing_model.K, 
            self.option_pricing_model.T - dT, self.option_pricing_model.r, 
            self.option_pricing_model.sigma, self.option_pricing_model.M, 
            self.option_pricing_model.N
        ).price_option()
        theta = (option_price_later - option_price) / dT
        return theta

    def calculate_rho(self):
        """Calculate the Rho of the option (sensitivity to interest rates)."""
        dr = 1e-4
        option_price = self.option_pricing_model.price_option()
        option_price_up = self.option_pricing_model.__class__(
            self.option_pricing_model.S0, self.option_pricing_model.K, 
            self.option_pricing_model.T, self.option_pricing_model.r + dr, 
            self.option_pricing_model.sigma, self.option_pricing_model.M, 
            self.option_pricing_model.N
        ).price_option()
        rho = (option_price_up - option_price) / dr
        return rho
