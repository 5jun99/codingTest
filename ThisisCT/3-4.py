n, k = map(int, input().split())
count = 0

while True:
    if n == 1:
        break
    if n % k != 0:  
        count += 1
        n -= 1
    else:
        count += 1
        n /= k  

print(count)

while n > k: # 이게 입력 크기에 영향 덜 받음
    count += n - (n % k)
    n = (n // k) * k
    if n <k:
        break

    count += 1
    n //= k