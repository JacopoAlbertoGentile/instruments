

class Options(object):
    def __init__(self):
        self.strike = None
        self.price = None
        self.expire = None
        self.underlying = None

    @classmethod
    def call(cls, strike, price, expire, underlying):
        functions_args_values = locals()
        option = cls()

        class Call(object):
            def __init__(self):
                self._option = option
                for arg, value in functions_args_values.items():
                    if hasattr(self._option, arg):
                        setattr(self, arg, value)
                    else:
                        pass

            def __class_name__(self):
                return "Call"

        return Call()

    @classmethod
    def put(cls, strike, price, expire, underlying):
        functions_args_values = locals()
        option = cls()

        class Put(object):
            def __init__(self):
                self._option = option
                for arg, value in functions_args_values.items():
                    if hasattr(self._option, arg):
                        setattr(self, arg, value)
                    else:
                        pass

            def payoff(self):

        return Put()

if __name__=="__main__":
    call = Options.call(1,1,1,1)
    print(call.__class__)