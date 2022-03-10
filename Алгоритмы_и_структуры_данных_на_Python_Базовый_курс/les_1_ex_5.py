first = ord(input('введите первую букву: '))
second = ord(input('введите вторую букву: '))

number_1 = first - ord('a') + 1
number_2 = second - ord('a') + 1

print(f'порядковый номер первой буквы: {first} \n порядковый номер второй буквы: {second}')
print(f'Число букв между введенными: {abs(first - second) - 1}')