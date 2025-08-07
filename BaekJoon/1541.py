evalutation = list(input())
answer = 0
sutja = 0
flag = False

def calculate():
    global answer, flag, sutja
    if flag:
        answer -= sutja
        sutja = 0
    else:
        answer += sutja
        sutja = 0

for i in range(len(evalutation)):
    if evalutation[i] == '-':
        calculate()
        flag = True
    elif evalutation[i] == '+':
        calculate()
    else:
        sutja = sutja * 10 + int(evalutation[i])
calculate()

print(answer)