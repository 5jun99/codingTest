import sys
from collections import deque
input = sys.stdin.readline

n,m,t = map(int,input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    queue = deque()
    gram = 10001
    queue.append((0,0))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        if (x, y) == (n -1, m - 1):
                return min(gram, visited[x][y] - 1)
        if board[x][y] == 2:
            gram = visited[x][y] - 1 + n - 1 - x + m - 1 - y
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if (nx < 0 or nx >= n or ny < 0 or ny >= m) or visited[nx][ny]> 0 :
                continue
            if board[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return gram

result = bfs()

if result > t:
    print("Fail")
else:
    print(result)