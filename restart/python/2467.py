n = int(input())

liquid = list(map(int, input().split()))

left = 0
right = n - 1

check = 2 * int(1e9)
answer = (0, 0)
while left < right:
  if abs(liquid[left] + liquid[right]) < check:
    answer = (left, right)
    check = abs(liquid[left] + liquid[right])

  if liquid[left] + liquid[right] < 0:
    left += 1
  else:
    right -= 1
x, y = answer
print(liquid[x], liquid[y])






