n, k = map(int, input().split())
cases = sorted([list(map(int, input().split())) for _ in range(n)])

dp = [[0, 0] for _ in range(n)]
# dp.append([0, 0])
for i in range(n):
    for j in range(n):
        tmp = dp[j][0] + cases[i][0]
        if (tmp <= k) & (dp[i][1] < dp[j][1] + cases[i][1]):
            dp[i][0] = tmp
            dp[i][1] = dp[j][1] + cases[i][1]

print(max(dp, key=lambda x: x[1])[1])
            