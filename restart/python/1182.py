n, s = map(int, input().split())

numbers = list(map(int, input().split()))
answer = 0
def search(idx, sum):
  global answer
  if sum + numbers[idx] == s:
    answer += 1
  if idx == n - 1:
    return
  search(idx + 1, sum) 
  search(idx + 1, sum + numbers[idx])

search(0, 0)
print(answer) 