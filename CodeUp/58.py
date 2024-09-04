a, b = map(bool, map(int, input().split()))
print((a and b) or not  (b and a))