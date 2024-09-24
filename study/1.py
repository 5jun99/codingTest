import heapq

n = int(input())
lectures = sorted([list(map(int, input().split())) for _ in range(n)])
room_num = 0
room = []
for lecture in lectures:
    if len(room) == 0:
        room.append(lecture[1])
        continue
    if room[0] > lecture[0]:
        heapq.heappush(room, lecture[1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lecture[1])
    
print(len(room))
