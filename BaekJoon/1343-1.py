board = input()
board_index = 0
board_covered = []

while board_index < len(board):
    if board[board_index:board_index+4] == 'XXXX':
        board_covered.append('AAAA')
        board_index += 4
    elif board[board_index:board_index+2] == 'XX':
        board_covered.append('BB')
        board_index += 2
    elif board[board_index] == 'X':
        board_covered = ['-1']
        break
    else:
        board_covered.append(board[board_index])
        board_index +=1

print(''.join(board_covered))
    