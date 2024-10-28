n = int(input())

works = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)
for i in range(1,n+1):
    if works[i][0] + i - 1 <= n:
        dp[i] = works[i][1]
    else:
        dp[i] = 0
        continue
    for j in range(1, i):
        if works[j][0] + j - 1 < i:
            dp[i] = max(dp[j] + works[i][1], dp[i])
print(max(dp))
