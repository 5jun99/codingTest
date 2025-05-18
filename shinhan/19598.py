import heapq

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]

meeting.sort(key=lambda x: x[0])

room = []

for m in meeting:
    if not room:
        room.append(m[1])
        continue
    if room[0] <= m[0]:
        heapq.heappop(room)
        heapq.heappush(room, m[1])
    else:
        heapq.heappush(room, m[1])
print(len(room))