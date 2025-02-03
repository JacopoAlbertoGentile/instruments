from derivatives.black_sholes import BlackScholes
import datetime as dt

class Call(object):

    def __init__(self, strike : float, option_price : float, expiry : dt.datetime, spot : float, interest_rate : float, buy_or_sell:str):

        self.strike = strike
        self.option_price = option_price
        self.expiry = expiry
        self.spot = spot
        self.interest_rate = interest_rate
        self.buy_or_sell = buy_or_sell
        self.bs = BlackScholes(strike=self.strike, spot=self.spot, interest_rate=self.interest_rate, expiry=self.expiry, option_type='C')


    def payoff(self, spot : float):
        if self.buy_or_sell == 'buy':
            if (spot - self.strike) >= 0:
                return (spot - self.strike) - self.option_price
            else:
                return -self.option_price

        elif self.buy_or_sell == 'sell':
            if (spot - self.strike) >= 0:
                return -((spot - self.strike) - self.option_price)
            else:
                return self.option_price
        else:
            return TypeError("buy_or_sell can be either buy or sell")



class Put(object):

    def __init__(self, strike: float, option_price: float, expiry: dt.datetime, spot: float,
                 interest_rate: float, buy_or_sell: str):
        self.strike = strike
        self.option_price = option_price
        self.expiry = expiry
        self.spot = spot
        self.interest_rate = interest_rate
        self.buy_or_sell = buy_or_sell
        self.bs = BlackScholes(strike=self.strike, spot=self.spot, interest_rate=self.interest_rate,
                               expiry=self.expiry, option_type='P')



    def payoff(self, spot : float):
        if self.buy_or_sell == 'buy':
            if (self.strike - spot) >= 0:
                return (self.strike - spot) - self.option_price
            else:
                return -self.option_price

        elif self.buy_or_sell == 'sell':
            if (self.strike - spot) >= 0:
                return -((self.strike - spot) - self.option_price)
            else:
                return self.option_price
        else:
            return TypeError("buy_or_sell can be either buy or sell")
