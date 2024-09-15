n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

people_rank = [1] * n

for i in range(n):
    for j in range(n):
        if (people[i][0] < people[j][0]) & (people[i][1] < people[j][1]):
            people_rank[i] += 1
     

print(33)
for rank in people_rank:
    print(rank, end=' ')