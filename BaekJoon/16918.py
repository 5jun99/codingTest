from collections import deque

r, c, n = map(int, input().split())

board = [list(input()) for _ in range(r)]
q = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(q, board):
            while q:
                x, y = q.pop()
                board[x][y] = '.'
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c or board[nx][ny] =='.':
                        continue
                    board[nx][ny] = '.'

def execute(t):
    global board, q
    if t == 1:
        for row in range(r):
            for col in range(c):
                if board[row][col] == "O":
                    q.append((row, col))
    elif t % 2 == 1:
        bfs(q, board)
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    q.append((i,j))
    else:
        board = [['O']*c for _ in range(r)]

for i in range(1, n + 1):
     execute(i)

for i in board:
    print(''.join(i))