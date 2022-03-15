a = input('введите число: ')
sum_1 = 0
sum_2 = 0

for i in a:
	i = int(i)
	if i % 2 == 0:
		sum_1 +=1
	else:
		sum_2 +=1

print(f'кол-во четных чисел: {sum_1}')
print(f'кол-во нечетных чисел: {sum_2}')