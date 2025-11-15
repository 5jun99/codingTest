n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]

bags = [list(map(int, input().split())) for _ in range(n)]

#for i in range(1, n + 1):
#  w, v = bags[i - 1]

#  for weight in range(1, k + 1):
#    if weight >= w:
#      dp[i][weight] = max(dp[i - 1][weight], v + dp[i - 1][weight - w])
#    else:
#      dp[i][weight] = dp[i - 1][weight]

#print(dp[n][k])


#n, k = map(int, input().split())

#dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, k + 1):
    if bags[i-1][0] <= j:
      dp[i][j] = max(dp[i-1][j], bags[i-1][1] + dp[i][j-bags[i-1][0]])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[-1][-1])















