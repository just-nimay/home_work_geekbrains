'''
В одномерном массиве целых чисел определить 
два наименьших элемента. Они могут быть как равны 
между собой (оба являться минимальными), так и различаться.
'''

import random
MIN = 0
MAX = 100
SIZE = 10
array = [random.randint(MIN, MAX) for _ in range(SIZE)]
#array = [12, 2, 2, 43, 45, 34]
print(f'массив до изменения: {array}')

min_1 = 50
min_2 = 50
for numb in array:
    if numb < min_1:
        min_1 = numb
count = array.count(min_1)

if count == 1:
    for numb in array:
        if numb == min_1:
            continue
        elif numb < min_2:
            min_2 = numb
else:
    min_2 = min_1

print(f'первый наименьший элемент: {min_1}; второй наименьший элемент: {min_2}')