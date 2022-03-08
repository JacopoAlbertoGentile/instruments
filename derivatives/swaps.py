import datetime as dt

class Swap(object):
    """
    Class that defines swap object
    """
    def __init__(self, start_date : str, end_date : str, rate : float):
        self._start_date = start_date
        self._end_date = end_date
        self.rate = rate
        self.today = dt.datetime.today()
        self.start_date = (self.today.date() + dt.timedelta(self._mapping_date(self._start_date)))
        self.end_date = (self.start_date + dt.timedelta(self._mapping_date(self._end_date)))

    def _mapping_date(self, date : str):
        date = date.upper()
        list_of_date = list(date)
        to_return = ''
        for i in list_of_date:
            if i == 'Y' or i =='M':
                continue
            else:
                to_return = to_return + i
        int_to_return = int(to_return)
        if 'Y' in list_of_date:
            return 360 * int_to_return
        elif 'M' in list_of_date:
            return 30 * int_to_return
        else:
            return 0



