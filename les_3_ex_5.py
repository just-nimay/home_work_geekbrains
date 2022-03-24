'''
В массиве найти максимальный отрицательный элемент. 
Вывести на экран его значение и позицию в массиве. 
Примечание к задаче: пожалуйста не путайте «минимальный» и 
«максимальный отрицательный». Это два абсолютно разных значения.

'''


import random
MIN = -50
MAX = 50
SIZE = 10
array = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(f'массив до изменения: {array}')

min_negative = 0
max_negative = 0

for numb in array:
    if numb < min_negative:
        min_negative = numb

for numb in array:
    if numb < 0:
    


indx = array.index(max_negative)

print(f'максимальный отрицательный элемент {max_negative} с индексом {indx}')