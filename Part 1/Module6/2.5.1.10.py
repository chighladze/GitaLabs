def in_word(search_arg, word):
    lst = []
    word = word.lower()
    for i in search_arg:
        if word.find(i) < 0:
            lst.append(False)
        else:
            lst.append(True)

    if all(lst):
        return 'Yes'
    else:
        return 'No'


print(in_word('donor', 'Nabucodonosor'))
print(in_word('donut', 'Nabucodonosor'))
