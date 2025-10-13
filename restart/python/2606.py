def find_parents(parents, x):
  if parents[x] != x:
    parents[x] = find_parents(parents, parents[x])
  
  return parents[x]

def union_parents(parents, x, y):
  xp = find_parents(parents, x)
  yp = find_parents(parents, y)

  if xp > yp:
    parents[xp] = yp
  else:
    parents[yp] = xp

n = int(input())
parents = [i for i in range(n + 1)]
m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    union_parents(parents, a, b)

for i in range(1, n + 1):
    find_parents(parents, i)

cnt = sum(1 for i in range(2, n + 1) if parents[i] == parents[1])
print(cnt)

#from collections import deque

#n = int(input())
#m = int(input())
#answer = n
#graph = [[] for _ in range(n + 1)]

#for _ in range(m):
#  s, e = map(int, input().split())
#  graph[s].append(e)
#  graph[e].append(s)


#q = deque([1])

#visited = [False] * (n + 1)

#while q:
#  now = q.popleft()

#  visited[now] = True

#  for next in graph[now]:
#    if not visited[next]:
#      q.append(next)

#for v in visited[1:]:
#  if not v:
#    answer -= 1

#print(answer - 1)