import sys

input = sys.stdin.readline
n, m = map(int, input().split())

titles = []
power = []

for _ in range(n):
    t, p = input().split()
    titles.append(t)
    power.append(int(p))

from bisect import bisect_left

for _ in range(m):
    p = int(input().strip())
    idx = bisect_left(power, p)
    print(titles[idx])


# rank = [input().split() for _ in range(n)]
# abilities = enumerate([int(input().strip()) for _ in range(m)])
# abilities = sorted(abilities, key = lambda x: x[1])
# answer = []
# for idx, a in abilities:
#     flag = 0
#     for rn, ra in rank:
#         if a <= int(ra):
#             answer.append((idx, rn))
#             break
#         else:
#             flag += 1
#     for _ in range(flag):
#         rank.pop(0)
#
# answer.sort()
# for idx, rn in answer:
#     print(rn)

