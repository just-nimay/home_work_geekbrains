n = int(input('введите целое число: '))
odd_to_15 = [x for x in range(0, n + 1) if x % 2 != 0]
print(*odd_to_15)