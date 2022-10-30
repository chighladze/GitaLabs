def digit_of_life():
    d = input('Please enter your dbirth date (ent.format ex:YYYY-MM-DD): ')
    year = str(d[:4])
    month = str(d[5:7])
    day = str(d[8:])

    lst = []
    for i in (year + month + day):
        lst.append(int(i))

    sum1 = str(sum(lst))

    lst2 = []
    for x in sum1:
        lst2.append(int(x))

    sum2 = sum(lst2)

    return sum2


print(digit_of_life())
