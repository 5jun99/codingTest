n = int(input())
member = list(map(int, input().split()))

member.sort()
group_cnt = 0

count = 0
for i in member:
    count += 1
    if count >= i:
        group_cnt += 1
        count = 0

print(group_cnt)