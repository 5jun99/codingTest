n = int(input())

rand_nums = list(map(int, input().split()))

min_num = 10000
for i in rand_nums:
    if i < min_num:
        min_num = i

print(min_num)
