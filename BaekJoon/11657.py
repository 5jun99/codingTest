INF = int(1e9)

n, m = map(int, input().split())

edges = []
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bf(start):
    distance[start]  = 0
    for i in range(n):
        for j in range(m):
            current, next, cost = edges[j]

            if distance[current] != INF and distance[current] + cost < distance[next]:
                distance[next] = distance[current] + cost

                if i == n - 1:
                    return False
    return True


if bf(1):
    for d in range(2, n + 1):
        if distance[d] == INF:
            print(-1)
        else:
            print(distance[d])
else:
    print(-1)