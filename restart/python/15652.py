n, m = map(int, input().split())

answer = []
def dfs(path, depth):
  if depth == m:
    answer.append(path)
    return
  start = 1
  if path:
    start = path[-1]
  for i in range(start, n + 1):
    dfs(path + [i], depth + 1)

dfs([], 0)

for a in answer:
  print(*a)