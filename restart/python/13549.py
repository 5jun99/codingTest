from collections import deque
import heapq

N, K = map(int, input().split())

visited = [False] * (100001)
q = deque([(0, N)])

result = []
while q:
  time, now = q.popleft()
  
  visited[now] = True
  
  if now == K:
    result.append(time)
    continue

  for idx, nx in enumerate([now - 1, now + 1, now * 2]):
    if nx < 0 or nx > 100000 or visited[nx]:
      continue
    if idx == 2:
      q.append((time, nx))
    else:
      q.append((time + 1, nx))

print(min(result))
      

