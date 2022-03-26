def odd_nums(numb):
	for item in range(0, numb + 1):
		if item % 2 != 0:
			yield item

odd_to_15 = odd_nums(int(input('введите целое число:')))
print(next(odd_to_15))
