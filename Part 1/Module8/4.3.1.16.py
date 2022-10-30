user_enter = 'text2.txt'  # input("Please enter file name ex:(text.txt): ")
file_name = user_enter.lower()

try:
    file = open(file_name, 'r')
    txt = file.read().lower()
    txt_unique = ''.join(set(txt))

    dct = {}

    for i in sorted(txt_unique):
        if i != '\n':
            dct[txt.count(i)] = i

    lst = list(sorted(dct.items().__reversed__()))[::-1]

    for x in lst:
        print(f'{x[1]} -> {x[0]}')

    file.close()
except Exception as ex:
    print(ex)
