n, m, b = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
answer = []

for h in range(257):
    time = 0
    b_tmp = b
    for i in range(n):
        for j in range(m):
            diff = board[i][j] - h
            if diff > 0:  # 블록 파기
                time += 2 * diff
                b_tmp += diff
            elif diff < 0:  # 블록 쌓기
                time += -diff
                b_tmp += diff  # b_tmp -= (-diff)
    if b_tmp >= 0:
        answer.append((time, h))

# print(answer)
print(*sorted(answer, key=lambda x: (x[0], -x[1]))[0])
