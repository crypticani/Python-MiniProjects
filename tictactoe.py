def print_field(board):
    print('---------')
    for n in range(3):
        row = '| '
        for m in range(3):
            row = row + board[m][n] + ' '
        print(row + '|')
    print('---------')


def evaluate_game(board):
    win_x = 0
    win_o = 0
    play_x = 0
    play_o = 0

    for n in range(3):
        for m in range(3):
            if board[m][n] == 'X':
                play_x += 1
            elif board[m][n] == 'O':
                play_o += 1

    if board[0][0] == board[0][1] == board[0][2] == 'X':  # rows
        win_x += 1
    if board[1][0] == board[1][1] == board[1][2] == 'X':
        win_x += 1
    if board[2][0] == board[2][1] == board[2][2] == 'X':
        win_x += 1
    if board[0][0] == board[1][0] == board[2][0] == 'X':  # columns
        win_x += 1
    if board[0][1] == board[1][1] == board[2][1] == 'X':
        win_x += 1
    if board[0][2] == board[1][2] == board[2][2] == 'X':
        win_x += 1
    if board[0][0] == board[1][1] == board[2][2] == 'X':  # diagonals
        win_x += 1
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        win_x += 1

    if board[0][0] == board[0][1] == board[0][2] == 'O':  # rows
        win_o += 1
    if board[1][0] == board[1][1] == board[1][2] == 'O':
        win_o += 1
    if board[2][0] == board[2][1] == board[2][2] == 'O':
        win_o += 1
    if board[0][0] == board[1][0] == board[2][0] == 'O':  # columns
        win_o += 1
    if board[0][1] == board[1][1] == board[2][1] == 'O':
        win_o += 1
    if board[0][2] == board[1][2] == board[2][2] == 'O':
        win_o += 1
    if board[0][0] == board[1][1] == board[2][2] == 'O':  # diagonals
        win_o += 1
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        win_o += 1

    if win_x == 1 and win_o == 0:
        return 'x'
    elif win_x == 0 and win_o == 1:
        return 'o'
    elif play_x + play_o == 9:
        return 'd'
    else:
        return ''


field = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

cells = '         '
result = ''
turn = 'x'

i = 0
for n in range(3):
    for m in range(3):
        field[m][n] = cells[i]
        i += 1

print_field(field)
print("Instructions:")
print("A matrix based two player tic-tac-toe game")
print("matrix format = (row, column)")

while True:  # evaluate game

    while turn == 'x':  # Player X
        print("X's turn")
        choice = input('Enter the coordinates: ').split()
        try:
            if int(choice[0]) < 1 or int(choice[0]) > 3 or int(choice[1]) < 1 or int(choice[1]) > 3:
                print('Coordinates should be from 1 to 3!')
            else:
                column = int(choice[0]) - 1
                row = int(choice[1]) - 1
                if field[row][column] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    field[row][column] = 'X'
                    turn = 'o'
        except ValueError:
            print('You should enter numbers!')

    print_field(field)
    result = evaluate_game(field)
    if result != '':
        break

    while turn == 'o':  # Player O
        print("O's turn")
        choice = input('Enter the coordinates: ').split()
        try:
            if int(choice[0]) < 1 or int(choice[0]) > 3 or int(choice[1]) < 1 or int(choice[1]) > 3:
                print('Coordinates should be from 1 to 3!')
            else:
                column = int(choice[0]) - 1
                row = int(choice[1]) - 1
                if field[row][column] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    field[row][column] = 'O'
                    turn = 'x'
        except ValueError:
            print('You should enter numbers!')

    print_field(field)
    result = evaluate_game(field)
    if result != '':
        break

if result == 'x':
    print('X wins')
elif result == 'o':
    print('O wins')
elif result == 'd':
    print('Draw')
