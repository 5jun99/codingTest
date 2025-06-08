from collections import defaultdict

s, p = map(int, input().split())
dna_count = defaultdict(int)
dna = input()
a, c, g, t = map(int, input().split())


answer = 0
left = 0
right = p - 1
for d in dna[left:right]:
    dna_count[d] += 1

while right < s:
    dna_count[dna[right]] += 1

    if dna_count['A'] >= a and dna_count['C'] >= c and dna_count['G'] >= g and dna_count['T'] >= t:
        answer += 1

    dna_count[dna[left]] -= 1
    left += 1
    right += 1

print(answer)
