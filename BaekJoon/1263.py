n = int(input())
list_works = sorted([list(map(int, input().split())) for _ in range(n)], key= lambda x: x[1])
first_work = list_works.pop(0)
fastest_time = first_work[1] - first_work[0]
last_time = first_work[1]
for t, s in list_works:
    if fastest_time < 0:
        fastest_time = -1
        break
    if last_time + t > s:
        fastest_time -= last_time + t - s
        last_time = s
    else:
        last_time += t

print(fastest_time)