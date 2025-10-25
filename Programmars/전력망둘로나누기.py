def solution(n, wires):
    from collections import deque
    answer = 100000
    graph = [[] for _ in range(n + 1)]
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)

    def bfs(s, e):
        q = deque([s])
        tower = 0
        visited = [False] * (n + 1)
        while q:
            now = q.popleft()
            tower += 1
            for next in graph[now]:
                if (now, next) == (s, e) or (now, next) == (e, s):
                    continue
                if visited[next]:
                    continue
                q.append(next)
                visited[next] = True
        
        g1 = 0
        g2 = 0

        for v in visited[1:]:
            if v:
                g1 += 1
            else:
                g2 += 1

              
        return abs(g1 - g2)
    
    for s, e in wires:
        answer = min(answer, bfs(s, e))
    return answer