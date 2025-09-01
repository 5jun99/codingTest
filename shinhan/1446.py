# from collections import deque
# n, d = map(int, input().split())

# shortcuts = sorted([list(map(int, input().split())) for _ in range(n)])
# dp = [0] + [i for i in range(1, d + 1)]
# now = 0
# run = 0
# for ss, se, dist in shortcuts:
#     if se > d:
#         continue
#     if dp[ss] + dist < dp[se]:
#         dp[se] = dp[ss] + dist
#         for i in range(se, d + 1):
#             dp[i] = min(dp[se] + (i - se), dp[i])

# print(dp[d])


n, d = map(int, input().split())

shortcuts = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [i for i in range(d + 1)]
for start, end, dist in shortcuts:
    if end > d:
        continue
    dp[end] = min(dp[end], dp[start] + dist)
    for n in range(end + 1, d + 1):
        dp[n] = min(dp[n], dp[end] + n - end)

print(dp[-1])
