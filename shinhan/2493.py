n = int(input())
towers = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(n):
    while stack and stack[-1][1] < towers[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1][0] + 1
    stack.append((i, towers[i]))

print(*answer)