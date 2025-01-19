n = int(input())
count = int(input())

recommend = list(map(int, input().split()))
remain = dict()

for r in recommend:
    if r in remain:
        remain[r] += 1
    elif len(remain) == n:
        min_key = min(remain, key=remain.get)
        del remain[min_key]
        remain[r] = 1
    else:
        remain[r] = 1

sorted_remain = sorted(remain.keys())
for sr in sorted_remain:
    print(sr, end=' ')