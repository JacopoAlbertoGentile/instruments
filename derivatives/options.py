from derivatives.black_sholes import BlackScholes

class Options(object):
    def __init__(self):
        self.strike = None
        self.price = None
        self.expiry = None
        self.underlying_price = None
        self.delta = None
        self.gamma = None
        self.vega = None
        self.theta = None

    @classmethod
    def call(cls, strike, price, expiry, underlying_price, rate, buy_or_sell:str, underlying_name:str):
        functions_args_values = locals()
        option = cls()
        bs = BlackScholes(
            strike = strike,
            underlying_price=underlying_price,
            rate=rate,
            expiry=expiry,
            type='C'
        )

        class Call(object):
            def __init__(self):
                self._option = option
                self.bs=bs
                self._buy_or_sell = buy_or_sell
                self.underlying_name = underlying_name
                for arg, value in functions_args_values.items():
                    if hasattr(self._option, arg):
                        setattr(self, arg, value)
                    else:
                        pass
                self.option_name = str(self.underlying_name) + " C" + str(self.strike) + " " + str(self.expiry)

            def payoff(self, underlying_price):
                if self._buy_or_sell == 'buy':
                    if (underlying_price - self.strike) >= 0:
                        return (underlying_price - self.strike) - self.price
                    else:
                        return -self.price
                elif self._buy_or_sell == 'sell':
                    if (underlying_price - self.strike) >= 0:
                        return -((underlying_price - self.strike) - self.price)
                    else:
                        return self.price
                else:
                    return TypeError("buy_or_sell can be either buy or sell")

        return Call()

    @classmethod
    def put(cls, strike, price, expiry, underlying_price, rate, buy_or_sell:str, underlying_name:str):
        functions_args_values = locals()
        option = cls()
        bs = BlackScholes(
            strike = strike,
            underlying_price=underlying_price,
            rate=rate,
            expiry=expiry,
            type='P'
        )

        class Put(object):
            def __init__(self):
                self._option = option
                self.bs=bs
                self._buy_or_sell = buy_or_sell
                self.underlying_name = underlying_name
                for arg, value in functions_args_values.items():
                    if hasattr(self._option, arg):
                        setattr(self, arg, value)
                    else:
                        pass
                self.option_name = str(self.underlying_name) + " P" + str(self.strike) + " " + str(self.expiry)

            def payoff(self, underlying_price):
                if self._buy_or_sell == 'buy':
                    if (self.strike - underlying_price) >= 0:
                        return (self.strike - underlying_price) - self.price
                    else:
                        return -self.price
                elif self._buy_or_sell == 'sell':
                    if (self.strike - underlying_price) >= 0:
                        return -((self.strike - underlying_price) - self.price)
                    else:
                        return self.price
                else:
                    return TypeError("buy_or_sell can be either buy or sell")

        return Put()
