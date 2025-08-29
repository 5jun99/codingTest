import heapq
import sys
input = sys.stdin.readline
n = int(input())
X = []
for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        if X:
            print(-1 * heapq.heappop(X))
        else:
            print(0)
    else:
        heapq.heappush(X, -1 * tmp)

