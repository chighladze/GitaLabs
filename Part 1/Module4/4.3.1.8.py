def is_year_leap(year):
    if year < 1582:
        return "Not within the Gregorian calendar period"
    elif year % 4 == 0 and year >= 1582:
        return True
    elif year % 100 != 0 and year >= 1582:
        return False


def days_in_month(year, month):
    if is_year_leap(year) and month == 2:
        return 28
    if not is_year_leap(year) and month == 2:
        return 29
    elif month == 1:
        return 31
    elif month == 11:
        return 30


def day_of_year(year, month, day):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days_in_months[1] = 29
    day = sum(days_in_months[:month - 1]) + day
    return day


#
# Write your new code here.
#

print(day_of_year(2000, 12, 31))
