class WeekDayError(Exception):
    pass


class Weeker:
    __wd = ['Mon',
            'Tus',
            'Wed',
            'Thu',
            'Fri',
            'Sat',
            'Sun'
            ]

    def __init__(self, d):
        try:
            self.__stat = self.__wd.index(d)
        except:
            raise WeekDayError

    def __str__(self):
        return self.__wd[self.__stat]

    def add_days(self, n):
        self.__stat = (self.__stat + n) % 7

    def subtract_days(self, n):
        self.__stat = (self.__stat - n) % 7


try:
    wd = Weeker('Fri')
    print(wd)
    wd.add_days(15)
    print(wd)
    wd.subtract_days(23)
    print(wd)
    # print(weekday._Weeker__stat)
    wd = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
