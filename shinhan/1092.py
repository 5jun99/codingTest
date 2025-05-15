n = int(input())

crane = sorted(list(map(int, input().split())), reverse=True)

m = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)
duration = 0
if max(crane) < max(boxes):
    print(-1)
else:
    while boxes:
        for c in crane:
            for b in boxes:
                if c >= b:
                    boxes.remove(b)
                    break
        duration += 1
    print(duration)

