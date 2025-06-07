from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
numbers = list(map(int, input().split()))

d = [0] * n

d[0] = numbers[0]
dq = deque()

for i in range(n):
    while dq and dq[-1][0] > numbers[i]:
        dq.pop()

    dq.append((numbers[i], i))

    while dq[0][1] < i - l + 1:
        dq.popleft()

    d[i] = dq[0][0]

print(*d)