import heapq

n = int(input())
lecture = sorted([list(map(int, input().split())) for _ in range(n)])
lecture_num = 0
lecture_time = []
for start, end in lecture:
    if not lecture_time:
        lecture_time.append(end)
        continue
    if start < lecture_time[0]:
        heapq.heappush(lecture_time, end)
    else:
        heapq.heappop(lecture_time)
        heapq.heappush(lecture_time, end)


print(lecture_time)

