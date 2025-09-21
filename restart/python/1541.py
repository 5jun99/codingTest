exps = list(map(str, input().split('-')))

first = sum(map(int, exps[0].split('+')))

for exp in exps[1:]:
  first -= sum(map(int, exp.split('+')))

print(first)
