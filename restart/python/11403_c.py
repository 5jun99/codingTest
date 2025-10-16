n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  for j in range(n):
    if graph[i][j] != 1:
      continue
    for k in range(n):
      if graph[k][i] == 1:
        graph[k][j] = 1


for g in graph:
  print(*g)
