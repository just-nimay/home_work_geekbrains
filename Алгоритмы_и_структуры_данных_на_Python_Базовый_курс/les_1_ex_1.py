inp = input('введите число: ')
if len(inp) == 3:
	first = int(inp[0])
	second = int(inp[1])
	third = int(inp[2])
	result_1 = first + second + third
	print('сумма цифр =', result_1)
	result_2 = first * second * third
	print('произведение цифр =', result_2)

else:
	print('введите трехзначное число')