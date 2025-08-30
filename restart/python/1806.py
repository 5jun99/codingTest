n, s = map(int, input().split())

array = list(map(int, input().split()))
min_lenth = n + 1

left = 0

current = 0

for right in range(n):
  current += array[right]

  while current >= s:
    min_lenth = min(min_lenth, right - left + 1)
    current -= array[left]
    left += 1

if min_lenth == n + 1:
  print(0)
else:
  print(min_lenth)