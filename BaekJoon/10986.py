from exceptiongroup import catch

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

sums = [0]
sum_tmp = 0
result = 0
for i in range(n):
    sum_tmp += numbers[i]
    sums.append(sum_tmp)

print(sums)
left = 0
right = 1

while right
print(result)