import sys
from collections import deque
input = sys.stdin.readline

n, m, t = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
queue = deque()
princess = True
dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = -1
def bfs():
    while queue:
        x, y, gram, time = queue.popleft()
        if time > t:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if nx == n and ny == m:
                global answer
                answer = time
                return
            if nx == n - 1 and ny == m - 1:
                queue.append((nx,ny,gram, time + 1))
            elif castle[nx][ny] == 1:
                if not gram:
                    continue
                queue.append((nx,ny,gram, time + 1))
            else:
                queue.append((nx,ny,True, time + 1))
        print(queue)

queue.append((0, 0, False, 0))

bfs()
print(answer)
        