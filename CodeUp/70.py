month = int(input())

months = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
seasons = ['winter', 'spring', 'summer', 'fall']
for i in range(0, 10, 3):
    print(i)
    if month in months[i:i+3]:
        print(seasons[i])
