# g = int(input())
# p = int(input())

# gate = [i + 1 for i in range(g)]
# possibleDockedPlane = 0
# for i in range(p):
#     plane = int(input())
#     if gate[plane - 1] == 0:
#         break
#     gate[plane - 1:g] = [i - 1 for i in gate[plane - 1:g]]
#     possibleDockedPlane += 1

# print(possibleDockedPlane) ****시간 초과 ******
    
def find_parent(x):
    if x != parents[x]:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

g = int(input())
p = int(input())
parents = [i for i in range(g + 1)]
planes = [int(input()) for _ in range(p)]
possibleDockedPlane = 0

for plane in planes:
    gate_parent = find_parent(plane)
    if gate_parent == 0:
        break
    union_parent(gate_parent, gate_parent - 1)
    possibleDockedPlane += 1

print(possibleDockedPlane)