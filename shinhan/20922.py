from collections import defaultdict

n, k = map(int, input().split())

numbers = list(map(int, input().split()))
dd = defaultdict(int)
max_sequence = 0
left = 0

for right in range(n):
    dd[numbers[right]] += 1

    while dd[numbers[right]] > k:
        dd[numbers[left]] -= 1
        left += 1

    max_sequence = max(max_sequence, right - left + 1)
print(max_sequence)
