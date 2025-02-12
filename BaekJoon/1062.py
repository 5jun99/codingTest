n, k = map(int, input().split())

words = [input() for _ in range(n)]

capacity = {'a', 't', 'n', 'i', 'c'}

def get_unoverlap(learned, word):
    true_word = word[4:-4]
    return set(true_word) - learned

def check_readable(learned, unoverlap):

    if len(unoverlap) + len(learned) > k:
        return False
    return True  

answer = 0
learned = set(capacity)

sorted_words = sorted(words, key=lambda w: len(get_unoverlap(learned, w)))

for sw in sorted_words:
    unoverlap = get_unoverlap(learned, sw)  
    if check_readable(learned, unoverlap):
        answer += 1
        learned.update(unoverlap)  # 새 문자 추가

print(answer)
# from itertools import combinations

# n, k = map(int, input().split())
# words = [input() for _ in range(n)]

# # 기본적으로 배워야 하는 문자
# essential = {'a', 't', 'n', 'i', 'c'}

# # 각 단어에서 필요한 추가 문자
# word_sets = []
# for word in words:
#     true_word = set(word[4:-4]) - essential  # 기본 문자 제외
#     word_sets.append(true_word)

# # 만약 k가 5보다 작다면 어떤 단어도 배울 수 없음
# if k < 5:
#     print(0)
#     exit()

# # k개의 문자로 읽을 수 있는 최대 단어 개수 찾기
# answer = 0
# extra_chars = set().union(*word_sets)  # 학습 가능한 추가 문자 전체

# # 배울 수 있는 문자 개수(k-5)만큼 조합을 생성하여 최대값 탐색
# for selected in combinations(extra_chars, min(len(extra_chars), k-5)):
#     learned = essential | set(selected)  # 배운 문자
#     readable_count = sum(1 for word_set in word_sets if word_set <= learned)  # 읽을 수 있는 단어 수
#     answer = max(answer, readable_count)

# print(answer)