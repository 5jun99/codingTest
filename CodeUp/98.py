xl, yl = map(int, input().split())
board = [[0] * yl for _ in range(xl)]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for col in range(y - 1 , y - 1 + l):
            board[x-1][col] = 1 - board[x-1][col]
    else:
        for row in range(x - 1 , x - 1 + l):
            board[row][y-1] = 1 - board[row][y-1]

for row in range(xl):
    for col in range(yl):
        print(board[row][col], end=' ')
    print()
    
