from collections import deque

for _ in range(int(input())):
    func = input()
    n = int(input())
    arr = input().strip()
    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr[1:-1].split(',')))

    reverse_flag = False
    flag = True
    for f in func:
        if f == 'R':
            reverse_flag = not reverse_flag
        else:
            if arr:
                if not reverse_flag:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print('error')
                flag = False
                break
    if flag:
        if reverse_flag:
            arr.reverse()
        print("[" + ','.join(map(str, arr)) + "]")

