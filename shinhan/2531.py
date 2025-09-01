# from collections import defaultdict
# n, d, k, c = map(int, input().split())
# sushi = [int(input()) for _ in range(n)]
# sushi += sushi[:k-1]

# count = defaultdict(int)
# unique_count = 0
# max_result = 0

# for i in range(k):
#     if count[sushi[i]] == 0:
#         unique_count += 1
#     count[sushi[i]] += 1

# if count[c] == 0:
#     max_result = unique_count + 1
# else:
#     max_result = unique_count

# for i in range(1, n):
#     left = sushi[i - 1]
#     count[left] -= 1
#     if count[left] == 0:
#         unique_count -= 1

#     right = sushi[i + k - 1]
#     if count[right] == 0:
#         unique_count += 1
#     count[right] += 1

#     if count[c] == 0:
#         max_result = max(max_result, unique_count + 1)
#     else:
#         max_result = max(max_result, unique_count)
# print(max_result)


n, d, k, c = map(int, input().split())

sushi = list(int(input()) for _ in range(n))

sushi += sushi[:k-1]

right = k
tmp_list = sushi[:k]
max_di = len(set(tmp_list + [c]))
for i in range(1, n):
    tmp_list -= sushi[i]
    tmp_list += sushi[right]
    max_di = max(max_di, len(set(tmp_list + [c])))
    right += 1
print(max_di)