from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
min_result = 100000

def bfs(start):
    q = deque()
    q.append((start, 0))
    global min_result
    while q:
        now, time = q.popleft()
        visited[now] = True

        if now == k and min_result > time:
            min_result = time
            continue
        for np in [now + 1, now - 1, now * 2]:
            if np < 0 or np > 100000 or visited[np]:
                continue
            q.append((np, time + 1))

bfs(n)

print(min_result)