import heapq

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
  distance = [int(1e9)] * (n + 1)

  q = [(0, start)]

  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
      continue

    for next, cost in graph[now]:
      if dist + cost < distance[next]:
        distance[next] = dist + cost
        heapq.heappush(q, (dist + cost, next))

  return distance

distance1 = dijkstra(1)
distancev1 = dijkstra(v1)
distancev2 = dijkstra(v2)

case1 = distance1[v1] + distancev1[v2] + distancev2[n]
case2 = distance1[v2] + distancev2[v1] + distancev1[n]
result = min(case1, case2)
print(result if result != int(1e9) else -1)


