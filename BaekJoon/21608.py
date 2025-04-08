n = int(input())
graph = [[] for _ in range(n ** 2 + 1)]
board = [[-1 for _ in range(n)] for _ in range(n)]
student = [list(map(int, input().split())) for _ in range(n ** 2)]
student_order = []
print(student)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 학생 정보와 선호하는 학생을 연결
for s in student:
    student_order.append(s[0])
    for ss in s[1:]:
        graph[s[0]].append(ss)

# 인접한 칸에서 좋아하는 학생의 수를 셈
def check_near_fav(i, j, s):
    temp = 0
    for d in range(4):
        nx, ny = i + dx[d], j + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[nx][ny] in graph[s]:
            temp += 1
    return temp

# 빈 칸의 수를 셈
def check_empty(i, j):
    temp = 0
    for d in range(4):
        nx, ny = i + dx[d], j + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[nx][ny] == -1:
            temp += 1
    return temp

# 가장 좋아하는 학생이 인접한 빈 칸을 찾음
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

# 빈 칸 중 가장 많은 빈 칸이 있는 곳을 찾음
def check_two(check_one_res, s):
    max_empty_near = -1
    max_block = []
    
    # 최대 빈 칸이 있는 곳을 먼저 찾음
    for i, j in check_one_res:
        max_empty_near = max(check_empty(i, j), max_empty_near)
    
    # 그 빈 칸을 가지는 곳들을 찾아서 반환
    for i, j in check_one_res:
        if check_empty(i, j) == max_empty_near:
            max_block.append([i, j])

    return max_block

# 학생 배치
for s in student_order:
    check_one_res = check_one(s)
    
    if len(check_one_res) == 0:  # 가능한 자리가 없으면 그냥 빈 칸 중에서 하나를 고름
        for i in range(n):
            for j in range(n):
                if board[i][j] == -1:
                    check_one_res.append((i, j))
    
    if len(check_one_res) >= 2:  # 선택된 자리가 2개 이상이면 check_two로 추가 처리
        check_two_res = check_two(check_one_res, s)
        check_two_res.sort()  # 좌표 오름차순으로 정렬
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