from collections import defaultdict

n = int(input())
dd = defaultdict(int)

x = list(map(int, input().split()))
x_set = list(set(x))

x_sort = sorted(x_set)


for i in range(len(x_sort)):
    dd[x_sort[i]] = i

for i in x:
    print(dd[i], end=' ')



