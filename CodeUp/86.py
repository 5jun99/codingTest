n = int(input())

hap = 0
check = 1
while hap < n:
    hap += check
    check += 1

print(hap)