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
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'
print(enter_move(board))