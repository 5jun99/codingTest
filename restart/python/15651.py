from itertools import product

n, m = map(int, input().split())

numbers = [i for i in range(1, n + 1)]

## library
#for pr in product(numbers, repeat=m):
#  print(*pr)

result = []

def product_(depth, path):
  if depth == m:
    result.append(path)
    return
  
  for i in range(1, n + 1):
    product_(depth + 1, path + [i])

product_(0, [])

for r in result:
  print(*r)