from collections import deque

def bfs(sx, sy, board, state):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(board)
    q = deque([(sx, sy)])
    blocks = []
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()
        blocks.append((x, y))
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if board[nx][ny] == state:
              q.append((nx, ny))
              visited[nx][ny] = True

    return blocks

def solution(game_board, table):
    answer = -1
    n = len(game_board)
    visited = [[False] * n for _ in range(n)]
    blanks = []
    blocks = []
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if game_board[i][j] != 0:
                visited[i][j] = True
                continue
            
            blank = bfs(i, j, game_board, 0)
              
            if not blank:
                continue
            for x, y in blank:
                visited[x][y] = True
            blanks.append(blank)
            
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if table[i][j] != 1:
                visited[i][j] = True
                continue
            
            block = bfs(i, j, table, 1)
              
            if not block:
                continue
            for x, y in block:
                visited[x][y] = True
      
            blocks.append(block)
    
    return blocks
