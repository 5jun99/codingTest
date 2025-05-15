n = int(input())

work = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])

answer = work[0][1] - work[0][0]
fastest_last = work[0][1]
for i in range(1, n):
    if answer < 0:
        break
    if fastest_last + work[i][0] > work[i][1]:
        answer -= fastest_last + work[i][0] - work[i][1]
        fastest_last = work[i][1]
    else:
        fastest_last += work[i][0]

if answer < 0:
    print(-1)
else:
    print(answer)