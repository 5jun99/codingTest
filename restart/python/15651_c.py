n, m = map(int, input().split())
answer = []
def dfs(path, depth):
  if depth == m:
    answer.append(path)
    return
  
  for i in range(1, n + 1):
    dfs(path + [i], depth + 1)

dfs([], 0)

print(answer)