while 1:
    c0 = int(input("Please enter The integer: "))

    if c0 <= 0:
        print('Please enter non-negative and non-zero integer!')
        continue
    steps = 0
    while c0 != 1:
        if not c0 % 2:
            c0 = c0 / 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
        print(round(c0))
    print(f"steps = {steps}")
