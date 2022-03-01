numb = []
for number in range(1000):
	if number % 2 != 0:
		ready = number ** 3;
		numb.append(ready)
	else:
		pass
print(numb)

sum_list = []
for n in numb:
	i = 0
	n = str(n)
	for num in n:
		i = i + int(num)
	if i % 7 == 0:
		n = int(n)
		sum_list.append(n)
	else:
		pass
finish = sum(sum_list)
print(finish)