'''
В одномерном массиве найти сумму элементов, 
находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
'''


import random
MIN = 0
MAX = 100
SIZE = 10
array = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(f'массив до изменения: {array}')

min_ = 50
max_ = 0
for numb in array:
    if numb > max_:
        max_ = numb
		
    elif numb < min_:
        min_ = numb
		
indx_max = array.index(max_)
indx_min = array.index(min_)

print(f'наибольшее число: {max_}; наименьшее число: {min_}')

summ_ = 0
if indx_max > indx_min:
    for numb in array[indx_min + 1:indx_max]:
        summ_ = summ_ + numb
else:
    for numb in array[indx_max + 1:indx_min]:
        summ_ = summ_ + numb

print(f'сумма элементов, находящихся между минимальным и максимальным элементами: {summ_}')