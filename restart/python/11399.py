n = int(input())

people = sorted(list(map(int, input().split())))

answer = 0
temp = 0
for p in people:
  temp += p
  answer += temp

print(answer)

