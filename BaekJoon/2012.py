n = int(input())

expected_rank = sorted([int(input()) for _ in range(n)])

boolman = 0

for i in range(n):
    boolman += abs(expected_rank[i] - (i +1))

print(boolman)