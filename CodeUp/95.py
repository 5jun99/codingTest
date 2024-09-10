n = int(input())

badookdol = [list(map(int, input().split())) for _ in range(n)]

for row in range(19):
    for col in range(19):
        if [row + 1, col + 1] in badookdol:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

