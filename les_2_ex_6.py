import random

rand_numb = random.randint(0, 100)
count = 10

while True:
	if count == 0:
		print(f'вы проиграли! было загадано число {rand_numb}')
		break

	a = int(input('введите число: '))
	if a == rand_numb:
		print('вы выиграли!')
		break

	elif a > rand_numb:
		print('ваше число больше чем то, что загадано')
		count -= 1

	else:
		print('ваше число меньше чем то, что загадано')
		count -= 1

