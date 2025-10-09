from collections import defaultdict

n = int(input())
dd = defaultdict(int)
coord = list(map(int, input().split()))
s_coord = sorted(list(set(coord)))

for i in range(len(s_coord)):
  dd[s_coord[i]] = i

for c in coord:
  print(dd[c], end=' ')

