n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]

bags = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n + 1):
  w, v = bags[i - 1]

  for weight in range(1, k + 1):
    if weight >= w:
      dp[i][weight] = max(dp[i - 1][weight], v + dp[i - 1][weight - w])
    else:
      dp[i][weight] = dp[i - 1][weight]

print(dp[n][k])