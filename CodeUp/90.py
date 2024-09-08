a, m, d, n = map(int, input().split())

for _ in range(n - 1):
    a = a * m + d

print(a)
