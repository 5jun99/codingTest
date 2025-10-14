t = int(input())
dp = [0] * 11
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 11):
  for j in range(1, 4):
    dp[i] += dp[i - j]

for _ in range(t):
  print(dp[int(input())])
