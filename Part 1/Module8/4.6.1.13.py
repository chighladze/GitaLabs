import calendar


class MyCalendar(calendar.Calendar):

    def __init__(self):
        self.setfirstweekday(calendar.SUNDAY)

    def count_weekday_in_year(self, year, weekday):
        count = 0
        yearD = []
        for x in range(1, 13):
            yearD.append(list(self.monthdays2calendar(year, x)))

        for x in yearD:
            for y in x:
                for z in y:
                    if z[1] == weekday:
                        count += 1
        return count


mc = MyCalendar()
print(mc.count_weekday_in_year(2019, 0))
print(mc.count_weekday_in_year(2000, 6))
