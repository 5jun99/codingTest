from collections import deque

n = int(input())
k = int(input())
snake = deque([(0, 0)])
apples = []
for _ in range(k):
    x, y = map(int, input().split())
    apples.append((x - 1, y - 1))

l =int(input())
moves = deque([list(input().split()) for _ in range(l)])

time = 0
d = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    x, y = snake[0]
    nx, ny = x + dx[d], y + dy[d]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
        time += 1
        break
    snake.appendleft((nx, ny))

    if (nx, ny) in apples:
        apples.remove((nx, ny))
    else:
        snake.pop()

    time += 1
    if moves and time == int(moves[0][0]):
        if moves[0][1] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        moves.popleft()

print(time)

