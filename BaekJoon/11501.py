t = int(input())
for _ in range(t):
    n = int(input())
    juka = list(map(int, input().split()))
    juka.reverse()    
    max_price = 0
    answer = 0

    for price in juka:
        if price > max_price:
            max_price = price
        else:
            answer += max_price - price
    print(answer)

    # answer = 0
    # while True:
    #     buy = 0
    #     sell = 0
    #     ju = 0
    #     max_idx = -1
    #     max_temp = -1
    #     if not juka:
    #         break
    #     for i in range(len(juka)):
    #         if juka[i] > max_temp:
    #             max_idx = i
    #             max_temp = juka[i]
    #     for i in range(max_idx):
    #         buy += juka[i]
    #     sell += max_idx * juka[max_idx]
    #     answer += sell - buy
        
    #     juka = juka[max_idx+1:]
        
    # print(answer)
