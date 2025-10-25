from collections import deque

n, l, r = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0

def bfs(i, j):
  q = deque([(i, j)])
  temp = [(i, j)]

  while q:
    x, y = q.popleft()
    for d in range(4):
      nx, ny = x + dx[d], y + dy[d]
      if nx >= n or nx < 0 or ny >= n or ny < 0:
        continue
      diff = abs(ground[x][y] - ground[nx][ny])
      if diff >= l and diff <= r and (nx, ny) not in temp and (nx, ny) not in q:
        temp.append((nx, ny))
        q.append((nx, ny))
  if len(temp) <= 1:
    return []
  
  return temp

while True:
  unions = []
  flag = False
  visited = [[False] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      union = []
      if visited[i][j]:
        continue
      
      union = bfs(i, j)

      if not union:
        visited[i][j] = True
        continue
      flag = True

      for ux, uy in union:
        visited[ux][uy] = True
      unions.append(union)

  for union in unions:
    adjust = 0
    for ux, uy in union:
      adjust += ground[ux][uy]

    adjust //= len(union)
    for ux, uy in union:
      ground[ux][uy] = adjust

  if not flag:
    break
  answer += 1


print(answer)
