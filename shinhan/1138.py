n = int(input())

people = list(map(int, input().split()))
line = [0] * n
for i in range(n):
    index = 0
    for j in range(n):
        if people[i] == index and not line[j]:
            line[j] = i + 1
            break
        if not line[j]:
            index += 1
print(*line)
