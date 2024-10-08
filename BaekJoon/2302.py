import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
vip = [int(sys.stdin.readline()) for _ in range(m)]

if n == 1:
    print(1)
else:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer = 1
    if m >= 1:
        pivot_vip = 0
        for i in range(m):
            answer *= dp[vip[i] - 1 - pivot_vip]
            pivot_vip = vip[i]
        answer *= dp[n-pivot_vip]
    else:
        print(dp[-1])

    print(answer)