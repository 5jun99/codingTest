t = int(input())
dp = [[0 ,0 ,0] for _ in range(10001)]
dp[1] = [1, 0, 0]
dp[2] = [1, 1, 0]
dp[3] = [1, 1, 1]

for _ in range(t):
    n = int(input())

    for i in range(4, n + 1):
        dp[i][0] = dp[i-3][0]
        dp[i][1] = dp[i-2][0] + dp[i-2][1]
        dp[i][2] = sum(dp[i-3])

    print(sum(dp[n]))