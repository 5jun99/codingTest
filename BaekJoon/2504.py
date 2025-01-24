brackets = list(input())

def validate(bracket):
    stack = []
    answer = 0
    temp = 1

    for i in range(len(bracket)):
        if brackets[i] == '(':
            stack.append(0)
            temp *= 2
        elif brackets[i] == '[':
            stack.append(1)
            temp *= 3
        elif brackets[i] == ')':
            if not stack or stack[-1] == 1:
                answer = 0
                break
            if brackets[i-1] == '(':
                answer += temp
            stack.pop()
            temp //= 2
        else:
            if not stack or stack[-1] == 0:
                answer = 0
                break
            if brackets[i-1] == '[':
                answer += temp
            stack.pop()
            temp //= 3
    if stack:
        return 0
    return answer


print(validate(brackets))            
