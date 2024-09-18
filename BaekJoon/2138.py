n = int(input())
before = list(input())
for i in range(n):
    before[i] = int(before[i])
after = list(input())
for i in range(n):
    after[i] = int(after[i])

print(before, after)