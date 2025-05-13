n = int(input())

expected = [int(input()) for _ in range(n)]

expected.sort()
unsatisfy = 0
for i in range(n):
    unsatisfy += abs(expected[i] - (i + 1))

print(unsatisfy)