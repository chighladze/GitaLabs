"""task 1"""
n = range(10)

for x in n:
    x += 1
    print(f'Hellow World! {x}')

dash = 100 * '-'
print(f"{dash}\n")

"""task 2"""
n = range(1, 11)

for i in n:
    for x in n:
        print(f'{i * x:4}', end='')
    print()

print(f"{dash}\n")

"""task 3"""
n = range(15)
last_item_in_range = list(n[-1:])[0] + 1
value_1_length = len(f'{last_item_in_range} * {last_item_in_range} = {last_item_in_range * last_item_in_range}')
value_2_length = len(f'{last_item_in_range} ^ 10 = {last_item_in_range ** 10}')
value_3_length = len(f'{last_item_in_range} ^ {last_item_in_range} = {last_item_in_range ** last_item_in_range}')

for x in n:
    x += 1
    print(f'{x} * {x} = {x * x}'.ljust(value_1_length) + ' | ' + f'{x} ^ 10 = {x ** 10}'.ljust(
        value_2_length) + ' | ' + f'{x} ^ {x} = {x ** x}'.ljust(value_2_length))
print(f"{dash}\n")
