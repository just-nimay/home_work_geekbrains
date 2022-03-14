a = input('введите первое число: ')
b = input('введите цифру, которую ищете: ')
count = 0

for i in a:
	if i == b:
		count += 1

print(f'цифра {b} повторяется {count} раз')