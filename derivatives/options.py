from derivatives.black_scholes import BlackScholes
import datetime as dt

class Call(object):

    def __init__(self, t : dt.datetime, strike : float, option_price : float, expiry : dt.datetime, spot : float, interest_rate : float, buy_or_sell:str):

        self.strike = strike
        self.option_price = option_price
        self.expiry = expiry
        self.spot = spot
        self.interest_rate = interest_rate
        self.buy_or_sell = buy_or_sell
        self.bs = BlackScholes(t=t, strike=self.strike, spot=self.spot, interest_rate=self.interest_rate,
                               expiry=self.expiry, option_type='C')


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


    def smooth_payoff(self, spot : float, eps : float=0.5):
        """
        Using Smooth payoff quadratic formula, eps is the error to give usually set around 0.5
        :param spot:
        :param eps:
        :return:
        """
        if self.buy_or_sell == 'buy':

            call_value = ((spot - self.strike) + ((spot - self.strike)**2 + eps**2)**0.5) / 2
            return call_value - self.option_price

        elif self.buy_or_sell == 'sell':

            call_value = ((spot - self.strike) + ((spot - self.strike)**2 + eps**2)**0.5) / 2
            return self.option_price - call_value

        else:

            return TypeError('buy_or_sell can be either buy or sell')








class Put(object):

    def __init__(self, t : dt.datetime, strike: float, option_price: float, expiry: dt.datetime, spot: float,
                 interest_rate: float, buy_or_sell: str):
        self.strike = strike
        self.option_price = option_price
        self.expiry = expiry
        self.spot = spot
        self.interest_rate = interest_rate
        self.buy_or_sell = buy_or_sell
        self.bs = BlackScholes(strike=self.strike, spot=self.spot, interest_rate=self.interest_rate,
                               expiry=self.expiry, option_type='P', t=t)



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


    def smooth_payoff(self, spot: float, eps: float = 0.5):
        """
        Using Smooth payoff quadratic formula, eps is the error to give usually set around 0.5
        :param spot:
        :param eps:
        :return:
        """
        if self.buy_or_sell == 'buy':

            put_value = ((self.strike - spot) + ((self.strike - spot)**2 + eps**2)**0.5) / 2
            return put_value - self.option_price

        elif self.buy_or_sell == 'sell':

            put_value = ((self.strike - spot) + ((self.strike - spot)**2 + eps**2)**0.5) / 2
            return self.option_price - put_value

        else:

            return TypeError('buy_or_sell can be either buy or sell')

