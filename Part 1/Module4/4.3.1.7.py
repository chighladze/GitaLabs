def is_year_leap(year):
    if year < 1582:
        return "Not within the Gregorian calendar period"
    elif year % 4 == 0 and year >= 1582:
        return True
    elif year % 100 != 0 and year >= 1582:
        return False


#
# Your code from LAB 4.3.1.6.
#

def days_in_month(year, month):
    if is_year_leap(year) and month == 2:
        return 28
    if not is_year_leap(year) and month == 2:
        return 29
    elif month == 1:
        return 31
    elif month == 11:
        return 30


#
# Write your new code here.
#

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
