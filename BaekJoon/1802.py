t = int(input())

def definePossible(list_list):
    flag = True
    if len(list_list) < 3:
        return True
    for i in range(len(data) // 2):
        if data[i] == data[len(data) - i - 1]:
            flag = False
            break
    if not flag:
        return False
    else:
        return definePossible(list_list[:len(list_list) // 2]) & definePossible(list_list[len(list_list) // 2 + 1 :])
    
    # flag = True
    # if len(list_list) <= 3:
    #     if len(list_list) == 1:
    #         return True
    #     elif list_list[0] != list_list[2]:
    #         return True
    #     else:
    #         return False
    # else:
    #     print(list_list[:len(list_list) // 2])
    #     print(list_list[len(list_list) // 2 + 1 :])
    #     return definePossible(list_list[:len(list_list) // 2]) & definePossible(list_list[len(list_list) // 2 + 1 :]) 

for _ in range(t):
    data = input()
    print('YES') if definePossible(data) else print('NO')
     