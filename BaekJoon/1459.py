x, y, w, s = map(int, input().split())
result = 0
if w > s:
    if abs(x-y) % 2 == 0:
        result = max(x, y) * s
    else:
        result = (min(x, y) + abs(x - y) - 1) * s + w
elif (s >= w) & (s<(2*w)):
    result = min(x, y) * s + abs(x-y) * w
else:
    result = (x+y) * w

print(result)