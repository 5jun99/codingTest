n = int(input())

road = list(map(int, input().split()))

oil_price = list(map(int, input().split()))

dp = [[int(1e9), oil_price[i]] for i in range(n)]
dp[0][0] = 0

for i in range(1, n):
  if oil_price[i - 1] > dp[i - 1][1]:
    dp[i][0] = dp[i-1][0] + road[i-1] * dp[i - 1][1]
    dp[i][1] = dp[i - 1][1]
  else:
    dp[i][0] = dp[i - 1][0] + road[i -1] * oil_price[i - 1]
    dp[i][1] = oil_price[i - 1]

print(dp[-1][0])