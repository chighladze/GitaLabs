year = int(input("Enter a year: "))

#
# Write your code here.
#
if year < 1582:
    print("Not within the Gregorian calendar period")

if year % 4 == 0 and year >= 1582:
    print("Leap year")
elif year % 100 != 0 and year >= 1582:
    print("Common year")
