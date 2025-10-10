from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  s, l = map(int, input().split())
  graph[s].append(l)
  indegree[l] += 1

q = deque([])

for i in range(1, n + 1):
  if indegree[i] == 0:
    q.append(i)

answer = []

while q:
  now = q.popleft()

  answer.append(now)

  for next in graph[now]:
    indegree[next] -= 1
    # 새롭게 진입차수가 0이 되면 큐에 삽입
    if indegree[next] == 0:
        q.append(next)
  
print(*answer)