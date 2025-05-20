from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
answer = []

def bfs(start):
    q = deque()

    q.append((start, 0))
    visited[start] = True

    while q:
        now, time = q.popleft()
        if now == k:
            answer.append(time)
            continue

        for next_pos in [now - 1, now + 1, now * 2]:
            if next_pos < 0 or next_pos > 100000 or visited[next_pos]:
                continue
            visited[now] = True
            q.append((next_pos, time + 1))
bfs(n)
print(min(answer))
print(answer.count(min(answer)))




