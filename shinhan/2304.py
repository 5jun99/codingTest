n = int(input())

pillar = sorted([list(map(int, input().split())) for _ in range(n)])

area = 0

max_index = 0

for i in range(1, n):
    if pillar[i][1] > pillar[max_index][1]:
        max_index = i

left = 0
for i in range(1, max_index + 1):
    if pillar[left][1] < pillar[i][1]:
        area += (pillar[i][0] - pillar[left][0]) * pillar[left][1]
        left = i

right = n - 1

for i in range(n - 2, max_index - 1, -1):
    if pillar[right][1] < pillar[i][1]:
        area += (pillar[right][0] - pillar[i][0]) * pillar[right][1]
        right = i

area += pillar[max_index][1]

print(area)

# last = 0
#
# while True:
#     flag = False
#     max_p = last + 1
#     next_p = 0
#
#     for i in range(last + 1, n):
#         if pillar[last][1] <= pillar[i][1]:
#             flag = True
#             next_p = i
#             break
#         if pillar[max_p][1] < pillar[i][1]:
#             max_p = i
#
#     if not flag:
#         area += pillar[last][1]
#
#         if last == n - 1:
#             break
#         area += (pillar[max_p][0] - (pillar[last][0] + 1)) * pillar[max_p][1]
#
#         if max_p == n - 1:
#             area += pillar[-1][1]
#             break
#
#         last = max_p
#     else:
#         area += (pillar[next_p][0] - pillar[last][0]) * pillar[last][1]
#         last = next_p
#
# print(area)

n = int(input())
pillar = sorted([list(map(int, input().split())) for _ in range(n)])

max_idx = -1
max_h = -1
area = 0
for i in range(n):
    if max_h < pillar[i][1]:
        max_idx = i
        max_h = pillar[i][1]

left = 0

for i in range(i, max_idx + 1):
    if pillar[i][1] > pillar[left][1]:
        area += (pillar[i][0] - pillar[left][0]) * pillar[left][1]
        left = i  

right = n - 1

for i in range(n - 2, max_idx - 1, -1):
    if pillar[i][1] > pillar[right][1]:
        area += (pillar[right][0] - pillar[i][0]) * pillar[right][1]
        right = i

area += max_h
print(area)