n = int(input())

numbers = sorted(list(map(int, input().split())))
answer = 0
for i in range(n):
    good_num = numbers[i]
    other_num = numbers[:i] + numbers[i + 1:]

    start = 0
    end =  n - 2
    while start < end:
        if other_num[start] + other_num[end] == good_num:
            answer += 1
            break
        if other_num[start] + other_num[end] > good_num:
            end -= 1
        else:
            start += 1

print(answer)