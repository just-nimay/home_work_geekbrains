import random
while True:
	first = input('введите значение 1: ')
	second = input('введите значение 2: ')
	if '.' in first:
		first = float(first)
		second = float(second)
		if first > second:
			result = random.uniform(second, first)
			print(result)
		elif first < second:
			result = random.uniform(first, second)
			print(result)
		else:
			print("введены одинаковые числа")
	else:
		try:
			first = int(first)
			second = int(second)
			if first > second:
				result = random.randint(second, first)
				print(result)
			elif first < second:
				result = random.randint(first, second)
				print(result)
			else:
				print("введены одинаковые числа")
		except ValueError:
			first = ord(first)
			second = ord(second)
			result = random.randint(first, second)
			print(chr(result))
 