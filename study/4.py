N = int(input())

numbers = list(map(int, input().split()))
delimeters = list(map(int, input().split()))

results = []

def dfs(idx, result, plus, minus, multiply, divide):
    if idx == N:
        results.append(result)
        return
    if plus > 0:
        dfs(idx + 1, result + numbers[idx], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(idx + 1, result - numbers[idx], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(idx + 1, result * numbers[idx], plus, minus, multiply - 1, divide)
    if divide > 0:
        if result < 0:
            result *= -1
            result //= numbers[idx]
            dfs(idx + 1, -1 * result, plus, minus, multiply, divide - 1)
        else:
            dfs(idx + 1, result // numbers[idx], plus, minus, multiply, divide - 1)

dfs(1, numbers[0], delimeters[0], delimeters[1], delimeters[2], delimeters[3])
print(max(results))
print(min(results))