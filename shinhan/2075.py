import heapq

n = int(input())
hq = []

for _ in range(n):
    for num in map(int, input().split()):
        heapq.heappush(hq, num)
        if len(hq) > n:
            heapq.heappop(hq)

print(hq[0])