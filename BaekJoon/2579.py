import sys
input = sys.stdin.readline
step_num = int(input())
score_list = [0] * step_num
A = [int(input()) for _ in range(step_num)]

if len(A) <= 2:
    print(sum(A))
else:
    score_list[0] = A[0]
    score_list[1] = A[1] + A[0]
    for i in range(2, step_num):
        score_list[i] = max(score_list[i-3] + A[i-1] + A[i], score_list[i-2]+ A[i])
    print(score_list[-1])


# def select_bigger_score(now_step, res, count):
#     if (count >= 2):
#         return
    
#     if now_step == len(A) - 1:
#         score_list.append(res)
#         return
    
#     if now_step == len(A) - 2:
#         select_bigger_score(now_step+1, res+A[now_step+1], count + 1)
#     else:
#         select_bigger_score(now_step+2, res+A[now_step+2], 0)
#         select_bigger_score(now_step+1, res+A[now_step+1], count + 1)

# select_bigger_score(1, A[1], 0)
# print(max(score_list))
