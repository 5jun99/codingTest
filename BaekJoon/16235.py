import heapq

n, m, k = map(int, input().split())
feed = [list(map(int, input().split())) for _ in range(n)]
board_feed = [[5] * n for _ in range(n)]
tree = []

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(m):
    x, y, z = map(int, input().split())
    heapq.heappush(tree, (z, x - 1, y - 1))

heapq.heapify(tree)

def summer(tree_dead):
    for z, x, y in tree_dead:
        board_feed[x][y] += z // 2
    
def spring():
    tree_alive = []
    tree_dead = []
    
    while tree:
        z, x, y = heapq.heappop(tree)
        
        if board_feed[x][y] < z:
            tree_dead.append((z,x,y))
        else:
            tree_alive.append((z + 1,x,y))
            board_feed[x][y] -= z

    for ta in tree_alive:
        heapq.heappush(tree, ta)
    return tree_dead


def fall():
    tree_new = []
    for z, x, y in tree:
        if z % 5 != 0:
            continue
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            tree_new.append((1, nx, ny))
    for tn in tree_new:
        heapq.heappush(tree, tn)

def winter():
    for x in range(n):
        for y in range(n):
            board_feed[x][y] += feed[x][y]

for _ in range(k):
    tree_dead = spring()
    summer(tree_dead)
    fall()
    winter()

print(len(tree))


n, m, k = map(int, input().split())
feed = [list(map(int, input().split())) for _ in range(n)]
board_feed = [[5] * n for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 초기 트리 정보 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

# 시뮬레이션 시작
for _ in range(k):
    # 봄과 여름
    for x in range(n):
        for y in range(n):
            if not trees[x][y]:
                continue
            trees[x][y].sort()  # 나이순으로 정렬
            alive_trees = []
            dead_feed = 0
            for age in trees[x][y]:
                if board_feed[x][y] >= age:
                    board_feed[x][y] -= age
                    alive_trees.append(age + 1)
                else:
                    dead_feed += age // 2
            trees[x][y] = alive_trees
            board_feed[x][y] += dead_feed

    # 가을
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

    # 겨울
    for x in range(n):
        for y in range(n):
            board_feed[x][y] += feed[x][y]

# 살아남은 나무 개수 계산
result = sum(len(trees[x][y]) for x in range(n) for y in range(n))
print(result)


