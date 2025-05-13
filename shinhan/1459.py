x, y, w, s = map(int, input().split())
answer = 0

def find_house():
    if 2 * w < s :
        return (x + y) * w
    if w < s :
        return abs(x - y) * w + min(x, y) * s
    if abs(x - y) % 2 == 0:
        return abs(x - y) * s + min(x, y) * s
    else:
        return abs(x - y) // 2 * 2 * s + min(x, y) * s + w

print(find_house())