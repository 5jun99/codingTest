n = int(input())

liquid = sorted(list(map(int, input().split())))

left = 0
right = n - 1

res = []
while left < right:
  res.append((abs(liquid[left] + liquid[right]), liquid[left], liquid[right]))

  if abs(liquid[left]) < abs(liquid[right]):
    right -= 1
  else:
    left += 1
res.sort()

print(res[0][1], res[0][2])


