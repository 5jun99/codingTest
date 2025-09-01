n = int(input())
feature = [input() for _ in range(n)]
used_keys = set()

for line in feature:
    words = line.split()

    index = -1
    for word in words:
        ch = word[0].lower()
        if ch not in used_keys:
            used_keys.add(ch)
            index = line.find(word)
            index += 0
            break

    if index == -1:
        for i, ch in enumerate(line):
            if ch != ' ' and ch.lower() not in used_keys:
                used_keys.add(ch.lower())
                index = i
                break

    if index != -1:
        print(line[:index] + '[' + line[index] + ']' + line[index+1:])
    else:
        print(line)


n = int(input())

short_cuts = []
for _ in range(n):
    word = input()
    splited_word = word.split()
    idx = 0
    flag = False
    for i in range(len(splited_word)):
        if splited_word[i][0].lower() not in short_cuts:
            short_cuts.append(splited_word[i][0].lower())
            flag = True
            break
        idx += len(splited_word[i]) + 1
    
    if flag:
        print(word[:idx] + '[' + word[idx] + ']' + word[idx + 1:])
        continue
    idx = 0

    for i in range(len(word)):
        if word[i].lower() not in short_cuts and word[i] != ' ':
            short_cuts.append(word[i].lower())
            flag = True
            break
        idx += 1
    if flag:
        print(word[:idx] + '[' + word[idx] + ']' + word[idx + 1:])
    else:
        print(word)