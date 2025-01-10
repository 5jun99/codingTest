n = int(input())
works = sorted([list(map(int, input().split())) for _ in range(n)], key= lambda x: x[1])
lastest = works[0][1] - works[0][0]
now = works[0][1]
works.pop(0)

for work in works:
    if lastest < 0:
        lastest = -1
        break
    if now + work[0] > work[1]:
        lastest -= now + work[0] - work[1]
        now = work[1]
    else:
        now += work[0]


print(lastest)