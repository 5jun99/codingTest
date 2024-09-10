a = int(input())
list_even = [i for i in range(1, a + 1) if i % 2 == 0]
print(sum(list_even))