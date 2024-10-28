n = int(input())

works = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])

lastest_time = works[0][1] - works[0][0]
now_time = works[0][1]

for i in range(1, n):
    if lastest_time < 0:
        lastest_time = -1
        break
    if now_time + works[i][0] > works[i][1]:
        lastest_time -= now_time + works[i][0] - works[i][1]
        now_time = works[i][1]
    else:
        now_time += works[i][0]

print(lastest_time)


n = int(input())

rank = sorted([int(input()) for _ in range(n)])
unsatisfy = 0
for i in range(n):
    unsatisfy += abs(rank[i] - (i +1))

print(unsatisfy)


n = int(input())
works = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * n
for i in range(n):
    if works[i][0] + i <= n: ## 할 수 있으면
        dp[i] = works[i][1]
    else:
        continue
    for j in range(i):
        if works[j][0] + j <= i: # 할 수 있을때
            dp[i] = max(dp[j] + works[i][1], dp[i])
print(max(dp))