n = int(input())

numbers = list(map(int, input().split()))

if (max(numbers)) <= 0:
  print(max(numbers))
else:
  dp = [-1001] * 100001
  dp[0] = numbers[0]
  for i in range(1, n):
    dp[i] = max(dp[i - 1] + numbers[i], numbers[i])

  print(max(dp[:n]))

  