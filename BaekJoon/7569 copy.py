import sys
from collections import deque

input = sys.stdin.readline

m,n,h = map(int, input().split())

matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
print(matrix)
queue = deque()

answer = 0
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        x, y, z = queue.popleft()
        
        for d in range(6):
            nx, ny, nz = x + dx[d], y + dy[d], z + dz[d]

            if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                continue

            if matrix[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                queue.append((nx,ny,nz))
                matrix[nz][ny][nx] = 1 + matrix[z][y][x]
                visited[nz][ny][nx] = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1:
                queue.append((k,j,i))
                visited[i][j][k] = True

bfs()

flag = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0:
                flag = False
        answer = max(answer, max(matrix[i][j]))
if flag:
    print(answer - 1)
else:
    print(-1)