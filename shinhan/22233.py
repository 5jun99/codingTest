from collections import defaultdict
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

keywords = set([input().rstrip() for _ in range(n)])
answer = n
for _ in range(m):
    used_words = list(input().rstrip().split(','))
    for uw in used_words:
        if uw in keywords:
            answer -= 1
            keywords.remove(uw)
    print(answer)