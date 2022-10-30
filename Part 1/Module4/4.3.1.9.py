def is_prime(num):
    ran = list(range(2, num))
    ret = True
    for x in ran:
        if num % x == 0:
            ret = False
    return ret


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
