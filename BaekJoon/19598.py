from collections import deque

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

