from collections import deque

n, k = map(int, input().split())

result = int(1e9)
visited = [False] * 100001

q = deque([(n, 0)])

while q:
  now, time = q.popleft()

  visited[now] = True

  if now == k:
    result = min(result, time)
    continue
  
  for i in [1, -1, now]:
    next = now + i
    if next <= 100000 and next >= 0 and not visited[next]:
      q.append((next, time + 1))

print(result)