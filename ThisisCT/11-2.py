S = input()
new_s = []
for i in S:
    new_s.append(int(i))

result = 0

for i in new_s:
    if (result == 0) | (i == 0):
        result += i
    else:
        result *= i
        
print(result)