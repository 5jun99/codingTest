from itertools import combinations
n = int(input())
answers = []

def check_odd(num):
    count = 0
    for n in num:   
        if n % 2 == 1:
            count += 1
    return count


def dfs(n, answer):
    n = list(map(int, str(n)))
    answer += check_odd(n)
    if len(n) == 1:
        answers.append(answer)
    elif len(n) == 2:
        n = sum(n)
        dfs(n, answer)
    else:
        for a, b in combinations(range(1,len(n)), 2):
            temp = []
            temp.append(n[0:a])
            temp.append(n[a:b])
            temp.append(n[b:])
            tempint= 0
            for t in temp:
                for e in range(len(t)):
                    tempint += t[e] * 10 ** (len(t) - e - 1)
            dfs(tempint, answer)

            
dfs(n, 0)
print(min(answers), max(answers))

