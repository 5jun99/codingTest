n, m = map(int, input().split())

a = list(map(int, input().split()))

dp = [0] 
curr = 0
for i in a:
  curr += i
  dp.append(curr)

for _ in range(m):
  s, e = map(int, input().split())
  print(dp[e] - dp[s - 1])
  