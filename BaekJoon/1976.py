n = int(input())
m = int(input())


parents = [i for i in range(n)]

def find_parent(x):
    if x == parents[x]:
        return x
    parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(x, y):
    x= find_parent(x)
    y = find_parent(y)

    if x > y:
        parents[x] = y
    else:
        parents[y] = x


for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            union_parent(i, j)

travel = list(map(int, input().split()))

parent = parents[travel[0] - 1]

flag = True
for i in range(1, len(travel)):
    if parent != parents[travel[i] - 1]:
        flag = False
        break

if flag:
    print('YES')
else:
    print("NO")