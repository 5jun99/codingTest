from collections import deque

n = int(input())
balloons = deque(enumerate(map(int, input().split()), start=1))

answer = []

while balloons:
    idx, move = balloons.popleft()
    answer.append(idx)

    if not balloons:
        break

    balloons.rotate(-(move - 1) if move > 0 else -move)

print(*answer)