n = int(input())
schedule = [0] * 366
inputs = [list(map(int, input().split())) for _ in range(n)]
# inputs.sort(key= lambda x:(x[0], -x[1]))

for s, e in inputs:
    for i in range(s, e + 1):
        schedule[i] += 1

# print(schedule)

lenth = 0
width = 0
answer = 0

for d in range(1, 366):
    if schedule[d] == 0:
        answer += lenth * width
        width = 0
        lenth = 0
        continue
    if schedule[d] > width:
        width = schedule[d]
    lenth += 1
    # print(d, answer)

answer += lenth * width
print(answer)