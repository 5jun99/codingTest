import heapq
import sys
input = sys.stdin.readline

#V, E = map(int, input().split())
#k = int(input())

#graph = [[] for _ in range(V + 1)]
#distance = [int(1e9)] * (V + 1)

#for _ in range(E):
#    u, v, w = map(int, input().split())
#    graph[u].append((v, w))

#def dijkstra(start):
#    q = []
#    heapq.heappush(q, (0, start))
#    distance[start] = 0

#    while q:
#        dist, now = heapq.heappop(q)

#        # 이미 더 짧은 경로로 방문한 적 있으면 스킵
#        if dist > distance[now]:
#            continue

#        for next, w in graph[now]:
#            cost = dist + w
#            if cost < distance[next]:
#                distance[next] = cost
#                heapq.heappush(q, (cost, next))

#dijkstra(k)

#for d in distance[1:]:
#    print("INF" if d == int(1e9) else d)

import heapq


V, E = map(int, input().split())

K = int(input())
graph = [[] for _ in range(V + 1)]
distance = [int(1e9)] * (V + 1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


q = [(0, K)]
distance[K] = 0

while q:
    cost, now  = heapq.heappop(q)

    if distance[now] < cost:
        continue

    for next, dist in graph[now]:
        s = cost + dist
        if s < distance[next]:
            distance[next] = s
            heapq.heappush(q, (s, next))

for d in distance[1:]:
    if d == int(1e9):
        print('INF')
        continue
    print(d)

