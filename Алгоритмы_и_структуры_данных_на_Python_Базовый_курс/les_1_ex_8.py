year = int(input('введите год: '))

if year % 4 != 0:
	print('обычный')
elif year % 100 == 0:
	if year & 400 == 0:
		print('високосный')
	else:
		print('обычный')
else:
	print('високосный')