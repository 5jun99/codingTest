n = int(input())

dp = [0] * 5001
dp[1] = int(1e9)
dp[2] = int(1e9)
dp[3] = 1
dp[4] = int(1e9)
dp[5] = 1

for i in range(6, n + 1):
  dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)

if dp[n] >= int(1e9):
  print(-1)
else:
  print(dp[n])