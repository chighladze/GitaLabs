from random import randrange


def display_board(board):
    board_size = range(3)
    print(('+' + '-' * 7) * 3, '+', sep='')
    for r in board_size:
        print(('|' + ' ' * 7) * 3, '|', sep='')
        for c in board_size:
            print('|' + ' ' * 3 + str(board[r][c]) + ' ' * 3, end='')
        print('|')
        print(('|' + ' ' * 7) * 3, '|', sep='')
        print(('+' + '-' * 7) * 3, '+', sep='')


def enter_move(board):
    ok = False
    while not ok:
        move = input('Enter your move: ')
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print('Not a correct move - repeat your move')
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        sign = board[row][col]
        ok = sign not in ['O', 'X']
        if not ok:
            print('Filed already occupied')
            continue
        board[row][col] = 'O'


def make_list_of_free_fields(board):
    free_lst = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free_lst.append((row, col))
    return free_lst


def victory_for(board, sign):
    if sign == 'X':
        who = 'me'
    elif sign == 'O':
        who = 'you'
    else:
        who = None

    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
            return who
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
            return who
        if board[rc][rc] != sign:
            cross1 = False
        if board[2 - rc][2 - rc] != sign:
            cross2 = False
        if cross1 or cross2:
            return who
        return None


def draw_move(board):
    free = make_list_of_free_fields(board)
    cmt = len(free)
    if cmt > 0:
        this = randrange(cmt)
        row, col = free[this]
        board[row][col] = 'X'


board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'
free_lst = make_list_of_free_fields(board)
human_turn = True
while len(free_lst):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print('You won!')
elif victor == 'me':
    print('I won')
else:
    print('Tie!')
