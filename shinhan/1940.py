n = int(input())
m = int(input())

numbers = sorted(list(map(int, input().split())))
left = 0
right = n - 1
answer = 0

while left < right:
    check_sum = numbers[left] + numbers[right]
    if check_sum == m:
        answer += 1
        left += 1
    elif check_sum < m:
        left += 1
    else:
        right -= 1
print(answer)