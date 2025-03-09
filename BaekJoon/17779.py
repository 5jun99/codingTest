n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

answer = []
def check(d1, d2, x, y):
    jaehyunsi = [0] * 5
    area = [[0] * n for _ in range(n)]

    for i in range(d1 + 1):
        area[x + i][y - i] = 5
        area[x + d2 + i][y + d2 - i] = 5 
    for i in range(d2 + 1):
        area[x + i][y + i] = 5 
        area[x + d1 + i][y - d1 + i] = 5

    for r in range(x + 1, x + d1 + d2):
        fill = False
        for c in range(n):
            if area[r][c] == 5:
                fill = not fill
            if fill:
                area[r][c] = 5

    for r in range(n):
        for c in range(n):
            if area[r][c] == 5:
                continue
            if 0 <= r < x + d1 and 0 <= c <= y:
                area[r][c] = 1
            elif 0 <= r <= x + d2 and y < c < n:
                area[r][c] = 2
            elif x + d1 <= r < n and 0 <= c < y - d1 + d2:
                area[r][c] = 3
            elif x + d2 < r < n and y - d1 + d2 <= c < n:
                area[r][c] = 4

    for r in range(n):
        for c in range(n):
            jaehyunsi[area[r][c] - 1] += board[r][c]

    # for r in range(x + d1):
    #     for c in range(y + 1 - r):
    #         jaehyunsi[0] += board[r][c]
    #         visited.append((r,c))
    # for r in range(x + d2 + 1):
    #     for c in range(y + 1 + r, n):
    #         jaehyunsi[1] += board[r][c]
    #         visited.append((r,c))
    # for r in range(x + d1 - 1, n):
    #     for c in range(y - d1 + d2 - 2 + r):
    #         jaehyunsi[2] += board[r][c]
    #         visited.append((r,c))
    # for r in range(x + d2, n):
    #     for c in range(y - d1 + d2 - 1, n):
    #         jaehyunsi[3] += board[r][c]
    #         visited.append((r,c))
    
    # for r in range(n):
    #     for c in range(n):
    #         if (r, c) not in visited:
    #             jaehyunsi[4] += board[r][c]

    return max(jaehyunsi) - min(jaehyunsi)
         

for d1 in range(1, n - 1):
    for d2 in range(1, n - 1 - d1):
        for x in range(1, n - 1 - d1 - d2):
            for y in range(2, n - 1 - d2):
                answer.append(check(d1, d2, x, y))

print(min(answer))


