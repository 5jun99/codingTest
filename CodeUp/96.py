board = [list(map(int, input().split())) for _ in range(19)]
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for row in range(19):
        board[row][y - 1] = 1 - board[row][y - 1]
    for col in range(19):
        board[x - 1][col] = 1 - board[x - 1][col]

for row in range(19):
    for col in range(19):
        print(board[row][col], end=' ')
    print()

    