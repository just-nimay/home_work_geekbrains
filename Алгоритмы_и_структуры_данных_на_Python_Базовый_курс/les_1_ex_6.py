num = int(input('введите номер буквы русского алфавита: '))
num = ord('а') + num - 1
leter = chr(num)
print(f'Ваша буква: {leter}')