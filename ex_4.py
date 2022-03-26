src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

print(result)

def comp(list_1):
	for number in list_1:
		indx = list_1.index(number)
		if indx == 0:
			pass
		else:
			if number > list_1[indx-1]:
				result.append(number)
		return result

print(comp(src))