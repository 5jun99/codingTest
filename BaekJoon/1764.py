n, m = map(int, input().split())

not_heard = set([input() for _ in range(n)])
not_saw = set([input() for _ in range(m)])

not_hs = sorted(list(not_saw & not_heard))

print(len(not_hs))
for nhs in not_hs:
    print(nhs)


