def check_col(board):
    lst = []
    for i in board:
        if i != '\n' and i != ' ':
            lst.append(int(i))

    lst = lst[::9]
    lst = set(lst)
    if len(lst) == 9:
        return True
    else:
        return False


def check_row(board):
    lst = []
    for i in board:
        if i != '\n' and i != ' ':
            lst.append(int(i))

    lst2 = []
    z = 0
    for x in range(1, 10):
        lst2.append(lst[:9])
        lst = lst[9:]

    t = []
    for d in lst2:
        if len(set(d)) == 9:
            d.append(True)
        else:
            d.append(False)

    return all(t)


def check_3x3(board):
    lst = []
    for i in board:
        if i != '\n' and i != ' ':
            lst.append(int(i))

    lst2 = []
    z = 0
    for x in range(1, 28):
        lst2.append(lst[:3])
        lst = lst[3:]

    nn1 = lst2[::3]
    nn2 = lst2[1::3]
    nn3 = lst2[2::3]

    ll= []
    for a in range(1, 4):
        ll.append(nn1[0] + nn1[1] + nn1[2])
        nn1 = nn1[3:]
        ll.append(nn2[0] + nn2[1] + nn2[2])
        nn2 = nn2[3:]
        ll.append(nn3[0] + nn3[1] + nn3[2])
        nn3 = nn3[3:]


    for k in ll:
        if len(set(k)) < 9:
            return False
    return True


def sudoku_cheaker(board):
    s = check_col(board)
    w = check_row(board)
    q = check_3x3(board)

    if all([s,w,q]):
        return 'Yes'
    else:
        return 'No'






print(sudoku_cheaker(""" 
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
"""))

print(sudoku_cheaker("""195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671"""))
