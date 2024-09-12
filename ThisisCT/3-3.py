n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
maximum = -1
for i in range(n):
    temp_min = 10000
    for j in range(m):
        if board[i][j] < temp_min:
            temp_min = board[i][j]
    if maximum < temp_min:
        maximum = temp_min

print(maximum)