n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

parents = [i for i in range(n + 1)]

def find_parents(x, parents):
    if parents[x] != x:
        parents[x] = find_parents(parents[x], parents)
    return parents[x]

def union_parents(x, y, parents):
    x_root = find_parents(x, parents)
    y_root = find_parents(y, parents)

    if x_root != y_root:
        if x_root < y_root:
            parents[y_root] = x_root
        else:
            parents[x_root] = y_root

for u in range(1, n + 1):
    for v in graph[u]:
        union_parents(u, v, parents)

for i in range(1, n + 1):
    find_parents(i, parents)

component_count = len(set(parents[1:]))
print(component_count)
    