import heapq

n, m, k = map(int, input().split())
board_feed = [list(map(int, input().split())) for _ in range(n)]
tree = []

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(m):
    y, x, z = map(int, input().split())
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

for _ in range(k):
    tree_dead = spring()
    summer(tree_dead)
    fall()

print(len(tree))
