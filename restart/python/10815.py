n = int(input())

hcard = sorted(list(map(int, input().split())))

m = int(input())
qcard = list(map(int, input().split()))

def binary(s, e, a):
  
  m = (s + e) // 2
  
  if hcard[m] == a:
    return 1
  
  if s >= e:
    return 0
  
  if hcard[m] > a:
    return binary(s, m - 1, a)
  else:
    return binary(m + 1, e, a)

answer = []
for q in qcard:
  answer.append(binary(0, n - 1, q))

print(*answer)
