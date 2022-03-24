'''
В массиве случайных целых чисел поменять 
местами минимальный и максимальный элементы.
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

array[indx_max] = min_
array[indx_min] = max_

print(f'наибольшее число: {max_}; наименьшее число: {min_}')
print(f'массив после изменения: {array}')