n = int(input())
nums = list(map(int, input().split()))
delimeter = list(map(int, input().split()))
answer = []
def dfs(delimeter_input, res, idx):
    if idx == n:
        answer.append(res)
        return
    if delimeter_input[0] > 0:
        delimeter_input[0] -= 1
        dfs(delimeter_input, res + nums[idx], idx + 1)
        delimeter_input[0] += 1
    if delimeter_input[1] > 0:
        delimeter_input[1] -= 1
        dfs(delimeter_input, res - nums[idx], idx + 1)
        delimeter_input[1] += 1
    if delimeter_input[2] > 0:
        delimeter_input[2] -= 1
        dfs(delimeter_input, res * nums[idx], idx + 1)
        delimeter_input[2] += 1
    if delimeter_input[3] > 0:
        delimeter_input[3] -= 1
        if res < 0:
            dfs(delimeter_input, -(-res // nums[idx]), idx + 1)
        else:
            dfs(delimeter_input, res // nums[idx], idx + 1)
        delimeter_input[3] += 1
    
dfs(delimeter, nums[0], 1)
print(max(answer))
print(min(answer))