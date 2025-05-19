from collections import defaultdict

n = int(input())
dd = defaultdict()
left = 1
numbers = [i for i in range(1, n + 1)]
check_sum = 0
answer = 0

for right in range(1, n + 1):
    check_sum += right

    while check_sum > n:
        check_sum -= left
        left += 1

    if check_sum == n:
        answer += 1
print(answer)