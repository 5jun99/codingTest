n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)
time = 0

if cranes[0] < boxes[0]:
    time = -1
else:
    while boxes:
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        time += 1

print(time)