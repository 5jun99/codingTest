from collections import deque
m, n , h = map(int, input().split())

tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
queue = deque()
dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]

answer = 0

def bfs():
    while queue:
        x, y, z = deque.popleft()

        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]
        if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
            continue
        if tomatoes[nz][ny][nx] == 0 and visited[nz][ny][nx] == False:
            queue.append((nx,ny,nz))
            tomatoes[nz][ny][nx] = 1
            visited[nz][ny][nx] = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatoes[i][j][k] == 1:
                queue.append((i,j,k))
                visited[i][j][k] = True

bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatoes[i][j][k] == 0:
                print(-1)
                exit(0)
        answer = max(answer, tomatoes[i][j][k])

print(answer - 1)