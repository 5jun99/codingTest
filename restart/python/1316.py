from collections import defaultdict

n = int(input())

answer = 0

for _ in range(n):
  dd = defaultdict(int)
  word = input()
  flag = True
  for i in range(len(word)):
    if i == 0:
      dd[word[i]] += 1
      continue

    if dd[word[i]] != 0 and word[i] != word[i - 1]:
      flag = False
      break
    dd[word[i]] += 1
  if flag:
    answer += 1

print(answer)