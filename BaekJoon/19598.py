import heapq

# n = int(input())
# lecture = sorted([list(map(int, input().split())) for _ in range(n)])

# lecture_room = []

# for start, end in lecture:
#     if not lecture_room:
#         lecture_room.append([start,end])
#         continue
#     flag = 0
#     for i in lecture_room:
#         if i[1] <= start:
#             i[0] = start
#             i[1] = end
#             flag = 1
#             break
#     if not flag:
#         lecture_room.append([start, end])
# print(len(lecture_room))
# 시간 초과

# n = int(input())
# lecture = sorted([list(map(int, input().split())) for _ in range(n)])
# lecture_num = 0
# lecture_time = deque()
# for start, end in lecture:
#     if not lecture_time:
#         lecture_time.append(end)
#         continue
#     if start > lecture_time[0]:
#         lecture_time.appendleft(end)
#     else:
#         lecture_time.popleft()
#         lecture_time.appendleft(end)

# print(len(lecture_time))

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