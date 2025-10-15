from collections import deque

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())

board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

well = []
for i in range(h):
  for j in range(n):
    for k in range(m):
      if board[i][j][k] == 1:
        well.append((i, j, k, 0))
        
q = deque(well)
answer = -1

while q:
  z, x, y, t = q.popleft()
  answer = max(t, answer)
  for d in range(6):
    nz, nx, ny = z + dz[d], x + dx[d], y + dy[d]

    if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if board[nz][nx][ny] == 0:
      board[nz][nx][ny] = 1
      q.append((nz, nx, ny, t + 1))

flag = False

for i in range(h):
  for j in range(n):
    for k in range(m):
      if board[i][j][k] == 0:
        flag = True

if flag:
  print(-1)
else:
  print(answer)