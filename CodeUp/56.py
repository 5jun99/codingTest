a, b = map(bool, map(int, input().split()))
print((not a and b) and (not b and a))