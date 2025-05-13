board = input()
answer = ""
flag = True

while True:
    if not board:
        break
    if board[:4] == 'XXXX':
        answer += 'AAAA'
        board = board[4:]
    elif board[:2] == 'XX':
        answer += 'BB'
        board = board[2:]
    elif board[0] == '.':
        answer += '.'
        board = board[1:]
    else:
        flag = False
        break

if flag:
    print(answer)
else:
    print(-1)