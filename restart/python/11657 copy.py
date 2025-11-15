n, m = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m)]

distance = [int(1e9)] * (n + 1)
distance[1] = 0

flag = False
for i in range(n):
  for j in range(m):
    s, e, t = edges[j]

    if distance[s] != int(1e9) and distance[e] > distance[s] + t:
      distance[e] = distance[s] + t
      if i == n - 1:
        flag = True

if flag:
  print(-1)
else:
  for d in distance[2:]:
    if d == int(1e9):
      print(-1)
      continue
    print(d)
    