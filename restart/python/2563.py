#n = int(input())

#papers = [list(map(int, input().split())) for _ in range(n)]
#answer = 0
#for i in range(n):
#  p1x, p1y = papers[i][0], papers[i][1]
#  answer += 100
#  for j in range(i):
#    p2x, p2y = papers[j][0], papers[j][1]
#    x, y = min(p1x, p2x) + 10 - max(p1x, p2x), min(p1y, p2y) + 10 - max(p1y, p2y)
#    if x > 0 and y > 0:
#      answer -= x * y
#print(answer)

n = int(input())
board = [[False] * 100 for _ in range(100)]
papers = [list(map(int, input().split())) for _ in range(n)]

for px, py in papers:
  for i in range(px, px + 10):
    for j in range(py, py + 10):
      board[i][j] = True
  
answer = 0
for i in range(100):
  for j in range(100):
    if board[i][j]:
      answer += 1

print(answer)