s = int(input())
dp = [i for i in range(1001)]
dp[0] = 0

for i in range(2, 1001):
    for j in range(1, 1000 // i + 1):
        dp[i * j] = min(dp[i] + j, dp[i * j])
        dp[i * j - 1] = min(dp[i * j - 1], dp[i * j] + 1)


# for i in range(2, s + 1):
#     dp[i] = i
#     min_dp = 1001
#     for j in range(i - 1, 1, -1):
#         if i % j == 0:
#             min_dp = min(min_dp, dp[j] + i // j)
#     if min_dp == 1001:
#         dp[i] = i
#     else:
#         dp[i] = min_dp
#         dp[i - 1] = min(min_dp + 1, dp[i - 1])
print(dp[s])