from copy import deepcopy
rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]

def shift():
    rc.insert(0, rc[-1])
    rc.pop()
    return rc

def rotate():
    rc_copy = deepcopy(rc)

    for j in [0, len(rc[0]) - 1]:
        if j == 0:
            for i in range(1, len(rc)):
                rc_copy[i - 1][j] = rc[i][j]
        else:
            for i in range(len(rc) - 1):
                rc_copy[i + 1][j] = rc[i][j]

    for i in [0, len(rc) - 1]:
        if i == 0:
            for j in range(len(rc[0]) - 1):
                rc_copy[i][j + 1] = rc[i][j]
        else:
            for j in range(1, len(rc[0])):
                rc_copy[i][j - 1] = rc[i][j]
    return rc_copy

for operation in operations:
    if operation == "Rotate":
        rc = rotate()
    else:
        # print()
        rc = shift()
    print(rc)
print(rc)