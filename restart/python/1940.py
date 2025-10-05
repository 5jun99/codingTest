n = int(input())
m = int(input())

armor = sorted(list(map(int, input().split())))

left = 0

right = n - 1
answer = 0

while left < right:
  check = armor[left] + armor[right]

  if check > m:
    right -= 1
  elif check < m:
    left += 1
  else:
    answer += 1
    left += 1

print(answer)
  

