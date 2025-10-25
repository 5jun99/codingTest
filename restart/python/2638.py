from collections import deque

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0 , 0]
dy = [0, 0, 1 , -1]

def bfs(i, j, state):
  q = deque([(i, j)])
  visited = [[False] * m for _ in range(n)]
  visited[i][j] = True
  union = [(i, j)]
  while q:
    x, y = q.popleft()
    
    for d in range(4):
      nx, ny = x + dx[d], y + dy[d]

      if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
        continue
      if board[nx][ny] == state:
        q.append((nx, ny))
        union.append((nx, ny))
        visited[nx][ny] = True
  return union

def init():
  blank_cnt = 0
  cheese_board = [[0] * m for _ in range(n)]
  visited = [[False] * m for _ in range(n)]

  for i in range(n):
    for j in range(m):
      if visited[i][j]:
        continue
      union = bfs(i, j, board[i][j])

      for ux, uy in union:
        visited[ux][uy] = True

      if board[i][j] == 0:
        for ux, uy in union:
          cheese_board[ux][uy] = blank_cnt
        blank_cnt += 1
      else:
        for ux, uy in union:
          cheese_board[ux][uy] = -1

  return cheese_board

time = 0

while True:
  cheese_board = init()

  cheese = []
  for i in range(n):
    for j in range(m):
      if cheese_board[i][j] == -1:
        cheese.append((i, j))

  if not cheese:
    break

  melting = []
  for cx, cy in cheese:
    temp = 0
    for d in range(4):
      nx, ny = cx + dx[d], cy + dy[d]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      
      if cheese_board[nx][ny] == 0:
        temp += 1
    if temp >= 2:
      melting.append((cx, cy))
  
  for mx, my in melting:
    board[mx][my] = 0

  time += 1

print(time)