'''
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо
заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. 
именно в этих позициях первого массива стоят четные числа.
'''

import random
MIN = 0
MAX = 100
SIZE = 10
array_1 = [random.randint(MIN, MAX) for _ in range(SIZE)]

array_2 = []

for i, numb in enumerate(array_1, start=0):
    if numb % 2 == 0:
        array_2.append(i)

print(array_1, array_2,)