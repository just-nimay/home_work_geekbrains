'''
Матрица 5x4 заполняется вводом с клавиатуры, 
кроме последних элементов строк. Программа должна 
вычислять сумму введенных элементов каждой строки и 
записывать ее в последнюю ячейку строки. В конце 
следует вывести полученную матрицу.
'''

M = 3
N = 5

matrix = [[input(f'введите целое число на позиции {_}: ') for _ in range(M)] for _ in range(N)]
print(matrix)
print(*matrix, sep='\n')

for line in matrix:
    sum_line = 0
    for i, item in enumerate(line):
        sum_line += int(item)
        print(f'{item:>5}', end='')
    print(f'|{sum_line:>8}')
