from collections import deque
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
cloud = deque([(n - 1, 0), (n - 1, 1), (n-2, 0), (n-2, 1)])
rained = []
dae = [1, 3, 5, 7]

def movecloud(cloud, di, si):
    lenthcloud = len(cloud)
    for _ in range(lenthcloud):
        x, y = cloud.popleft()
        nx, ny = (dx[di - 1] * si + x) % n, (dy[di - 1] * si + y) % n
        cloud.append((nx,ny))
    return cloud

def rain(cloud):
    rained = []
    for x, y in cloud:
        A[x][y] += 1
        rained.append((x, y))
    return rained

def bug(rained):
    for rx, ry in rained:
        rain_avail = 0
        for d in dae:
            nrx, nry = dx[d] + rx, dy[d] + ry
            if nrx >= n or nrx < 0 or nry >= n or nry < 0:
                continue
            if A[nrx][nry] != 0:
                rain_avail += 1
        A[rx][ry] += rain_avail

def cloudmake(rained):
    new_cloud = []
    for x in range(n):
        for y in range(n):
            if A[x][y] >= 2 and (x,y) not in rained:
                new_cloud.append((x,y))
                A[x][y] -= 2

    cloud = deque(new_cloud)

    return cloud


for di, si in move:
    cloud = movecloud(cloud, di, si)
    rained = rain(cloud)
    bug(rained)
    cloud = cloudmake(rained)


answer = 0
for a in A:
    answer += sum(a)
print(answer)