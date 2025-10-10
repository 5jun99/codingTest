n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
dist = [int(1e9) for _ in range(n + 1)]

dist[1] = 0
flag = False
for i in range(n):
  for j in range(m):
    now, next, cost = edges[j]

    if dist[now] != int(1e9) and dist[next] > dist[now] + cost:
      dist[next] = dist[now] + cost
      if i == n - 1:
        flag = True

if flag:
  print(-1)
else:
  for d in dist[2:]:
    print(d if d != int(1e9) else  -1)

#q = deque([(1, 0)])

#while q:
#  now, cost = q.popleft()
#  if dist[now] < cost:
#    continue

#  for next, distance in graph[now]:
#      if dist[next] > distance + cost:
#         dist[next] = distance + cost
#         q.append((next, distance + cost + 1))

#print(dist)