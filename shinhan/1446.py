from collections import deque
n, d = map(int, input().split())

shortcuts = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [0] + [i for i in range(1, d + 1)]
now = 0
run = 0
for ss, se, dist in shortcuts:
    if se > d:
        continue
    if dp[ss] + dist < dp[se]:
        dp[se] = dp[ss] + dist
        for i in range(se, d + 1):
            dp[i] = min(dp[se] + (i - se), dp[i])

print(dp[d])
