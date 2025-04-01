n = int(input())
graph = [[] for _ in range(n ** 2 + 1)]
board = [[[] for _ in range(n)] for _ in range(n)]
student = [list(map(int, input().split())) for _ in range(n ** 2)]
student_order = []
for s in student:
    student_order.append(s[0])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in student:
    for j in i[1:]:
        graph[i[0]].append(j)

def check_near_fav(i, j, s):
    temp = 0
    for d in range(4):
        nx, ny = i + dx[d], j + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[nx][ny] in graph[s]:
            temp += 1
    return temp

def check_empty(i, j):
    temp = 0
    for d in range(4):
        nx, ny = i + dx[d], j + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[i][j] == []:
            temp += 1
    return temp

def check_one(s):
    max_s = -1
    max_idx = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == []:
                max_s = max(max_s, check_near_fav(i, j, s))
    if max_s == -1:
        return max_idx
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == []:
                temp = check_near_fav(i, j, s)
                if temp == max_s:
                    max_idx.append((i, j))
    return max_idx

def check_two(check_one_res, s):
    max_empty_near = -1
    max_block = []
    for i, j in check_one_res:
        max_empty_near = max(check_empty(i, j), max_empty_near)
    for i, j in check_one_res:
        temp = check_empty(i, j)
        if temp == max_empty_near:
            max_block.append([i, j])

    return max_block

for s in student_order:
    check_one_res = check_one(s)
    if len(check_one_res) == 0:
        for i in range(n):
            for j in range(n):
                check_one_res.append((i, j))
    if len(check_one_res) >= 2:
        check_two_res = check_two(check_one_res, s)
        check_two_res.sort()
        x, y = check_two_res[0][0], check_two_res[0][1]
        board[x][y] = s
    else:
        i, j = check_one_res[0]
        board[i][j] = s


print(board)