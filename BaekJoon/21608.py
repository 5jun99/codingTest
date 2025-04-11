n = int(input())
graph = [[] for _ in range(n ** 2 + 1)]
board = [[-1 for _ in range(n)] for _ in range(n)]
student = [list(map(int, input().split())) for _ in range(n ** 2)]
student_order = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for s in student:
    student_order.append(s[0])
    for ss in s[1:]:
        graph[s[0]].append(ss)

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
        if board[nx][ny] == -1:
            temp += 1
    return temp

def check_one(s):
    max_s = -1
    max_idx = []

    for i in range(n):
        for j in range(n):
            if board[i][j] != -1:
                continue

            score = check_near_fav(i, j, s)

            if score > max_s:
                max_s = score
                max_idx = [(i, j)]
            elif score == max_s:
                max_idx.append((i, j))

    return max_idx if max_s > 0 else []

def check_two(check_one_res, s):
    max_empty_near = -1
    max_block = []
    for i, j in check_one_res:
        max_empty_near = max(check_empty(i, j), max_empty_near)
    for i, j in check_one_res:
        if check_empty(i, j) == max_empty_near:
            max_block.append([i, j])

    return max_block

for s in student_order:
    check_one_res = check_one(s)

    if len(check_one_res) == 0: 
        for i in range(n):
            for j in range(n):
                if board[i][j] == -1:
                    check_one_res.append((i, j))
    if len(check_one_res) >= 2:
        check_two_res = check_two(check_one_res, s)
        check_two_res.sort()
        x, y = check_two_res[0][0], check_two_res[0][1]
        board[x][y] = s
    else:
        i, j = check_one_res[0]
        board[i][j] = s


answer = 0

satisfy = [0, 1, 10, 100, 1000]

for i in range(n):
    for j in range(n):
        now_student = board[i][j]
        answer += satisfy[check_near_fav(i, j, now_student)]

print(answer)