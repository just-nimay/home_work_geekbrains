
while True:
	a = int(input('введите первое число: '))
	b = int(input('введите второе число: '))
	c =  input('введите знак операции: ')

	if c == '0': 
		break

	elif c == '+':
		result = a + b
		print(f'сумма чисел: {result}')

	elif c == '-':
		result = a - b
		print(f'разность чисел: {result}')

	elif c == '*':
		result = a * b
		print(f'произведение чисел:  {result}')
	elif c == '/':
		if b == 0:
			print('на нуль делить нельзя')
			
		else:
			result = a / b
			print(f'частное чисел: {result}')
	else:
		print('введите корректные знак операции')
		continue
