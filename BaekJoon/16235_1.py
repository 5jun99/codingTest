n, m, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]

trees = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, a = map(int, input().split())
    trees[x-1][y-1].append(a)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

eat = [[5] * n for _ in range(n)]

for _ in range(k):

    for i in range(n):
        for j in range(n):
            if not trees[i][j]: 
                continue
            trees[i][j].sort()
            alive_trees = []
            dead_feed = 0
            for a in trees[i][j]:
                if eat[i][j] < a:
                    dead_feed += a // 2
                else:
                    eat[i][j] -= a 
                    alive_trees.append(a + 1) 

            trees[i][j] = alive_trees
            eat[i][j] += dead_feed

    for x in range(n):
        for y in range(n):
            if not trees[x][y]:
                continue
            for age in trees[x][y]:
                if age % 5 == 0:
                    for d in range(8):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            trees[nx][ny].append(1)

    for i in range(n):
        for j in range(n):
            eat[i][j] += A[i][j]

result = sum(len(trees[x][y]) for x in range(n) for y in range(n))
print(result)
