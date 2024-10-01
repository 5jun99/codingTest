import sys
input = sys.stdin.readline
INF = 999999999
N = int(input())
A = list(map(int, input().split()))

dp = [0] + [INF] * (N - 1)

for i in range(1, N):
    for j in range(i):
        k = max((i - j) * (1 + abs(A[i] - A[j])), dp[j])
        dp[i] = min(dp[i], k)

print(dp[-1])