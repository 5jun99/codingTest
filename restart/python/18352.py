from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

dist = [int(1e9) for _ in range(n + 1)]

for _ in range(m):
  s, e = map(int, input().split())
  graph[s].append(e)

q = deque([(x, 0)])
dist[x] = 0
while q:
  now, cost = q.popleft()
  if dist[now] < cost:
    continue
  for next in graph[now]:
    if dist[next] < 1 + cost:
        continue
    dist[next] = cost + 1
    q.append((next, cost + 1))

answer = []

for i in range(1, n + 1):
  if dist[i] == k:
    answer.append(i)

answer.sort()

if answer:
  for a in answer:
    print(a)
else:
  print(-1)
