"""
시간이 터지면 스택을 생각해봐라
왼쪽 오른쪽이 상황ㅇ ㅣ다르다면 스택으로 오른쪽 왼쪽 다르게 생각해보는 것도 좋은 방법이다!
"""

# left_stack = list(input())
# m = int(input())
# commands = [input().split() for _ in range(m)]
# right_stack = []
# for cmd in commands:
#     if cmd[0] =='P':
#         left_stack.append(cmd[1])
#     elif cmd[0] == 'B':
#         if left_stack:
#             left_stack.pop()
#     elif cmd[0] == 'L':
#         if left_stack:
#             ls = left_stack.pop()
#             right_stack.append(ls)
#     elif cmd[0] == 'D':
#         if right_stack:
#             rs = right_stack.pop()
#             left_stack.append(rs)
# right_stack.reverse()
# print(''.join(left_stack + right_stack))

line = list(input())

n = int(input())

command = list(input().split() for _ in range(n))

left = line
right = []

for co in command:
    c = co[0]
    if c == 'L':
        if left:
            right.append(left.pop())
    elif c == 'D':
        if right:
            left.append(right.pop())
    elif c == 'B':
        if left:
            left.pop()
    else:
        left.append(co[1])
    print(left, end=' ')
    print(right)

for l in left:
    print(l, end='')

while right:
    print(right.pop(), end='')