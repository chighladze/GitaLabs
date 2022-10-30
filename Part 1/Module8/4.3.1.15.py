user_enter = 'text.txt'  # input("Please enter file name ex:(text.txt): ")
file_name = user_enter.lower()

try:
    file = open(file_name, 'r')
    txt = file.read().lower()
    txt_unique = ''.join(set(txt))

    for i in sorted(txt_unique):
        if i != '\n':
            print(f'{i} -> {txt.count(i)}')
    file.close()
except Exception as ex:
    print(ex)
