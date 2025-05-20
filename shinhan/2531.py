from collections import defaultdict
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
sushi += sushi[:k-1]

count = defaultdict(int)
unique_count = 0
max_result = 0

for i in range(k):
    if count[sushi[i]] == 0:
        unique_count += 1
    count[sushi[i]] += 1

if count[c] == 0:
    max_result = unique_count + 1
else:
    max_result = unique_count

for i in range(1, n):
    left = sushi[i - 1]
    count[left] -= 1
    if count[left] == 0:
        unique_count -= 1

    right = sushi[i + k - 1]
    if count[right] == 0:
        unique_count += 1
    count[right] += 1

    if count[c] == 0:
        max_result = max(max_result, unique_count + 1)
    else:
        max_result = max(max_result, unique_count)
print(max_result)
# max_diff = -1
# max_comb = []
#
# for i in range(n):
#     if max_diff < len(set(sushi[i:i+k])):
#         max_diff = len(set(sushi[i:i+k]))
#         max_comb = [sushi[i:i+k]]
#     elif max_diff == len(set(sushi[i:i+k])):
#         max_comb.append(sushi[i:i+k])
#
# flag = False
# for mc in max_comb:
#
#     if c not in mc:
#         flag = True
#
# if flag:
#     print(max_diff + 1)
# else:
#     print(max_diff)