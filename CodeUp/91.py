num_list = list(map(int, input().split()))

def find_gcd(a, b):
    if a < b:
        a, b = b, a
    gcd = 1
    while True:
        if a % b == 0:
            gcd = b
            break
        a, b = b, a % b
    return gcd

first_gcd = find_gcd(num_list[1], num_list[2])
first_lsm = num_list[1]*num_list[2]/first_gcd

second_gcd = find_gcd(num_list[0], first_lsm)
second_lsm = num_list[0]*first_lsm/second_gcd

print(int(second_lsm))