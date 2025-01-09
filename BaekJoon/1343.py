board = list(input())

start_X_point = 0
X_sequence_count = 0

board_covered = [''] * len(board)
game_status = True
for i in range(len(board)):
    if board[i] == 'X':
        X_sequence_count += 1
    elif X_sequence_count % 2 == 1:
        game_status = False
        break
    else:
        board_covered[i] = '.'
        start_X_point = i - X_sequence_count
        while X_sequence_count > 2:
            board_covered[start_X_point:start_X_point+4] = ['A', 'A', 'A', 'A']
            X_sequence_count -= 4
            start_X_point += 4
        if X_sequence_count == 2:
            board_covered[start_X_point:start_X_point+2] = ['B', 'B']
            X_sequence_count -= 2
            start_X_point += 2
        X_sequence_count = 0

if X_sequence_count % 2 == 1:
    game_status = False
start_X_point = len(board) - X_sequence_count
while X_sequence_count > 2:
    board_covered[start_X_point:start_X_point+4] = ['A', 'A', 'A', 'A']
    X_sequence_count -= 4
    start_X_point += 4
if X_sequence_count == 2:
    board_covered[start_X_point:start_X_point+2] = ['B', 'B']
    start_X_point += 2
    X_sequence_count = 0

if game_status:
    for char in board_covered:
        print(char, end='')
else:
    print(-1)

    