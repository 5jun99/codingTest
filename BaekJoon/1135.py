n = int(input())

input_ = list(map(int, input().split()))
tree = [[] for _ in range(n)]
for i in range(1, n):
    tree[input_[i]].append(i)


def dfs(node):
    if len(tree[node]) == 0:
        return 0
    result = []
    for child in tree[node]:
        result.append(dfs(child))
    result.sort(reverse=True)
    result = [result[i] + i + 1 for i in range(len(result))]
    return max(result)

print(dfs())
# burden = [0] * n

# def findChileNum(node):
#     next = [node]
#     child = -1
#     while next:
#         temp = []
#         for c in next:
#             child += 1
#             temp += tree[c]
#         next = temp
#     return child

# def initiate():
#     for i in range(n):
#         burden[i] = findChileNum(i)
# initiate()




        
