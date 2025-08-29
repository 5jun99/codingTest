n = int(input())
m = int(input())
s = input()

p = "I" + n * "OI"
pl = len(p)
answer = 0
count = 0
window = []
i = 0
while i < (m - 1):
    if s[i:i+3] == "IOI":
        count += 1
        i += 2
        if count == n:
            count -= 1
            answer += 1
    else:
        i += 1
        count = 0

print(answer)