from collections import deque

n, m = map(int, input().split())

indegree = [0] * (n + 1)
edges = [[] for _ in range(n + 1)]
result = []

for _ in range(m):
  s, e = map(int, input().split())
  edges[s].append(e)
  indegree[e] += 1

q = deque()

for i in range(1, n + 1):
  if indegree[i] == 0:
    q.append(i)
    result.append(i)
while q:
  now = q.popleft()

  for next in edges[now]:
    indegree[next] -= 1
    
    if indegree[next] == 0:
      q.append(next)
      result.append(next)

print(*result)