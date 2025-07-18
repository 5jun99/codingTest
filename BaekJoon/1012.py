from collections import deque
t = int(input())

dx = [0 , 0, 1, -1]
dy = [1 , -1, 0, 0]

for _ in range(t):
    m, n, k = map(int, input().split())
    bae = set()
    for _ in range(k):
        x, y  = map(int, input().split())
        bae.add((y, x))
    result = 0
    while bae:
        q = deque()
        q.append(bae.pop())
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if (nx, ny) in bae:
                    bae.remove((nx, ny))
                    q.append((nx, ny))
        result += 1
    print(result)



