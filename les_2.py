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
print("задание 2")
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for elem in my_list:
    if elem.isdigit():
        new_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_list.extend(['"', f'{elem[0]}{int(elem[1:]):02}', '"'])
    else:
        new_list.append(elem)

out_info = ' '.join(new_list)
print(out_info)

# задание 4
words_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for word in words_list:
    print('Привет', word.split()[-1].title())

# задание 5
print('задание 5')
items = [23.5, 65.93, 12, 10.2, 50.50, 63.99, 99.99, 1]
finish_list = ''
for item in items:
	sorting = str(item).split('.')
	if len(sorting) <= 1:
		sorting.append('00')
	rubls = sorting[0]
	penny = sorting[1]
	if len(sorting[1]) <= 1:
		sorting[1] ='1' + sorting[1]
	finish = (f'{rubls} руб {penny} коп, ')
	finish_list = finish_list + finish

print('цены:', finish_list)
print('список, отсортированный по возрастанию:', sorted(items))
print('список, отсортированный по убыванию:', sorted(items, reverse=True))

count = 5
print('цены самых дорогих продуктов:')
while count > 0:
	list_max = sorted(items)
	print(list_max[count+2])
	count -= 1






















