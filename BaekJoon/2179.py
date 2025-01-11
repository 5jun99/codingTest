

# answer = int(1e9)
# def dfs(x, y, time):
#     global answer
#     if x >= n or x < 0 or y >= m or y < 0:
#         return
#     if visited[x][y] or miro[x][y] == 0:
#         return
    
#     if x == n - 1 and y == m - 1:
#         answer = min(time, answer)
#         return
#     visited[x][y] = True
    
#     dfs(x + 1, y, time + 1)
#     dfs(x, y + 1, time + 1)
#     dfs(x, y - 1, time + 1)
#     dfs(x - 1, y, time + 1)
    
#     visited[x][y] = False

# dfs(0, 0, 1)

# print(answer)


from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque([(0,0)])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if miro[nx][ny] == 0:
                continue
            if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return

bfs()

print(visited[-1][-1])
