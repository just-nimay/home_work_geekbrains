# задание 1

expression = 15 * 3
print(type(expression))

expression = 15 / 3
print(type(expression))

expression = 15 // 2
print(type(expression))

expression = 15 ** 2
print(type(expression))

# задание 2

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for word in my_list:
	try:
		word = int(word)
		#word = str(word)
		print(word)
		index = my_list.index(word)
		if len(word) < 2:
			my_list[index] = '0' + word
		my_list.insert(index, '"')
		my_list.insert(index + 2, '"')
	except ValueError:
		pass
print(my_list)

# задание 3

