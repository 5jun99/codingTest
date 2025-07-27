import sys

input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    sum = 0
    mid = (start + end) // 2
    for t in trees:
        if mid < t:
            sum += t - mid

    if sum < m:
        end = mid - 1
    elif sum > m:
        start = mid + 1
    else:
        break

print(mid)