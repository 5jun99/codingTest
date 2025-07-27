n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
b = 0
w = 0
def check(x, y, n):
    global b, w

    start = board[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if (start + 1) % 2 == board[i][j]:
                check(x, y, n // 2)
                check(x + n // 2, y, n // 2)
                check(x, y + n // 2, n // 2)
                check(x + n // 2, y + n // 2, n // 2)
                return

    if start == 1:
        b += 1
    else:
        w += 1

check(0, 0, n)
print(w)
print(b)
