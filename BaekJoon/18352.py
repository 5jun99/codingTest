from collections import deque
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distnace = [-1] * (n + 1)
distnace[x] = 0 # 자기 자신은 0

queue = deque([x])
while queue:
    now = queue.popleft()
    for i in graph[now]:
        if distnace[i] == -1:
            distnace[i] = distnace[now] + 1
            queue.append(i)

check = False
result = []
for i in range(1, n + 1):
    if distnace[i] == k:
        check = True
        print(i)

if not check:
    print(-1)