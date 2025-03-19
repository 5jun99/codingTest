from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
# answer = []
min_value = 1e9
people = list(range(n))

# def cap_calc(team):
#     cap = 0
#     for i in team:
#         for j in team:
#             if i != j:
#                 cap += s[i][j]
#     return cap

def cap_calc(team):
    return sum(s[i][j] for i in team for j in team if i != j)


for comb in combinations(range(n), n//2):
    # team = []
    # team.append(list(comb))
    # other_team = list(set(people) - set(comb))
    # team.append(other_team)
    # teams.append(team)
    other_team = [x for x in people if x not in comb]
    start_cap = cap_calc(list(comb))
    link_cap = cap_calc(other_team)
    min_value = min(min_value, abs(start_cap - link_cap))

print(min_value)
# for one, two in teams:
#     one_cap = cap_calc(one)
#     two_cap = cap_calc(two)
#     answer.append(abs(one_cap - two_cap))
    
# print(min(answer))
