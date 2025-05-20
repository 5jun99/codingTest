from collections import deque

n, k = map(int, input().split())
answer = []
visited = [False] * 100001

def bfs(start):
    q = deque()
    q.append((start, 0))
    while q:
        now, time = q.popleft()

        if now == k:
            answer.append(time)
            continue
        visited[now] = True
        for np in [now + 1, now - 1]:
            if np < 0 or np > 100000 or visited[np]:
                continue
            q.append((np, time + 1))
        if now * 2 < 0 or now * 2 > 100000 or visited[now * 2]:
            continue
        q.append((now * 2, time))
bfs(n)
print(min(answer))