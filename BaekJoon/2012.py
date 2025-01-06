n = int(input())

ranks = sorted([int(input()) for _ in range(n)])

temp = 1
answer = 0
for r in ranks:
    answer += abs(temp - r)
    temp += 1

print(answer)