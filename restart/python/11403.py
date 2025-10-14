n = int(input())
INF = int(1e9)
graph = [[INF] * n for _ in range(n)]

for i in range(n):
  temp = list(map(int, input().split()))

  for j in range(len(temp)):
    if temp[j] == 1:
      graph[i][j] = 1

for k in range(n):
  for a in range(n):
    for b in range(n):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(n):
  for j in range(n):
    if graph[i][j] >= 1 and graph[i][j] != INF:
      print(1, end=' ')
    else:
      print(0, end=' ')
  print()