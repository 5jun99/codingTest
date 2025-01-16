n = int(input())

board = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global visited, count
    visited[x][y] = True
    board[x][y] = count 

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if not visited[nx][ny] and board[nx][ny] != 0:
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if board[i][j] != 0 and visited[i][j] == False:
            dfs(i, j)
            count += 1

size = []

for i in range(1, count):
    temp = 0
    for j in range(n):
        temp += board[j].count(i)
    size.append(temp)
size.sort()
print(count - 1)
for s in size:
    print(s)