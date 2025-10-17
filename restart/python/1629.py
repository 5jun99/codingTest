a, b, c = map(int, input().split())

degree = b


def binary(degree):
    if degree == 1:
        return a % c
    
    half = binary(degree // 2)
    
    if degree % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c

print(binary(b))