n = int(input())

triangles = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(n):
  for j in range(i + 1):
    if j == 0:
      dp[i][j] = triangles[i][j] + dp[i-1][0]
    elif j == i:
      dp[i][j] = triangles[i][j] + dp[i-1][j-1]
    else:
      dp[i][j] = triangles[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))