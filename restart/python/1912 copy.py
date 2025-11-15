n = int(input())

numbers = list(map(int, input().split()))

dp = [0] * n

if max(numbers) <= 0:
  print(max(numbers))
else:
  for i in range(n):
    dp[i] = max(dp[i], numbers[i] + dp[i - 1])

  print(max(dp))