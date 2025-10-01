n = int(input())

left = 0
answer = 0
tmp_sum = 0
for right in range(n + 1):
  tmp_sum += right

  while tmp_sum > n:
    tmp_sum -= left
    left += 1
  
  if tmp_sum == n:
    answer += 1

print(answer)
