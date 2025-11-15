n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))
dp = [[int(1e9), oil[i]] for i in range(n)]
min_price = oil[0]

result = oil[0] * road[0]

for i in range(1, n - 1):
  min_price = min(min_price, oil[i])
  result += min_price * road[i]
  print(min_price, result)
print(result)

