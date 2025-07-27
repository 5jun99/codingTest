import heapq
import sys

input = sys.stdin.readline
output = []

n = int(input())
hq = []
for _ in range(n):
    operation = int(input())
    if operation == 0:
        output.append(str(heapq.heappop(hq)) if hq else '0')
    else:
        heapq.heappush(hq, operation)

# 한 번에 출력
print('\n'.join(output))
