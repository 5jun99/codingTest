n, m = map(int, input().split())

a = list(map(int, input().split()))

left = 0

curr = 0
ans = 0
for right in range(n):
  curr += a[right]

  while curr > m:
    curr -= a[left]
    left += 1

  if curr == m:
    ans += 1

print(ans)