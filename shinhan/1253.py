n = int(input())

good_numbers = sorted(list(map(int, input().split())))
answer = 0
for i in range(n):
    left = 0
    right = n - 1
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        temp = good_numbers[left] + good_numbers[right]

        if temp < good_numbers[i]:
            left += 1
        elif temp == good_numbers[i]:
            answer += 1
            break
        else:
            right -= 1

print(answer)