n, m, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]

trees = [[[] for _ in range(n)] for _ in range(n)]

# 나무 입력 받기 (x, y, age)
for _ in range(m):
    x, y, a = map(int, input().split())
    trees[x-1][y-1].append(a)

# 8방향 이동을 위한 dx, dy
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 초기 양분
eat = [[5] * n for _ in range(n)]


# k년 동안의 계절 변화
for _ in range(k):
    # 봄, 여름 (나무가 양분을 소비하고 자라기)
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:  # 나무가 없으면 continue
                continue
            trees[i][j].sort()  # 나무 나이를 오름차순으로 정렬
            alive_trees = []  # 살아남은 나무
            dead_feed = 0  # 죽은 나무가 남긴 양분
            for a in trees[i][j]:
                if eat[i][j] < a:  # 양분이 부족하면 나무가 죽음
                    dead_feed += a // 2  # 죽은 나무의 양분은 반으로 증가
                else:
                    eat[i][j] -= a  # 나무가 양분을 소비
                    alive_trees.append(a + 1)  # 나무가 자라면서 나이가 1 증가

            trees[i][j] = alive_trees  # 살아남은 나무들만 업데이트
            eat[i][j] += dead_feed  # 죽은 나무들이 남긴 양분을 추가

    # 가을 (나무 나이가 5의 배수이면 주변에 새로운 나무가 생김)
    for x in range(n):
        for y in range(n):
            if not trees[x][y]:  # 나무가 없으면 continue
                continue
            for age in trees[x][y]:
                if age % 5 == 0:  # 나이가 5의 배수인 나무에서 새로운 나무가 생김
                    for d in range(8):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:  # 유효한 좌표인지 확인
                            trees[nx][ny].append(1)  # 새로운 나무가 나이 1로 추가

    # 겨울 (각 칸에 양분이 추가됨)
    for i in range(n):
        for j in range(n):
            eat[i][j] += A[i][j]  # 겨울에 양분 추가

# 최종적으로 살아남은 나무의 개수를 출력
result = sum(len(trees[x][y]) for x in range(n) for y in range(n))
print(result)
