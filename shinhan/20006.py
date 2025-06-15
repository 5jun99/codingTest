p, m = map(int, input().split())

rooms = []

for _ in range(p):
    level, nickname = input().split()
    level = int(level)
    flag = False
    for i in range(len(rooms)):
        if abs(rooms[i][0] - level) <= 10 and len(rooms[i][1]) < m:
            flag = True
            rooms[i][1].append((nickname, level))
            break
    if not flag:
        rooms.append([level, [(nickname, level)]])

for level, members in rooms:
    members.sort()
    if len(members) == m:
        print("Started!")
    else:
        print("Waiting!")
    for member_nickname, member_level in members:
        print(member_level, member_nickname)

