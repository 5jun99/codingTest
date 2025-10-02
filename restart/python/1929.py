m, n = map(int, input().split())

for i in range(m, n + 1):
  flag = True
  for j in range(2, int(i ** (1/2)) + 1):
    if i % j == 0:
      flag = False
  if flag:
    print(i)