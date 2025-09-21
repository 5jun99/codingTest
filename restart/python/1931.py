n = int(input())

meetings = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : (x[1], x[0]))

end_time = 0

ans = 0

for s, e in meetings:
  if end_time <= s:
    end_time = e
    ans += 1
  
print(ans)