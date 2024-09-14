n = int(input())

rank_expected = [int(input()) for _ in range(n)]
remain_rank = n
rank_expected.sort(reverse=True)
dissatisfiy = 0
for r in rank_expected:
    dissatisfiy += abs(r - remain_rank)
    remain_rank -= 1

print(dissatisfiy)