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
