n, h = map(int, input().split())

at = []
ab = []
for i in range(n):
  if i % 2:
    at.append(int(input()))
  else:
    ab.append(int(input()))
  
ab.sort(reverse=True)
at.sort(reverse=True)

for i in range(1, h + 1):
  


#for i in range(1, h + 1):
#  cnt = 0
#  for j in range(n):
#    if (j % 2 == 0 and a[j] >= i) or (j % 2 == 1 and h - a[j] < i):
#      cnt += 1
#  res.append(cnt)

#min_cnt = min(res)

#for i in res:
#  if i == min_cnt:
#    ans += 1

#print(min_cnt, ans)