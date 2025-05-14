import datetime as dt
import math as m
import scipy.stats as st


class BlackScholes(object):
    """
    Class to calculate values for option prices. Check good ways to use locals() the build in function
    """
    def __init__(self, strike : float, spot : float, interest_rate : float,
                 expiry : dt.datetime, option_type : str, vol : float=None):
        self.strike = strike
        self.spot = spot
        self.vol = vol
        self.interest_rate = interest_rate
        self.option_type = option_type
        self.expiry = expiry
        today = dt.datetime.today()
        T = (self.expiry - today).days / 252
        self.T = T
        self.discount_factor = m.exp(-self.interest_rate * self.T)
        self.d1 = None
        self.d2 = None

    def price(self, vol : float):
        d1 = (m.log(self.spot / self.strike) + (self.interest_rate + 0.5 * vol ** 2) * self.T) / (vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        if self.option_type == 'Call' or self.option_type == "C":
            call = st.norm.cdf(d1, 0, 1) * self.spot- self.discount_factor * self.strike * st.norm.cdf(d2, 0, 1)
            return call
        else:
            put = st.norm.cdf(-d2, 0, 1) * self.strike * self.discount_factor - self.spot * st.norm.cdf(-d1, 0, 1)
            return put

    def delta(self, vol : float):
        d1 = (m.log(self.spot/ self.strike) + (self.interest_rate + 0.5 * vol ** 2) * self.T) / (
                vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        if self.option_type == "Call" or self.option_type == "C":
            deltaBS = st.norm.cdf(d1, 0, 1)
            return (deltaBS)
        elif self.option_type == 'Put' or self.option_type == 'P':
            deltaBS = st.norm.cdf(-d1, 0, 1)
            return -(deltaBS)

        else:
            return 0

    def gamma(self, vol : float):
        d1 = (m.log(self.spot/ self.strike) + (
                self.interest_rate + 0.5 * vol ** 2) * self.T) / (
                     vol * m.sqrt(self.T))
        return (st.norm.pdf(d1)) / (vol * self.spot* m.sqrt(self.T))

    def vega(self, vol :float):
        d1 = (m.log(self.spot/ self.strike) + (self.interest_rate + 0.5 * vol ** 2) * self.T) / (
                vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        vega_value = self.spot* st.norm.cdf(d1, 0, 1) * m.sqrt(self.T)
        return vega_value

    def implied_vol(self, option_mkt_price : float, vol_est : float):
        print(('OptionPrice', self.price(vol_est), 'OptionDelta', self.delta(vol_est), 'OptionVega', self.vega(vol_est)))
        i = 1
        while (i <= 100):
            vol_est = vol_est - ((self.price(vol_est) - option_mkt_price) / self.vega(vol_est))
            if abs(self.price(vol_est) - option_mkt_price) <= 0.0001:
                print("Numbers of attemps:", i)
                print("Implied_Vol:", vol_est)
                return vol_est
            else:
                i = i + 1

    def volga(self, vol : float):
        Vega = self.vega(vol)
        d1 = (m.log(self.spot/ self.strike) + (self.interest_rate + 0.5 * vol ** 2) * self.T) / (
                vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        volga = Vega * (d1 * d2) / vol
        return (volga)

    def vanna(self, vol :float):
        d1 = (m.log(self.spot/ self.strike) + (self.interest_rate + 0.5 * vol ** 2) * self.T) / (
                vol * m.sqrt(self.T))
        dNorm = m.exp(-0.5 * d1 ** 2) * (1 / 2 * m.pi)
        vanna = m.sqrt(self.T) * dNorm * (1 - d1)
        return (vanna)

    def theta(self, vol :float):
        d1 = (m.log(self.spot/ self.strike) + (self.interest_rate + 0.5 * vol ** 2) * self.T) / (
                vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        bs_theta = - (self.spot* st.norm.pdf(d1) * vol * 0.5 / m.sqrt(
            self.T)) - self.interest_rate * self.strike * self.discount_factor * st.norm.cdf(d2, 0, 1)
        return bs_theta
