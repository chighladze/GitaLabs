def shifts_character(st, shif=0):
    if shif <= 25:
        new_str = ''
        for i in st:
            if i.islower():
                if (ord(i) + shif) > 122:
                    x = ord(i) + shif - 122 + 97
                    new_str += str(chr(x))
                else:
                    new_str += str(chr(ord(i) + shif))
            elif i.isupper():
                if (ord(i) + shif) > 90:
                    x = ord(i) + shif - 90 + 65
                    new_str += str(chr(x))
                else:
                    new_str += str(chr(ord(i) + shif))
            else:
                new_str += chr(ord(i))
    else:
        return 'Please enter shift 25 >= 1'
    return new_str

print(shifts_character('afjgdfgAAA    11   1', 24))

