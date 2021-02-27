from derivatives.black_sholes import BlackScholes

class Options(object):
    def __init__(self):
        self.strike = None
        self.price = None
        self.expire = None
        self.underlying_price = None

    @classmethod
    def call(cls, strike, price, expiry, underlying_price, rate):
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
                for arg, value in functions_args_values.items():
                    if hasattr(self._option, arg):
                        setattr(self, arg, value)
                    else:
                        pass

            def payoff(self, underlying_price):
                return (underlying_price - self.strike) - self.price

        return Call()

    @classmethod
    def put(cls, strike, price, expiry, underlying_price, rate):
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
                for arg, value in functions_args_values.items():
                    if hasattr(self._option, arg):
                        setattr(self, arg, value)
                    else:
                        pass

            def payoff(self, underlying_price):
                return (self.strike - underlying_price) - self.price

        return Put()