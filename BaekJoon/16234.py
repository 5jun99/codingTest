from collections import deque

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check():
    visited = [[False] * n for _ in range(n)]
    groups = []
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            q = deque([(i, j)])
            group = [(i, j)]
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                        continue
                    if l <= abs(board[x][y] - board[nx][ny]) <= r:
                        visited[nx][ny] = True
                        group.append((nx, ny))
                        q.append((nx, ny))
            if len(group) >= 2:
                groups.append(group)
    if not groups:
        return False
    move(groups)
    return True

def move(groups):
    for group in groups:
        summation = sum(board[x][y] for x, y in group)
        personAfter = summation // len(group)
        for x, y in group:
            board[x][y] = personAfter

while check():
    count += 1

print(count)