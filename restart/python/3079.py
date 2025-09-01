n, m = map(int, input().split())

time = [int(input()) for _ in range(n)]

lo = 0

hi = m * max(time)
answ = hi + 1
while lo <= hi:
  mid = (lo + hi) // 2

  curr = 0
  for ti in time:
    curr += mid // ti
  if curr >= m:
    answ = min(answ, mid)
    hi = mid - 1
  else:
    lo = mid + 1

print(answ)