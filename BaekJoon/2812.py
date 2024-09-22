n, k = map(int, input().split())
number = input()
number_list = []
for i in number:
    number_list.append(int(i))
result = []
last_check = -1
for i in range(n - k):
    temp = max(number_list[last_check + 1:k + i + 1])
    result.append(temp)
    last_check = number_list.index(temp, last_check + 1,k + i + 1 )

jari = n - k - 1
final = 0

for i in result:
    final += 10 ** jari * i
    jari-= 1

print(final)