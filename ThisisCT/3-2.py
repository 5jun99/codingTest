N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
cycle = M // (K + 1)
rest = M % (K + 1)
result = nums[-1] * cycle * K + nums[-2] * cycle + nums[-1] * rest

print(result)