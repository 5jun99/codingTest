n, c = map(int, input().split())

house = sorted([int(input()) for _ in range(n)])

low = 1
high = house[-1] - house[0]
answer = -1

def can(mid):
  last = house[0]
  cnt = 1
  for i in range(1, n):
    if house[i] - last >= mid:
      cnt += 1
      last = house[i]
  return cnt >= c

while low <= high:
  mid = (low + high) // 2
  if can(mid):
    answer = mid
    low = mid + 1
  else:
    high = mid - 1

print(answer)