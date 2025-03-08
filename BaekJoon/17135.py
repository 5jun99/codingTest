from itertools import combinations

n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = []

def find_shortest(enemies, c):
    valid_targets = []
    for x, y in enemies:
        cost = abs(c - y) + abs(n - x)
        if cost <= d:
            valid_targets.append((cost, y, x, (x, y)))  # (거리, 왼쪽, 위쪽, 좌표)

    if valid_targets:
        valid_targets.sort()  # 거리 -> 왼쪽 -> 위쪽 순으로 정렬
        return valid_targets[0][3]  # 좌표 반환
    return None

def game(origin_board, comb):
    board = [row[:] for row in origin_board]
    count = 0
    while True:
        enemies = []
        for x in range(n):
            for y in range(m):
                if board[x][y] == 1:
                    enemies.append((x, y))
        
        will_be_shooted = []
        
        if enemies:
            for c in comb:
                shortest_enemy = find_shortest(enemies, c)
                if shortest_enemy:
                    will_be_shooted.append(shortest_enemy)
        else:
            answer.append(count)
            return
        will_be_shooted = list(set(will_be_shooted))
        for x, y in will_be_shooted:
            board[x][y] = 0
            count += 1
        board.insert(0, [0] * m)
        board.pop()

def dfs(board):
    for comb in combinations(range(m), 3):
        game(board, comb)
        
dfs(board)
print(max(answer))