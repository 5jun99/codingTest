from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    n, e = map(int, input().split())
    graph[n].append(e)
    graph[e].append(n)

for g in graph:
    g.sort()

visited_dfs = []

def dfs(node):
    visited_dfs.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited_dfs:
            dfs(neighbor)

def bfs(start):
    visited = []
    dq = deque()
    dq.append(start)

    while dq:
        now = dq.popleft()
        if now in visited:
            continue
        visited.append(now)
        for neighbor in graph[now]:
            dq.append(neighbor)
    return visited

dfs(v)
print(*visited_dfs)
print(*bfs(v))

