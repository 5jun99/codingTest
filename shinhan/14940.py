from collections import deque

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
shortest_board = [[-1] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy):
    q = deque()
    q.append((sx,sy))
    shortest_board[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if board[nx][ny] == 1 and shortest_board[nx][ny] == -1:
                shortest_board[nx][ny] = shortest_board[x][y] + 1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(shortest_board[i][j], end=' ')
    print()