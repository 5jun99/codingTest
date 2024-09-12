N = 1260

coin_count = 0
coins = [500, 100, 50, 10]

for i in coins:
    coin_count += N // i
    N %= i

print(coin_count)
