from collections import deque

n, m = map(int, input().split())
area = []
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(board_x):
    q = deque()
    for i in range(n):
        for j in range(m):
            if board_x[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
     
        if nx < 0 or nx >= m or ny <0 or ny >= n:
            continue
        if board_x[nx][ny] == 0:
            board_x[nx][ny] = 2
            q.append((nx, ny))

    result = 0
    
    for i in range(n):
        for j in range(m):
            if board_x[nx][ny] == 0:
                result += 1

    area.append(result)

def wall(board_y, wall_):
    if wall_ == 2:
        bfs(board_y)
        return
    for i in range(n):
        for j in range(m):
            if board_y[i][j] == 0:
                board_y[i][j] = 1
                wall(board_y, wall_ + 1)
                board_y[i][j] = 0

wall(board, 0)

print(area)