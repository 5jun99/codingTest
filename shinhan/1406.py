"""
시간이 터지면 스택을 생각해봐라
왼쪽 오른쪽이 상황ㅇ ㅣ다르다면 스택으로 오른쪽 왼쪽 다르게 생각해보는 것도 좋은 방법이다!
"""

left_stack = list(input())
m = int(input())
commands = [input().split() for _ in range(m)]
right_stack = []
for cmd in commands:
    if cmd[0] =='P':
        left_stack.append(cmd[1])
    elif cmd[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif cmd[0] == 'L':
        if left_stack:
            ls = left_stack.pop()
            right_stack.append(ls)
    elif cmd[0] == 'D':
        if right_stack:
            rs = right_stack.pop()
            left_stack.append(rs)
right_stack.reverse()
print(''.join(left_stack + right_stack))

#
# cursor = n
#
# for c in command:
#     if c[0] == 'P':
#         if cursor == n:
#             input_string.append(c[1])
#         else:
#             input_string.insert(cursor, c[1])
#         cursor += 1
#         n = len(input_string)
#     elif c[0] == 'L' and cursor > 0:
#         cursor -= 1
#     elif c[0] == 'D' and cursor < n:
#         cursor += 1
#     elif c[0] == 'B' and cursor > 0:
#         input_string.pop(cursor - 1)
#         cursor -= 1
#         n = len(input_string)
#
# for c in input_string:
#     print(c, end='')
#
