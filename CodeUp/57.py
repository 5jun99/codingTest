a, b = map(bool, map(int, input().split()))
print(not ((a or b) and not (a and b)))