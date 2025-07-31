n, r, c = map(int, input().split())
edge_len = 2 ** n

sum = 0

while edge_len > 1:
    edge_len //= 2
    if r >= edge_len and c >= edge_len:
        sum += edge_len ** 2 * 3
        r -= edge_len
        c -= edge_len
    elif r >= edge_len:
        sum += edge_len ** 2 * 2
        r -= edge_len
    elif c >= edge_len:
        sum += edge_len ** 2
        c -= edge_len
    else:
        sum += 0


print(sum)