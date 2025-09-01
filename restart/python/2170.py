import sys
input = sys.stdin.readline
n = int(input())

edges = sorted([list(map(int, input().split())) for _ in range(n)])

left = -1e9 - 1
right = -1e9 - 1
ans = 0
for s, e in edges:
  if s > right: 
    ans += e - s
    left = s
    right = e
  elif e > right:
    ans += e - right
    right = e

print(ans)