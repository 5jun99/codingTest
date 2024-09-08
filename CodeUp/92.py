n = int(input())

rand_nums = map(int, input().split())
num_list = [0 for _ in range(23)]
for i in rand_nums:
    num_list[i - 1] += 1

for i in num_list:
    print(i, end=" ")