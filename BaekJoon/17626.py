N = int(input())

dp = [int(1e9) for _ in range(50001)]
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, N + 1):
    j = 1
    while j ** 2 <= i:
        dp[i] = min(dp[i-j**2] + 1, dp[i])
        j += 1

print(dp[N])