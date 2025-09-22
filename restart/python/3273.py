n = int(input())

a = sorted(list(map(int, input().split())))

x = int(input())

left = 0
right = n - 1

ans = 0

while left < right:
  curr = a[left] + a[right]
  if curr > x:
    right -= 1
  elif curr == x:
    ans += 1
    left += 1
    right -= 1
  else:
    left += 1

print(ans)