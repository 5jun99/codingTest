n, m = map(int, input().split())

numbers = list(map(int, input().split()))

sums = [0]
sum_tmp = 0
for i in range(n):
    sum_tmp += numbers[i]
    sums.append(sum_tmp)

for i in range(m):
    start, end = map(int, input().split())
    print(sums[end] - sums[start - 1])

"""
해당 인덱스 까지의 누적 합을 저장해놨다가 시작 j 번째 누적합 - i 번째 누적합 으로 사이 값을 계산 
"""
