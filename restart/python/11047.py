n, k = map(int, input().split())

money = sorted([int(input()) for _ in range(n)], reverse=True)

answer = 0

for i in range(n):
  if k < money[i]:
    continue
  answer += k // money[i]
  k %= money[i]

print(answer)


