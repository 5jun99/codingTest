from collections import defaultdict

n, k = map(int, input().split())

a = list(map(int, input().split()))
dd = defaultdict(int)
left = 0
ans = 0

for right in range(n):
  dd[a[right]] += 1
  
  while dd[a[right]] > k:
    dd[a[left]] -= 1
    left += 1
  
  ans = max(ans, right - left + 1)

print(ans)
