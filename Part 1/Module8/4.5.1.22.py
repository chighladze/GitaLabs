from datetime import datetime


dd = datetime(2020, 11, 4, 14, 53, 00)

print(datetime.strftime(dd, '%Y/%m/%d %H:%M:%S'))
print(datetime.strftime(dd, '%Y/%B/%d %H:%M:%S %p'))
print(datetime.strftime(dd, '%a, %Y %b %d '))
print(datetime.strftime(dd, '%A, %Y %B %d '))
print(datetime.strftime(dd, '%A: %w'))
print(datetime.strftime(dd, '%Day of the year: %j'))
print(datetime.strftime(dd, '%Week number of the year: %W'))
