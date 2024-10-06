import sys
input = sys.stdin.readline
N = int(input())
works = [list(map(int, input().split())) for _ in range(N)]
dp = [w[1] for w in works]
for i in range(1, N):
    if works[i][0] + i > N:
        dp[i] = 0
        continue
    for j in range(i + 1):
        if works[j][0] + j <= i:
            dp[i] = max(dp[i], dp[j] + works[i][1])
            # print(i, j, dp[i], dp[j])
    # dp[i] = max(dp[i], works[i][1])      
print(max(dp))


