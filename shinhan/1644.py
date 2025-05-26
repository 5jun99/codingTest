import math

n = int(input())
answer = 0

def is_prime_num(pn):
    if pn < 2:
        return False
    for i in range(2, int(math.sqrt(pn)) + 1):
        if pn % i == 0:
            return False
    return True

prime_nums = []

for i in range(2, n + 1):
    if is_prime_num(i):
        prime_nums.append(i)


left = 0
temp_plus = 0

for right in range(len(prime_nums)):
    temp_plus += prime_nums[right]

    while temp_plus > n:
        temp_plus -= prime_nums[left]
        left += 1

    if temp_plus == n:
        answer += 1
        continue

print(answer)