for _ in range(int(input())):
    pw_input = input()
    left = []
    right = []

    for p in pw_input:
        if p == '<':
            if left:
                right.append(left.pop())
        elif p =='>':
            if right:
                left.append((right.pop()))
        elif p == '-':
            if left:
                left.pop()
        else:
            left.append(p)
    right.reverse()
    print(''.join(left + right))
