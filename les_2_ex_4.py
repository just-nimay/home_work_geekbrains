n = int(input('введите целое число:'))
a_1 = 1
a_2 = -0.5

q = a_2 / a_1

s_n = a_1 * (1 - q ** n) / 1 - q

print(f'сумма {n} элементов геометрической прогресии 1, -0.5, 0.25, -0.125,...  будет равен {s_n}')