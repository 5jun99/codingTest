n = int(input())
balls = input()
def count_moves(color, direction):
    n = len(balls)
    count = 0
    if direction == "left":
        for i in range(n):
            if balls[i] == color:
                count += 1
            else:
                break
        return balls[count:].count(color)
    else:
        for i in range(n - 1, -1, -1):
            if balls[i] == color:
                count += 1
            else:
                break
        return balls[:n - count].count(color)

print(min(
    count_moves('B', 'left'),
    count_moves('B', 'right'),
    count_moves('R', 'left'),
    count_moves('R', 'right')
))