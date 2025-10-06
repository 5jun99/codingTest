n = int(input())

works = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * n

for i in range(n):
  if works[i][0] + i <= n:
    dp[i] = works[i][1]
  else:
    continue
  for j in range(i):
    if works[j][0] + j <= i:
      dp[i] = max(dp[i], dp[j] + works[i][1])
  
print(max(dp))